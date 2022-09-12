from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,PageBreak
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter,legal,landscape,portrait,A3,A4
from reportlab.lib.enums import TA_LEFT, TA_CENTER,TA_JUSTIFY
from listtocsv import listacsv as SAIDA 
import string
import os
from códigos import Codigos as COD
from programa.modulos.apuracao.limador import corretor as COK




class gerar_tabela():

    def __init__(self,semes,ano,cuf):
        CC=COD()
        NOMEUF=CC.codigo
        self.semes=semes
        self.ano=ano
        self.PAGE_HEIGHT=defaultPageSize[0]
        self.PAGE_WIDTH=defaultPageSize[0]
        self.dirp=((os.getcwd()))
        self.dirARQ=os.path.join(self.dirp,"programa","saida",
                                 "apuracao",NOMEUF[str(cuf)])
 


##    def TAB12(self,LL1,LL2):
##        for ll in LL1:
##            print(ll)
##        for ll in LL2:
##            print(ll)
    def TAB12(self,lista1,lista2):
        lista12=[]
        lista12.append(lista1)
        lista12.append(lista2)

        styles = getSampleStyleSheet()
        Title = "LSPA"
        pageinfo = "TABELAS"
        doc = SimpleDocTemplate(self.dirARQ+"\\TAB12_UF.pdf")
        Story = [Spacer(0,0.1*inch)]
        style = styles["Normal"]
        style.alignment =TA_CENTER
        style.fontSize=12
        j=0
        tab=[]
        for lista in lista12:
            t=Table(lista,style=[
            ('FONTSIZE',(0,0),(-1,-1),8),
            ('ALIGN',(0,0),(-1,-1),'CENTER'),
            ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
            ('FONT',(0,0),(-1,-1),'Times-Roman'),
            ('FONTNAME',(0,0),(-1,1),'Times-Bold'),
            ('SPAN',(0,0),(-1,0)),
            ('SPAN',(0,1),(-1,1)),
            ('SPAN',(2,2),(-1,2)),
            ('SPAN',(2,3),(3,3)),
            ('SPAN',(4,3),(5,3)),
            ('SPAN',(6,3),(-1,3)),
            ('SPAN',(0,2),(0,4)),
            ('SPAN',(1,2),(1,4)),
            ('SPAN',(0,-1),(-1,-1)),
            ('ALIGN',(0,5),(0,-1),'LEFT'),
            ('ALIGN',(1,5),(-1,-2),'RIGHT'),
            ('LINEABOVE',(0,1),(-1,4),1,colors.black),
            ('LINEBELOW',(0,0),(-1,4),1,colors.black),
            ('LINEBELOW',(0,-2),(-1,-2),1,colors.black),
            ('GRID',(1,2),(-2,4),1,colors.black),

             ])
            tab.append(t)
        Story.append(tab[0])
        Story.append(Spacer(1,0.9*inch))
        Story.append(tab[1])
        #doc.build(Story, onFirstPage=myPage)
        doc.build(Story)

    def TAB34(self,lista1,lista2):
        lista12=[]
        lista12.append(lista1)
        lista12.append(lista2)

        styles = getSampleStyleSheet()
        Title = "LSPA"
        pageinfo = "TABELAS"
        doc = SimpleDocTemplate(self.dirARQ+"\\TAB34_UF.pdf")
        Story = [Spacer(0,0.1*inch)]
        style = styles["Normal"]
        style.alignment =TA_CENTER
        style.fontSize=12

        t1=Table(lista1,style=[
        ('FONTSIZE',(0,0),(-1,-1),8),
        ('ALIGN',(0,0),(-1,-1),'CENTER'),
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        ('FONT',(0,0),(-1,-1),'Times-Roman'),
        ('FONTNAME',(0,0),(-1,1),'Times-Bold'),
        ('SPAN',(0,0),(-1,0)),
        ('SPAN',(0,1),(-1,1)),
        ('SPAN',(1,2),(2,2)),
        ('SPAN',(0,-1),(2,-1)),
        ('SPAN',(0,2),(0,3)),
        ('LINEABOVE',(0,1),(-1,3),1,colors.black),
        ('LINEBELOW',(0,0),(-1,3),1,colors.black),
        ('LINEBELOW',(0,-2),(-1,-2),1,colors.black),
        ('GRID',(1,2),(-2,3),1,colors.black),
        ('ALIGN',(0,4),(0,-1),'LEFT'),
         ])

        t2=Table(lista2,style=[
        ('FONTSIZE',(0,0),(-1,-1),8),
        ('ALIGN',(0,0),(-1,-1),'CENTER'),
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        ('FONT',(0,0),(-1,-1),'Times-Roman'),
        ('FONTNAME',(0,0),(-1,1),'Times-Bold'),
        ('SPAN',(0,0),(-1,0)),
        ('SPAN',(0,1),(-1,1)),
        ('SPAN',(1,2),(-1,2)),
        ('SPAN',(1,3),(2,3)),
        ('SPAN',(3,3),(4,3)),
        ('SPAN',(5,3),(6,3)),
        ('SPAN',(0,2),(0,4)),
        ('SPAN',(0,-1),(-1,-1)),
        ('LINEABOVE',(0,1),(-1,4),1,colors.black),
        ('LINEABOVE',(0,2),(0,2),1,colors.black),
        ('LINEBELOW',(0,0),(-1,4),1,colors.black),
        ('LINEBELOW',(0,-2),(-1,-2),1,colors.black),
        ('GRID',(1,2),(-2,4),1,colors.black),
        ('ALIGN',(0,5),(0,-1),'LEFT'),
         ])
            
##        legtext = ("<para autoLeading='off'fontSize=12><b>Produção e Variação anual Brasil e Regiões</b></para>" ) 
##        p = Paragraph(legtext,style )
##        Story.append(p)
##        Story.append(Spacer(1,0.2*inch))
        Story.append(t1)
        Story.append(Spacer(1,0.9*inch))
        Story.append(t2)
        #doc.build(Story, onFirstPage=myPage)
        doc.build(Story)
        
    def TAB5(self,lista1):
        styles = getSampleStyleSheet()
        Title = "LSPA"
        pageinfo = "TABELAS"
        doc = SimpleDocTemplate(self.dirARQ+"\\TAB5_UF.pdf")
        Story = [Spacer(0,0.1*inch)]
        style = styles["Normal"]
        style.alignment =TA_CENTER
        style.fontSize=12

        t1=Table(lista1,style=[
        ('FONTSIZE',(0,0),(-1,-1),8),
        ('ALIGN',(0,0),(-1,-1),'CENTER'),
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        ('FONT',(0,0),(-1,-1),'Times-Roman'),
        ('FONTNAME',(0,0),(-1,1),'Times-Bold'),
        ('SPAN',(0,0),(-1,0)),
        ('SPAN',(0,1),(-1,1)),
        ('SPAN',(0,-1),(2,-1)),
        ('LINEABOVE',(0,1),(-1,2),1,colors.black),
        ('LINEBELOW',(0,0),(-1,2),1,colors.black),
        ('LINEBELOW',(0,-2),(-1,-2),1,colors.black),
        ('GRID',(1,2),(-2,2),1,colors.black),
        ('ALIGN',(0,3),(0,-1),'LEFT'),
        ('ALIGN',(3,3),(3,-1),'RIGHT'),
         ])

        Story.append(t1)
        #doc.build(Story, onFirstPage=myPage)
        doc.build(Story)  

    def TAB6(self,lista1,tipo):
        styles = getSampleStyleSheet()
        Title = "LSPA"
        pageinfo = "TABELAS"
        if tipo=="emp":
            doc = SimpleDocTemplate(self.dirARQ+"\\TAB6_UF.pdf",pagesize=landscape(letter))
        if tipo=="ativ":
            doc = SimpleDocTemplate(self.dirARQ+"\\TAB7_UF.pdf",pagesize=landscape(letter))
        Story = [Spacer(0,0.1*inch)]
        style = styles["Normal"]
        style.alignment =TA_CENTER
        style.fontSize=12

        t1=Table(lista1,style=[
        ('FONTSIZE',(0,0),(-1,-1),9),
        ('ALIGN',(0,0),(-1,-1),'CENTER'),
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        ('FONT',(0,0),(-1,-1),'Times-Roman'),
        ('FONTNAME',(0,0),(-1,1),'Times-Bold'),
        ('SPAN',(0,0),(-1,0)),
        ('SPAN',(0,1),(-2,1)),
        ('SPAN',(0,17),(-1,17)),
        ('SPAN',(0,18),(-2,18)),
        ('SPAN',(0,16),(-1,16)),
        ('SPAN',(0,26),(-1,26)),
        ('SPAN',(1,2),(2,2)),
        ('SPAN',(3,2),(4,2)),
        ('SPAN',(5,2),(6,2)),
        ('SPAN',(7,2),(8,2)),
        ('SPAN',(9,2),(10,2)),
        ('SPAN',(11,2),(12,2)),
        ('SPAN',(1,9),(2,9)),
        ('SPAN',(3,9),(4,9)),
        ('SPAN',(5,9),(6,9)),
        ('SPAN',(7,9),(8,9)),
        ('SPAN',(9,9),(10,9)),
        ('SPAN',(11,9),(12,9)),
        ('SPAN',(1,19),(2,19)),
        ('SPAN',(3,19),(4,19)),
        ('SPAN',(5,19),(6,19)),
        ('SPAN',(7,19),(8,19)),
        ('SPAN',(9,19),(10,19)),
        ('SPAN',(11,19),(12,19)),
        ('SPAN',(0,2),(0,3)),
        ('SPAN',(0,9),(0,10)),
        ('SPAN',(0,19),(0,20)),
        ('LINEABOVE',(0,16),(-1,16),1,colors.black),
        ('LINEABOVE',(0,26),(-1,26),1,colors.black),
        ('LINEBELOW',(0,0),(-1,3),1,colors.black),
        ('LINEBELOW',(0,8),(-1,10),1,colors.black),
        ('LINEBELOW',(0,17),(-1,20),1,colors.black),
        ('GRID',(1,2),(-2,3),1,colors.black),
        ('GRID',(1,9),(-2,10),1,colors.black),
        ('GRID',(1,19),(-2,20),1,colors.black),
        ('ALIGN',(0,4),(0,8),'LEFT'),
        ('ALIGN',(0,11),(0,16),'LEFT'),
        ('ALIGN',(0,21),(0,26),'LEFT'),
         ])
        for k in range(4,9):
            t1._argH[k]=0.3*inch
        for k in range(11,16):
            t1._argH[k]=0.3*inch
        for k in range(21,26):
            t1._argH[k]=0.3*inch
        t1._argH[2]=0.4*inch
        t1._argH[8]=0.4*inch
        t1._argH[9]=0.4*inch
        t1._argH[15]=0.4*inch
        t1._argH[19]=0.4*inch
        t1._argH[14]=0.3*inch
        Story.append(t1)
        #doc.build(Story, onFirstPage=myPage)
        doc.build(Story)        
 
    def TAB89(self,lista_C,LESP,tipo):
        corretor=COK(lista_C,89,"nada")
        lista1=corretor.saida
        styles = getSampleStyleSheet()
        Title = "LSPA"
        pageinfo = "TABELAS"
        if tipo=="emp":
            doc = SimpleDocTemplate(self.dirARQ+"\\TAB8_UF.pdf")
        if tipo=="ativ":
            doc = SimpleDocTemplate(self.dirARQ+"\\TAB9_UF.pdf")
        Story = [Spacer(0,0.1*inch)]
        style = styles["Normal"]
        style.alignment =TA_CENTER
        style.fontSize=12
        xcomp=len(lista1)
        for kx in range(0,xcomp-1):
            print("TAB-ENTREI")
            t1=Table(lista1[kx],style=[
            ('FONTSIZE',(0,0),(-1,-1),8),
            ('ALIGN',(0,0),(-1,-1),'CENTER'),
            ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
            ('FONT',(0,0),(-1,-1),'Times-Roman'),
            ('FONTNAME',(0,0),(-1,1),'Times-Bold'),
            ('SPAN',(0,0),(-1,0)),
            ('SPAN',(0,1),(-2,1)),
            ('SPAN',(1,2),(-1,2)),
#            ('SPAN',(0,-1),(-1,-1)),
            ('SPAN',(2,3),(-1,3)),
            ('SPAN',(0,2),(0,4)),
            ('SPAN',(1,3),(1,4)),
            ('ALIGN',(0,5),(0,-1),'LEFT'),
            ('LINEBELOW',(0,0),(-1,4),1,colors.black),
#            ('LINEABOVE',(0,-1),(-1,-1),1,colors.black),
            ('GRID',(1,2),(-2,4),1,colors.black),
             ])
            km=0
            for lista in lista1[kx]:
                print("TAB-ENTREI")
                if km>4:
                    chave=lista[0].lstrip()
                    try:
                        if (LESP[chave])==3:
                            t1._argH[km]=0.15*inch
                        if (LESP[chave])==2:
                            t1._argH[km]=0.25*inch
                        if (LESP[chave])==1:
                            t1._argH[km]=0.31*inch
                    except:
                        pass
                km+=1
##        for k in range(15,24):
##            t1._argH[k]=0.17*inch
##        for k in range(25,29):
##            t1._argH[k]=0.17*inch
##        for k in range(30,33):
##            t1._argH[k]=0.17*inch
##        for k in range(34,38):
##            t1._argH[k]=0.17*inch
##        t1._argH[6]=0.45*inch
##        t1._argH[14]=0.45*inch
##        t1._argH[24]=0.45*inch
##        t1._argH[29]=0.45*inch
##        t1._argH[33]=0.45*inch
##        t1._argH[37]=0.2*inch
            Story.append(t1)
            Story.append(PageBreak())
        t1=Table(lista1[xcomp-1],style=[
            ('FONTSIZE',(0,0),(-1,-1),8),
            ('ALIGN',(0,0),(-1,-1),'CENTER'),
            ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
            ('FONT',(0,0),(-1,-1),'Times-Roman'),
            ('FONTNAME',(0,0),(-1,1),'Times-Bold'),
            ('SPAN',(0,0),(-1,0)),
            ('SPAN',(0,1),(-2,1)),
            ('SPAN',(1,2),(-1,2)),
            ('SPAN',(0,-1),(-1,-1)),
            ('SPAN',(2,3),(-1,3)),
            ('SPAN',(0,2),(0,4)),
            ('SPAN',(1,3),(1,4)),
            ('ALIGN',(0,5),(0,-1),'LEFT'),
            ('LINEBELOW',(0,0),(-1,4),1,colors.black),
            ('LINEABOVE',(0,-1),(-1,-1),1,colors.black),
            ('GRID',(1,2),(-2,4),1,colors.black),
             ])
        km=0
        for lista in lista1[xcomp-1]:
            print("TAB-ENTREI-again")
            if km>4:
                chave=lista[0].lstrip()
                try:
                    if (LESP[chave])==3:
                        t1._argH[km]=0.15*inch
                    if (LESP[chave])==2:
                        t1._argH[km]=0.25*inch
                    if (LESP[chave])==1:
                        t1._argH[km]=0.31*inch
                except:
                    pass
            km+=1
        #doc.build(Story, onFirstPage=myPage)
        Story.append(t1)
        doc.build(Story)

    def TAB10(self,lista_C,LESP):
        print("-----")
        for ll,pp in LESP.items():
            print(ll,pp)
        print("--LESP--")
        corretor=COK(lista_C,10,"nada")
        lista1=corretor.saida
        styles = getSampleStyleSheet()
        Title = "LSPA"
        pageinfo = "TABELAS"
        doc = SimpleDocTemplate(self.dirARQ+"\\TAB10_UF.pdf")
        Story = [Spacer(0,0.1*inch)]
        style = styles["Normal"]
        style.alignment =TA_CENTER
        style.fontSize=12
        xcomp=len(lista1)
        for kx in range(0,xcomp-1):
            t1=Table(lista1[kx],style=[
            ('FONTSIZE',(0,0),(-1,-1),8),
            ('ALIGN',(0,0),(-1,-1),'CENTER'),
            ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
            ('FONT',(0,0),(-1,-1),'Times-Roman'),
            ('FONTNAME',(0,0),(-1,1),'Times-Bold'),
            ('SPAN',(0,0),(-1,0)),
            ('SPAN',(0,1),(-2,1)),
            ('SPAN',(2,2),(3,2)),
            ('SPAN',(4,2),(5,2)),
            ('SPAN',(6,2),(7,2)),
            ('SPAN',(0,2),(0,3)),
            ('SPAN',(1,2),(1,3)),
#            ('SPAN',(0,-1),(-1,-1)),
            ('ALIGN',(0,4),(0,-1),'LEFT'),
            ('LINEBELOW',(0,0),(-1,3),1,colors.black),
#            ('LINEABOVE',(0,-1),(-1,-1),1,colors.black),
            ('GRID',(1,2),(-2,3),1,colors.black),
             ])
            km=0
#OLHAR AQUI
            for lista in lista1[kx]:
                print(lista)
                if km>3:
                    chave=lista[0].lstrip()
                    print(chave)
                    print(LESP[chave])
                    print("--chave--")
                    try:
                        if (LESP[chave])==3:
                            t1._argH[km]=0.15*inch
                        if (LESP[chave])==2:
                            t1._argH[km]=0.25*inch
                        if (LESP[chave])==1:
                            t1._argH[km]=0.31*inch
                    except:
                        pass
                km+=1
            Story.append(t1)
            Story.append(PageBreak())

        t1=Table(lista1[xcomp-1],style=[
            ('FONTSIZE',(0,0),(-1,-1),8),
            ('ALIGN',(0,0),(-1,-1),'CENTER'),
            ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
            ('FONT',(0,0),(-1,-1),'Times-Roman'),
            ('FONTNAME',(0,0),(-1,1),'Times-Bold'),
            ('SPAN',(0,0),(-1,0)),
            ('SPAN',(0,1),(-2,1)),
            ('SPAN',(2,2),(3,2)),
            ('SPAN',(4,2),(5,2)),
            ('SPAN',(6,2),(7,2)),
            ('SPAN',(0,2),(0,3)),
            ('SPAN',(1,2),(1,3)),
            ('SPAN',(0,-1),(-1,-1)),
            ('ALIGN',(0,4),(0,-1),'LEFT'),
            ('LINEBELOW',(0,0),(-1,3),1,colors.black),
            ('LINEABOVE',(0,-1),(-1,-1),1,colors.black),
            ('GRID',(1,2),(-2,3),1,colors.black),
             ])
        km=0
        try:
            for lista in lista1[xcomp-1]:
                if km>3:
                    chave=lista[0].lstrip()
                    try:
                        if (LESP[chave])==3:
                            t1._argH[km]=0.15*inch
                        if (LESP[chave])==2:
                            t1._argH[km]=0.25*inch
                        if (LESP[chave])==1:
                            t1._argH[km]=0.31*inch
                    except:
                        pass
                km+=1
        except:
            for lista in lista1:
                if km>3:
                    chave=lista[0].lstrip()
                    try:
                        if (LESP[chave])==3:
                            t1._argH[km]=0.15*inch
                        if (LESP[chave])==2:
                            t1._argH[km]=0.25*inch
                        if (LESP[chave])==1:
                            t1._argH[km]=0.31*inch
                    except:
                        pass
                km+=1
        Story.append(t1)
        #doc.build(Story, onFirstPage=myPage)
        doc.build(Story)

    def TAB11(self,lista1,LESP,indice):
        styles = getSampleStyleSheet()
        Title = "LSPA"
        pageinfo = "TABELAS"
        doc = SimpleDocTemplate(self.dirARQ+"\\TAB11_UF_"+str(indice)+".pdf")
        Story = [Spacer(0,0.1*inch)]
        style = styles["Normal"]
        style.alignment =TA_CENTER
        style.fontSize=12
        xcomp=len(lista1)
        #print(xcomp)
        for kx in range(0,xcomp-1):
            t1=Table(lista1[kx],style=[
            ('FONTSIZE',(0,0),(-1,-1),8),
            ('ALIGN',(0,0),(-1,-1),'CENTER'),
            ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
            ('FONT',(0,0),(-1,-1),'Times-Roman'),
            ('FONTNAME',(0,0),(-1,1),'Times-Bold'),
            ('SPAN',(0,0),(-1,0)),
            ('SPAN',(0,1),(-2,1)),
            ('SPAN',(1,2),(2,2)),
            ('SPAN',(3,2),(4,2)),
            ('SPAN',(5,2),(6,2)),
            ('SPAN',(7,2),(8,2)),
            ('SPAN',(9,2),(10,2)),
            ('SPAN',(11,2),(12,2)),
            ('SPAN',(0,2),(0,3)),
#            ('SPAN',(0,-1),(-1,-1)),
            ('ALIGN',(0,4),(0,-1),'LEFT'),
            ('LINEBELOW',(0,0),(-1,3),1,colors.black),
#            ('LINEABOVE',(0,-1),(-1,-1),1,colors.black),
            ('GRID',(1,2),(-2,3),1,colors.black),
             ])
            km=0
            for lista in lista1[kx]:
                if km>3:
                    chave=lista[0].lstrip()
                    try:
                        if (LESP[chave])=="MUNIC":
                            t1._argH[km]=0.15*inch
                        if (LESP[chave])=="MICRO":
                            t1._argH[km]=0.25*inch
                        if (LESP[chave])=="MESO":
                            t1._argH[km]=0.31*inch
                    except:
                        pass
                km+=1
            Story.append(t1)
            Story.append(PageBreak())
        t1=Table(lista1[xcomp-1],style=[
        ('FONTSIZE',(0,0),(-1,-1),8),
        ('ALIGN',(0,0),(-1,-1),'CENTER'),
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        ('FONT',(0,0),(-1,-1),'Times-Roman'),
        ('FONTNAME',(0,0),(-1,1),'Times-Bold'),
        ('SPAN',(0,0),(-1,0)),
        ('SPAN',(0,1),(-2,1)),
        ('SPAN',(1,2),(2,2)),
        ('SPAN',(3,2),(4,2)),
        ('SPAN',(5,2),(6,2)),
        ('SPAN',(7,2),(8,2)),
        ('SPAN',(9,2),(10,2)),
        ('SPAN',(11,2),(12,2)),
        ('SPAN',(0,2),(0,3)),
        ('SPAN',(0,-1),(-1,-1)),
        ('ALIGN',(0,4),(0,-1),'LEFT'),
        ('LINEBELOW',(0,0),(-1,3),1,colors.black),
        ('LINEABOVE',(0,-1),(-1,-1),1,colors.black),
        ('GRID',(1,2),(-2,3),1,colors.black),
         ])
        km=0
        try:
            for lista in lista1[xcomp-1]:
                if km>3:
                    chave=lista[0].lstrip()
                    try:
                        if (LESP[chave])=="MUNIC":
                            t1._argH[km]=0.15*inch
                        if (LESP[chave])=="MICRO":
                            t1._argH[km]=0.25*inch
                        if (LESP[chave])=="MESO":
                            t1._argH[km]=0.31*inch
                    except:
                        pass
                km+=1
        except:
            for lista in lista1:
                if km>3:
                    chave=lista[0].lstrip()
                    try:
                        if (LESP[chave])=="MUNIC":
                            t1._argH[km]=0.15*inch
                        if (LESP[chave])=="MICRO":
                            t1._argH[km]=0.25*inch
                        if (LESP[chave])=="MESO":
                            t1._argH[km]=0.31*inch
                    except:
                        pass
                km+=1

        Story.append(t1)
        #doc.build(Story, onFirstPage=myPage)
        doc.build(Story)

    def TAB12B(self,lista1):
        styles = getSampleStyleSheet()
        Title = "LSPA"
        pageinfo = "TABELAS"
        doc = SimpleDocTemplate(self.dirARQ+"\\TAB12B_UF.pdf")
        Story = [Spacer(0,0.1*inch)]
        style = styles["Normal"]
        style.alignment =TA_CENTER
        style.fontSize=12
        t1=Table(lista1,style=[
        ('FONTSIZE',(0,0),(-1,-1),9),
        ('ALIGN',(0,0),(-1,-1),'CENTER'),
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        ('FONT',(0,0),(-1,-1),'Times-Roman'),
        ('FONTNAME',(0,0),(-1,1),'Times-Bold'),
        ('SPAN',(0,0),(-1,0)),
        ('SPAN',(0,1),(-1,1)),
        ('SPAN',(0,-1),(-1,-1)),
        ('ALIGN',(0,3),(0,-1),'LEFT'),
        ('ALIGN',(1,3),(1,5),'RIGHT'),
        ('ALIGN',(1,6),(1,8),'LEFT'),
        ('LINEBELOW',(0,0),(-1,2),1,colors.black),
        ('LINEBELOW',(0,5),(-1,5),1,colors.black),
        ('LINEABOVE',(0,-1),(-1,-1),1,colors.black),
        ('GRID',(1,2),(-2,2),1,colors.black),
         ])
        t1._argH[3]=0.45*inch
        t1._argH[6]=0.45*inch
        t1._argH[5]=0.45*inch
        t1._argH[8]=0.45*inch
        Story.append(t1)
        doc.build(Story)
