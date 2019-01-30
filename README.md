# BDRC Ontology Schema

This repository contains the files associated with the Buddhist Digital Ontology (BDO). You can use [Protege](http://protege.stanford.edu/) to edit it. The main file is `bdo.owl`.

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
$ sed 's,http://www.w3.org/1999/02/22-rdf-syntax-ns#PlainLiteral,http://www.w3.org/1999/02/22-rdf-syntax-ns#langString,' bdo.owl > bdo-rdf11.owl
```

### License

The `bdo.owl` file and associated documentation are distributed under the [CC0](LICENSE) license.
