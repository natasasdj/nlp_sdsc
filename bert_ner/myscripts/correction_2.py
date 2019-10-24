import os
bert_ner_dir ='/home/IRISAD/natasa.sdj/nlp_sdsc/BERT-NER/'
fname = os.path.join(bert_ner_dir, 'output/bert-pretrained-all_data-all_e10', 'label_test_corr1.txt')
f1 = open(fname, encoding='utf8')
fname = os.path.join(bert_ner_dir, 'output/bert-pretrained-all_data-all_e10', 'label_test_corr2.txt')
f2 = open(fname, 'w', encoding='utf8')


for line in f1:
    line = line.strip()
    if len(line)==0:
        f2.write('\n')
        continue
    words = line.split()
    if 'PER' in words[1]:
        perWords = ['herr', 'herrn', 'herren', 'her', 'hr', 'ant', 'und', 'chef', 'des', 'eisenbahn', 'dr', 'dr.', 'präsident', 'des', 'mehrheit', 'deutsche', 'national', 'conseiller', 'kollegen', 'le', 'der', 'kollegen', 'präsident', 'kommission',  'departement', 'bundesrat', 'bundesrichter']
        if words[0].strip().lower() in perWords:
            words[1]='O'
            line = '\t'.join(words)
            
    f2.write(line + '\n')


f1.close()
f2.close()

# h jo PER
# BILL -> O
#Ant B-MISC
#des I-MISC
#Herrn I-MISC
#Jo I-MISC
