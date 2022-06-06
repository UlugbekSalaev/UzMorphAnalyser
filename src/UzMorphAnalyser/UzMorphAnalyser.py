# from project import class
# from project.file import class
import csv
import os
#import time

class UzMorphAnalyser:
    __affixes = []  # list of affixes table from affixes.csv file
    __small_stems = []  # list of small stems from small_stems.csv file
    __non_affixed_stems = []  # list of non affixed stems from non_affixed_stems.csv file
    __number_stems = []  # list of number stems from number_stems.csv file
    __exception_stems = []  # list of exception stems from exception_stems.csv file
    __lemma_map = []  # list of lemma convertion mapping from lemma_map.csv file
    # __ambiguity_stems = []  # list of ambiguity stems from ambiguity_stems.csv file | oxiri affix bn tugaydigan asos suzlar

    __vovel = ['a', 'u', 'e', 'i', 'o']
    __consonant_hard = ['b', 'd', 'g', 'j', 'l', 'm', 'n', 'r', 'v', 'y', 'z', "g'", 'ng']  # jarangli undosh
    __consonant_soft = ['f', 'h', 'k', 'p', 'q', 's', 't', 'x', 'sh', 'ch']  # jarangsiz undosh

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
        '''if affix == '(S)i':
            print('-----------')
            print(affix_v1)
            print(affix_v2)
            print(uc_v1)
            print(uc_v2)
        '''
        if uc_v1 > -1:  # katta harfi bulgan varianti
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
            if affix_v1[uc_v1] == "S":  # S:s,y opasi,avzoyi
                GenAff.append(affix_v1[:uc_v1] + "s" + affix_v1[uc_v1 + 1:])
                GenAff.append(affix_v1[:uc_v1] + "y" + affix_v1[uc_v1 + 1:])
        else:
            GenAff.append(affix_v1)  # katta harfi bulmagan varianti

        if parentesis:
            if uc_v2 > -1:  # qavsli va katta harfli varianti
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
                if affix_v2[uc_v2] == "S":  # S:s,y
                    GenAff.append(affix_v2[:uc_v2] + "s" + affix_v2[uc_v2 + 1:])
                    GenAff.append(affix_v2[:uc_v2] + "y" + affix_v2[uc_v2 + 1:])
            else:
                GenAff.append(affix_v2)  # qavsli lekin Katta harfsiz varianti

        return GenAff
        # end of Generate Allmorph

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
        with open(os.path.join(dirname + "lemma_map.csv"), "r") as f:
            reader = csv.DictReader(f)
            self.__lemma_map = list(reader)

        # generate all allomorphs for each affix and allomorph list to affixes list
        for item in self.__affixes:
            item['allomorphs'] = self.__GeneratedAllomorph(item['affix'])

        # enf of read_data

    def __check_affixation_rules(self, affix: str, word: str, i: int):
        # True = affix qirqilsin, aks holda qirqilmasin
        # 1-rule
        if affix.startswith("(i)m"):  # (i)m egalik qushimchasida, m dan oldin kupincha a harfi keladi, agar bunday bulmasa, bu m qushimchasini qirqamay utirib yuboramiz
            if word[i] == "m" and word[i-1] not in ['a','i']:  # agar oldigi harfi a ga teng bulmasa bunda m ni qirqmasin
                return False  # don't chop, break it
        # 2-rule
        if affix.startswith("(S)i"):  # (S)i {S=s,y}  quchimchasidan oldin a,i harfi keladi. bunday bulmasa, bu m qushimchasini qirqamay utirib yuboramiz
            if word[i] == "s" and word[i-1] not in ['a','i']:  # agar oldigi harfi a ga teng bulmasa bunda m ni qirqmasin
                return False  # don't chop, break it
        # 3-rule
        if affix.startswith('G'):  # Guncha, Gani,Gan,Gancha,Gani {G=g,k,q}  qushimchasidan oldin k,q harfi kelishi kerak, agar bunday bulmasa bu qushimchani qirqamay utirib yuboramiz
            if (word[i] == "k" and word[i-1] not in ['k']) or (word[i] == "q" and word[i-1] not in ['q']):  # bulsa qushimchani qirqmasin
                return False  # don't chop, break it
        # 4-rule
        if affix.startswith("ir"):  # ir  qushimchasi t,ch,sh harflaridan keyin qushiladi faqat. botir,ichir,shishir
            if word[i-1] != "t" and word[i-2:i] not in ["ch", "sh"]:  # bulsa bunda qushimchani qirqmasin
                return False  # don't chop, break it

        return True  # it is ok, go on chopping

    def __correction_stem(self, self1, result):
        # 1-rule

        return result

    #  umumiy holda yani stem, lemma, analyse metodlaridan turib __processing metodidan foydalanamiz

    def __processing(self, word: str, pos: str = None, is_lemmatize: bool = False, multi_item: bool = False):
        affixes = []

        if pos is not None:  # if "pos" argument is given, "pos" argument may be given in lemmatize
            affixes = [i for i in self.__affixes if i['pos'] == pos]
        else:
            affixes = self.__affixes
        # print(affixes)

        def stem_find_exceptions(self, word: str, pos: str, position: int):
            if pos is not None:
                ex_stem_list = [ex_stem for ex_stem in self.__exception_stems if ex_stem['pos'] == pos]
            else:
                ex_stem_list = [ex_stem for ex_stem in self.__exception_stems]

            for i in range(position, len(word) + 1):  # +1 bu word[:i] i+1 yani oxirgisigacha olishi uchun
                #print("find from excp == " + word[:i])
                ex_stem_find = list(filter(lambda ex_stem: ex_stem['stem'] == word[:i], ex_stem_list))  # pythonic way -> https://stackoverflow.com/questions/8653516/python-list-of-dictionaries-search
                if ex_stem_find:
                    ex_stem_find[0]['affixed'] = word[i:]
                    #print('found from excp')
                    #print(ex_stem_find)
                    return True, ex_stem_find[0]
                # if word[:i] in ex_stem_list:
                #    return True, {'stem': word[:i], 'pos':}  #return two value, stem from exception
            return False, ""

        def stem_find(self, word: str, pos: str, position: int = 1):
            for i in range(position, len(word)):
                # predict_as_stem = word[:i]
                # predict_as_affix = word[i:]
                result_items = []  # list of dictionary [{'stem':'biz', 'affixed':'lar', ...},{...}]

                for item in affixes:
                    # if word[i:] in self.__GeneratedAllomorph(item["affix"]):
                    if word[i:] in item["allomorphs"]:

                        # print(self.__GeneratedAllomorph(item["affix"]))
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
                                item['stem'], item['affixed'] = word[:i], word[i:]  # add stem key_value to item dictionary from affixes
                                result_items.append(item)
                                if not multi_item:  # bu kod stem va lemmatize metodlari chaqirlganda faqat bitta asosni topsa bulgani va shuni qaytaradi, anaylyse metodi orqali kirganda barcha affixeslarni kurib chiqin multi_item xolida chiqarish uchun yozildi, agar multi_item bulsa sikl aylanaveradi, aks holda return bub tuxtaydi
                                    return result_items
                            continue
                                ###return item
                                ###break

                        # check different kind of affixation rules
                        if not self.__check_affixation_rules(item['affix'], word, i):  # xar xil qoidalar, biron qushimchalar buyicha, masalan, (i)m egalik qushimchasida, m dan oldin kupincha a harfi keladi, agar bunday bulmasa, bu m qushimchasini qirqamay utirib yuboramiz
                           continue

                        # exception dan suzlarni tekshirib olish
                        if len(word[i:]) <= 5:  # 3 bu yerda fine-tuning qilingan, yani 3 harfdan katta qushimchalarda xatolik bulmaydi va bundaylarni tugri qirqsak buladi

                            result, item_ex = stem_find_exceptions(self, word, pos, i + 1)
                            if result:
                                found_aff = False
                                for i_affixes in affixes:  # agar exception.csv dan topilsa, undan qolgan qushimchani affixes dan qidirib topib, undagi malumotlarni olamiz
                                    if item_ex['affixed'] in i_affixes["allomorphs"]:
                                        i_affixes['stem'], i_affixes['affixed'] = item_ex['stem'], item_ex['affixed']
                                        result_items.append(i_affixes)
                                        found_aff = True
                                        if not multi_item:
                                            return result_items

                                        #####break
                                        ###return i_affixes
                                if found_aff:
                                    return result_items
                                else:
                                    result_items.append(item_ex)
                                    return result_items

                                break  # agar len(affix)<=3 bulsa va stem exception.csv dan topilmasa, bu affixni qirqmay, navbatdagi affixni yasash uchun bu sikl sindiriladi
                                ###return item_ex  # agar suz exceptionda bor bulsa va unda umuman qushimchasi bulmasa
                            # end of stem_find_exception

                        # 2.1-rule qushimchasi topilgandan keyin oldingi turgan stem small_stemni ichida bormi yuqmi
                        if i <= 2:  # i==2 bulsa 0 va 1 belgini oladi, [:2] da 2 ikkini uzi kirmaydi
                            if word[:i] in self.__small_stems:
                                item['stem'], item['affixed'] = word[:i], word[i:]
                                result_items.append(item)
                                if not multi_item:
                                    return result_items
                                continue
                                ###return item
                            else:
                                break  # agar len(stem)<=2 bulsa-yu, lekin smal_stem ichidan topilmasa, u xolda stemni uzunligini oshirishi uchun bu yerdan tuliq chiqib ketishi kerak
                                ###break

                        # 2.2-rule confidence past bulgan suzlarni exception_words dan qaraydi.
                        # exwords da faqat affix bn tugaydigan suzlar turadi.
                        # agar suz exwordda bulsa qirqmaydi va alternativini qaraydi,
                        # aks holda yani suz exwordda bulmasa qirqib tashlaydi

                        #if float(item["confidence"]) <= 0.1 and False:
                        if False:
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

                        item['stem'], item['affixed'] = word[:i], word[i:]
                        result_items.append(item)
                        if not multi_item:
                            return result_items
                        ###return item  # chopping with 100% confidence

                if result_items:  # if not empty
                    return result_items

            return [{'stem': word, 'affixed': '', 'pos': None}]
            # end of stem_find

        # algorithm for stem
        # 1-step: check non affixed words list
        for na_stem in self.__non_affixed_stems: #stem,pos,affixed
            if word == na_stem['stem']:
                na_stem['affixed'] = ''
                return [na_stem]

        ##if word in [na_stem['stem'] for na_stem in self.__non_affixed_stems]: # in self.__non_affixed_stems
        ##    return word

        # 2-step sat faqat ko'rsat bulganda qirqiladi (so'zni boshi ko'rsat ga teng bulganda)
        if word[:7] == "ko'rsat":
            result_items = []
            for i_affixes in affixes:  # agar kursat topilsa, undan qolgan qushimchani affixes dan qidirib topib, undagi malumotlarni olamiz
                if word[7:] in i_affixes["allomorphs"]:
                    i_affixes['stem'], i_affixes['affixed'] = word[:4], word[4:]  # bu dictga kursat felini nisbati haqidagi informatsiyani qushib yuborsa xam buladi
                    result_items.append(i_affixes)
                    if not multi_item:
                        return result_items
                    ###return [i_affixes]
            if result_items:  # if not empty
                return result_items
            return [{'stem': "ko'r", 'affixed': "sat", 'pos': self.POS.VERB}]

        if is_lemmatize:
            for item_lemma in self.__lemma_map:  # agar exception.csv dan topilsa, undan qolgan qushimchani affixes dan qidirib topib, undagi malumotlarni olamiz
                if word.startswith(item_lemma['word']):
                    lemma = item_lemma['lemma']
                    full_affix = item_lemma['affix'] + word[len(item_lemma['word']):]  # [-n:] bunda suzdagi qolganlar harflarni oxirigacha olamiz
                    result_items = []
                    for i_affixes in affixes:  # qushimchani affixes dan qidirib topib, undagi malumotlarni olamiz
                        if full_affix in i_affixes["allomorphs"]:
                            i_affixes['stem'], i_affixes['affixed'] = lemma, full_affix
                            result_items.append(i_affixes)
                            if multi_item:
                                return result_items
                            ###return i_affixes
                    if result_items:  # if not empty
                        return result_items
            # enf of is_lemmatize

        # 3-step find stem by affix checking from affixes list
        # print("stem_find")
        result = stem_find(self, word, pos)
        # if len(stem)<=2:    #checking the small stem is exist or not
        #    if not stem in self.__small_stems:
        #        stem=stem_find(self, word, 3)

        #check stem after chopped affixs, if it should be change, corrected it as lemma, for example: [qiyinchilig+i ->qiyinchilik (xarf uzgarishi)], [avzoy+im->avzo, (xarf ortishi)]
        result = self.__correction_stem(self, result)

        return result
        # end of processing

    def stem(self, word: str):
        list_item = self.__processing(word)
        #print(list_item)
        # return str([d['stem'] for d in list_item])
        return list_item[0]['stem']    # dict['stem] == dict.get('stem')

    def lemmatize(self, word: str, pos: str = None):
        # print(self.__lemma_map)
        list_item = self.__processing(word, pos, is_lemmatize=True)
        # print(list_item)
        return list_item[0]['stem']  # .get('stem')

    def analyze(self, word: str, pos: str = None):
        # morpheme, bound morpheme [maktablar, maktab=morphem, lar=bound morphem]
        list_item = self.__processing(word, pos, is_lemmatize=True, multi_item=True)
        # print(list_item)
        res_list_item = []
        for item in list_item:
            res_dict = {'word': word, 'lemma': item['stem'], 'pos': item['pos']}
            for key in ['id','affix','affixed','tense','person','cases','singular','plural','question','negative','impulsion','copula','verb_voice','verb_func']:   # impulsion=mayl, copula=boglama
                if key in item:
                    if item[key] != "":
                        res_dict[key] = item[key]
            res_list_item.append(res_dict)

        # genetive case - qaratqich kelishigi
        # Accusative -tushum
        # Dative - jo'nalish
        # Ablative - chiqish
        # Locative o'rin payt

        #  Parse(word='benim', lemma='ben', pos='Noun', morphemes=['Noun', 'A3sg', 'P1sg'], formatted='[ben:Noun] ben:Noun+A3sg+im:P1sg')
        return res_list_item
        # {'affix': 'larni', 'pos': '', 'tense': '', 'person': '', 'cases': 'Tushum', 'singular': '', 'plural': '1', 'question': '', 'negative': '',
        # 'lexical_affixes': '', 'syntactical_affixes': '', 'stem': 'maktab', 'affixed': 'larni'}

    def morphemes(self, word: str, pos: str = None):
        # preprocessing       ['pre', 'process', 'ing']
        # https://github.com/aboSamoor/polyglot/blob/master/notebooks/MorphologicalAnalysis.ipynb
        pass

    class POS:
        NOUN = "NOUN"  # Noun
        VERB = "VERB"  # Verb
        ADJ = "ADJ"  # Adjective
        NUM = "NUM"  # Numeric
        ADV = "ADV"  # Adverb
        PRN = "PRN"  # Pronoun

    def pos(self):
        return (
            {'pos': self.POS.NOUN, 'def': 'Noun'},
            {'pos': self.POS.VERB, 'def': 'Verb'},
            {'pos': self.POS.ADJ, 'def': 'Adjective'},
            {'pos': self.POS.NUM, 'def': 'Number'},
            {'pos': self.POS.ADV, 'def': 'Adverb'},
            {'pos': self.POS.PRN, 'def': 'Pronoun'}
        )

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

import time
start_time = time.time()

obj = UzMorphAnalyser()
'''
sent = "olmasi taqgandim olma taqdimmi kurs kursi gacha namuna ko'plab ular bular sizlar kuchli shanba yuztagacha yuztaga kursi eksport eksportidan masjid masjidi tuman tumani tumanimizni taqdim taqdimi barmoqi barmoq muzqaymoq"
with open(os.path.join(os.path.dirname(__file__) + "/" + "test.txt"), 'r', encoding='utf8') as file:
    sent1 = file.read().rstrip()
sent1 = sent1.replace('	', ' ')
sent1 = sent1.replace('!', ' ')
sent1 = sent1.replace('?', ' ')
sent1 = sent1.replace('“', ' ')
sent1 = sent1.replace('”', ' ')
sent1 = sent1.replace(',', ' ')
sent1 = sent1.replace('.', ' ')
sent1 = sent1.replace('\n', ' ')
sent1 = sent1.replace('(', ' ')
sent1 = sent1.replace(')', ' ')

for token in sent1.split(" "):
    token = token.lower()
    if token == "":
        continue
    print(token + '\t' + obj.stem(token) + '\t' + obj.lemmatize(token) + '\t' + str(obj.analyze(token)))
print("--- %s seconds ---" % (time.time() - start_time))
'''
with open(os.path.join(os.path.dirname(__file__) + "/" + "test_token.txt"), 'r', encoding='utf8') as file:
    for token in file:
        token = token.rstrip()
        # print(token + '\t' + obj.stem(token) + '\t' + obj.lemmatize(token) + '\t' + str(obj.analyze(token)))
print("--- %s seconds ---" % (time.time() - start_time))

while (True):
    s = input().lower()
    print(s + '\t' + obj.stem(s) + '\t' + obj.lemmatize(s) + '\t' + str(obj.analyze(s)))

# print(analyzer.lemmatize('benim'))
# [('benim', ['ben'])]

# print(analyzer.analyze('benim'))
# Parse(word='benim', lemma='ben', pos='Noun', morphemes=['Noun', 'A3sg', 'P1sg'], formatted='[ben:Noun] ben:Noun+A3sg+im:P1sg')
# Parse(word='benim', lemma='ben', pos='Pron', morphemes=['Pron', 'A1sg', 'Gen'], formatted='[ben:Pron,Pers] ben:Pron+A1sg+im:Gen')
# Parse(word='benim', lemma='ben', pos='Verb', morphemes=['Noun', 'A3sg', 'Zero', 'Verb', 'Pres', 'A1sg'], formatted='[ben:Noun] ben:Noun+A3sg|Zero→Verb+Pres+im:A1sg')
# Parse(word='benim', lemma='ben', pos='Verb', morphemes=['Pron', 'A1sg', 'Zero', 'Verb', 'Pres', 'A1sg'], formatted='[ben:Pron,Pers] ben:Pron+A1sg|Zero→Verb+Pres+im:A1sg')

# (s)i opasi kitobi larda yi varianti xam bor, avzoyi, obro'yi (S)i shaklida olsak, bunda S{s,y} buladi. Manba:https://lex.uz/docs/-1625271

# tovush uzgarishlarini lemmatize ga kiritish

'''
Zeyrek's morphological analyzer returns instances of Parse object (based on pymorphy2's Parse), which is a wrapper of namedtuple class.
Parse object fields include:
 word: the word itself
 lemma: base form of the word, as found in a dictionary
 pos: part of speech of the word. Note: Turkish is an agglutinative language, which makes it quite different from widespread European languages. A word can usually be much longer, made of Inflection Groups (IG), which can correspond to words in other languages. Each of these IGs can have its own part of speech, and the part of speech of the word as a whole is determined by the part of speech of the last IG.
 morphemes: sequence of morphemes in the word, a list of strings - abbreviations of English names of morphemes.
 formatted: a human-readable string representation of the analysis. There are several kinds of possible formats. Default formatter shows the dictionary item and its part of speech, and morphemes (with their surfaces, if available), divided into inflectional groups by | character.
'''

#(i)t kirit, (i)l ko'ril, (i)n ko'rin, Y{bora,kuylay}, (a)r{borar,kuylar} qo'shimchalarini uchiramiz bazadan, chunki bir xarfli qushimchalar suzlarni oxirini kup qirqib yuboradi

# test file statistics:
# source:daryo.uz, category:4, documents for each category: 10
# 5,288 unique words of 11,952 total (44.24%):
