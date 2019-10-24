# it may be necessary to execute this command before running this file
# export PYTHONIOENCODING=utf-8

'''
preprocessing europeNewspaper 'lft' and 'onb' dataset 
prepare the dataset in a format necessary as input to Bert
input: enp_DE.lft.bio (or enp_DE.onb.bio) file
output: enp_DE.lft.sentences.txt (or enp_DE.lft.sentences.txt) file
        each sentence is put in one line  
'''

import os
import pandas as pd
data_dir = '/home/IRISAD/natasa.sdj/nlp_sdsc/europeNewspaper'
#fname = os.path.join(data_dir, 'enp_DE.lft.bio', 'enp_DE.lft.bio')
fname = os.path.join(data_dir, 'enp_DE.onb.bio', 'enp_DE.onb.bio')

df = pd.read_csv(fname, names = ['token', 'tag'], sep = '\s+|\n', engine = 'python', encoding = 'utf-8')
df['token'] = df['token'].astype(dtype='str')

text = ''
for token in df['token']:
    if token in ['.', ';', ',', ':', '!', '?']:
        text = text + token.strip()
    else:
        text = text + ' ' + token.strip()

text = text.strip()



import nltk.data 
tokenizer = nltk.data.load('tokenizers/punkt/german.pickle')
sentences = tokenizer.tokenize(text)

#fname2 = os.path.join(data_dir, 'enp_DE.lft.sentences.txt')
fname2 = os.path.join(data_dir, 'enp_DE.onb.sentences.txt') 

f = open(fname2, 'w+', encoding = 'utf-8')
for sentence in sentences:
    _ = f.write(sentence + '\n')
    
f.close()

