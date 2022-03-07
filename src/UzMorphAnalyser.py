import csv
data = []

def ng():
    print("dsfdgg")

def read_data():
    global data
    with open("data.csv", "r") as f:
        reader = csv.DictReader(f)
        data = list(reader)

class UzMorphAnalyser:
    read_data()

    def GeneratedAffixes(affix):
        GenAff=[]
        #agar qavsli bulsa
        if "(" in affix:
            GenAff.append("nchi")
            return GenAff
        #agar Katta harfli allomorf bulsa
        if (affix[0]).isupper():
            affix[0]:
            case "G":
            case "K":
            case "Y":
            case "T":
            case "G":

            GenAff.append("gan")
            GenAff.append("kan")
            GenAff.append("larning")
            return GenAff
        return affix

    def stem(word):
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
            for item in data:
                if(affix in UzMorphAnalyser.GeneratedAffixes(item["affix"])):
                    return word[:i]
        return word

print(UzMorphAnalyser.stem("ularning"))

