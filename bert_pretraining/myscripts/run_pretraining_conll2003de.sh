BERT_BASE_DIR=multi_cased_L-12_H-768_A-12
python run_pretraining.py \
       --input_file=data_conll2003de/* \
       --output_dir=./tmp/pretraining_conll2003de-train \
       --do_train=True \
       --do_eval=True \
       --bert_config_file=$BERT_BASE_DIR/bert_config.json \
       --init_checkpoint=$BERT_BASE_DIR/bert_model.ckpt \
       --train_batch_size=32 \
       --max_seq_length=64 \
       --max_predictions_per_seq=20 \
       --num_train_steps=10000 \
       --num_warmup_steps=1000 \
       --learning_rate=2e-5

