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
TMP = "http://purl.bdrc.io/ontology/tmp/"
ADM = "http://purl.bdrc.io/ontology/admin/"
WD = "http://www.wikidata.org/entity/"
DILA = "http://purl.dila.edu.tw/resource/"
VIAF = "http://viaf.org/viaf/"
RKTS = "http://purl.rkts.eu/resource/"

PREFIXES = {
    "bdo": BDO,
    "bda": BDA,
    "bdu": BDU,
    "bdr": BDR,
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
    "rkts": RKTS,
    "tmp": TMP
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
        if p == "bdo":
            continue
        ctx[p] = ns
    ctx["type"] = "@type"
    ctx["id"] = "@id"
    ctx["@vocab"] = BDO
    ctx["adm:hasAdmin"] = { "@reverse": "http://purl.bdrc.io/ontology/admin/adminAbout" }
    ctx["owl:sameAs"] = { "@type": "@id" }
    ctx["skos:closeMatch"] = { "@type": "@id" }
    ctx["tmp:hasRole"] = { "@type": "@id" }
    ctx["tmp:thumbnailIIIFService"] = { "@type": "@id" }

def shortname(r):
    pref, _, lname = NSM.compute_qname_strict(r)
    if pref == 'bdo':
        return lname
    return pref+":"+lname

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
    rshort = shortname(r)
    if rshort in ["xsd:string", "rdf:langString", "xsd:boolean", "xsd:integer", "xsd:float"]:
        return
    pshort = shortname(prop)
    if (pshort.startswith("ns") or ":" not in rshort):
        return
    ctx[pshort] = { "@type" : rshort }

def add_annotation_prop(model, prop, ctx):
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
    pshort = shortname(prop)
    
    for _, _, t in models.triples((r, RDF.type)):
        if t != RDFS.Datatype:
            ctx[pshort] = { "@type" : "@id" }
            return
        else:
            break
    rshort = shortname(r)
    if rshort in ["xsd:string", "rdf:langString", "xsd:boolean", "xsd:integer", "xsd:float"]:
        return
    
    if (pshort.startswith("ns") or ":" not in rshort):
        return
    ctx[pshort] = { "@type" : rshort }

def add_file(fname, ctx):
    model = rdflib.Graph()
    model.parse(str(fname), format="ttl")
    for p, _, _ in model.triples((None,  RDF.type, OWL.ObjectProperty)):
        if ((p, OWL.deprecated, None)) in model:
            continue
        pshort = shortname(p)
        ctx[pshort] = { "@type" : "@id" }
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
    print(json.dumps(res, sort_keys=True, indent=2))

main()