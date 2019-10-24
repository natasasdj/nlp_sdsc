import os
bert_ner_dir ='/home/IRISAD/natasa.sdj/nlp_sdsc/BERT-NER/'
fname = os.path.join(bert_ner_dir, 'output/bert-pretrained-all_data-all_e10', 'label_test.txt')
f1 = open(fname, encoding='utf8')
fname = os.path.join(bert_ner_dir, 'output/bert-pretrained-all_data-all_e10', 'label_test_corr1.txt')
f2 = open(fname, 'w', encoding='utf8')

def get_bare_entity(word):
    if word.startswith('B-'):
        label = word.lstrip('B-')
        return label
    if word.startswith('I-'):
        label = word.lstrip('I-')
        return label
    return word

for line in f1:
    line = line.strip()
    if len(line)==0:
        f2.write('\n')
        continue
    words = line.split()
    if words[2]==words[1]:
        f2.write(line + '\n')
        continue
    label1 = get_bare_entity(words[1])
    label2 = get_bare_entity(words[2])
    if label1==label2:
        words[2] = words[1]
        line = '\t'.join(words)
        f2.write(line + '\n')
        continue
    f2.write(line + '\n')
        
f1.close()
f2.close()

'''
f2 = open(fname, encoding='utf8')
for line in f2:
    line = line.strip()
    if len(line)==0:
        continue
    l = len(line.split())
    if len(line.split())!=3:
        print(line)
    print(l)    

f2.close()
'''
