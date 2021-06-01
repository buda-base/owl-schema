import rdflib
from rdflib.namespace import RDF, RDFS, SKOS, OWL, Namespace, NamespaceManager, XSD, URIRef
import csv
import pathlib
import glob
import json

BDR = "http://purl.bdrc.io/resource/"
BDO = "http://purl.bdrc.io/ontology/core/"
BDA = "http://purl.bdrc.io/admindata/"
BDU = "http://purl.bdrc.io/resource-nc/user/"
BF = "http://id.loc.gov/ontologies/bibframe/"
BDG = "http://purl.bdrc.io/graph/"
ADM = "http://purl.bdrc.io/ontology/admin/"
WD = "http://www.wikidata.org/entity/"
DILA = "http://purl.dila.edu.tw/resource/"
VIAF = "http://viaf.org/viaf/"
RKTS = "http://purl.rkts.eu/resource/"

PREFIXES = {
    "": BDO,
    "bdo": BDO,
    "bda": BDA,
    "bdu": BDU,
    "bf": BF,
    "adm": ADM,
    "bdg": BDG,
    "skos": str(SKOS),
    "xsd": str(XSD),
    "rdfs": str(RDFS),
    "rdf": str(RDF),
    "owl": str(OWL),
    "wd": WD,
    "viaf": VIAF,
    "dila": DILA,
    "rkts": RKTS
}

PATHS = [
    "../adm/**/*.ttl", 
    "../core/*.ttl" , 
    #"../ext/**/*.ttl"
    ]

NSM = NamespaceManager(rdflib.Graph())
for p, ns in PREFIXES.items():
    NSM.bind(p, Namespace(ns))


def add_static(ctx):
    for p, ns in PREFIXES.items():
        ctx[p] = ns
    ctx["type"] = "@type"
    ctx["id"] = "@id"
    ctx["@vocab"] = BDO

def add_datatype_prop(model, prop, ctx):
    if ((prop, OWL.deprecated, None)) in model:
        return
    ranges = []
    for _, _, r in model.triples((prop, RDFS.range, None)):
        ranges.append(r)
    if len(ranges) > 1:
        print("too many ranges on %s" % p)
        return
    if len(ranges) < 1:
        return
    r = ranges[0]
    rpref, _, rlname = NSM.compute_qname_strict(r)
    ppref, _, plname = NSM.compute_qname_strict(prop)
    if (ppref.startswith("ns") or rpref.startswith("bdo")):
        return
    ctx[ppref+":"+plname] = { "@type" : rpref+":"+rlname }

def add_file(fname, ctx):
    model = rdflib.Graph()
    model.parse(str(fname), format="ttl")
    for p, _, _ in model.triples((None,  RDF.type, OWL.ObjectProperty)):
        if ((p, OWL.deprecated, None)) in model:
            continue
        pref, _, lname = NSM.compute_qname_strict(p)
        ctx[pref+":"+lname] = { "@type" : "@id" }
    for p, _, _ in model.triples((None,  RDF.type, OWL.AnnotationProperty)):
        add_datatype_prop(model, p, ctx)
    for p, _, _ in model.triples((None,  RDF.type, OWL.DatatypeProperty)):
        add_datatype_prop(model, p, ctx)

def main():
    ctx = {}
    res = {"@context": ctx}
    add_static(ctx)
    for g in PATHS:
        for fname in glob.glob(g, recursive=True):
            add_file(fname, ctx)
    print(json.dumps(ctx, sort_keys=True, indent=2))

main()