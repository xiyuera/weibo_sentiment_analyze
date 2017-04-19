# -*- coding: utf-8 -*-
# 
# 情感分析

import xlwt
import xlrd
from xlutils.copy import copy
from snownlp import SnowNLP

snownlp.load("sentiment/sentiment.marshal")

book = xlrd.open_workbook("data/target.xls", encoding_override='utf-8', formatting_info=True, on_demand=True)
source_sheet = book.sheet_by_name(u"数据源")

workbook = copy(book)
workbook.encoding = 'utf-8'
try:
	target_sheet = workbook.get_sheet(u"情感分析")
except IndexError as e:
	target_book = workbook.add_sheet("情感分析", cell_overwrite_ok=True)

target_sheet.write(0, 0, u"正面值")
target_sheet.write(0, 1, u"语句")

for i in range(1, source_sheet.nrows):
	txt = source_sheet.cell_value(i, 10)
	s = SnowNLP(txt)
	target_sheet.write(i, 0, s.sentiments)
	target_sheet.write(i, 1, txt)

	if i % 100 == 0:
		target_sheet.flush_row_data()

workbook.save("data/target.xls")