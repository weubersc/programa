from PIL import Image, ImageDraw,ImageFont
import os

def legenda_per(lcores,ano_ant,sem):
    im = Image.new('RGB', (960,124), (255,255,255))
    draw = ImageDraw.Draw(im)
    l_cor=[]
    dirpath=os.getcwd()
    for x,y in lcores.items():
        l_cor.append(y)
    l_rot=[["-20","-10"],["-10","-5"],
           ["-5","0"],"sem inf.","sem var.",
           ["0","5"],["5","10"],["10","20"]]
    font = ImageFont.truetype("arial", size=18)
    font2 = ImageFont.truetype("arial", size=20)
    draw.text((200,10),"Percentual em relação ao "+sem+" semestre de "+ano_ant+ " em nível de UF",font=font2,fill="black")
    draw.text((60,100), "< -20",font=font, fill="black")
    draw.text((870,100), "> 20",font=font, fill="black")
    draw.polygon([(33,40), (2,65), (33,90)], fill = l_cor[0],outline=(250,250,250))
    for x in range(0,len(l_cor)):
        draw.rectangle((30+x*90, 40, 120+x*90, 90), fill=l_cor[x], outline=(250,250,250),width=3)

        if x <8 and x!=3 and x!=4:
            c1=(3-len(l_rot[x][0]))*4
            c2=(3-len(l_rot[x][1]))*4
            draw.text((125+90*x+c1, 100),l_rot[x][0],font=font, fill="black")
            draw.text((175+90*x+c2, 100),l_rot[x][1],font=font, fill="black")
            draw.line((160+90*x,110,170+90*x,110),fill="red",width=3)
            draw.line((160+90*x,105,160+90*x,115),fill="red",width=3)
        if x==3 or x==4:
            draw.text((135+90*x, 100),l_rot[x],font=font, fill="black")
    draw.polygon([(33,40), (2,65), (33,90)], fill = l_cor[0],outline=l_cor[0])                   
    draw.polygon([(927,40), (958,65), (927,90)], fill = l_cor[9],outline=l_cor[9]) 
    im.save(dirpath+'\\programa\provisórios\\legenda_percentual.jpg', quality=95)

def legenda_cap(lcores,faixa,rot,txt):
    lado=40
    im = Image.new('RGB', (300,120), (255,255,255))
    draw = ImageDraw.Draw(im)
    l_cor=[]
    dirpath=os.getcwd()
    for x,y in lcores.items():
        if  x<6:
            l_cor.append(y)
    #print(l_cor)
    maxi=max(faixa)
    l_raz=[]
    for ff in faixa:
        raz=round((ff/maxi),2)
        s_raz=(str(raz)).replace(".",",")
        l_raz.append(s_raz)
    font = ImageFont.truetype("arial", size=12)
    font2 = ImageFont.truetype("arial", size=14)
    for x in range(0,len(l_cor)):
        draw.rectangle((20+x*lado, 10, 20+lado+x*lado,10+lado), fill=l_cor[x], outline=(250,250,250),width=1)
        draw.line((22+x*lado,50,22+x*lado,60),fill="black",width=3)
        comp=len(l_raz[x])-3
        draw.text((15+x*lado-comp*3,60),l_raz[x],font=font, fill="black")
    comp=len(l_raz[len(l_raz)-1])-3
    if x>0:
        draw.text((15+(len(l_raz)-1)*lado-comp*3,60),l_raz[len(l_raz)-1],font=font, fill="black")
        draw.line((18+(len(l_raz)-1)*lado,50,18+(len(l_raz)-1)*lado,60),fill="black",width=3)
    rmax=int(round(maxi/1000,2))
    s_max="{:,}".format(rmax).replace(",", " ")
    if txt==1:
        texto="Capacidade relativa (1000m³) ao máximo \n"
        texto+="valor "+s_max +"  por município."
    if txt==2:
        texto="Capacidade relativa (1000t) ao máximo \n"
        texto+="valor "+s_max +"  por município."
    draw.text((30,75),texto,font=font2, fill="black")
    im.save(dirpath+'\\programa\provisórios\\legenda_fig_'+rot+'.jpg', quality=95)

def legenda_cap_vertical(lcores,faixa,rot,txt):
    lado=40
    im = Image.new('RGB', (450,300), (255,255,255))
    draw = ImageDraw.Draw(im)
    dirpath=os.getcwd()
    if rot=="SILO":
        rotulo="Silos \n"
    if rot=="GRAN":
        rotulo="Armazéns graneleiros e \n granelizados"
    if rot=="CONV":
        rotulo="Armazéns convencionais, \n estruturais e infláveis"
    l_cor=[]
    for x,y in lcores.items():
        if  x<6:
            l_cor.append(y)
    #print(l_cor)
    maxi=max(faixa)
    l_raz=[]
    lenmax=0
    for ff in faixa:
        if len(str(ff))>lenmax:
            lenmax=len(str(ff))
        raz=int(round(float(ff),2))
        s_raz="{:,}".format(raz).replace(",", " ")
        l_raz.append(s_raz)
    font = ImageFont.truetype("arial", size=16)
    font2 = ImageFont.truetype("arial", size=18)
    for y in range(0,len(l_cor)):
        draw.rectangle((20, 50+y*lado, 20+lado,50+lado+y*lado), fill=l_cor[y], outline=(250,250,250),width=1)
        comp=len(l_raz[y])
        draw.text((63,60+y*lado),l_raz[y],font=font, fill="black")
        draw.text((63+9*comp+40,60+y*lado),l_raz[y+1],font=font, fill="black")
        draw.line((63+9*comp+10,70+y*lado,63+9*comp+30,70+y*lado),fill="black",width=3)
        if y>0:
            draw.line((63+9*comp+8,70+y*lado-5,63+9*comp+8,70+y*lado+5),fill="black",width=3)
        if y==(len(l_cor)-1):
            draw.line((63+9*comp+32,70+y*lado-5,63+9*comp+32,70+y*lado+5),fill="black",width=3)
    texto="Volume (t) de "+rot +"\n"
    texto+=" em nível de município."
    if txt==1:
        texto="Capacidade (m³) de "+rotulo 
        texto+=" em nível de município."
    if txt==2:
        texto="Capacidade  (t) de "+rotulo 
        texto+=" em nível de município."
    draw.text((30,5),texto,font=font2, fill="black")
    im.save(dirpath+'\\programa\provisórios\\legenda_fig_'+rot+'_vertical.jpg', quality=95)  
    
def legenda_prod(lcores,faixa,rot):
    lado=40
##    print("----------------")
##    print("retirar as cores")
##    print(lcores)
##    print("retirar as faixas")
##    print(faixa)
##    print("----------------")
    dirpath=os.getcwd()
    im = Image.new('RGB', (290,120), (255,255,255))
    draw = ImageDraw.Draw(im)
    l_cor=lcores
    maxi=max(faixa)
    l_raz=[]
    for ff in faixa:
        raz=round((ff/maxi),2)
        s_raz=(str(raz)).replace(".",",")
        l_raz.append(s_raz)
    font = ImageFont.truetype("arial", size=12)
    font2 = ImageFont.truetype("arial", size=14)
    for x in range(0,len(l_cor)):
        draw.rectangle((20+x*lado, 10, 20+lado+x*lado,10+lado), fill=l_cor[x], outline=(250,250,250),width=1)
        if x>0:
            draw.line((22+x*lado,50,22+x*lado,60),fill="black",width=3)
            comp=len(l_raz[x])-3
            draw.text((15+x*lado-comp*3,60),l_raz[x],font=font, fill="black")
    comp=len(l_raz[len(l_raz)-1])-3
    draw.text((15+(len(l_raz)-1)*lado-comp*3,60),l_raz[len(l_raz)-1],font=font, fill="black")
    draw.line((18+(len(l_raz)-1)*lado,50,18+(len(l_raz)-1)*lado,60),fill="black",width=3)
    rmax=int(round(maxi/1000,2))
    s_max="{:,}".format(rmax).replace(",", " ")

    texto="Volume relativo (t) ao máximo \n"
    texto+="valor "+s_max +"  por município."

    draw.text((30,75),texto,font=font2, fill="black")
    im.save(dirpath+'\\programa\provisórios\\legenda_fig_'+rot+'.jpg', quality=95)    

def legenda_prod_vertical(lcores,faixa,rot):
    lado=40
    im = Image.new('RGB', (400,300), (255,255,255))
    draw = ImageDraw.Draw(im)
    l_cor=lcores
    maxi=max(faixa)
    l_raz=[]
    lenmax=0
    dirpath=os.getcwd()
    for ff in faixa:
        if len(str(ff))>lenmax:
            lenmax=len(str(ff))
        raz=int(round((float(ff)/1000),2))
        s_raz="{:,}".format(raz).replace(",", " ")
        l_raz.append(s_raz)
    font = ImageFont.truetype("arial", size=16)
    font2 = ImageFont.truetype("arial", size=18)
    for y in range(0,len(l_cor)):
        draw.rectangle((20, 50+y*lado, 20+lado,50+lado+y*lado), fill=l_cor[y], outline=(250,250,250),width=1)
        comp=len(l_raz[y])
        draw.text((63,60+y*lado),l_raz[y],font=font, fill="black")
        draw.text((63+9*comp+40,60+y*lado),l_raz[y+1],font=font, fill="black")
        draw.line((63+9*comp+10,70+y*lado,63+9*comp+30,70+y*lado),fill="black",width=3)
        if y>0:
            draw.line((63+9*comp+8,70+y*lado-5,63+9*comp+8,70+y*lado+5),fill="black",width=3)
        if y==(len(l_cor)-1):
            draw.line((63+9*comp+32,70+y*lado-5,63+9*comp+32,70+y*lado+5),fill="black",width=3)
    texto="Volume (t) de "+rot+"\n"
    texto+=" em nível de município."

    draw.text((30,5),texto,font=font2, fill="black")
    im.save(dirpath+'\\programa\provisórios\\legenda_fig_'+rot+'_vertical.jpg', quality=95)   
