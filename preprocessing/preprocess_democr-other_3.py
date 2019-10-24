import json
import os

# preprocessing of the test democracy dataset
# the same as in preprocess_democr-other.py except that BILL and LAW are not replaced with MISC
# this is for the purpose of not using these lines for evaluation



data_dir = '/home/IRISAD/natasa.sdj/nlp_sdsc/democrasci_bert/data'
fname = os.path.join(data_dir,'other','democrasci_prodt_part1_April8.jsonl')
f = open(fname, encoding='utf-8')
fname = os.path.join(data_dir,'other','pp_accepted_bill-law-to-misc.txt')
fw = open(fname, 'w+', encoding='utf-8')

for line in f:
    #line = f.readline()
    json_line = json.loads(line)
    if not json_line['answer']=='accept': continue
    n = len(json_line['tokens'])
    tags = ['O']*n
    for span in json_line['spans']:
        first = True
        if 'LAW' in span['label'] or 'BILL' in span['label']:
            span['label'] = 'MISC'
        for j in range(span['token_start'],span['token_end']+1):
            if span['label']=='O':
                continue               
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
