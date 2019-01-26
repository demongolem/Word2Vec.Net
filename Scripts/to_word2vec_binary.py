from gensim.models import Word2Vec, KeyedVectors
import gensim
sentences = gensim.models.word2vec.LineSentence('glove.6B.100d.txt')
model = gensim.models.Word2Vec(
sentences, size=100, window=5, min_count=5, workers=5,
sg=1, hs=1, negative=0
)
model.wv.save_word2vec_format('glove.6B.100d.bin', binary=True)