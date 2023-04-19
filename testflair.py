from flair.data import Sentence
from flair.models import SequenceTagger

model = SequenceTagger.load('D:/304/example-ner/final-model.pt')

sentence = Sentence('Atom CMS v2.0 was discovered to contain a SQL injection vulnerability via the id parameter in /admin/ajax/avatar.php.')

model.predict(sentence)
print(sentence.to_tagged_string())