# -*- coding: utf-8 -*-

from pdf2image import convert_from_path, convert_from_bytes

images = convert_from_path(r'C:\\Users\\Usuario\\Documents\\Python3_Projects\\splitPDF\\document-page0.pdf')
images[0].save('test.png', 'png')