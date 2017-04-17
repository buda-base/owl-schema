# BDRC Ontology Schema

This repository contains the files associated with the BDRC ontology schema. You can use [Protege](http://protege.stanford.edu/) to edit it.

### Features

See [reasoning](reasoning/) directory for reasoning rules, and [i18n](i18n/) directory for string translations.

### Changes

See [Change log](CHANGELOG.md).

### RDF 1.0 / 1.1

Due to Protege handling only RDF 1.0, the files are in this format. They can be easily converted to RDF 1.1 (handled by Jena 3 among others) with:

```
$ sed 's,http://www.w3.org/1999/02/22-rdf-syntax-ns#PlainLiteral,http://www.w3.org/1999/02/22-rdf-syntax-ns#langString,' bdrc.owl > bdrc-rdf11.owl
```

### License

The data is *Copyright 2010-2017 Buddhist Digital Resource Center*, and is distributed under the [CC-BY 4.0](LICENSE) license.