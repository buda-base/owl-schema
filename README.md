# Buddhist Digital Ontology vocabulary

This repository contains the files that define the Buddhist Digital Ontology (BDO).

### Organization of the Ontology components

The overall ontology is organized in a collection of directories and files as follows: 

- [core](core): contains the base ontology file ([bdo.ttl](core/bdo.ttl)) that defines the classes and properties that make up the core concepts of the cultural heritage vocabulary for the domain of Asian Buddhist cultures. The [bdo.ttl](core/bdo.ttl) imports files in the [types](types) and [roles](roles) directories that contain constants and their classes that are used in the core ontology.
- [roles](roles): contains files of constant definitions relevant to various sorts of _roles_ that a `Person` may play in events related to `Works`, `Places`, and other `Persons`
- [types](types): contain files that define models via classes and constants related to various types such as the kind of `:Binding` or `:Script` of an `:Instance`
- [adm](adm): contains vocabulary related to the operation and administration of the BUDA platform
- [ext](ext): contains _extensions_ to the core and admin models
- [schemes](schemes): contains `skos:Scheme`s that organize some of the types
- [reasoning](reasoning): contains files that use Jena rules to add triples to the dataset via inferencing.
- [context.jsonld](context.jsonld) file is a JSON-LD context file that can be accessed via the url `http://purl.bdrc.io/context.jsonld`.
- [lang-tags.md](lang-tags.md) documents the language tag conventions BDRC is using.
- [ont-policy.rdf](ont-policy.rdf) contains the Jena policy for locating files during importing and referencing components of the ontology.

### Using ont-policy.rdf

The policy is used with the Jena library to locate components of the ontology and cache them for later use. There are two ways to load an ontology: 1) processing imports; and 2) ignoring imports during loading of an ontology document.

```java
import org.apache.jena.ontology.OntDocumentManager;
import org.apache.jena.ontology.OntModel;
import org.apache.jena.ontology.OntModelSpec;

public class OntExample {

    static String bdoNS = "http://purl.bdrc.io/ontology/core/";
    static String policyURL = "https://raw.githubusercontent.com/buda-base/owl-schema/master/ont-policy.rdf";
    public static void main( String[] args ){

        OntDocumentManager ontMgr = new OntDocumentManager( policyURL );
        ontMgr.setProcessImports( true ); // default but it doesn't hurt to be explicit
        
        OntModelSpec ontSpec = new OntModelSpec( OntModelSpec.OWL_DL_MEM );
        ontSpec.setDocumentManager( ontMgr );
        
        OntModel bdoModel = ontMgr.getOntology( bdoNS, ontSpecImporting );
        System.out.println( "bdoModel.size() = " + bdoModel.size() + " triples" );
    }
}
```
The above loads the entire Buddhist Digital Ontology, `bdoModel`, into a model which can then be interrogated, inferencing run on it and so on. The reported size is currently 4067 triples.

If you want to just access the `bdoNS` document without processing any of the imports defined in the document then `ontMgr.setProcessImports( false )` before using the `ontMgr` the first time, in which case the reported size currently is 2602 triples 
- once an instance of `OntDocumentManager` has been accessed via `getOntology` (or `getModel`) with one setting of `processImports` then all future references will use that setting.

So if you need both aggregate models (all imports processed) and just the documents, then you need two instances of `OntDocumentManager` one with `processImports == true` and one with `processImports == false`.

### Changes

See [Change log](CHANGELOG.md).

### RDF 1.0 / 1.1

Protégé handles only RDF 1.0 while TopBraid Composer and Jena handles RDF 1.1. The files are in RDF 1.1 format. They can be easily converted to RDF 1.0 (handled by Protégé) with:

```sh
$ sed 's,http://www.w3.org/1999/02/22-rdf-syntax-ns#langString,http://www.w3.org/1999/02/22-rdf-syntax-ns#PlainLiteral' bdo.ttl > bdo-rdf10.ttl
```

### License

All files, such as [bdo.ttl](bdo.ttl) and associated documentation are distributed under the [CC0 license](https://creativecommons.org/publicdomain/zero/1.0/).
