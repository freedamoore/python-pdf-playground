import PyPDF2
import sys # this is for the inputs 

### below is an example of rotating a file and saving it under another name
### command: python pdf.py
# with open('dummy.pdf', 'rb') as file:
#     reader = PyPDF2.PdfFileReader(file)
#     page = reader.getPage(0)
#     page.rotateCounterClockwise(90)
#     writer = PyPDF2.PdfFileWriter()
#     writer.addPage(page)
#     with open('tilt.pdf', 'wb') as new_file: 
#         writer.write(new_file)



### combine two or more files
### command: python pdf.py <<file1.pdf>> <<file2.pdf>> .... e.g. python pdf.py dummy.pdf twopage.pdf
# inputs = sys.argv[1:]

# def pdf_combiner(pdf_list):
#     merger = PyPDF2.PdfFileMerger()
#     for pdf in pdf_list:
#         merger.append(pdf)
#     merger.write('super.pdf')

# pdf_combiner(inputs)    



### watermark a file
### command: python pdf.py
template = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open('watermarked_output.pdf', 'wb') as file:
        output.write(file)



