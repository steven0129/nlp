# -*- coding: utf-8 -*-
import sys
import os
import jieba

sent='在包含問題的所有解的解空間樹中，按照深度優先搜尋的策略，從根節點出發深度優先搜尋解空間樹'

# 全模式
wordList=jieba.cut(sent, cut_all=True)
print(' | '.join(wordList)) 

# 精準切分
wordList=jieba.cut(sent)
print(' | '.join(wordList))

# 搜尋引擎模式
wordList=jieba.cut_for_search(sent)
print(' | '.join(wordList))