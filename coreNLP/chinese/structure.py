import sys
import os
from nltk.tree import Tree
from stanford import *

# os.environ['JAVA_HOME']

root = '../stanford-corenlp-full-2017-06-09/'
modelPath = root + 'models/lexparser/chinesePCFG.ser.gz'
optType = 'penn'
parser = StanfordParser(modelPath, root, optType)
result = parser.parse('羅馬尼亞 的 首都 是 布加勒斯特 。 ')
print(result)
# tree = Tree.fromstring(result)
# tree.draw()
