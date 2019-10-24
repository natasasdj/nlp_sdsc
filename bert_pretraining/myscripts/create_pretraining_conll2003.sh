
#dataDir=/home/IRISAD/natasa.sdj/nlp_sdsc/BERT-NER/data_conll2003de
dataDir=/home/IRISAD/natasa.sdj/nlp_sdsc/eci_multilang_txt/ner
outputDir=./data_conll2003de
mkdir $outputDir

python create_pretraining_data.py \
       --input_file=$dataDir/deu.testb.sentences \
       --output_file=$outputDir/tf_examples_deutestb.tfrecord \
       --vocab_file=./multi_cased_L-12_H-768_A-12/vocab.txt \
       --do_lower_case=False \
       --max_seq_length=64 \
       --max_predictions_per_seq=20 \
       --masked_lm_prob=0.15 \
       --random_seed=12345 \
       --dupe_factor=5

#--input_file=$dataDir/deu.train.sentences \
#--output_file=$outputDir/tf_examples_deutrain.tfrecord \
#--input_file=$dataDir/deu.testa.sentences \
#--output_file=$outputDir/tf_examples_deutesta.tfrecord \
#--input_file=$dataDir/deu.testb.sentences \
#--output_file=$outputDir/tf_examples_deutestb.tfrecord \       
