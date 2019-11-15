######  preprocessing of the democratic test dataset #####
preprocess_democr-other.py
- prepare the democratic test dataset in the format necessary for input to BERT-NER
preprocess_democr-other_2.py
- the same as in preprocess_democr-other.py except that BILL and LAW are not replaced with O (for the purpose of inspecting results)
preprocess_democr-other_3.py
- the same as in preprocess_democr-other.py except that BILL and LAW are replaced with MISC (for the purpose of not using these lines for evaluation)

###### preprocessing europe Newspapers dataset
preprocess_europeNewspaper.py
- prepare the europe Newspaper 'lft' and 'onb' dataset in the format necessary for input to BERT-NER
('sbb' datasets have many mistakes and thus it is not used)
preprocess_europeNewspaper_toSentences.py 
- prepare the dataset in a format necessary as input to Bert (each line is a sentence, empty line denotes a separation between documents)

###### preprocessing democrasci (training) dataset
preprocess_democrasci.py
- prepare the dataset in a format necessary as input to Bert (each line is a sentence, empty line denotes a separation between different speeches)

###### preprocessing CoNLL-2003 German dataset dataset
preprocess_conll2003de.py
- this is needed to get a format for input to Bert, in order to further fine-tune Bert 
- train.txt is a merged file of train.deu, testa.deu and testb.deu (seperated by an empy file)
- the CoNLL-2003 datasets are already in the format suitable for the BERT-NER, so no preprocessing is needed
