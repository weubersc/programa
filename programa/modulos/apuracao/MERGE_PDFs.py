from reportlab.pdfgen.canvas import Canvas
from pdfrw import PdfReader
from PyPDF2 import PdfFileMerger
from pdfrw.toreportlab import makerl
from pdfrw.buildxobj import pagexobj
import os

def TABULACAO(ano,sem):
    merger = PdfFileMerger()
    dirp=((os.getcwd()))
    dirARQ=os.path.join(dirp,"programa","saida",
                        "apuracao","Brasil")
    merger.append(dirARQ+"\\TAB12.pdf")
    merger.append(dirARQ+"\\TAB34.pdf")
    merger.append(dirARQ+"\\TAB5.pdf")
    merger.append(dirARQ+"\\TAB6.pdf")
    merger.append(dirARQ+"\\TAB7.pdf")
    merger.append(dirARQ+"\\TAB8.pdf")
    merger.append(dirARQ+"\\TAB9.pdf")
    merger.append(dirARQ+"\\TAB10.pdf")
    merger.append(dirARQ+"\\TAB111.pdf")
    merger.append(dirARQ+"\\TAB112.pdf")
    merger.append(dirARQ+"\\TAB113.pdf")
    merger.append(dirARQ+"\\TAB114.pdf")
    merger.append(dirARQ+"\\TAB115.pdf")
    merger.append(dirARQ+"\\TAB116.pdf")
    merger.append(dirARQ+"\\TAB12B.pdf")
    merger.write(dirARQ+"\\TAB_BRASIL.pdf")
    input_file =dirARQ+"\\TAB_BRASIL.pdf"      
    output_file = dirARQ+"\\TAB_BRASIL_"+sem+"-semestre_"+ano+".pdf"

    # Get pages
    reader = PdfReader(input_file)
    pages = [pagexobj(p) for p in reader.pages]


    # Compose new pdf
    canvas = Canvas(output_file)

    for page_num, page in enumerate(pages, start=1):

        # Add page
        canvas.setPageSize((page.BBox[2], page.BBox[3]))
        canvas.doForm(makerl(canvas, page))

        # Draw footer
    #    footer_text = "Page %s of %s" % (page_num, len(pages))
        footer_text = " %s" % (page_num)
        x = 128
        canvas.saveState()
        canvas.setStrokeColorRGB(0, 0, 0)
    #   canvas.setLineWidth(0.5)
    #   canvas.line(66, 78, page.BBox[2] - 66, 78)
        canvas.setFont('Times-Roman', 12)
    #   canvas.drawString(page.BBox[2]-x, 30, footer_text)
        canvas.drawString(page.BBox[2]-300,30, footer_text)
        canvas.restoreState()
        canvas.showPage()

    canvas.save()
        
