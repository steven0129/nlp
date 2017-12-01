import sys
import os
from pyltp import *

MODEDIR = './data/ltp_data_v3.3.1'
sentence = '歐洲東部的羅馬尼亞，首都是布加勒斯特，也是一座世界性的城市。'
segmentor = Segmentor()
segmentor.load(os.path.join(MODEDIR, 'cws.model'))
words = segmentor.segment(sentence)
wordList = list(words)
postagger = Postagger()
postagger.load(os.path.join(MODEDIR, 'pos.model'))
postags = postagger.postag(words)

parser = Parser()
parser.load(os.path.join(MODEDIR, 'parser.model'))
arcs = parser.parse(words, postags)

recognizer = NamedEntityRecognizer()
recognizer.load(os.path.join(MODEDIR, 'ner.model'))
netags = recognizer.recognize(words, postags)

labeller = SementicRoleLabeller()
labeller.load(os.path.join(MODEDIR, 'srl/'))
roles = labeller.label(words, postags, netags, arcs)

for role in roles:
    print('rel:' + wordList[role.index])  # 謂詞
    for arg in role.arguments:
        if arg.range.start != arg.range.end:
            print(arg.name + ' '.join(wordList[arg.range.start:arg.range.end]))
        else:
            print(arg.name + wordList[arg.range.start])
