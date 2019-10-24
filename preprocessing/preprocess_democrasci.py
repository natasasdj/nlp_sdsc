'''
preprocess democratic unsupervised data
input: all democrasci data (1950-1980)
output: democrasci.txt
        each line is a sentence, and with empty line between different speeches

export PYTHONIOENCODING=UTF8
'''
import os
import pickle
import nltk.data
from langdetect import detect

tokenizer_de = nltk.data.load('tokenizers/punkt/german.pickle')
tokenizer_fr = nltk.data.load('tokenizers/punkt/french.pickle')
tokenizer_it = nltk.data.load('tokenizers/punkt/italian.pickle')

def language_detect(text):
    language = detect(text)
    if language == 'de':
        sentences = tokenizer_de.tokenize(text)
    elif language == 'fr':
        sentences = tokenizer_fr.tokenize(text)
    elif language == 'it':
        sentences = tokenizer_it.tokenize(text)
    else:
        #print('no de, fr or it')
        #print(text)
        sentences = tokenizer_de.tokenize(text)

    return sentences


data_dir = '/home/IRISAD/natasa.sdj/nlp_sdsc/democrasci_bert/data/AB/'

for year in range(1950,1981):
    #year = 1950
    print(year)
    fname = os.path.join(data_dir, str(year), '06_collectedinformation.pickle')
    with open(fname,'rb') as f:
        data_dict = pickle.load(f)

    fname2 = os.path.join(data_dir, str(year), 'sentences.txt')
    f2 = open(fname2, 'w+', encoding='utf-8')

    for key1 in data_dict.keys():
        #print(key1)
        for key2 in data_dict[key1]['dict_speeches'].keys():
            #print(key2)
            text = data_dict[key1]['dict_speeches'][key2][1].strip()
            #print(text)
            try:
                if len(text)==0: continue
                sentences = language_detect(text)
                #print(sentences)
            except:
                print("Exception:")
                #print(text, len(text))
                continue
            for sentence in sentences:
                f2.write(sentence.strip())
                f2.write('\n')

            f2.write('\n')

    f2.close()
