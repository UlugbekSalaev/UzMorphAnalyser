#from project import class
#from project.file import class
import csv

class UzMorphAnalyser:
    __data = []

    def __init__(self):
        self.__read_data()

    def __read_data(self):
        with open("data.csv", "r") as f:
            reader = csv.DictReader(f)
            self.__data = list(reader)

    def __GeneratedAllomorph(self, affix): #return a list that contain all allomorphs of the current affix
        GenAff=[]
        #agar qavsli allomorflari bulsa
        if affix[0]=="(":
            GenAff.append( affix[1]+affix[3:] ) #(affix.replace("(","")).replace(")","")
            GenAff.append( affix[3:] )
            return GenAff
        #agar katta harfli allomorflari bulsa
        if (affix[0]).isupper():
            if affix[0]=="G": #G:g,k,q
                GenAff.append("g" + affix[1:])
                GenAff.append("k" + affix[1:])
                GenAff.append("q" + affix[1:])
            if affix[0]== "K": #K:g,k
                GenAff.append("g" + affix[1:])
                GenAff.append("k" + affix[1:])
            if affix[0]=="Y": #Y:a,y
                GenAff.append("a" + affix[1:])
                GenAff.append("y" + affix[1:])
            if affix[0]=="T": #T:t,d
                GenAff.append("t" + affix[1:])
                GenAff.append("d" + affix[1:])
            if affix[0]=="Q": #Q:g,g',k,q
                GenAff.append("g" + affix[1:])
                GenAff.append("gʻ" + affix[1:])
                GenAff.append("k" + affix[1:])
                GenAff.append("q" + affix[1:])
            return GenAff
        return affix #agar allomorf bulmasa affixni uzini qaytaradi

    def stem(self, word):
        #root=word[:1]
        #affix=word[1:]
        #print(root, ' ', affix)
        #row=next((item for item in data if item["affix"] == affix), None)
        #if row==None:
        #    print(row)
        #else: print(row["affix"])

        size=len(word)
        for i in range(1, size):
            affix=word[i:]
            for item in self.__data:
                if(affix in self.__GeneratedAllomorph(item["affix"])):
                    return word[:i]
        return word

    def lemma(self, word):
        return word

    def lemmatize(self, word: str, POS: str = "n"):
        return word
        
    def analyze(self, word):
        return word

    def normalize(self, word):
        return word

    def word_tokenize(self, text):
        tokens=[]
        return tokens

    def sent_tokenize(self, text):
        tokens=[]
        return tokens

obj = UzMorphAnalyser()
print(obj.stem("meniki"))

#print(UzMorphAnalyser.stem("meniki"))

#print(analyzer.lemmatize('benim'))
#[('benim', ['ben'])]

#print(analyzer.analyze('benim'))
#Parse(word='benim', lemma='ben', pos='Noun', morphemes=['Noun', 'A3sg', 'P1sg'], formatted='[ben:Noun] ben:Noun+A3sg+im:P1sg')
#Parse(word='benim', lemma='ben', pos='Pron', morphemes=['Pron', 'A1sg', 'Gen'], formatted='[ben:Pron,Pers] ben:Pron+A1sg+im:Gen')
#Parse(word='benim', lemma='ben', pos='Verb', morphemes=['Noun', 'A3sg', 'Zero', 'Verb', 'Pres', 'A1sg'], formatted='[ben:Noun] ben:Noun+A3sg|Zero→Verb+Pres+im:A1sg')
#Parse(word='benim', lemma='ben', pos='Verb', morphemes=['Pron', 'A1sg', 'Zero', 'Verb', 'Pres', 'A1sg'], formatted='[ben:Pron,Pers] ben:Pron+A1sg|Zero→Verb+Pres+im:A1sg')

