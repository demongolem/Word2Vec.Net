from gensim.test.utils import datapath, get_tmpfile
from gensim.models import KeyedVectors
from gensim.scripts.glove2word2vec import glove2word2vec
import os
from pathlib import Path

OUT_FILENAME = 'C:\\Users\\g.werner\\Desktop\\demongolem\\AgentAnnotator\\AnnotationTool\\wordvec\\word2vec.6B.100d.txt'

IN_FILENAME = 'C:\\Users\\g.werner\\Desktop\\demongolem\\AgentAnnotator\\AnnotationTool\\wordvec\\glove.6B.100d.txt'

glove_file = datapath(IN_FILENAME)
tmp_file = get_tmpfile(OUT_FILENAME)

_ = glove2word2vec(glove_file, tmp_file)

model = KeyedVectors.load_word2vec_format(tmp_file)