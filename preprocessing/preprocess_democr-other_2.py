import json
import os

# preprocessing of the test democracy dataset
# the same as in preprocess_democr-other.py except that BILL and LAW are not replaced with O

data_dir = '/home/IRISAD/natasa.sdj/nlp_sdsc/democrasci_bert/data'
fname = os.path.join(data_dir,'other','democrasci_prodt_part1_April8.jsonl')
f = open(fname, encoding='utf-8')
fname = os.path.join(data_dir,'other','pp_accepted_2.txt')
fw = open(fname, 'w+', encoding='utf-8')

for line in f:
    #line = f.readline()
    json_line = json.loads(line)
    if not json_line['answer']=='accept': continue
    n = len(json_line['tokens'])
    tags = ['O']*n
    for span in json_line['spans']:
        first = True
        tag = None
        #if 'LAW' in span['label'] or 'BILL' in span['label']:
        #    tag = 'O'
        for j in range(span['token_start'],span['token_end']+1):
            if tag: continue
            if first:
                tags[j] = 'B-' + span['label']
                first = False
            else:
                tags[j] = 'I-' + span['label']
    for i in range(n):
        _ = fw.write(json_line['tokens'][i]['text'])
        _ = fw.write(' ')
        _ = fw.write(tags[i])
        _ = fw.write('\n')
    _ = fw.write('\n')
                        
f.close()
fw.close()

# replace B-LAW, I-LAW, B-BILL, I-BILL with O (with 'sed' from shell)
# sed -i -e 's/(B|I)-LAW|(B|I)-BILL/O/g'
