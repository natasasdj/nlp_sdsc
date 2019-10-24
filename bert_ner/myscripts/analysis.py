# change BERT-NER to write empty lines when there is CLS
# remove line 772 (empty line) in data_democracy/test.txt
import os
bert_ner_dir ='/home/IRISAD/natasa.sdj/nlp_sdsc/BERT-NER/'
labels_test_fname = os.path.join(bert_ner_dir, 'output/bert-pretrained-all_data-all_e10', 'label_test.txt')
data_test_fname = os.path.join(bert_ner_dir, 'data_democracy', 'test.txt')
diff_fname = os.path.join(bert_ner_dir, 'data_democracy', 'test_diff.txt')
f1 = open(labels_test_fname, encoding='utf8')
f2 = open(data_test_fname, encoding='utf8')
f3 = open(diff_fname, 'w', encoding='utf8')

s = '';
diff = False
line1=f1.readline().strip()
print("line1:",line1)
i = 2
j = 1
while 1:
    line1 = f1.readline().strip()
    words1 = line1.split()
    print(i, "line1:",line1, words1)
    i += 1
    line2 = f2.readline().strip()
    words2 = line2.split()
    print(j, "line2:",line2, words2)
    j += 1

    if len(line1)==0:
        while len(line2)>0:
            s = s + words2[0] + ' ' + 'noword' + ' ' + words2[1] + ' ' + 'X' + ' ' + 'X' + '\n'
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

    s = s + words2[0] + ' ' + words1[0] + ' ' + words2[1] + ' ' + words1[1] + ' ' + words1[2] + '\n'

    if words2[1] != words1[1]:
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
