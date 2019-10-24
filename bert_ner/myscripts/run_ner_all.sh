#!/usr/bin/env bash
#model_dir=multi_cased_L-12_H-768_A-12
#output_dir=./output/result_conll2003de_e20
#model_dir=multi_cased_pretrained-democrasci
#output_dir=./output/result_conll2003de_pretrained-democrasci_e20
BERT_BASE_DIR=multi_cased_L-12_H-768_A-12
model_dir=pretrained_bert_models/multi-cased_all-10k
output_dir=./output/bert-pretrained-all_data-all_e20
mkdir $output_dir

python BERT_NER.py\
    --task_name="NER"  \
    --do_lower_case=True \
    --crf=True \
    --do_train=True   \
    --do_eval=False   \
    --do_predict=True \
    --data_dir=data_all\
    --vocab_file=$BERT_BASE_DIR/vocab.txt  \
    --bert_config_file=$BERT_BASE_DIR/bert_config.json \
    --init_checkpoint=$model_dir/model.ckpt-10000   \
    --max_seq_length=64   \
    --train_batch_size=32   \
    --learning_rate=2e-5   \
    --num_train_epochs=20 \
    --output_dir=$output_dir


#    --init_checkpoint=$model_dir/bert_model.ckpt  # for multi_cased_L-12_H-768_A-12
#    --init_checkpoint=$model_dir/model.ckpt-10000 # for multi_cased_pretrained-democrasci

#perl conlleval.pl -d '\t' < ./output/result_dir/label_test.txt
perl conlleval.pl -l -d '\t' < $output_dir/label_test.txt 
