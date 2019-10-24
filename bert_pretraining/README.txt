Pretraining requires input data in a file where each line contains a sentence and an empty line between paragraphs.
In the case of the democracy dataset: an empty line denotes split between different speeces.

The folder 'myscripts' contains:
- scripts for creating pretraining data in bert (these scripts require that the corresponding scripts for datasets' preprocessing (in folder preprocessing) are already run)
create_pretraining_conll2003.sh, create_pretraining_democrasci.sh, create_pretraining_europeNewspaper.sh
- scripts for runnung bert pretraining data
run_pretraining_democrasci.sh, run_pretraining_conll2003de.sh, run_pretraining_all.sh

The folder 'pretrained_bert_models' contains:
- multi_cased_L-12_H-768_A-12: a pretrained multi-language-cased bert model done by Google
- multi-cased_democrasci-10k: a pretrained model with the democrasci dataset for 10K time steps (start from multi-language-cased pretrained bert model)
- multi-cased_conll2003de-train-10k: a pretrained model with the German CoNLL-2003 dataset for 10K time steps
- multi-cased_all-10k: a pretrained model with all the available German dataset (democrasci, european newspapers, CoNLL-2003) for 10K time steps
(pretraining starts from multi-language-cased pretrained bert model (multi_cased_L-12_H-768_A-12))
