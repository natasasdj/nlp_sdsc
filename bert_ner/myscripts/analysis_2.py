# export PYTHONIOENCODING=UTF-8
# change BERT-NER to write empty lines when there is CLS
# remove line 772 (empty line) in data_democracy/test.txt
# sed -i '772d' data_democracy/pp_accepted_2.txt
# sed -i '4216,4305d' data_democracy/pp_accepted_2.txt
# sed -i '4622,4660d' data_democracy/pp_accepted_2.txt
# sed -i '7363d' data_democracy/pp_accepted_2.txt
# sed -i '8626,8689d' data_democracy/pp_accepted_2.txt
# sed -i '10111,10163d' data_democracy/pp_accepted_2.txt
import os
bert_ner_dir ='/home/IRISAD/natasa.sdj/nlp_sdsc/BERT-NER/'

labels_test_fname = os.path.join(bert_ner_dir, 'output/bert-pretrained-all_data-all_e10', 'label_test1.txt')
f1 = open(labels_test_fname, encoding='utf8')
data_test_fname = os.path.join(bert_ner_dir, 'data_democracy', 'pp_accepted_2.txt')
f2 = open(data_test_fname, encoding='utf8')
diff_fname = os.path.join(bert_ner_dir, 'data_democracy', 'test_diff.txt')
f3 = open(diff_fname, 'w', encoding='utf8')

s = '';
diff = False
line1=f1.readline().strip()
print("line1:",line1)
i = 2
j = 1

def get_tabSeparator(word):
    if len(word)>15:
        sep='\t'
    elif len(word)>7:
        sep='\t\t'
    else:
        sep='\t\t\t'
    return sep

while 1:
    line1 = f1.readline()
    if line1=='': break
    line1 = line1.strip()
    
    words1 = line1.split()
    print(i, "line1:",line1, words1)
    i += 1
    line2 = f2.readline().strip()
    words2 = line2.split()
    print(j, "line2:",line2, words2)
    j += 1

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
        
    print(len(words1), len(words2))
    if len(words1)!=3 or len(words2)!=2:
        continue
    
    c=0
    
    while words1[0]!='[UNK]' and not(words1[0] in words2[0]):
        c+=1
        if c>100: print("c>100"); break
        line2=f2.readline().strip()
        j += 1
        if len(line2)==0: continue
        words2 = line2.split()                                                                                                                           
        

    sep1=get_tabSeparator(words2[0])
    sep2=get_tabSeparator(words1[0])


    s = s + words2[0] + sep1 + words1[0] + sep2 + words2[1] + '\t' + words1[1] + '\t' + words1[2] + '\n'
    if 'BILL' in words2[1] or 'LAW' in words2[1]:
        label = 'O'
    else:
        label = words2[1]
        
    if words1[0]!='[UNK]' and not(words1[0] in words2[0]) or label!=words1[1]:
        print("something is wrong")
        break
    
    if words1[1] != words1[2]:
        diff = True
    
'''
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
f3.close()
