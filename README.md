# BDRC Ontology Schema

This repository contains the files associated with the BDRC ontology schema. You can use [Protege](http://protege.stanford.edu/) to edit it.

The `bdrc-migration.owl` ontology is used in the conversion from the XML metadata documents used in the legacy system. This ontology should not be modified without considering the impacts on the `xmltoldmigration` and `fusekicouchdb` projects.

The `bdrc-production.owl` ontology is the evolving ontology that will be used in developing the production BUDA system going forward, This ontology will include replacements of migration classes and properties with ontology elements from other ontogies such bibframe, foaf and so on.

The `bdrc.owl` is the original migration ontology and at some point should become the production ontology once references from the migration toolchain projects are sorted out.

The [resources](resources/) directory contains reference copies of third-party ontologies used in developing the production ontology.

### Features

See [reasoning](reasoning/) directory for reasoning rules, and [i18n](i18n/) directory for string translations.

### Changes

See [Change log](CHANGELOG.md).

### RDF 1.0 / 1.1

Due to Protege handling only RDF 1.0, the files are in this format. They can be easily converted to RDF 1.1 (handled by Jena 3 among others) with:

```sh
$ sed 's,http://www.w3.org/1999/02/22-rdf-syntax-ns#PlainLiteral,http://www.w3.org/1999/02/22-rdf-syntax-ns#langString,' bdrc.owl > bdrc-rdf11.owl
```

### License

The data is *Copyright 2010-2017 Buddhist Digital Resource Center*, and is distributed under the [CC-BY 4.0](LICENSE) license.