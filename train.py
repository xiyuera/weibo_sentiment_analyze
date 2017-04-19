# -*- coding: utf-8 -*-
# 
# 情感分析训练

from snownlp import sentiment

sentiment.train("sentiment/neg.txt", "sentiment/pos.txt")
sentiment.save("sentiment/sentiment.marshal")

print("训练完成")