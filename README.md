# UzMorphAnalyser

https://pypi.org/project/UzMorphAnalyser <br>
https://github.com/UlugbekSalaev/UzMorphAnalyser

UzMorpAnalyser tool is focused to make morphological analysis of Uzbek word based on morphemes. The tool includes Stemmer, Lemmatizer, Morphological Analyze methods.
It is created as a python library and uploaded to [PyPI](https://pypi.org/). It is simply easy to use in your python project or other programming language projects via the API. 

## About project
The tool is focused to make morphological analysis of Uzbek word based on morphemes. The tool includes Stemmer, Lemmatizer, Morphological Analyze methods.

## Quick links

- [Github](https://github.com/UlugbekSalaev/UzMorphAnalyser)
- [PyPI](https://pypi.org/project/UzMorphAnalyser/)
- [Web-UI](https://nlp.urdu.uz/?page=uzmorphanalyser)

## Demo

You can use [web interface](http://nlp.urdu.uz/?page=morphanalyser).

## Features

- Stemmer
- Lemmatizer
- Lemmatizer with POS tag
- Extract Morphemes list
- Analyzer
- Analyzer with POS tag

## Usage

Three options to run UzMorphAnalyser:

- pip
- API 
- Web interface

### pip installation

To install UzMorphAnalyser, simply run:

```code
pip install UzMorphAnalyser
```

After installation, use in python like following:
```yml
# import the library
from UzMorphAnalyser import UzMorphAnalyser
# create an object 
analyzer = UzMorphAnalyser()
# call stem method
analyzer.stem('maktabimda')
# call lemmatize method
analyzer.lemmatize('maktabimda')
# call lemmatize method with POS tag
analyzer.lemmatize('maktabimda', analyzer.POS.NOUN)
# call analyze method
analyzer.analyze('maktabimda')
# call analyze method with POS tag
analyzer.analyze('maktabimda', analyzer.POS.NOUN)
```

### API
API configurations: 
 - Method: GET
 - Response type: <code>string</code>


 - URL: https://nlp.urdu.uz:8080/uzmorphanalyser/stem
   - Parameters: <code>word:string</code></code>
   - Sample Request: https://nlp.urdu.uz:8080/uzmorphanalyser/stem?word=maktabimda


 - https://nlp.urdu.uz:8080/uzmorphanalyser/lemmatize
   - Parameters: <code>word:string</code>, <code>pos:string</code>
   - Sample Request: https://nlp.urdu.uz:8080/uzmorphanalyser/lemmatize?word=maktabimda&pos=NOUN


 - https://nlp.urdu.uz:8080/uzmorphanalyser/analyze
   - Parameters: <code>word:string</code>, <code>pos:string</code>
   - Sample Request: https://nlp.urdu.uz:8080/uzmorphanalyser/analyze?word=maktabimda&pos=NOUN

<i>Note: argument <code>pos</code> is optional in all methods</i>
### Web-UI

The web interface created to use easily the library:
You can use web interface [here](http://nlp.urdu.uz/?page=uzmorphanalyser).

![Demo image](./docs/images/web-interface-ui.png)


### Options
When you use PyPI or API, you should use following options as POS tag of a word which is optional parameters of `lemmatize()` and `analyze()` metods:<br>
    `NOUN`  Noun<br>
    `VERB`  Verb<br>
    `ADJ`   Adjective<br>
    `NUM`   Numerical<br>
    `PRN`   Pronoun<br>
    `ADV`   Adverb

_`pos` parameters is optional for `lemmatize` and `analyze` metods._

### Result Explaining

It returns single word in a string type from each method, `stem` and `lemmatize`, that is stem and lemma of given word, respectively. 
#### Result from `analyze` method
`analyze` method returns a response as list of dictionary which is may contain following keys: 
```yml
 {'word', 'lemma', 'pos', 'affix','affixed','tense','person','cases','singular','plural','question','negative','impulsion','copula','verb_voice','verb_func'}: 
```

## Documentation

See [here](https://github.com/UlugbekSalaev/UzMorphAnalyser).

## Citation

```tex
@CONFERENCE{Salaev2024,
	author = {Salaev, Ulugbek},
	title = {UzMorphAnalyser: A Morphological Analysis Model for the Uzbek Language Using Inflectional Endings},
	year = {2024},
	journal = {AIP Conference Proceedings},
	volume = {3244},
	number = {1},
	doi = {10.1063/5.0241461},
	url = {https://www.scopus.com/inward/record.uri?eid=2-s2.0-85212084325&doi=10.1063%2f5.0241461&partnerID=40&md5=2aebf2ea03ea0a3a7850c4fb867480ba},
	source = {Scopus},
}
```

## Contact

For help and feedback, please feel free to contact [the author](https://github.com/UlugbekSalaev).
