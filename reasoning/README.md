# BDRC Ontology reasoning

This directory contains the documentation and files for the inference rules that can be used with this ontology.

## Inference

It may be useful to automatically infer some triples on some data in order to be able to do more meaningful SPARQL requests.

#### Kinship rules

The file [kinship.rules](kinship.rules) contains rules in the [Jena rules format](https://jena.apache.org/documentation/inference/#rules) that can be used to infer triples linked to kinship. As an example in natural language:

```
If a is a male and has b as brother, then b has a as brother.
```

#### Subclass/Subproperty inferences

The ontology schema uses a lot of subproperties and subclasses, but you may not want to add all the triples for that, as not all are meaningful from a SPARQL request point of view. The classes and properties for which we advise to use inference have the annotation `:inferSubTree` set to `true`.

#### Other inferences

The schema uses a few `owl:SymmetricProperty` and `owl:inverseOf`.


## Validation

The schema uses usual OWL validation techniques, setting `range` and `domain` everywhere it is relevant. Some rules for Kinship and other specific validation may appear in the future.