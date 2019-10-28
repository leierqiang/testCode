## 概念

工作簿、表、单元格

---
使用xlrd读取文件，使用xlwt生成Excel文件（可以控制Excel中单元格的格式）。但是用xlrd读取excel是不能对其进行操作的；而xlwt生成excel文件是不能在已有的excel文件基础上进行修改的，如需要修改文件就要使用xluntils模块。pyExcelerator模块与xlwt类似，也可以用来生成excel文件。




Office2003的是.xls
Excel 2007支持文件格式:
Excel Workbook (.xlsx) - 默认格式
Excel Macro-enabled Workbook (.xlsm)
Excel Template (.xltx)
Excel Macro-enabled Workbook Template (.xltm)
Excel Binary Workbook (.xlsb)
Excel Add-in (.xlam)
