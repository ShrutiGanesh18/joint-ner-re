
#NER tagging using HMM

from __future__ import division
import random

train = open('new_train.txt')
test = open('new_test.txt')

#make a dictionary in which key is (words, NER) and value is counts for training file
def wordNERCount(train):
    #dic is a dictionary having (word, NER) as key & count as value
    train = open('new_train.txt')
    dic = dict()
    x = 1
    while(True):
        line = train.readline()
        if not line:
            break
        if (x%3==1):
            word_lst = line.split()
        if (x%3==0):
            ner_lst = line.split()
            for i in range(0,len(word_lst)):
                if (word_lst[i], ner_lst[i]) in dic:
			dic[word_lst[i], ner_lst[i]] = dic[word_lst[i], ner_lst[i]] + 1
                else:
			dic[word_lst[i], ner_lst[i]] = 1
        x = x+1
    train.close()
    return dic

#input is a dictionary of (words, NER) as key, counts as value which denote total number of each seen-once NER
def hashOnce(lexicon):
    #B_PER = 0
    B_ORG = 0
    B_LOC = 0
    B_MISC = 0
    I_PER = 0
    I_ORG = 0
    I_LOC = 0
    I_MISC = 0
    O = 0
    for key, value in lexicon.iteritems():
        if value == 1:
            '''if key[1] == "B-PER":
                B_PER = B_PER + 1'''
            if key[1] == "I-PER":
                I_PER = I_PER + 1
            if key[1] == "B-ORG":
                B_ORG = B_ORG + 1
            if key[1] == "I-ORG":
                I_ORG = I_ORG + 1
            if key[1] == "B-LOC":
                B_LOC = B_LOC + 1
            if key[1] == "I-LOC":
                I_LOC = I_LOC + 1
            if key[1] == "B-MISC":
                B_MISC = B_MISC + 1
            if key[1] == "I-MISC":
                I_MISC = I_MISC + 1
            if key[1] == "O":
                O = O + 1
    
    return B_ORG, B_LOC, B_MISC, I_PER, I_ORG, I_LOC, I_MISC, O


# dictionary of (words, NER) as key and counts as value to insert UNK into training set in plance of seen once counts.
def insertUnk(lexicon):
    lexicon_once = hashOnce(wordNERCount(train))
    
    B_ORG_ONCE = lexicon_once[0]
    B_LOC_ONCE = lexicon_once[1]
    B_MISC_ONCE = lexicon_once[2]
    I_PER_ONCE = lexicon_once[3]
    I_ORG_ONCE = lexicon_once[4]
    I_LOC_ONCE = lexicon_once[5]
    I_MISC_ONCE = lexicon_once[6]
    O_ONCE = lexicon_once[7]
    
    #lexicon[("UNK", "B-PER")] = B_PER_ONCE
    lexicon[("UNK", "B-ORG")] = B_ORG_ONCE
    lexicon[("UNK", "B-LOC")] = B_LOC_ONCE
    lexicon[("UNK", "B-MISC")] = B_MISC_ONCE
    lexicon[("UNK", "I-PER")] = I_PER_ONCE
    lexicon[("UNK", "I-ORG")] = I_ORG_ONCE
    lexicon[("UNK", "I-LOC")] = I_LOC_ONCE
    lexicon[("UNK", "I-MISC")] = I_MISC_ONCE
    lexicon[("UNK", "O")] = O_ONCE
    
    return lexicon

# to count each NER count
def countEntityTag(lexicon):
    #B_PER = 0
    B_ORG = 0
    B_LOC = 0
    B_MISC = 0
    I_PER = 0
    I_ORG = 0
    I_LOC = 0
    I_MISC = 0
    O = 0
    
    for key in lexicon.iterkeys():
        ''' if key[1] == "B-PER":
            B_PER = B_PER + lexicon[key]'''
        if key[1] =="I-PER":
            I_PER = I_PER + lexicon[key]
        if key[1] == "B-ORG":
            B_ORG = B_ORG + lexicon[key]
        if key[1] == "I-ORG":
            I_ORG = I_ORG + lexicon[key]
        if key[1] == "B-LOC":
            B_LOC = B_LOC + lexicon[key]
        if key[1] == "I-LOC":
            I_LOC = I_LOC + lexicon[key]
        if key[1] == "B-MISC":
            B_MISC = B_MISC + lexicon[key]
        if key[1] == "I-MISC":
            I_MISC = I_MISC + lexicon[key]
        if key[1] == "O":
            O = O + lexicon[key]
    return [ ("B_ORG", B_ORG), ("B_LOC", B_LOC) , ("B_MISC", B_MISC)
        , ("I_PER", I_PER) , ("I_ORG", I_ORG) , ("I_LOC", I_LOC), ("I_MISC", I_MISC) , ("O", O)]
NER_array = countEntityTag(insertUnk(wordNERCount(train)))

# emission probability
def emissionProbs(NER_array, lexicon):
    #get the count for each NER.
    B_ORG = NER_array[0][1]
    B_LOC = NER_array[1][1]
    B_MISC = NER_array[2][1]
    I_PER = NER_array[3][1]
    I_ORG = NER_array[4][1]
    I_LOC = NER_array[5][1]
    I_MISC = NER_array[6][1]
    O = NER_array[7][1]
    
    for key in lexicon.iterkeys():
        '''if key[1] == "B-PER":
            lexicon[key] = lexicon[key] / B_PER'''
        if key[1] == "I-PER":
            lexicon[key] = lexicon[key] / I_PER
        if key[1] == "B-ORG":
            lexicon[key] = lexicon[key] / B_ORG
        if key[1] == "I-ORG":
            lexicon[key] = lexicon[key] / I_ORG
        if key[1] == "B-LOC":
            lexicon[key] = lexicon[key] / B_LOC
        if key[1] == "I-LOC":
            lexicon[key] = lexicon[key] / I_LOC
        if key[1] == "B-MISC":
            lexicon[key] = lexicon[key] / B_MISC
        if key[1] == "I-MISC":
            lexicon[key] = lexicon[key] / I_MISC
        if key[1] == "O":
            lexicon[key] = lexicon[key] / O
    return lexicon

#to find number of sentences start with a particular tag.
def tagSentStartCounts():
    train = open('new_train.txt')
    lexicon = dict()
    x = 1
    while(True):
        line = train.readline()
        if not line:
            break
        if (x%3==0):
            ner_lst = line.split()
            if ner_lst[0] in lexicon:
                lexicon[ner_lst[0]] = lexicon[ner_lst[0]] + 1
            else:
                lexicon[ner_lst[0]] = 1
        x = x+1
    train.close()
    return lexicon

#start probability
def startProbs(counts):
    lexicon = dict()
    total = 0
    for key,value in counts.iteritems():	# to find total number of sentences in corpus
        total += value
    for key in counts.iterkeys():
        if key == "B-MISC":
            lexicon["B-MISC"] = counts["B-MISC"] / total
        if key == "B-ORG":
            lexicon["B-ORG"] = counts["B-ORG"] / total
        '''if key == "B-PER":
            lexicon["B-PER"] = counts["B-PER"] / total'''
        if key == "O":
            lexicon["O"] = counts["O"] / total
        if key == "B-LOC":
            lexicon["B-LOC"] = counts["B-LOC"] / total
    return lexicon


# number of sequences from Tag-i to Tag-j
def transitionalCounts(train):
    train = open('new_train.txt')
    hash_tokens = dict()
    x = 1
    while(True):
        line = train.readline()
        if not line:
            break
        if (x%3==0):
            tokens = line.split()
            for i in range(0, len(tokens) - 1):
                if ( hash_tokens.has_key( (tokens[i], tokens[i+1])) ):
                    hash_tokens[(tokens[i], tokens[i+1])] += 1
                else:
                    hash_tokens[(tokens[i], tokens[i+1])] = 1
        x=x+1
    train.close()
    return hash_tokens

transition_NER = countEntityTag(transitionalCounts(train))
    
# trainsitional counts into probablitites
def hashTransitionalProbs(lexicon):
    return emissionProbs(transition_NER, lexicon)


# to obatin tree-structure input is a dictionary of (word, NER) as key and probability as value. Output is a dictionary of word as key and NER, prob as value
def conversionFunction(hashtable):
    lexicon = dict()
    for key in hashtable.iterkeys():
        if key[0] not in lexicon:
            lexicon[key[0]] = { key[1]: hashtable[key] }
        else:
            table = lexicon[key[0]]
            table[key[1]] = hashtable[key]
    return lexicon

lexical_prob = conversionFunction(emissionProbs(NER_array, insertUnk(wordNERCount(train))))
transitional_prob = conversionFunction(hashTransitionalProbs(transitionalCounts(train)))

# smoothing, when any tag is not there then make its transition prob to .0000001 
def smoothing(lexicon):
    new_lexicon = dict()
    for key in lexicon.iterkeys():
        new_lexicon[key] = lexicon[key]
        '''if ('B-PER' not in lexicon[key]):
            new_lexicon[key]['B-PER'] = 0.0000001'''
        if ('I-PER' not in lexicon[key]):
            new_lexicon[key]['I-PER'] = 0.0000001
        if ('B-LOC' not in lexicon[key]):
            new_lexicon[key]['B-LOC'] = 0.0000001
        if ('I-LOC' not in lexicon[key]):
            new_lexicon[key]['I-LOC'] = 0.0000001
        if ('B-ORG' not in lexicon[key]):
            new_lexicon[key]['B-ORG'] = 0.0000001
        if ('I-ORG' not in lexicon[key]):
            new_lexicon[key]['I-ORG'] = 0.0000001
        if ('B-MISC' not in lexicon[key]):
            new_lexicon[key]['B-MISC'] = 0.0000001
        if ('I-MISC' not in lexicon[key]):
            new_lexicon[key]['I-MISC'] = 0.000001
        if ('O' not in lexicon[key]):
            new_lexicon[key]['O'] = 0.0000001
        for ner in lexicon[key].iterkeys():
            new_lexicon[key][ner] = lexicon[key][ner]        
    return new_lexicon

transitional_prob = smoothing(transitional_prob)

def findMax(lexicon):
    largest = 0
    largestKey = 'no max'
    for key,value in lexicon.iteritems():
        if value > largest:
            largest = value
            largestKey = key
    return (largestKey, largest)

#creating output in the form as first word of each line represent tag and then its corresponding index intervals. 
def createOutput(pos_list):
    output_hash = dict()
    per = "PER "
    loc = "LOC "
    org = "ORG "
    misc = "MISC "
    start_interval = 0
    end_interval = 0
    for i in range(len(pos_list)):
        if ('PER' in pos_list[i]):
            if('B' in pos_list[i]):
                start_interval = i
                end_interval = i
            if('I' in pos_list[i]):
                if ('O' in pos_list[i-1]):
                    start_interval = i-1
                    end_interval = i     
                else:
                    end_interval = i
            if ('I' not in pos_list[i+1]):
                per += (str(start_interval) + "-" + str(end_interval) + " ")
        
        if ('LOC' in pos_list[i]):
            if('B' in pos_list[i]):
                start_interval = i
                end_interval = i
            if('I' in pos_list[i]):
                if ('O' in pos_list[i-1]):
                    start_interval = i-1
                    end_interval = i     
                else:
                    end_interval = i
            if ('I' not in pos_list[i+1]):
                loc += (str(start_interval) + "-" + str(end_interval) + " ")
        
        if ('ORG' in pos_list[i]):
            if('B' in pos_list[i]):
                start_interval = i
                end_interval = i
            if('I' in pos_list[i]):
                if ('O' in pos_list[i-1]):
                    start_interval = i-1
                    end_interval = i     
                else:
                    end_interval = i
            if ('I' not in pos_list[i+1]):
                org += (str(start_interval) + "-" + str(end_interval) + " ")
                
        if ('MISC' in pos_list[i]):
            if('B' in pos_list[i]):
                start_interval = i
                end_interval = i
            if('I' in pos_list[i]):
                if ('O' in pos_list[i-1]):
                    start_interval = i-1
                    end_interval = i     
                else:
                    end_interval = i
            if ('I' not in pos_list[i+1]):
                misc += (str(start_interval) + "-" + str(end_interval) + " ")
    output = open('output_hmm.txt', 'w')
    output.write(per + "\n" + loc + "\n" + org + "\n" + misc)
    output.close()

#run test on training set
def runTestFile(test):
    NER_start_prob = startProbs(tagSentStartCounts())
    x = 1
    prevNER = "start"
    prevScore = 1
    pos = [] #pos is the key, NER is the value
    result = []
    while(True):
        line = test.readline()
        if not line:
            break
        if (x%3==1):
            word_lst = line.split()
        if (x%3==0):
            pos_lst = line.split()
            for i in range(0,len(word_lst)):
                scores = dict()
                if word_lst[i] in lexical_prob:
                    word = word_lst[i]
                else:
                    word = 'UNK'
                #start of the sentence
                if i == 0:
                    for s in NER_start_prob.iterkeys():
                        if s in lexical_prob[word]:
                            score = NER_start_prob[s] * lexical_prob[word][s]
                            scores[s] = score
                    if len(scores) == 0:
                            scores = NER_start_prob
                    prevNER = findMax(scores)[0]
                    prevScore = findMax(scores)[1]
                #rest of the sentence
                else:
                    for ner in transitional_prob[prevNER].iterkeys():
                        if ner in lexical_prob[word]:
                            score = (transitional_prob[prevNER][ner]
                                    * lexical_prob[word][ner])
                            scores[ner] = score
                    if len(scores) == 0:
                        scores = lexical_prob[word]
                    prevNER = findMax(scores)[0]
                    prevScore = findMax(scores)[1]
                pos.append(prevNER)
        x = x+1
    createOutput(pos)
runTestFile(test)



