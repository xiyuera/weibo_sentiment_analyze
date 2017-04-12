# -*- coding: utf-8 -*-
# 
# 转换 source.csv 为 excel

import csv
import xlwt
from snownlp import SnowNLP

source = open("data/source.csv", "r")

reader = csv.reader(source)

workbook = xlwt.Workbook(encoding="utf-8")
target_book = workbook.add_sheet("数据源", cell_overwrite_ok=True)

for i, line in enumerate(reader):
	row = target_book.row(i)
	for j, cell in enumerate(line):
		row.write(j, cell)

	if i % 100 == 0:
		target_book.flush_row_data()

workbook.save("data/target.xls")