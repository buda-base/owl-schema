# Buddhist Digital Ontology vocabulary


This repository contains the files that define the Buddhist Digital Ontology (BDO). You can use [TopBraid Composer Free Edition](https://www.topquadrant.com/downloads/topbraid-composer-install/#) or [Protégé](http://protege.stanford.edu/) to view and edit these files.

### Releases

To simply view the BDO ontology in Protégé without having to deal with imports, please download the latest `bdo.owl` file from the releases. 
The current release is [bdo.owl v2.0.0](https://github.com/buda-base/owl-schema/releases/download/v2.0.0/bdo.owl).

### Organization of the Ontology components

The overall ontology is organized in a collection of directories and files as follows: 

- [core](core): contains 
  - the base ontology file: [bdo.ttl](core/bdo.ttl) that defines the classes and properties that make up the core concepts of the cultural heritage vocabulary for the domain of Asian/Southeast Asian Buddhist cultures. The [bdo.ttl](core/bdo.ttl) imports files in the [types](types) and [roles](roles) directories that contain constants and their classes that are used in the core ontology.

  - [unknown-entities.ttl](core/unknown-entities.ttl) defines constants representing an unknown person, work, place and so on. This is imported by [bdo.ttl](core/bdo.ttl).
  - [bdo.owl.ttl](core/bdo.owl.ttl) defines [_owl restrictions_](http://www.infowebml.ws/rdf-owl/Restriction.htm) on the classes and properties defined in [bdo.ttl](core/bdo.ttl). These are used in validating resource definitions and to provide declarative information relevant to the UI's for viewing and editing.
  - [bdo.shapes.ttl](core/bdo.shapes.ttl) defines [_shacl constraints_](https://w3c.github.io/data-shapes/shacl/) on the classes and properties in in [bdo.ttl](core/bdo.ttl). These are used in validating resource definitions and to provide declarative information relevant to the UI's for viewing and editing.
- [roles](roles): contains files of constant definitions relevant to various sorts of _roles_ that a `Person` may play in events related to `Works`, `Places`, and other `Persons`. Each of these files defines the classes and their instances for a particular role which are then plugged in via `owl:subClassOf` properties in [bdo.ttl](core/bdo.ttl).

- [types](types): contain files that define models via classes and constants related to various types such as the kind of `Binding` that a `Work` has, or the `Script` in which a `Work` is _manifested_. Each of these files defines the classes and their instances for a particular kind of type which are then plugged into [bdo.ttl](core/bdo.ttl) via `owl:subClassOf` properties.
- [adm](adm): contains:
  - [admin.ttl](adm/admin.ttl) which defines classes and properties related to the operation and administration of the BUDA platform that represents BDRC's implementation of the core ontology, [bdo.ttl](core/bdo.ttl).
  
  - [types](types): contains files that define constants that are used in [admin.ttl](adm/admin.ttl) which imports these files. For example, [license_types.ttl](adm/types/license_types.ttl) and [status_types.ttl](adm/types/status_types.ttl)
- [ext](ext): contains _extensions_ to the core and admin models
    - [auth](auth): contains [auth.ttl](ext/auth/auth.ttl) which defines an authentication/authorization model used by various services to implement security controls on read and write access to portions of the platform
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
