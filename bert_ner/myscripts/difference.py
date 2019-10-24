# export PYTHONIOENCODING=UTF-8
# change BERT-NER to write empty lines when there is CLS
# remove line 772 (empty line) in data_democracy/test.txt
# sed -i '772d' data_democracy/pp_accepted_2.txt
# sed -i '4216,4305d' data_democracy/pp_accepted_2.txt
# sed -i '4622,4660d' data_democracy/pp_accepted_2.txt

import os
bert_ner_dir ='/home/IRISAD/natasa.sdj/nlp_sdsc/BERT-NER/'
#fname = os.path.join(bert_ner_dir, 'output/bert-pretrained-all_data-all_e10', 'label_test_corr2.txt')
fname = os.path.join(bert_ner_dir, 'output/bert-pretrained-all_data-all_e10', 'label_test.txt')
f1 = open(fname, encoding='utf8')
#fname = os.path.join(bert_ner_dir, 'output/bert-pretrained-all_data-all_e10', 'diff_corr2.txt')
fname = os.path.join(bert_ner_dir, 'output/bert-pretrained-all_data-all_e10', 'diff_orig.txt')
f2 = open(fname, 'w', encoding='utf8')

def get_tabSeparator(word):
    if len(word)>15:
        sep='\t'
    elif len(word)>7:
        sep='\t\t'
    else:
        sep='\t\t\t'
    return sep

s = ''
diff = False                

for line in f1:
    line = line.strip()
    if len(line)==0:
        if diff: f2.write(s + '\n')
        s = ''
        diff = False
        continue
    
    words = line.split()
    if words[1].strip()!=words[2].strip():
        diff = True

    s = s + '\n' + line


'''
    if len(line1)==0:
        while len(line2)>0:
            sep1=get_tabSeparator(words2[0])
            s = s + words2[0] + sep1 + 'noword' + '\t\t\t' + words2[1] + '\t' + 'X' + '\t' + 'X' + '\n'
            line2=f2.readline().strip()
            words2 = line2.split()
            print(j, "line2:",line2, words2)
            j += 1
        if diff:
            f3.write(s + '\n')
        s = ''
        diff = False
        continue

    if len(line2)==0:
        line2 = f2.readline().strip()
        words2 = line2.split()
        print(j, "line2:",line2, words2)
        j+=1
        

    sep1=get_tabSeparator(words2[0])
    sep2=get_tabSeparator(words1[0])
                
    s = s + words2[0] + sep1 + words1[0] + sep2 + words2[1] + '\t' + words1[1] + '\t' + words1[2] + '\n'
    

for line in f2:
    line = line.strip()
    print(line)
    if len(line)==0:
        if diff and len(s)>0:
            f3.write(s+'\n')
        s = ''
        diff = False
        continue
    words = line.split()
    line_test = f1.readline().strip()
    print(line_test)
    words_test = line_test.split()
    if words[1] != words_test[1]:
        print("something is wrong")
        print(line, words, line_test, words_test)
        print(words[1], words_test[1])
        break
    if words_test[1] != words_test[2]:
        diff = True
    s = s + words[0] + ' ' + words_test[0] + ' ' + words[1] + ' ' + words_test[1] + ' ' + words_test[2] + '\n'
'''    
f1.close()
f2.close()

