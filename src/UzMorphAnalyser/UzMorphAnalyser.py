# from project import class
# from project.file import class
import csv
import os


class UzMorphAnalyser:
    __affixes = []  # list of affixes table from affixes.csv file
    __small_stems = []  # list of small stems from small_stems.csv file
    __non_affixed_stems = []  # list of non affixed stems from non_affixed_stems.csv file
    __number_stems = []  # list of number stems from number_stems.csv file
    __exception_stems = []  # list of exception stems from exception_stems.csv file
    # __ambiguity_stems = []  # list of ambiguity stems from ambiguity_stems.csv file | oxiri affix bn tugaydigan asos suzlar
    __vovel = ['a', 'u', 'e', 'i', 'o']
    __consonant_hard = ['b', 'd', 'g', 'j', 'l', 'm', 'n', 'r', 'v', 'y', 'z', "g'", 'ng']  # jarangli undosh
    __consonant_soft = ['f', 'h', 'k', 'p', 'q', 's', 't', 'x', 'sh', 'ch']  # jarangsiz undosh

    def __init__(self):
        self.__read_data()

    def __read_data(self):
        # url = 'http://u92156l3.beget.tech/affix/export.php', it couldn't be get from url
        dirname = os.path.dirname(__file__) + "/"

        with open(os.path.join(dirname + "affixes.csv"), "r") as f:
            reader = csv.DictReader(f)
            self.__affixes = list(reader)
        with open(os.path.join(dirname + "small_stems.csv"), "r") as f:
            reader = csv.reader(f)
            # self.__small_stems = list(reader)
            self.__small_stems = [item for sublist in list(reader) for item in sublist]
        with open(os.path.join(dirname + "non_affixed_stems.csv"), "r") as f:
            reader = csv.DictReader(f)
            self.__non_affixed_stems = list(reader)
            # reader = csv.reader(f)
            # self.__non_affixed_stems = [item for sublist in list(reader) for item in sublist]

        with open(os.path.join(dirname + "number_stems.csv"), "r") as f:
            reader = csv.reader(f)
            # self.__small_stems = list(reader)
            self.__number_stems = [item for sublist in list(reader) for item in sublist]
        # with open("ambiguity_stems.csv", "r") as f:
        #    reader = csv.DictReader(f)
        #    self.__ambiguity_stems = list(reader)
        with open(os.path.join(dirname + "exception_stems.csv"), "r") as f:
            reader = csv.DictReader(f)
            self.__exception_stems = list(reader)
        # enf of read_data

    # affixes.csv da barcha allomorphlarni qulda generate qilib yozib quyamiz, dastur yordamida qilmaymiz, chalkash joylari kup
    # bu generate funksiya faqat qavs ichida bitta harf (katta/kichik) turganda va bitta katta harf mavjud bulganda tugri keladi.
    def __GeneratedAllomorph(self, affix):  # return a list that contain all allomorphs of the current affix
        GenAff = []
        # if allomorph has omitted letter # qavsli faqat affix boshida keladi
        parentesis = False  # is exist parentesis
        affix_v1, affix_v2 = "", ""  # v1-qavs ichidagi bn, v2-qavs ichidagisiz qushimcha
        uc_v1, uc_v2 = -1, -1  # postion of uppercase in affix

        if affix[0] == "(":
            affix_v1 = affix.replace("(", "").replace(")", "")  # affix[1]+affix[3:] #qavs ichidagi bilan olish
            affix_v2 = affix[affix.find(")") + 1:]  # qavs ichidagisiz olish
            parentesis = True
        else:
            affix_v1 = affix

        # if allomorph has uppper letter (several letters)
        for i in range(len(affix_v1)):
            if affix_v1[i].isupper():
                uc_v1 = i
                break
        for i in range(len(affix_v2)):
            if affix_v2[i].isupper():
                uc_v2 = i
                break

        if uc_v1 > -1:
            if affix_v1[uc_v1] == "G":  # G:g,k,q
                GenAff.append(affix_v1[:uc_v1] + "g" + affix_v1[uc_v1 + 1:])
                GenAff.append(affix_v1[:uc_v1] + "k" + affix_v1[uc_v1 + 1:])
                GenAff.append(affix_v1[:uc_v1] + "q" + affix_v1[uc_v1 + 1:])
            if affix_v1[uc_v1] == "K":  # K:g,k
                GenAff.append(affix_v1[:uc_v1] + "g" + affix_v1[uc_v1 + 1:])
                GenAff.append(affix_v1[:uc_v1] + "k" + affix_v1[uc_v1 + 1:])
            if affix_v1[uc_v1] == "Y":  # Y:a,y
                GenAff.append(affix_v1[:uc_v1] + "a" + affix_v1[uc_v1 + 1:])
                GenAff.append(affix_v1[:uc_v1] + "y" + affix_v1[uc_v1 + 1:])
            if affix_v1[uc_v1] == "T":  # T:t,d
                GenAff.append(affix_v1[:uc_v1] + "t" + affix_v1[uc_v1 + 1:])
                GenAff.append(affix_v1[:uc_v1] + "d" + affix_v1[uc_v1 + 1:])
            if affix_v1[uc_v1] == "Q":  # Q:g,g',k,q
                GenAff.append(affix_v1[:uc_v1] + "g" + affix_v1[uc_v1 + 1:])
                GenAff.append(affix_v1[:uc_v1] + "gʻ" + affix_v1[uc_v1 + 1:])
                GenAff.append(affix_v1[:uc_v1] + "k" + affix_v1[uc_v1 + 1:])
                GenAff.append(affix_v1[:uc_v1] + "q" + affix_v1[uc_v1 + 1:])

            if uc_v2 > -1:  # bu uc_v1 bulgandagina bulishi mumkin, shuni uchun uni ichida
                if affix_v2[uc_v2] == "G":  # G:g,k,q
                    GenAff.append(affix_v2[:uc_v2] + "g" + affix_v2[uc_v2 + 1:])
                    GenAff.append(affix_v2[:uc_v2] + "k" + affix_v2[uc_v2 + 1:])
                    GenAff.append(affix_v2[:uc_v2] + "q" + affix_v2[uc_v2 + 1:])
                if affix_v2[uc_v2] == "K":  # K:g,k
                    GenAff.append(affix_v2[:uc_v2] + "g" + affix_v2[uc_v2 + 1:])
                    GenAff.append(affix_v2[:uc_v2] + "k" + affix_v2[uc_v2 + 1:])
                if affix_v2[uc_v2] == "Y":  # Y:a,y
                    GenAff.append(affix_v2[:uc_v2] + "a" + affix_v2[uc_v2 + 1:])
                    GenAff.append(affix_v2[:uc_v2] + "y" + affix_v2[uc_v2 + 1:])
                if affix_v2[uc_v2] == "T":  # T:t,d
                    GenAff.append(affix_v2[:uc_v2] + "t" + affix_v2[uc_v2 + 1:])
                    GenAff.append(affix_v2[:uc_v2] + "d" + affix_v2[uc_v2 + 1:])
                if affix_v2[uc_v2] == "Q":  # Q:g,g',k,q
                    GenAff.append(affix_v2[:uc_v2] + "g" + affix_v2[uc_v2 + 1:])
                    GenAff.append(affix_v2[:uc_v2] + "gʻ" + affix_v2[uc_v2 + 1:])
                    GenAff.append(affix_v2[:uc_v2] + "k" + affix_v2[uc_v2 + 1:])
                    GenAff.append(affix_v2[:uc_v2] + "q" + affix_v2[uc_v2 + 1:])
            return GenAff

        if parentesis:  # agar yuqorida return bub ketmasa
            GenAff.append(affix_v1)
            GenAff.append(affix_v2)
        else:
            GenAff.append(affix)
        return GenAff
        # end of Generate Allmorph

    # stemni ichidagilarni alohida metodni ichiga ol, keyin undan umumiy holda yani stem, lemma, analyse metodlaridan foydalanamiz

    def __processing(self, word: str, pos: str = None):

        def stem_find_exceptions(self, word: str, pos: str, position: int):
            if pos is not None:
                ex_stem_list = [ex_stem for ex_stem in self.__exception_stems if ex_stem['pos'] == pos]
            else:
                ex_stem_list = [ex_stem for ex_stem in self.__exception_stems]

            for i in range(position, len(word) + 1):  # +1 bu word[:i] i+1 yani oxirgisigacha olishi uchun
                print("cnf suz == " + word[:i])
                ex_stem_find = list(filter(lambda ex_stem: ex_stem['stem'] == word[:i], ex_stem_list))  # pythonic way -> https://stackoverflow.com/questions/8653516/python-list-of-dictionaries-search
                if ex_stem_find:
                    print(ex_stem_find)
                    return True, ex_stem_find[0]
                # if word[:i] in ex_stem_list:
                #    return True, {'stem': word[:i], 'pos':}  #return two value, stem from exception
            return False, ""

        def stem_find(self, word: str, pos: str, position: int = 1):
            affixes = []
            if pos is not None:  # if "pos" argument is given, "pos" argument may be given in lemmatize
                affixes = [i for i in self.__affixes if i['pos'] == pos]
            else:
                affixes = self.__affixes

            for i in range(position, len(word)):
                # predict_as_stem = word[:i]
                # predict_as_affix = word[i:]
                for item in affixes:
                    if word[i:] in self.__GeneratedAllomorph(item["affix"]):
                        print(self.__GeneratedAllomorph(item["affix"]))
                        # print(position)
                        # print(self.__GeneratedAllomorph(item["affix"]))
                        # print(word[:i]+" "+word[i:]+" "+item["affix"])
                        # print(word[i:])
                        # print(item["affix"])
                        # print(self.__exception_stems)
                        # print(item["confidence"])

                        # 6-rule Ga{ga,ka,qa,} bulardan ka, qa g'a uchun undan oldingi xarf shu affixni birinchi harfi bn tugagan bulishi kerak

                        # 1-support rule:
                        if item['pos'] == self.POS.NUM:
                            if word[:i] in self.__number_stems:
                                item['stem'] = word[:i]  # add stem key_value to item dictionary from affixes
                                return item
                            else:
                                break

                        # exception dan suzlarni tekshirib olish
                        if len(word[i:]) <= 3:  # 3 bu yerda fine-tuning qilingan, yani 3 harfdan katta qushimchalarda xatolik bulmaydi va bundaylarni tugri qirqsak buladi
                            result, stem_ex = stem_find_exceptions(self, word, pos, i + 1)
                            if result:
                                return stem_ex
                        #

                        # 2.1-rule qushimchasi topilgandan keyin oldingi turgan stem small_stemni ichida bormi yuqmi
                        if i <= 2:  # i==2 bulsa 0 va 1 belgini oladi, [:2] da 2 ikkini uzi kirmaydi
                            if word[:i] in self.__small_stems:
                                item['stem'] = word[:i]
                                return item
                            else:
                                break

                        # 2.2-rule confidence past bulgan suzlarni exception_words dan qaraydi.
                        # exwords da faqat affix bn tugaydigan suzlar turadi.
                        # agar suz exwordda bulsa qirqmaydi va alternativini qaraydi,
                        # aks holda yani suz exwordda bulmasa qirqib tashlaydi
                        if float(item["confidence"]) <= 0.1 and False:
                            # print("affix "+item['affix'])
                            # 3-rule
                            # if word in [ambg_stem['stem'] for ambg_stem in self.__ambiguity_stems]:
                            #    return word
                            # 4-rule
                            stem_ex, result = stem_find_exceptions(self, word, i)
                            # print(stem_ex+" "+str(result))
                            if result:
                                return stem_ex
                            else:
                                break  # confidence past bulgan qushimchasi bn borib ex_stemni qidiradi, buni ichida bundin stem bulmasa qirqmay utib ketadi
                        item['stem'] = word[:i]
                        return item  # chopping with 100% confidence
            return {'stem': word}

        # end of stem_find

        # algorithm for stem
        # 1-step: check non affixed words list
        for na_stem in self.__non_affixed_stems:
            if word in na_stem['stem']:
                return {'stem': word, 'pos': na_stem['pos']}

        ##if word in [na_stem['stem'] for na_stem in self.__non_affixed_stems]: # in self.__non_affixed_stems
        ##    return word

        # 2-step sat faqat ko'rsat bulganda qirqiladi (so'zni boshi ko'rsat ga teng bulganda)
        if word[:7] == "ko'rsat":
            return {'stem': "ko'r", 'pos': self.POS.VERB}
        # 3-step find stem by affix checking from affixes list
        # print("stem_find")
        result = stem_find(self, word, pos)
        # if len(stem)<=2:    #checking the small stem is exist or not
        #    if not stem in self.__small_stems:
        #        stem=stem_find(self, word, 3)

        return result
        # end of processing

    def stem(self, word: str):
        ff = self.__processing(word)
        print(ff)
        return ff['stem']  # dict['stem] == dict.get('stem')

    def lemmatize(self, word: str, pos: str = None):
        # lemmatize da list qaytadi, bir nechta lemmalari bulishi mumkin, barchasi qaytadi
        ff = self.__processing(word, pos)
        print(ff)
        return ff['stem']  # .get('stem')

    def analyze(self, word: str, pos: str = None):
        stem, affix = self.__processing(word, pos)
        # morpheme, bound morpheme [maktablar, maktab=morphem, lar=bound morphem]

        return

    def morphemes(self, word: str, pos: str = None):
        # preprocessing       ['pre', 'process', 'ing']
        # https://github.com/aboSamoor/polyglot/blob/master/notebooks/MorphologicalAnalysis.ipynb
        pass

    def pos(self):
        return (
            {'pos': 'NOUN', 'def': 'Noun'},
            {'pos': 'VERB', 'def': 'Verb'},
            {'pos': 'ADJ', 'def': 'Adjective'},
            {'pos': 'NUM', 'def': 'Number'},
            {'pos': 'ADV', 'def': 'Adverb'},
            {'pos': 'PRN', 'def': 'Pronoun'}
        )

    class POS:
        NOUN = "NOUN"  # Noun
        VERB = "VERB"  # Verb
        ADJ = "ADJ"  # Adjective
        NUM = "NUM"  # Numeric
        ADV = "ADV"  # Adverb
        PRN = "PRN"  # Pronoun

    # shu yuqoridagi funksiyalarni yozamiz, pastdagilar esa keyinroq

    def normalize(self, text: str):
        # normalize text is making stemming and lemmatization
        # Mening maktabim senikidan chiroyliroq -> men maktab sen chiroyli
        return "word"

    def word_tokenize(self, text):
        tokens = []
        return tokens

    def sent_tokenize(self, text):
        tokens = []
        return tokens


obj = UzMorphAnalyser()

sent = "olmasi taqgandim olma taqdimmi kurs kursi gacha namuna ko'plab ular bular sizlar kuchli shanba yuztagacha yuztaga kursi eksport eksportidan masjid masjidi tuman tumani tumanimizni taqdim taqdimi barmoqi barmoq muzqaymoq"

with open(os.path.join(os.path.dirname(__file__) + "/" + "test.txt"), 'r', encoding='utf8') as file:
    sent1 = file.read().rstrip()

sent1 = sent1.replace(',', ' ')
sent1 = sent1.replace('.', ' ')
sent1 = sent1.replace('\n', ' ')
for token in sent.split(" "):
    print(token + ' ' + obj.stem(token.lower()))

while (True):
    s = input()
    print(s + ' ' + obj.lemmatize(s.lower(), obj.POS.NUM))

# print(UzMorphAnalyser.stem("meniki"))

# print(analyzer.lemmatize('benim'))
# [('benim', ['ben'])]

# print(analyzer.analyze('benim'))
# Parse(word='benim', lemma='ben', pos='Noun', morphemes=['Noun', 'A3sg', 'P1sg'], formatted='[ben:Noun] ben:Noun+A3sg+im:P1sg')
# Parse(word='benim', lemma='ben', pos='Pron', morphemes=['Pron', 'A1sg', 'Gen'], formatted='[ben:Pron,Pers] ben:Pron+A1sg+im:Gen')
# Parse(word='benim', lemma='ben', pos='Verb', morphemes=['Noun', 'A3sg', 'Zero', 'Verb', 'Pres', 'A1sg'], formatted='[ben:Noun] ben:Noun+A3sg|Zero→Verb+Pres+im:A1sg')
# Parse(word='benim', lemma='ben', pos='Verb', morphemes=['Pron', 'A1sg', 'Zero', 'Verb', 'Pres', 'A1sg'], formatted='[ben:Pron,Pers] ben:Pron+A1sg|Zero→Verb+Pres+im:A1sg')

# (s)i opasi kitobi larda yi varianti xam bor, avzoyi, obro'yi (S)i shaklida olsak, bunda S{s,y} buladi. Manba:https://lex.uz/docs/-1625271

# tovush uzgarishlarini lemmatize ga kiritish
anylyse kurinishini qilish parse ga uxshab
bazani tuliq holga keltirish