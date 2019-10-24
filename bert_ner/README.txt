
Folder 'myscripts' contains:
run_ner_all.sh - a script for fine-tuning BERT-NER with a custom dataset (in this case with european Newspaper and CoNLL-2003)
run_ner_predict.sh - a script for testing the BERT-NER model
analysis.py and analysis_2.py output text with original labels in the democracy test dataset and the labels obtained by the fine-tuned models
correction_1.py and correction_2.py - correction of performance evaluation (it is done because of the specifics of the labeling procedure)
difference.py - outputs sentences that contain model labels different than the true labels 

Folder 'results' contains:
text_diff.txt - the sentences where our model gives different results than the labeling
