#!/usr/bin/env bash
BERT_BASE_DIR=multi_cased_L-12_H-768_A-12
model_dir=pretrained_bert_models/multi-cased_all-10k
output_dir=./output/bert-pretrained-all_data-all_e10

python BERT_NER.py\
    --task_name="NER"  \
    --do_lower_case=False \
    --crf=True \
    --do_train=False \
    --do_eval=False \
    --do_predict=True \
    --data_dir=data_democracy \
    --vocab_file=$BERT_BASE_DIR/vocab.txt  \
    --bert_config_file=$BERT_BASE_DIR/bert_config.json \
    --init_checkpoint=$model_dir/model.ckpt-10000 \
    --max_seq_length=64  \
    --train_batch_size=32   \
    --learning_rate=2e-5  \
    --num_train_epochs=4.0   \
    --output_dir=$output_dir

#   --data_dir=data_democracy \
#   --data_dir=data_europeNewspaper_onb
#   --data_dir=data_europeNewspaper_lft

#perl conlleval.pl -d '\t' < ./output/result_dir/label_test.txt
perl conlleval.pl -l -d '\t' < $output_dir/label_test.txt
