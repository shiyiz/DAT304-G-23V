import pandas as pd
from flair.data import Corpus
from flair.datasets import ColumnCorpus
from flair.embeddings import WordEmbeddings, StackedEmbeddings, TokenEmbeddings, FlairEmbeddings
from typing import List
from flair.models import SequenceTagger
from flair.trainers import ModelTrainer


#data = pd.read_csv(r'BIO_tagged_CVE3.txt',sep=' ',error_bad_lines=False)
#print(data)
#data.to_csv(r'D:\304\Github\DAT304-G-23V\flair\train.txt')
columns = {0 : 'text', 1 : 'ner'}
data_folder = r'.\flair'
corpus: Corpus = ColumnCorpus(data_folder, columns,
                              train_file ='train.txt',
                              test_file='test.txt',
                              dev_file='dev.txt')
tag_type = 'ner'
label_dictionary = corpus.make_label_dictionary(label_type=tag_type)
print(label_dictionary)
embedding_types : List[TokenEmbeddings] = [
        WordEmbeddings('glove'),
        FlairEmbeddings('news-forward'),
        FlairEmbeddings('news-backward'),
        FlairEmbeddings('mix-forward'),
        FlairEmbeddings('mix-backward')
        ]
embeddings : StackedEmbeddings = StackedEmbeddings(
                                 embeddings=embedding_types)

tagger : SequenceTagger = SequenceTagger(hidden_size=256,
                                       embeddings=embeddings,
                                       tag_dictionary=label_dictionary,
                                       tag_type=tag_type,
                                       use_crf=True)
print(tagger)

trainer : ModelTrainer = ModelTrainer(tagger, corpus)
trainer.train('example-ner',
              learning_rate=0.1,
              mini_batch_size=4,
              max_epochs=2000)
