# this is only necessary to do for 'sbb' data

import os
import pandas as pd
data_dir = '/home/IRISAD/natasa.sdj/nlp_sdsc/europeNewspaper'
#fname = os.path.join(data_dir, 'enp_DE.lft.bio', 'enp_DE.lft.bio')
#fname = os.path.join(data_dir, 'enp_DE.onb.bio', 'enp_DE.onb.bio')

fname = os.path.join(data_dir, 'enp_DE.sbb.bio', 'enp_DE.sbb.bio')
f = open(fname, encoding = 'utf-8')
fname = os.path.join(data_dir, 'enp_DE.sbb.bio', 'enp_DE.sbb.bio2')
f2 = open(fname, 'w', encoding = 'utf-8')

for line in f:
    if line.startswith('# file'): continue
    if line.startswith('# sbb url'): continue
    if line.startswith('# tel url'): continue
    ss = (line.strip()).split()
    if len(ss)==2:
        _ = f2.write(line.strip()+'\n')
        continue
    if len(ss)<2: continue
    tag = ss[-1]
    for i in range(len(ss)-1):
        if ss[-1].startswith('B-') and i>0:
            tag = ss[-1].replace('B-','I-')
        _ = f2.write(ss[i]+ ' ' + ss[-1] + '\n')


        
f.close()
f2.close()
    
            











#df = pd.read_csv(fname, names = ['token', 'tag'], sep = '\s+|\n', engine = 'python', encoding = 'utf-8')
df = pd.read_csv(fname, names = ['token', 'tag'], sep = '\s+|\n', engine = 'python', encoding = 'utf-8', skiprows = 3) #only for .sbb file
text = ' '.join(df['token'])

