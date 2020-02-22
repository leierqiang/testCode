"""
1.安装tesseract-ocr
2.安装(汉语)语言库
2.1 检查本地支持的语言库  tesseract --list-langs
2.2下载 chi_sim.traindata 汉语字库放在本地 *Tesseract-OCR\tessdata\目录下
"""

import pytesseract  # python调用tesseract的库
from PIL import Image  # Python打开图片的库

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

image = Image.open("b.png")
# text = pytesseract.image_to_string(image, lang='chi_sim')  # 指定汉语
text = pytesseract.image_to_string(image)  # 指定语言
print(text)
