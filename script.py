from __future__ import unicode_literals
from isc_parser import Parser
parser = Parser(lang='hin')

synset = {
    "छोटा": {"Syn": [	"अनुज",  "छोटा",  "अनुजन्मा",  "अनुजात",  "कनिष्ठ",  "लघु",  "अवरज", ],
             "Ant": ["बड़ा",   "अग्रज",   "अग्रजन्मा",   "अग्रजात",   "बड़ा",  "पुरोजन्मा"],
             "Hyp": []

             },
    "अच्छा": {"Syn": [	"अच्छा",  "भला",  "बढ़िया",  "लतीफ़"],
              "Ant": ["बुरा", "बुरा",   "ख़राब",   "खराब",   "अनुचित",   "घटिया",   "खल",   "भ्रष्ट",   "निकृष्ट",   "कुत्सित",   "वाहियात",   "बद",   "अनभला",   "अनयस",   "अनीक",   "अनीठ",   "अप्रिय",   "अनैसा"],
              "Hyp": []
              },
    "खाना": {"Syn": ["खाना",  "अहारना",  "मुँह चलाना"],
             "Ant": [],
             "Hyp": []
             },
    "आना": {"Syn": ["आगमन",  "आना",  "आवक",  "आमद",  "अवाई",  "अवायी",  "आगति",  "आगम",  "आगवन",  "आगौन",  "आवन",  "आवनि",  "आवाती",  "उपागम"],
            "Ant": [],
            "Hyp": []

            },
    "भागना": {
        "Syn": ["भागना", "पलायन करना", "भाग जाना", "भाग खड़ा होना"],
        "Ant": [],
        "Hyp": []
    },
    "बात": {
        "Syn": ["उक्ति", "बोल", "उद्गार", "कथन", "वचन", "बात", "बतिया", "कहा", "वाद", "कलाम", "अभिलाप", "अभिहिति"],
        "Ant": [],
        "Hyp": ["अफवाह", "अफ़वाह", "गप", "उड़ती ख़बर", "हवाई ख़बर", "चर्चा", "जटल", "अफ़वा", "अफवा", "वाद", "श्रुति", "उत्तर", "जवाब"]
    },

    "बहुत": {
        "Syn": ["बहुत", "अधिक", "ज्यादा", "ज़्यादा", "ख़ूब", "खूब", "अति", "अतीव", "काफ़ी",  "काफी",  "बहुल",  "आत्यंतिक",  "आत्यन्तिक",  "अनल्प",  "अनून",  "अन्यून",  "अबेश",  "आकर",  "गहरा"],
        "Ant": [],
        "Hyp": []
    },
    "घर": {
        "Syn": ["घर", "गृह", "मकान", "सदन", "शाला", "आलय", "धाम", "निकेतन", "निलय", "केतन", "पण", "गेह", "सराय", "अमा", "निषदन", "अवसथ", "अवस्थान", "आगार", "आगर", "आयतन", "आश्रय",  "दम"],
        "Ant": [],
        "Hyp": ["आश्रम", "कुटिया", "गुरुकुल", "आचार्यकुल", "आचार्य्यकुल", "भवन", "इमारत", "वास्तु",   "बिल्डिंग", "हवेली",   "कोठी", "बँगला", "झोपड़ा", "झोंपड़ा", "झोंपड़ी"],
    },
    "लाल": {
        "Syn": ["लाल रंग", "लाल", "रोहित", "रोही"],
        "Ant": [],
        "Hyp": ["खारुआ", "खारुआँ", "आल"]
    },
    "खाता": {
        "Syn": ["खाता", "अकाउंट", "एकाउंट", "अकाउन्ट", "एकाउन्ट"],
        "Ant": [],
        "Hyp": ["चालू खाता",   "चलता खाता"]
    },
    "सोता": {
        "Syn": ["सोया", "सोता", "सोता हुआ", "सुप्त"],
        "Ant": [],
        "Hyp": []
    },
    "पास": {
        "Syn": ["पास", "पास में", "नज़दीक", "नजदीक", "निकट में", "क़रीब में", "समीप", "निकट", "क़रीब", "करीब", "सन्निकट", "नजीक", "मुत्तसिल",  "अर्वाक",  "अविदूर"],
        "Ant": [],
        "Hyp": []
    },
    "बगीचा": {
        "Syn": ["बगीचा", "बाग", "बाग-बगीचा", "बाग बगीचा", "बाग़", "बग़ीचा",  "बगिया"],
        "Ant": [],
        "Hyp": ["फुलवारी",   "फुलवाड़ी",   "फुलबाड़ी",   "पुष्प उपवन", "कुसुमालय",   "गुलजार"]
    },
    "मकान": {
        "Syn": ["घर", "गृह", "मकान", "सदन", "शाला", "आलय", "धाम", "निकेतन"],
        "Ant": [],
        "Hyp": ["आश्रम", "कुटिया", "गुरुकुल", "आचार्यकुल", "आचार्य्यकुल", "भवन", "इमारत", "वास्तु",   "बिल्डिंग", "हवेली",   "कोठी", "बँगला", "झोपड़ा", "झोंपड़ा", "झोंपड़ी"]
    },
    "पानी": {
        "Syn": ["जल", "पानी", "नीर", "अंबु", "अम्बु", "पय", "वारि", "आब", "तोय", "सलिल", "पुष्कर", "अंभ", "अपक", "उदक"],
        "Ant": [],
        "Hyp": ["गंगाजल", "गंगांबु", "गंगोदक", "ब्रह्मद्रव", "अर्घ्य", "अर्घ", "अरघ", "बँगा", "बंगा"]
    },
    "ठंडा": {
        "Syn": ["ठंडा", "शीतल", "ठण्डा", "ठंढा", "ठण्ढा", "ठन्डा", "ठन्ढा", "अनुष्ण", "अतप्त"],
        "Ant": ["गरम"],
        "Hyp": []
    },
    "गरम": {
        "Syn": ["गर्म", "गरम", "उष्ण", "ताबदार", "अशीतल"],
        "Ant": [],
        "Hyp": ["ठंडा", "ठंडा", "शीतल", "ठण्डा", "ठंढा", "ठण्ढा", "ठन्डा", "ठन्ढा"]
    },
    "पैसा": {
        "Syn": ["धन-दौलत", "दौलत", "धन", "रुपया-पैसा", "पैसा", "वित्त", "अर्थ", "वैभव"],
        "Ant": [],
        "Hyp": ["आय", "आमदनी", "कमाई", "इन्कम",   "इनकम",   "आमद",  "मूल्य",   "दाम",   "क़ीमत",   "कीमत",   "मोल",   "पण",   "दमोड़ा", "मूल्य",   "दाम",   "क़ीमत",   "कीमत",   "मोल",   "पण",   "दमोड़ा"],
    },
    "नकली": {
        "Syn": ["दिखावटी",  "दिखाऊ",  "बनावटी",  "नकली",  "नक़ली",  "बनौवा",  "कृत्रिम"],
        "Ant": ["असली"],
        "Hyp": []
    },
    "असली": {
        "Syn": ["वास्तविक", "यथार्थ", "सच्चा", "सही", "असली", "असल", "वास्तव"],
        "Ant": ["नकली"],
        "Hyp": []
    },
    "कमरा": {
        "Syn": ["कमरा",  "कक्ष",  "घर",  "कोष्ठ",  "रूम",  "सेल"],
        "Ant": [],
        "Hyp": ["गर्भ-गृह", "गर्भागार", "वार्ड", "कक्षा",   "क्लास",   "क्लासरूम",  " कक्षा-कमरा"]
    },
    "गया": {
        "Syn": ["गया",  "गया शहर",  "माया",  "तारकतीर्थ"],
        "Ant": [],
        "Hyp": ["आया"]
    },
    "आया": {
        "Syn": ["आया"],
        "Ant": [],
        "Hyp": ["गया"]
    },
    "तेजी": {
        "Syn": ["वेग",  "तीव्रता",  "तीक्ष्णता",  "तेज़ी",  "तेजी",  "ज़ोर",  "जोर",  "रवानी"],
        "Ant": [],
        "Hyp": ["लहर", "तरंग"]
    },
    "खेलना": {
        "Syn": ["खेलना"],
        "Ant": [],
        "Hyp": []
    },
    "रचना": {
        "Syn": ["सिरजन",  "बनाना",  "संस्थापना", ],
        "Ant": [],
        "Hyp": ["लिखना", "बंदिश", "तामीर", ]
    },
    "सुशील": {
        "Syn": ["सभ्य",  "भद्र",  "शिष्ट",  "शालीन",  "सुशील",  "शील",  "तमीज़दार",  "तमीजदार"],
        "Ant": [],
        "Hyp": []
    },
    "दुखी": {
        "Syn": ["दुखी",  "दुखिया",  "पीड़ित",  "दुखियारा",  "व्यथित",  "दुःखी",  "दुखित",  "विषादग्रस्त",  "खिन्न",  "आपद्ग्रस्त"],
        "Ant": ["सुखी",   "सुखी",   "ख़ुशहाल",   "खुशहाल",   "सुखमय",   "सुखभरा",   "सुखिया",   "खुशाल"],
        "Hyp": []
    },
    "शक्तिशाली": {
        "Syn": ["शक्तिशाली",  "बलशाली",  "शक्तिपूर्ण",  "ताकतवर",  "ताक़तवर",  "बलवान",  "शक्तिवान",  "शक्तिमान",  "शक्तिमान्",  "बलिष्ठ",  "बली",  "सबल",  "प्रबल"],
        "Ant": ["शक्तिहीन",   "कमजोर",   "कमज़ोर",   "दुर्बल",   "निर्बल",   "शक्तिहीन",   "अशक्त",   "बलहीन",   "अतुंद",   "अतुन्द",   "अपुष्ट",   "अप्रबल",   "लचर",   "अबर",   "अब्बर",   "अबरा",   "निबल",   "अबल"],
        "Hyp": []
    },
    "कमजोर": {
        "Syn": ["कमजोर",  "कमज़ोर",  "दुर्बल",  "निर्बल",  "शक्तिहीन",  "अशक्त",  "बलहीन",  "अतुंद",  "अतुन्द",  "अपुष्ट",  "अप्रबल",  "लचर",  "अबर",  "अब्बर",  "अबरा"],
        "Ant": ["शक्तिशाली",  "बलशाली",  "शक्तिपूर्ण",  "ताकतवर",  "ताक़तवर",  "बलवान",  "शक्तिवान"],
        "Hyp": []
    },
    "देखना": {
        "Syn": ["देखना",  "निहारना",  "ताकना",  "तकना",  "निरखना",  "विलोकना"],
        "Ant": [],
        "Hyp": []
    }
}


def syn_compare(word1, word2, arr):
    #arr [paraphrase,entailment,neutral]
    try:
        syn1 = synset[word1]
    except:
        syn1 = {"Syn": [], "Ant": [], "Hyp": []}

    if(word1 == word2 and word1 != "है" and word2 != "है"):
        try:
            syn1 = synset[word1]
            syn2 = synset[word2]
        except:

            arr[0] += 0.2 * (10 - arr[0])
            arr[1] += 0.2 * (10-arr[1])
            return arr

    # first check if wordforms match
    if(word1 == "है" and word2 == "है"):
        return arr

    elif word1 == word2 and word1 != "है" and word2 != "है":
        relation = 1
        arr[0] += 0.5 * (10 - arr[0])
        arr[1] += 0.5 * (10 - arr[1])
    elif word2 in syn1["Syn"]:  # check if words are synonyms
        arr[0] += 0.5 * (10 - arr[0])
        arr[1] += 0.5 * (10 - arr[1])

    elif word2 in syn1["Ant"]:  # check if words are antonyms
        arr[0] = -0.5 * (10 - arr[0])
    elif word2 in syn1["Hyp"]:

        arr[1] += 0.5 * (10 - arr[1])

    return arr


# tree is an list of lists . Each list has info about one word
# 7th index is karaka relation


def syn_karaka(arr, rel):  # helper in aligning the sentence structure
    PSP1 = ""  # PSP associated with the k* relation of true statement
    for i in range(0, len(tree1)):
        inst = tree1[i]
        k1Found = 0
        k1Found2 = 0
        PSP1 = ""
        PSP2 = ""
        if inst[7] == rel:
            word1 = inst[1]
            if (tree1[i+1][3] == "PSP"):
                PSP1 = tree1[i+1][1]
            idxMatch1 = i
            k1Found = 1
            break
    for i in range(0, len(tree2)):
        inst = tree2[i]
        if inst[7] == rel:
            word2 = inst[1]
            idxMatch2 = i
            k1Found2 = 1
            break

    if (k1Found == 0):
        return arr

    if (word1 == word2 and k1Found == 1 and k1Found2 == 1):
        prp1Found = 0
        prp2Found = 0
        for i in range(0, idxMatch1):
            inst = tree1[i]
            if inst[3] == "PRP":
                prp1 = inst[1]
                prp1Found = 1
                break
        for i in range(0, idxMatch2):
            inst = tree2[i]
            if inst[3] == "PRP":
                prp2 = inst[1]
                prp2Found = 1
                break
        if(prp1Found == 0 or prp2Found == 0):
            arr[2] += 0.5*(10-arr[2])
        elif(prp1Found == 1 and prp2Found == 1):
            if (prp1 == prp2):  # if prp same then paraphrase and entailment increases
                arr[0] += 0.5 * (10 - arr[0])
                arr[1] += 0.5 * (10 - arr[1])
            else:  # if prp not same then netural
                arr[2] += 0.5*(10-arr[2])
    elif (word1 != word2 and k1Found == 1 and k1Found2 == 1):
        temp = arr.copy()
        # compare synsets of the same rel word forms to check if they are related
        arr = syn_compare(word1, word2, arr)
        same = 1

        for i in range(0, len(arr)):
            if (temp[i] == arr[i]):
                continue
            else:
                same = 0
        if (same == 0):  # if we do find a relation then we are done

            return arr
        else:  # otherwise we check it with other k* tags
            bool1 = 0
            for i in range(0, len(tree2)):
                inst = tree2[i]
                if (inst[7][0] == "k"):
                    if (word1 == inst[7]):
                        inst2 = tree2[i+1]
                        if (inst2[3] == "PSP"):
                            PSP2 = inst2[1]
                            if PSP1 == PSP2:
                                arr[0] += 0.3*(10-arr[0])
                                bool1 = 1
                                inst[7][0] = "NULL"
                                break

            if(PSP1 == "" and PSP2 == ""):
                arr[0] += 0.3*(10-arr[0])

            elif(bool1 == 0):
                arr[2] += 0.3*(10-arr[2])

    return arr


def jprpCompare(arr, rel):
    for i in range(0, len(tree1)):
        inst = tree1[i]
        if inst[3] == rel:
            word1 = inst[1]
            for j in range(0, len(tree2)):
                if(tree2[i][3] == rel):
                    if(word1 == tree2[i][1]):
                        arr[0] += 0.3*(10-arr[0])
                        break
                    else:

                        temp = arr.copy()
                        arr = syn_compare(word1, tree2[i][1], arr)
                        same = 1
                        for z in range(0, 3):
                            if arr[i] == temp[i]:
                                continue
                            else:
                                same = 0
                        if (same == 0):
                            print("here")
                            arr[0] += 0.3*(10-arr[0])
                        elif(same == 1):
                            arr[2] += 0.3 * (10-arr[2])
                        break
    return arr


# if unbound local error then switch sent1 and sent2
sent1 = "राम की हवेली छोटा है |"
sent2 = "राम का घर छोटा है |"
neg1 = 0
neg2 = 0

split1 = sent1.split(" ")
split2 = sent2.split(" ")
sent1 = ""
sent2 = ""

for i in range(0, len(split1)):
    if split1[i] == "नही":
        neg1 = 1
        continue
    sent1 += split1[i] + " "

for i in range(0, len(split2)):
    if split2[i] == "नही":
        neg2 = 1
        continue
    sent2 += split2[i] + " "

sent1 = sent1.rstrip(" ")
sent2 = sent2.rstrip(" ")

split1 = sent1.split(" ")
split2 = sent2.split(" ")


tree1 = parser.parse(split1)
tree2 = parser.parse(split2)
sent1conj = 0  # tells if sent1 has a conjunction और
sent2conj = 0  # tells if sent2 has a conjunction और
sent1or = 0  # tells if sent1 has connector या
sent2or = 0  # tells if sent2 has connector या


# checking for any connectives in the sentence
if "और" in split1:
    sent1conj = 1
if "और" in split2:
    sent2conj = 1
if "या" in split1:
    sent1or = 1
if "या" in split2:
    sent2or = 1

if sent1conj == 1:
    seen = 0
    str1 = ""
    str2 = ""
    for i in range(0, len(split1)):

        if(split1[i] != "और" and seen == 0):
            str1 += split1[i] + " "
        else:
            if split1[i] == "और":
                seen = 1
                str1 += "है"
                j = i
                for k in range(0, j-1):
                    str2 += split1[k] + " "
            else:
                str2 += split1[i] + " "

    str2 = str2.rstrip(" ")
    split11 = str1.split(" ")
    split22 = str2.split(" ")
    tree1 = parser.parse(split11)
    tree2 = parser.parse(split2)

if sent1or == 1:
    seen = 0
    str1 = ""
    str2 = ""
    for i in range(0, len(split1)):

        if(split1[i] != "या" and seen == 0):
            str1 += split1[i] + " "
        else:
            if split1[i] == "या":
                seen = 1
                str1 += "है"
                j = i
                for k in range(0, j-1):
                    str2 += split1[k] + " "
            else:
                str2 += split1[i] + " "

    str2 = str2.rstrip(" ")
    split11 = str1.split(" ")
    split22 = str2.split(" ")
    tree1 = parser.parse(split11)
    tree2 = parser.parse(split2)

similarity = [0, 0, 0]

for i in range(0, len(tree1)):
    if (tree1[i][7] == "main"):
        words1 = tree1[i][1]
for i in range(0, len(tree2)):
    if(tree2[i][7] == "main"):
        words2 = tree2[i][1]

similarity = syn_compare(words1, words2, similarity)
# print(similarity)
similarity = syn_karaka(similarity, "k1")
# print(similarity)
similarity = syn_karaka(similarity, "k2")
# print(similarity)
similarity = syn_karaka(similarity, "k7")
# print(similarity)
similarity = syn_karaka(similarity, "k1s")
# print(similarity)
similarity = jprpCompare(similarity, "JJ")
# print(similarity)
similarity = jprpCompare(similarity, "PRP")


if(neg1 == 0 and neg2 != 0 or neg1 != 0 and neg2 == 0):
    similarity[0] = -1*similarity[0]
# print(similarity)

if (sent1conj == 0 and sent1or == 0):
    x = similarity[0]
    y = similarity[1]
    z = similarity[2]
    if(x == y and y == z and x == 0):
        print("Neutral")
    elif(x < 0):
        print("Contradiction")
    elif (x == y and x > z):
        print("Paraphrase")
    elif(x > y and x > z):
        print("Paraphrase")
    elif (y > x and y > z):
        print("Entailment")
    elif(z > x and z > y):
        print("Neutral")


if (sent1conj == 1):
    tree1 = parser.parse(split22)
    tree2 = parser.parse(split2)
    similarity1 = [0, 0, 0]

    for i in range(0, len(tree1)):
        if (tree1[i][7] == "main"):
            words1 = tree1[i][1]
    for i in range(0, len(tree2)):
        if(tree2[i][7] == "main"):
            words2 = tree2[i][1]

    similarity1 = syn_compare(words1, words2, similarity1)

    similarity1 = syn_karaka(similarity1, "k1")

    similarity1 = syn_karaka(similarity1, "k2")

    similarity1 = syn_karaka(similarity1, "k7")

    similarity1 = syn_karaka(similarity1, "k1s")

    similarity1 = jprpCompare(similarity1, "JJ")

    similarity1 = jprpCompare(similarity1, "PRP")

    a = (similarity[0]+similarity1[0])/2
    b = (similarity[1]+similarity1[1])/2
    c = (similarity[2]+similarity1[2])/2
    if(similarity[2]+similarity1[2] > 0):
        b += 0.9*(10-b)

    if(a < 0):
        print("Contradiction")
    elif(a == b and a > c):
        print("Paraphrase")
    elif (a > b and a > c):
        print("Paraphrase")
    elif (b > a and b > c):
        print("Entailment")
    elif(c > a and c > b):
        print("Neutral")
    elif (a == b and b == c and a == 0):
        print("Neutral")

if (sent1or == 1):
    tree1 = parser.parse(split22)
    tree2 = parser.parse(split2)
    similarity1 = [0, 0, 0]
    for i in range(0, len(tree1)):
        if (tree1[i][7] == "main"):
            words1 = tree1[i][1]
    for i in range(0, len(tree2)):
        if(tree2[i][7] == "main"):
            words2 = tree2[i][1]

    similarity1 = syn_compare(words1, words2, similarity1)
    # print(similarity1)
    #similarity1 = syn_karaka(similarity1, "k1")
    # print(similarity1)
    #similarity1 = syn_karaka(similarity1, "k2")
    # print(similarity1)
    #similarity1 = syn_karaka(similarity1, "k7")
    # print(similarity1)
    #similarity1 = syn_karaka(similarity1, "k1s")
    # print(similarity1)
    #similarity1 = jprpCompare(similarity1, "JJ")
    # print(similarity1)
    #similarity1 = jprpCompare(similarity1, "PRP")
    # print(similarity1)

    a = (similarity[0]+similarity1[0])/2
    b = (similarity[1]+similarity1[1])/2
    c = (similarity[2]+similarity1[2])/2
    if(similarity[2]+similarity1[2] > 0):
        a = 0
        b = 0
        c = 10
    else:
        a = -10
        b = 0
        c = 0

    if(similarity[0] > 0 or similarity1[0] > 0):
        print("Neutral")
    elif(a < 0):
        print("Contradiction")
