* Folder 'preprocessing' contains scripts for preparing datasets in a format suitable as input to BERT (https://github.com/google-research/bert) and BERT-NER (https://github.com/kyzhouhzau/BERT-NER).

* Folder 'bert_pretraining' contains scripts for pretraining (fine tuning) BERT.

* Folder 'bert-ner' contains scripts for fine-tuning BERT-NER, scripts for analysis of evaluation results, and scripts for correction of the performance evaluation (that needs to be perfromed due to the differences in the labeling procedure). 

* CoNLL-2003 German Dataset:
The link https://www.clips.uantwerpen.be/conll2003/ner/ contains the explanation of how to build train, test and validation datasets.
Download data:
https://polybox.ethz.ch/index.php/s/IcY8dH3WU8WMhmg
Download annotations:
http://www.cnts.ua.ac.be/conll2003/ner.tgz

Run ner/bin/make.deu (Before this, it is needed to setup the path towards the data).
Note that 'make.deu' file contains an error (tail +220190 tokenized | head -54713 > ../$DEV). I provide here the corrected 'make2.deu' file that I used (conll2003de/make2.deu). 
