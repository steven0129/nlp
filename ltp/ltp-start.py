# -*- coding: utf-8 -*-
from pyltp import Segmentor

modelPath='./data/ltp_data_v3.4.0/cws.model'
segmentor=Segmentor()
segmentor.load(modelPath)

sent='在包含問題的所有解的解空間樹中，按照深度優先搜尋的策略，從根節點出發深度優先搜尋解空間樹'
words=segmentor.segment(sent)
print(' | '.join(words))