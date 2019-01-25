# Word2Vec.Net
Based on Y. Abdullin's Word2Vec.Net port of Word2Vec forked on Jan 25, 2019.

The reason that we push forward our own copy is that there are more advanced features we would like to make available:

1) We would like to expose the `M` vector in the `Word2VecAnalysisBase.cs` file so that we can provide for linear operations on that vector such as add, subtract and average.
2) To my knowledge, this code does not properly read in externally trained data, such as data in either Word2Vec or Glove format.  It works fine if I want to train on my own data, but I would like to skip the training process and use pre-defined vector files.  In addition, the way the arrays are implemented, there is that 2M limitation which makes some of the larger pre-defined vectors impossible to use, even if they were readable in the first place by the code.
3) I like to study Russian and am somewhat familiar with that language from an NLP point-of-view, however it would also be useful to have some English examples to distribute to those who want to try the code out to see if it is for them.
