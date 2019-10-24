
dataDir=/home/IRISAD/natasa.sdj/nlp_sdsc/democrasci_bert/data/AB

for year in `seq 1950 1980`
do
python create_pretraining_data.py \
       --input_file=$dataDir/$year/sentences.txt \
       --output_file=./data_train_democrasci_cased/tf_examples_$year.tfrecord \
       --vocab_file=./multi_cased_L-12_H-768_A-12/vocab.txt \
       --do_lower_case=False \
       --max_seq_length=64 \
       --max_predictions_per_seq=20 \
       --masked_lm_prob=0.15 \
       --random_seed=12345 \
       --dupe_factor=5

done
