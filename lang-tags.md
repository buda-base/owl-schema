# Conventions for lang tags to be used in the ontology

This document describes some conventions BDRC is using for BCP-47 lang tags in its data.

## General conventions

#### The RDF and BCP-47 specifications

The [RDF-1.1 specification](https://www.w3.org/TR/rdf11-concepts/#h3_section-Graph-Literal) states that language tags must be well-formed according to [section 2.2.9](http://tools.ietf.org/html/bcp47#section-2.2.9) of [BCP-47](http://tools.ietf.org/html/bcp47). Checking if an RDF tag is well-formed is relatively easy and an [online validator](http://schneegans.de/lv/) is available.

A list of standardized BCP-47 tags are available in the [IANA registry](https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry).

#### Canonical form vs. lower case form

A feature of RDF + BCP-47 is quite surprising: while BCP-47 [specifies](https://tools.ietf.org/html/bcp47#section-2.1.1) that tags case should not carry meaning, the RDF-1.1 spec [specifies](https://www.w3.org/TR/rdf11-concepts/#h3_section-Graph-Literal) that literal term equality requires an equality character by character (thus case sensitive) of their language tags. This can leads to strange results (cf. [some](https://github.com/jsonld-java/jsonld-java/issues/199) bug [reports](https://issues.apache.org/jira/browse/JENA-1377)). 

So in order to prevent bugs from happening it is important to define a convention on BCP-47 case. Two candidates immediately arise:

- The BCP-47 canonical form (ex: `zh-Latn-pinyin`)
- The lower-case form (ex: `zh-latn-pinyin`), which seems to have been the preferred one for RDF-1.0.

As the canonical form is well defined and is what RDF softwares (Jena at least) use for normalizing literals, it seems the best choice, so we use it.

#### Adding the script tag for transliteration?

For some transliterations, the question of the script tag arises. Let’s take the EWTS as an example. If we take ewts as the private tag, two well-formed choices can be used:

- `bo-Latn-x-ewts`
- `bo-x-ewts`

The script tag use is subject to some subjectivity, and is detailed in [section 4.1](https://tools.ietf.org/html/bcp47#section-4.1).

The arguments against its use in our case would be that ewts is always in Latn script, so it adds no information to the tag.

The arguments for using it are that it seems to be kept in some IANA standard tags where it adds no information neither, like `zh-Latn-pinyin`.

The convention used by BDRC is not to use it when not mandatory.

## Specific Tag conventions

#### ALA-LC transliteration (all languages)

[ALA-LC](https://www.loc.gov/catdir/cpso/roman.html) is the only transliteration schema that is documented in some specifications. There are two different standards to specify it:

- the tag standardized in IANA registry: `-alalc97` (ex: `sa-alalc97`)
- the name `alaloc` is used in the [CLDR data](http://unicode.org/repos/cldr/trunk/common/bcp47/transform.xml) ([doc](http://www.unicode.org/reports/tr35/#BCP47_T_Extension), [source](https://www.iana.org/assignments/language-tag-extensions-registry/language-tag-extensions-registry)). It seems the way to use the CLDR tag would be by adding the suffix `-t-m0-alaloc` to the language (ex: `sa-t-m0-alaloc`).

We opened two tickets on the CLDR data to get some transliteration scheme normalized: [EWTS](http://unicode.org/cldr/trac/ticket/10547) and [IAST](http://unicode.org/cldr/trac/ticket/10548).

The convention BDRC uses is to use the IANA name.

#### Phonetic transcription

TODO

#### Language mixing

When a string contains multiple languages, we use the [Unicode T extension mechanism](http://www.unicode.org/reports/tr35/#BCP47_T_Extension), for example for English mixed with Tibetan we would have `en-t-bo-h0-hybrid`.

#### Chinese
Most Chinese tags are all standardized so their choice is easy:

- `zh-Hans` for simplified Chinese characters
- `zh-Hant` for traditional Chinese characters
- `zh-Latn-pinyin` for Pinyin transliteration
- `zh-x-wade` for Wade-Giles transliteration

#### Pali
For Pali our convention is to always use a script tag:

- `pi-Sinh` for Pali written in Sinhalese script
- `pi-Thai` for Pali written in Thai script
- `pi-x-iast` (BDRC) for Pali written in [IAST](https://en.wikipedia.org/wiki/International_Alphabet_of_Sanskrit_Transliteration)

#### Sanskrit
We also choose to keep the script tag for Sanskrit in Devanagari:

- `sa-Deva` for Sanskrit written in Devanagari
- `sa-Tibt` for Sanskrit transliterated into Tibetan
- `sa-x-iast` for Sanskrit written in [IAST](https://en.wikipedia.org/wiki/International_Alphabet_of_Sanskrit_Transliteration)
- `sa-x-ndia` for Sanskrit written in IAST with no diacritics
- `sa-x-slp1` for Sanskrit written in [SLP1](http://www.sanskrit-lexicon.uni-koeln.de/talkMay2008/SLP1.pdf)
- `sa-x-iso` for Sanskrit written in [ISO 15919](https://en.wikipedia.org/wiki/ISO_15919)
- `sa-Deva-bauddha` for Buddhist Hybrid Sanskrit (*BHS*) written in Devanagari
- `sa-bauddha-x-iast` for  Buddhist Hybrid Sanskrit (*BHS*) written in IAST

#### Tibetan
For Tibetan we do not keep the `-Tibt` script tag, although it would be legitimate to keep it as the IANA registry doesn't specify `Suppress-Script: Tibt` for the bo language. We thus have:

- `bo` for Tibetan written in Tibetan script
- `bo-x-ewts` for EWTS transliteration
- `bo-x-gbt` for precomposed Tibetan (see [here](https://sites.google.com/site/chrisfynn2/home/tibetanscriptfonts/standardization/precomposedtibetan-parta/precomposed-tibetan---part-a) and [here](https://sites.google.com/site/chrisfynn2/home/tibetanscriptfonts/standardization/precomposed-tibetan-part-b))
- `bo-x-acip` for ACIP transliteration