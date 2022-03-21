#from project import class
#from project.file import class
import csv

class UzMorphAnalyser:
    __affixes = [] #list of affixes table from affixes.csv file
    __small_words = [] #list of small words from small_words.csv file
    __non_affixed_words = []  # list of non affixed words from non_affixed_words.csv file
    __exception_words = []  # list of exception words from exception_words.csv file

    def __init__(self):
        self.__read_data()

    def __read_data(self):
        with open("affixes.csv", "r") as f:
            reader = csv.DictReader(f)
            self.__affixes = list(reader)
        with open("small_words.csv", "r") as f:
            reader = csv.reader(f)
            #self.__small_words = list(reader)
            self.__small_words = [item for sublist in list(reader) for item in sublist]
        with open("non_affixed_words.csv", "r") as f:
            reader = csv.reader(f)
            #self.__small_words = list(reader)
            self.__non_affixed_words = [item for sublist in list(reader) for item in sublist]
        with open("exception_words.csv", "r") as f:
            reader = csv.DictReader(f)
            self.__exception_words = list(reader)
    #enf of read_data

    #affixes.csv da barcha allomorphlarni qulda generate qilib yozib quyamiz, dastur yordamida qilmaymiz, chalkash joylari kup
    #bu generate funksiya faqat boshda qavsli turganiga va boshda turgan katta harfliga tugri keladi.
    def __GeneratedAllomorph(self, affix): #return a list that contain all allomorphs of the current affix
        GenAff=[]
        #if allomorph has omitted letter # qavsli faqat affix boshida keladi
        if affix[0]=="(":
            GenAff.append( affix.replace("(", "").replace(")","")  ) #affix[1]+affix[3:] #qavsdagi bilan olish
            GenAff.append( affix[affix.find(")")+1:] ) #qavsdan keyingilarini olish
            return GenAff
        #if allomorph has uppper letter (several letters)
        if (affix[0]).isupper():
            if affix[0] == "G": #G:g,k,q
                GenAff.append("g" + affix[1:])
                GenAff.append("k" + affix[1:])
                GenAff.append("q" + affix[1:])
            if affix[0] == "K": #K:g,k
                GenAff.append("g" + affix[1:])
                GenAff.append("k" + affix[1:])
            if affix[0] == "Y": #Y:a,y
                GenAff.append("a" + affix[1:])
                GenAff.append("y" + affix[1:])
            if affix[0] == "T": #T:t,d
                GenAff.append("t" + affix[1:])
                GenAff.append("d" + affix[1:])
            if affix[0] == "Q": #Q:g,g',k,q
                GenAff.append("g" + affix[1:])
                GenAff.append("gʻ" + affix[1:])
                GenAff.append("k" + affix[1:])
                GenAff.append("q" + affix[1:])
            return GenAff
        GenAff.append(affix)
        return GenAff #if the affix does't have allomorph then return itself
    #end of Generate

    def stem(self, word: str):

        def stem_find(self, word:str, position:int=2):
            for i in range(position, len(word)):
                #predict_as_affix = word[i:]
                for item in self.__affixes:
                    if word[i:] in self.__GeneratedAllomorph(item["affix"]):
                        #print(position)
                        #print(self.__GeneratedAllomorph(item["affix"]))
                        #print(word[i:])
                        #print(item["affix"])
                        #print(self.__exception_words)
                        #print(item["confidence"])
                        if float(item["confidence"]) < 0.3:
                            if word in [ex_word['word'] for ex_word in self.__exception_words]:
                                return word
                        return word[:i]
            return word
        #end of stem_find

        #algorithm
        #1. check non affixed words list
        if word in self.__non_affixed_words:
            return word

        #2. find stem by affix checking from affixes list
        stem = stem_find(self, word)
        if len(stem)<=2:
            if not stem in self.__small_words:
                stem=stem_find(self, word, 3)

        return stem
        #end of stem

    def lemma(self, word: str, POS: str="n"):
        return word

    def lemmatize(self, word: str, POS: str = "n"):
        #lemmatize da list qaytadi, bir nechta lemmalari bulishi mumkin, barchasi qaytadi
        return word

    def analyze(self, word):
        return word
    #shu yuqoridagi funksiyalarni yozamiz, pastdagilar esa keyinroq

    def normalize(self, word):
        return word

    def word_tokenize(self, text):
        tokens=[]
        return tokens

    def sent_tokenize(self, text):
        tokens=[]
        return tokens

obj = UzMorphAnalyser()
sent = "kitob daftar"
for token in sent.split(" "):
    print(obj.stem(token))

#print(UzMorphAnalyser.stem("meniki"))

#print(analyzer.lemmatize('benim'))
#[('benim', ['ben'])]

#print(analyzer.analyze('benim'))
#Parse(word='benim', lemma='ben', pos='Noun', morphemes=['Noun', 'A3sg', 'P1sg'], formatted='[ben:Noun] ben:Noun+A3sg+im:P1sg')
#Parse(word='benim', lemma='ben', pos='Pron', morphemes=['Pron', 'A1sg', 'Gen'], formatted='[ben:Pron,Pers] ben:Pron+A1sg+im:Gen')
#Parse(word='benim', lemma='ben', pos='Verb', morphemes=['Noun', 'A3sg', 'Zero', 'Verb', 'Pres', 'A1sg'], formatted='[ben:Noun] ben:Noun+A3sg|Zero→Verb+Pres+im:A1sg')
#Parse(word='benim', lemma='ben', pos='Verb', morphemes=['Pron', 'A1sg', 'Zero', 'Verb', 'Pres', 'A1sg'], formatted='[ben:Pron,Pers] ben:Pron+A1sg|Zero→Verb+Pres+im:A1sg')

