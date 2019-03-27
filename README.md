# Buddhist Digital Ontology vocabulary

This repository contains the files that define the Buddhist Digital Ontology (BDO). You can use [TopBraid Composer Free Edition](https://www.topquadrant.com/downloads/topbraid-composer-install/#) or [Protégé](http://protege.stanford.edu/) to view and edit these files.


The overall ontology is organized in a collection of directories as follows:

- [core](core): contains 
  - the base ontology file: [bdo.ttl](core/bdo.ttl) that defines the classes and properties that make up the core concepts of the cultural heritage vocabulary for the domain of Asian/Southeast Asian Buddhist cultures. The [bdo.ttl](core/bdo.ttl) imports files in the [types](types) and [roles](roles) directories that contain constants and their classes that used in the core ontology.

  - [unknown-entities.ttl](core/unknown-entities.ttl) defines constants representing an unknown person, work, place and so on. This imported by [bdo](core/bdo.ttl).
  - [bdo.owl.ttl](core/bdo.owl.ttl) defines _owl restrictions_ on the classes and properties defined in [bdo.ttl](core/bdo.ttl). These are used in validating resource definitions and to provide declarative information relevant to the UI's for viewing and editing.
  - [bdo.shapes.ttl](core/bdo.shapes.ttl) defines _shacl constraints_ on the classes and properties in in [bdo.ttl](core/bdo.ttl). These are used in validating resource definitions and to provide declarative information relevant to the UI's for viewing and editing.
- [roles](roles): contains files of constant definitions relevant to various sorts of _roles_ that a `Person` may play in events related to `Works`, `Places`, and other `Persons`. Each of these files defines the classes and their instances for a particular role which are then plugged in via `owl:subClassOf` properties in [bdo.ttl](core/bdo.ttl).

- [types](types): contain files that define models via classes and constants related to various types such as the kind of `Binding` that a `Work` has, or the `Script` in which a `Work` is manifested. Each of these files defines the classes and their instances for a particular kind of type which are then plugged in via `owl:subClassOf` properties in [bdo.ttl](core/bdo.ttl).
- [adm](adm): contains:
  - [admin.ttl](adm/admin.ttl) which defines classes and properties related to the operation and administration of the BUDA platform that represents BDRC's implementation of the core ontology, [bdo.ttl](core/bdo.ttl).
  
  - [types](types): contains files that define constants that are used in [admin.ttl](adm/admin.ttl) which imports these files. For example, [license_types.ttl](adm/types/license_types.ttl) and [status_types.ttl](adm/types/status_types.ttl)
- [ext](ext): contains _extensions_ to the core and admin models
    - [auth](auth): contains [auth.ttl](ext/auth/auth.ttl) which defines an authentication/authorization model used by various services to implement security controls on read and write access to portions of the platform
- [reasoning](reasoning): contains files that use Jena rules to add triples to the dataset via inferencing.
- [context.jsonld](context.jsonld) file is a JSON-LD context file that can be used, with the url `http://purl.bdrc.io/context.jsonld`.
- [lang-tags.md](lang-tags.md) file documents language tag conventions BDRC is using.

### Changes

See [Change log](CHANGELOG.md).

### RDF 1.0 / 1.1

Protégé handles only RDF 1.0 while TopBraid Composer and Jena handles RDF 1.1. The files are in RDF 1.1 format. They can be easily converted to RDF 1.0 (handled by Protégé) with:

```sh
$ sed 's,http://www.w3.org/1999/02/22-rdf-syntax-ns#langString,http://www.w3.org/1999/02/22-rdf-syntax-ns#PlainLiteral' bdo.ttl > bdo-rdf10.ttl
```

### License

All files, such as [bdo.ttl](bdo.ttl) and associated documentation are distributed under the [CC0 license](https://creativecommons.org/publicdomain/zero/1.0/).
