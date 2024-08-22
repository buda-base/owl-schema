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

It's important to note that the RDF 1.1 Spec seems to have two modes (indicated by a `MAY`): 
- one in which lang tags are always converted to lower-case and literal term equality compares lower-cased lang tags (this path is taken by [JSON-LD](https://github.com/json-ld/json-ld.org/issues/533), but not by [Jena](https://issues.apache.org/jira/browse/JENA-1377))
- one in which lang tags are not converted to lower-case and literal term equality compares the original lang tags

It's also important to note that some triple stores (like Jena Fuseki) only store literal values, not terms, in which case it will only store lower-cased language tags.

This means that you will always retrieve lower-cased language tags when dealing with
- formats or softwares taking advantage of the possibility offered by the `MAY` clause of RDF 1.1 (like JSON-LD)
- softwares only storing values and not terms (like Jena Fuseki)

In order to get as few bugs and surprises as possible and to be able to use RDF literal equality in all contexts, it seems thus best to use lower-cased values. The rest of the document will use BCP-47 canonical tags for the sake of readability, but make sure you do use only lower-cased forms in your data.

### Specifying the script tag?
#### In transliterations

For some transliterations, the question of the script tag arises. Let’s take the EWTS as an example. If we take ewts as the private tag, two well-formed choices can be used:

- `bo-Latn-x-ewts`
- `bo-x-ewts`

The script tag use is subject to some subjectivity, and is detailed in [section 4.1](https://tools.ietf.org/html/bcp47#section-4.1).

The arguments against its use in our case would be that ewts is always in Latn script, so it adds no information to the tag.

The arguments for using it are that it seems to be kept in some IANA standard tags where it adds no information neither, like `zh-Latn-pinyin`.

The convention used by BDRC is not to use it when not mandatory. See parts of [this thread](https://www.ietf.org/mail-archive/web/ietf-languages/current/msg00210.html) for some elements on this issue.

#### In more obvious cases

The two main sources to take the decision in the more common cases (such as `bo` vs. `bo-Tibt`) are:
- the `Suppress-Script` tags of the IANA registry
- the [Likely Subtags](https://www.unicode.org/cldr/charts/latest/supplemental/likely_subtags.html) list of CLDR

See [this thread](https://www.ietf.org/mail-archive/web/ietf-languages/current/msg00278.html) for more information on this. We do not follow any strict rule here, but tend to prefer simple tags over complex ones.

## Specific Tag conventions

#### ALA-LC transliteration (all languages)

[ALA-LC](https://www.loc.gov/catdir/cpso/roman.html) is the only transliteration schema that is documented in some specifications. There are two different standards to specify it:

- the tag standardized in IANA registry: `-alalc97` (ex: `sa-alalc97`)
- the name `alaloc` is used in the [CLDR data](http://unicode.org/repos/cldr/trunk/common/bcp47/transform.xml) ([doc](http://www.unicode.org/reports/tr35/#BCP47_T_Extension), [source](https://www.iana.org/assignments/language-tag-extensions-registry/language-tag-extensions-registry)). The way to use the CLDR tag is indicated in [RFC6497](https://tools.ietf.org/html/rfc6497) and would be for example for Sanskrit `sa-t-sa-m0-alaloc`.

We opened two tickets on the CLDR data to get some transliteration scheme normalized: [EWTS](http://unicode.org/cldr/trac/ticket/10547) and [IAST](http://unicode.org/cldr/trac/ticket/10548).

The convention BDRC uses is to use the IANA name (`sa-alalc97`, `bo-alalc97`, etc.).

#### Phonetic transcription

There does not seem to be any guideline on the way to encode phonetic transcriptions in BCP-47. We chose the following convention: `A-x-phon-B(-m-C)` where:
- `A` is the full BCP-47 tag of the source language, without the script tag as this information should be made clear in `B`
- `B` is the full BCP-47 tag of the language of the pronunciation, it should include a script tag when ambiguous
- `C` is the type of phonetic transcription, when phonetics follows a particular standard; this part (and the preceding `-m-`) can be omitted

Examples:
- `bo-x-phon-en-m-tbrc` would be Tibetan transcribed in English with the TBRC phonetic conventions (`A` is `bo`, `B` is `en`, `C` is `tbrc`)

#### Language mixing

When a string contains multiple languages, we use the [Unicode T extension mechanism](http://www.unicode.org/reports/tr35/#BCP47_T_Extension), for example for English mixed with Tibetan we would have `en-t-bo-h0-hybrid`.

#### Chinese
Most Chinese tags are all standardized so their choice is easy:

- `zh-Hani` for Chinese in Chinese characters (simplified vs. traditional undetermined)
- `zh-Hans` for simplified Chinese characters
- `zh-Hant` for traditional Chinese characters
- `zh-Latn-pinyin` for Pinyin transliteration
- `zh-Latn-pinyin-x-ndia` for Pinyin transliteration with no diacritics
- `zh-Latn-wadegile` for Wade-Giles transliteration
- `zh-x-phon-en` for Chinese in phonetics with an English style
- `zh-Tibt` for Chinese written in Tibetan script
- `zh-x-ewts` for Chinese written in Tibetan script, transliterated in EWTS (`zh-x-dts`, `zh-x-acip` and `zh-x-gbt` follow the same pattern)

#### Pali
For Pali our convention is to always use a script tag:

- `pi-Sinh` for Pali written in Sinhalese script
- `pi-Mymr` for Pali written in Myanmar script
- `pi-Thai` for Pali written in Thai script
- `pi-x-iast` (BDRC) for Pali written in [IAST](https://en.wikipedia.org/wiki/International_Alphabet_of_Sanskrit_Transliteration)
- `pi-Khmr` for Pali written in Khmer script
- `pi-x-efeo` for Pali written in Khmer via the EFEO romanization
- `pi-x-twktt-origKhmer` for Pali written in Khmer romanized via the [TWKTT](https://github.com/buda-base/twktt-doc/) romanization
- `pi-Khmr-x-kmpre20c` for Pali written in Khmer script using the archaic spelling predating any of the 20th-century reforms
- `pi-x-kmpre20c-efeo` for Pali written in Khmer script using the archaic spelling predating any of the 20th-century reforms transliterated using the EFEO romanization
- `pi-x-kmpre20c-twktt-origKhmer` for Pali written in Khmer script using the archaic spelling predating any of the 20th-century reforms transliterated using the [TWKTT](https://github.com/buda-base/twktt-doc/) romanization

#### Sanskrit
We also choose to keep the script tag for Sanskrit in Devanagari:

- `sa-Deva` for Sanskrit written in Devanagari
- `sa-Tibt` for Sanskrit transliterated into Tibetan
- `sa-x-ewts` for Sanskrit transliterated into Tibetan, in turn transliterated in EWTS (`sa-x-dts`, `sa-x-acip` and `sa-x-gbt` follow the same pattern)
- `sa-x-Tibt-alalc97` (?) for Sanskrit transliterated into Tibetan, in turn transliterated in ALA-LC
- `sa-x-iast` for Sanskrit written in [IAST](https://en.wikipedia.org/wiki/International_Alphabet_of_Sanskrit_Transliteration)
- `sa-x-haky` for Sanskrit written in [Harvard-Kyoto transliteration scheme](https://en.wikipedia.org/wiki/Harvard-Kyoto)
- `sa-x-ndia` for Sanskrit written in IAST with no diacritics
- `sa-x-slp1` for Sanskrit written in [SLP1](http://www.sanskrit-lexicon.uni-koeln.de/talkMay2008/SLP1.pdf)
- `sa-x-iso` for Sanskrit written in [ISO 15919](https://en.wikipedia.org/wiki/ISO_15919)
- `sa-Deva-bauddha` for Buddhist Hybrid Sanskrit (*BHS*) written in Devanagari
- `sa-bauddha-x-iast` for Buddhist Hybrid Sanskrit (*BHS*) written in IAST
- `sa-x-phon-zh-Hant` for Sanskrit written in Traditional Chinese characters

#### Tibetan
For Tibetan we do not keep the `-Tibt` script tag. We thus have:

- `bo` for Tibetan written in Tibetan script
- `bo-x-ewts` for [EWTS](http://www.thlib.org/reference/transliteration/#essay=/thl/ewts/) transliteration
- `bo-x-gbt` for precomposed Tibetan (see [here](https://sites.google.com/site/chrisfynn2/home/tibetanscriptfonts/standardization/precomposedtibetan-parta/precomposed-tibetan---part-a) and [here](https://sites.google.com/site/chrisfynn2/home/tibetanscriptfonts/standardization/precomposed-tibetan-part-b))
- `bo-x-acip` for ACIP transliteration
- `bo-Latn-pinyin` for Pinyin phonetic transcription
- `bo-x-dts` for a transliteration scheme sometimes called `Diacritical Transliteration Scheme` (DTS), used in some works ([ex1](https://www.tbrc.org/#!rid=W1KG13703), [ex2](https://www.tbrc.org/#!rid=W1PD95677))
- `bo-x-phon-zh-Hant` for Tibetan written in Traditional Chinese characters
- `bo-alalc97` for Tibetan transliterated following ALA-LC rules
- `bo-x-phon-en-m-tbrc` for Tibetan transcribed in English with the TBRC phonetic conventions
- `bo-x-phon-en-m-thlib` for Tibetan transcribed in English with the [Thlib phonetic conventions](http://www.thlib.org/reference/transliteration/#!essay=/thl/phonetics/)

#### Khmer

- `km` for Khmer in Khmer script
- `km-x-twktt` for Khmer Romanized via the [TWKTT](https://github.com/buda-base/twktt-doc/) romanization
- `km-x-efeo` for Khmer Romanized via the EFEO romanization
- `km-x-kmpre20c` for Khmer written in Khmer script using the archaic spelling predating any of the 20th-century reforms
- `km-x-kmpre20c-efeo` for Khmer written in Khmer script using the archaic spelling predating any of the 20th-century reforms transliterated using the EFEO romanization
- `km-x-kmpre20c-twktt` for Khmer written in Khmer script using the archaic spelling predating any of the 20th-century reforms transliterated using the [TWKTT](https://github.com/buda-base/twktt-doc/) romanization

#### Mongolian

- `mn-Mong` for Classical Mongolian written in Mongolian script
- `mn-Cyrl` for Classical Mongolian written in Cyrillic script
- `mn-x-poppe` for Classical Mongolian using [Poppe](https://viaf.org/viaf/22157344)'s translitteration (the one used in his [Grammar](http://www.worldcat.org/oclc/888131043))
- `mn-x-poppe-simpl` same as previous but with simplifications (`č` -> `c`; `ǰ` -> `j`; `š` -> `sh`; `γ` -> `g`)

#### Rare languages

Some Burushaski titles appear from time to time in the Tibetan canon (see Derge Kangyur, vol. 97, p. 86b, l. 1). When written in Tibetan, they can be recorded with the tag `bsk-Tibt`. Zhangzhung language written in Tibetan script is `xzh-Tibt`.

## See also
- [BIBFRAME Conventions](http://connect.ala.org/node/271553) and [this thread](https://listserv.loc.gov/cgi-bin/wa?A1=ind1712&L=BIBFRAME#7)
- [The BIBFRAME And MARC Bibliographic Encoding for Languages (BABEL) Final Report](https://www.loc.gov/aba/pcc/taskgroup/BABEL-Final-Report.docx)
- [W3C guidelines](https://www.w3.org/International/questions/qa-choosing-language-tags)
- [SARIT Guidelines](http://sarit.indology.info/apps/sarit-pm/docs/encoding-guidelines-simple.html#The-xmlid-and-xmllang-attributes)
