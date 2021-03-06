
import json
# f = open('workfile.txt', 'w')
# f.write('This is a test\n')
# f.write('0123456789abcdef')
# f.close()

f = open('workfile.txt', 'r+')

print f.read()

f.seek(0)
for l in f:
	print l

f.close()


import xlsxwriter

workbook = xlsxwriter.Workbook('demo.xlsx')
worksheet = workbook.add_worksheet()

# Widen the first column to make the text clearer.
worksheet.set_column('A:A', 20)

# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': True})

# Write some simple text.
worksheet.write('A1', 'Hello')

# Text with formatting.
worksheet.write('A2', 'World', bold)

# Write some numbers, with row/column notation.
worksheet.write(2, 0, 123)
worksheet.write(3, 0, 123.456)


workbook.close()