# -*- coding: utf-8 -*-
import sys
import os
from stanford import StanfordPOSTagger

root = '../stanford-corenlp-full-2017-06-09/'
modelPath = root + 'models/chinese-distsim.tagger'
st = StanfordPOSTagger(root, modelPath)

segSent = '在 包含 問題 的 所有 解 的 解空間樹 中 ， 按照 深度優先 搜尋 的 策略 ， 從 根節點 出發 深度優先 搜尋 解空間樹'
tagList = st.tag(segSent)
print(tagList)
