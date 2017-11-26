# -*- coding: utf-8 -*-
from pyltp import *

sent = '在 包含 問題 的 所有 解 的 解空間樹 中 ， 按照 深度優先 搜尋 的 策略 ， 從 根節點 出發 深度優先 搜尋 解空間樹'
words = sent.split(' ')
postagger = Postagger()
postagger.load('./data/ltp_data_v3.4.0/pos.model')
tags = postagger.postag(words)

for word, tag in zip(words, tags):
    print(word + '/' + tag)
