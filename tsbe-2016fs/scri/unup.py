#!/usr/bin/env python
import copy, sys
from pyPdf import PdfFileWriter, PdfFileReader
input = PdfFileReader(sys.stdin)
output = PdfFileWriter()
for p in [input.getPage(i) for i in range(0,input.getNumPages())]:
    q = copy.copy(p)
    (w, h) = p.mediaBox.upperRight
    p.mediaBox.lowerRight = (w, h/2)
    q.mediaBox.upperLeft = (0, h/2)
    output.addPage(p)
    output.addPage(q)
output.write(sys.stdout)
