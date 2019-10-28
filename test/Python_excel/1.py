#!/usr/bin/env python
# encoding: utf-8
# https://www.bilibili.com/video/av61960794?from=search&seid=11713152005019222459
import xlrd
import xlwt

# 读
data_list = []
with xlrd.open_workbook(r".\test_excel.xlsm") as data:
    table = data.sheet_by_index(0)
    rows_count = table.nrows
    for row_idw in range(1, rows_count):
        country = table.cell(row_idw, 1).value
        unit_saled = table.cell(row_idw, 4).value
        data_list.append((country, unit_saled))

contrys = list(set([country for country, ct in data_list]))
result = [(country, sum([s for c, s in data_list if country==c])) for contry in contrys]
for contry,rs in result:
    print(f'{country:9}:{rs:9}')

# 写
book = xlwt.Workbook
sheet = book.add_sheet('country_unit_saled')
sheet.write(0, 0, "country name")
sheet.write(0, 1, "unit saled")
idx = 1
for country, saled in result:
    sheet.write(idx, 0, country)
    sheet.write(idx, 1, saled)
    idx+=1
book.save('country_unit_saled')
