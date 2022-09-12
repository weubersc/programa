from PIL import Image, ImageFont, ImageDraw, ImageEnhance
import os
import string
from programa.modulos.cartograma.crop import recortar
from programa.modulos.cartograma.crop import recortar2
from programa.modulos.cartograma.MAXMIN import valm as maxmin

def APRESENTACAO(sem,ano,tipo,totbr,perbr,DF):

    dirpath=os.getcwd()
    dic,dic_m=maxmin(DF,tipo)
    """ Variaveis """
    ano_anterior=str(int(ano)-1)
    seml=sem.lower()

    if sem=="Primeiro":
        SSEM="1"

    if sem=="Segundo":
        SSEM="2"

    if seml=="primeiro":
        data_ref="30/06/"
    if seml=="segundo":
        data_ref="31/12/"

    """ fontes """
    font = ImageFont.truetype("arial", size=16)
    font2 = ImageFont.truetype("arial", size=30)
    font3 = ImageFont.truetype("arial", size=22)
    font4 = ImageFont.truetype("arial", size=24)
    font5=ImageFont.truetype("arial", size=20)

    """ Crop imagens """
    
    imagem=dirpath+"\\programa\\provisórios\\"+tipo+".png"
    recortar(imagem)
    imagem=dirpath+"\\programa\\provisórios\\"+tipo+"_mapa.png"
    recortar(imagem)

    """ Criar uma imagem """
    im = Image.new('RGBA', (1700,1050),(255,255,255))
    im.save(dirpath+"\\programa\\provisórios\\"+"fundo.png")
    im2 = Image.new('RGBA', (1700,1050),(255,255,255))
    im2.save(dirpath+"\\programa\\provisórios\\"+"fundo2.png")
    im3 = Image.new('RGBA', (1700,1050),(255,255,255))
    im3.save(dirpath+"\\programa\\provisórios\\"+"fundo3.png")
    
    """ Carregar imagens """
    im=Image.open(dirpath+"\\programa\\provisórios\\"+"fundo.png")
    perc=Image.open(dirpath+"\\programa\\provisórios\\"+tipo+"_r.png")
    leg=Image.open(dirpath+"\\programa\\provisórios\\"+"cor3.jpg")
    BAR=Image.open(dirpath+"\\programa\\provisórios\\"+tipo+"_bar.png")
    mun=Image.open(dirpath+"\\programa\\provisórios\\"+tipo+"_mapa_r.png")
    mun2=Image.open(dirpath+"\\programa\\provisórios\\"+tipo+"_mapa_r.png")
    lfig=Image.open(dirpath+"\\programa\\provisórios\\"+'legenda_fig_'+tipo+'.jpg')
    lfig_vertical=Image.open(dirpath+"\\programa\\provisórios\\"+'legenda_fig_'+tipo+'_vertical.jpg')
    "Desenhar em uma imagem"
    dr = ImageDraw.Draw(im)

    """ Redimensionar imagem """
    x,y=mun.size
    fator=0.6
    mun=mun.resize((int(x*fator),int(y*fator)))
    x,y=BAR.size
    fator=0.714
    BAR=BAR.resize((int(x*fator),int(y*fator)))

    """ Posicionar imagens na base (img) (y,x) """

    im.paste(perc,(20,170))
    im.paste(leg,(40,940))
    im.paste(BAR,(880,140))
    im.paste(mun,(920,450))
    im.paste(lfig,(990,894))
    im2.paste(mun2,(10,10))
    im2.paste(lfig_vertical,(674,502))
    """ Escrever os textos na imagem """

    pos=250
    TITULO="Quantidade de "+tipo+" estocada em "+data_ref+ano
    TITULO2="( "+sem+" semestre de "+ano+" )"
    dr.text((pos, 50), TITULO, fill='black',font=font2)
    dr.text((430,100),TITULO2,fill='black',font=font2)
    TITBAR="Percentual em relação à quantidade total (Brasil) em"
    TITBAR2="nível de UF"
    dr.text((946,110), TITBAR, fill='black',font=font)
    dr.text((1080,130),TITBAR2,fill='black',font=font)
    TITBR="Quantidade Total (BRASIL):"
    prod_tot="{:,}".format(totbr).replace(",", " ")
    dr.text((19,616), TITBR, fill='black',font=font3)
    dr.text((35,646), prod_tot+" (kg)", fill='blue',font=font4)
    TITBR2="Variação em comparação ao \n"+seml 
    TITBR2+=" semestre de "+ano_anterior+ " :"
    dr.text((19,696), TITBR2, fill='black',font=font3)
    dr.text((55,746), perbr, fill='blue',font=font4)
    TIT_LEG="Variação (%) da produçao relativa ao total (BR) comparada ao "+SSEM+"ºsem./"
    TIT_LEG+=ano_anterior
    dr.text((40,900), TIT_LEG, fill='black',font=font5)
    dic_linha={
     "24":[738,382],
     "25":[747,402],
     "26":[752,428],
     "27":[739,453],
     "28":[717,466],
     "32":[659,630],
     "33":[622,681],
     "42":[485,768]}
    for it,val in dic.items():
        posx=val[0]
        posy=val[1]
        cor=val[2]
        flag=False
        try:
            percentual=float(dic_m[it])
            flag=True
            print(percentual)
            if cor==0 and percentual<=0.0:
                corper="white"
            if cor==0 and percentual>0.0:
                corper="grey"
            if cor==1:
                corper="black"
            if percentual>0:
                percent="+"+str(percentual)
            else:
                percent=str(percentual)
            perc=percent.replace(".",",")
            print(perc,corper)
            dr.text((posx,posy),perc,fill=corper,font=font4)
        except:
            pass
        if cor==1 and flag==True:
            val2=dic_linha[it]
            posx2=val2[0]
            posy2=val2[1]
            dr.line((posx,posy,posx2,posy2),fill="black",width=2)
        
    
    """ Salvar a imagem """

    im.save(dirpath+"\\programa\\saida\\cartograma\\"+tipo+"_"+sem+"_"+ano+"_cartograma.png")
    im2.save(dirpath+"\\programa\\saida\\cartograma\\"+tipo+"_"+sem+"_"+ano+"_municipio.png")
    recortar2(dirpath+"\\programa\\saida\\cartograma\\"+tipo+"_"+sem+"_"+ano+"_municipio.png") 

