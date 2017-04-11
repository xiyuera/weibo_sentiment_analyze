# coding=utf-8

import csv
import xlrd
from snownlp import SnowNLP

source = open("data/source.csv", "r")
target = open("data/target.csv", "w")

reader = csv.reader(source)
writer = csv.writer(target)

for i, line in enumerate(reader):
	if i == 0:


	else:
		# s = SnowNLP(line[10])
		writer.writerow(line[10])

source.close()
target.close()
