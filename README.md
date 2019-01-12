# BDRC Ontology Schema

This repository contains the files associated with the BDRC OWL ontology. You can use [Protege](http://protege.stanford.edu/) to edit it.

The `bdrc-migration.owl` ontology was used in the initial conversion from the XML metadata documents used in the legacy system. This ontology should not be modified without considering the impacts on the `xmltoldmigration` and `fusekicouchdb` projects.

The `bdrc.owl` is the current ontology and at some point the migration toolchain will be sync'd to the this ontology.

The [resources](resources/) directory contains reference copies of third-party ontologies used in developing the production ontology.

The [context.jsonld](context.jsonld) file is a JSON-LD context file that can be used, with the url `http://purl.bdrc.io/context.jsonld`.

The [lang-tags.md](lang-tags.md) file documents language tag conventions BDRC is using.

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
