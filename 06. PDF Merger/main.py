'''PYCODE | @_py.code'''

# ? 6. PDF Merger
# ? Features: Merge multiple PDF files into one.

# * Source Code
from pypdf import PdfWriter
import os

files = [file for file in os.listdir() if file.endswith('.pdf')]
merger = PdfWriter()
for file in files:
    merger.append(file)
merger.write('Merged_Pdf.pdf')
