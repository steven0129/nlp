# -*- coding: utf-8 -*-
import nltk
from nltk.tree import Tree
from nltk.grammar import DependencyGrammar
from nltk.parse import *
from pyltp import *
import re

sent = '在 包含 問題 的 所有 解 的 解空間樹 中 ， 按照 深度優先 搜尋 的 策略 ， 從 根節點 出發 深度優先 搜尋 解空間樹'
words = sent.split(' ')
postagger = Postagger()
postagger.load('./data/ltp_data_v3.4.0/pos.model')
postags = postagger.postag(words)
tags=[]

for word, tag in zip(words, postags):
    tags.append(tag)

parser = Parser()
parser.load('./data/ltp_data_v3.4.0/parser.model')
arcs = parser.parse(words, tags)
arclen = len(arcs)
conll = ''

for i in range(arclen):
    if(arcs[i].head == 0):
        arcs[i].relation = 'ROOT'
    conll += "\t" + words[i] + "(" + tags[i] + ")" + "\t" + tags[i] + \
        "\t" + str(arcs[i].head) + "\t" + arcs[i].relation + "\n"

print(conll)
conlltree = DependencyGraph(conll)  # 轉換為依序句法樹
tree = conlltree.tree()
tree.draw()
