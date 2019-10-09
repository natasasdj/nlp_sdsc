import o

# create sentences from CoNLL-2003 German dataset
# this is needed to get a format for fine-tuning bert

fdir = '/home/IRISAD/natasa.sdj/nlp_sdsc/BERT-NER/data_conll2003de'
fname = os.path.join(fdir, 'train.txt')
f = open(fname, encoding='utf-8')
fname = os.path.join(fdir, 'sentences_train.txt')
f2 = open(fname, 'w', encoding='utf-8')
firstWord = True
#firstDoc = True
#firstLine = True
s = ''
#k = 0
for line in f:
    #k += 1
    #if k > 1430: break
    print(line, len(line))
    line = line.strip()
    print(line, len(line))
    if len(line)==0:
        #if not prevWord=='-DOCSTART-': f2.write(s + '\n')
        f2.write(s+'\n')
        s = ''
        firstWord = True
        continue    
    word = line.split()[0]
    prevWord = word
    print(word)
    if word=='-DOCSTART-':
        s = s + '\n'
        continue
    '''
        if firstDoc:
            print("1", s)
            firstDoc = False
        else:
            print("2", s)
            s = s + '\n'
        continue
    '''
    if firstWord:
        s += word
        firstWord = False
        continue
    if word in ['.',',',':',';']:
        s += word
    else:
        s += ' ' + word


f.close()
f2.close()
