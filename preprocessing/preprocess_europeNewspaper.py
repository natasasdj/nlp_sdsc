# it may be necessary to execute this command before running this file
# export PYTHONIOENCODING=utf-8

'''
preprocessing europeNewspaper 'lft' and 'onb' while 'sbb' requires more elaborate preprocessing due to tokens consisting of two words and others
input: enp_DE.lft.bio (or enp_DE.onb.bio) file
output: enp_DE.lft.txt (or enp_DE.lft.txt) file
- put an empty line after each sentence in the input file, because this is required as input to BERT-NER  
'''

import os
import pandas as pd
data_dir = '/home/IRISAD/natasa.sdj/nlp_sdsc/europeNewspaper'
fname = os.path.join(data_dir, 'enp_DE.lft.bio', 'enp_DE.lft.bio')
#fname = os.path.join(data_dir, 'enp_DE.onb.bio', 'enp_DE.onb.bio')
#fname = os.path.join(data_dir, 'enp_DE.sbb.bio', 'enp_DE.sbb.bio2')
df = pd.read_csv(fname, names = ['token', 'tag'], sep = '\s+|\n', engine = 'python', encoding = 'utf-8')
df['token'] = df['token'].astype(dtype='str')
text = ' '.join(str(df['token']))

import nltk.data 
tokenizer = nltk.data.load('tokenizers/punkt/german.pickle')
sentences = tokenizer.tokenize(text)

fname2 = os.path.join(data_dir, 'enp_DE.lft.txt')
#fname2 = os.path.join(data_dir, 'enp_DE.onb.txt') 
#fname2 = os.path.join(data_dir, 'enp_DE.sbb.txt')
f = open(fname2, 'w+', encoding = 'utf-8')
k = 0
sentence = sentences[k]
s = ''
for i in range(df.shape[0]):
    if len(s)>0: s += ' '
    s += df.loc[i,'token']
    #print(s, sentence)
    _ = f.write(df.loc[i,'token']+ ' ' + df.loc[i,'tag']+'\n')
    #if len(s)>500: break
    if df.loc[i,'token'] not in sentence:
        k += 1
        sentence += sentences[k]
        if not df.loc[i,'token'] in sentence:
            print(i, df.loc[i,'token'], sentence)
            break
    if s==sentence:
        _ = f.write('\n')
        s = ''
        k += 1
        if k<len(sentences):
            print('t1',k, len(sentences))
            sentence = sentences[k]
        else:
            print('t2',k, len(sentences))
            break
        #print(k,i)

f.close()

# for .lft data:
# sed -i -e 's/B-BER/B-PER/g' ../europeNewspaper/enp_DE.lft.txt

