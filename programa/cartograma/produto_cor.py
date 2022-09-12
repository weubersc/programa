import pandas as pd
import math

def DFCORES(df_produf,lmais,lmenos,fxmais,fxmenos):

    def rgb_hex(lista_rgb):
        LHEX=["0","1","2","3","4","5",
              "6","7","8","9","A","B",
              "C","D","E","F"]
        vhex="#"
        p1=lista_rgb[0]
        raz=p1/16
        f1=math.floor(raz)
        dif=raz-f1
        f2=dif*16
        #print(f1,f2)
        vhex+=LHEX[int(f1)]+LHEX[int(f2)]
        p2=lista_rgb[1]
        raz=p2/16
        f1=math.floor(raz)
        dif=raz-f1
        f2=dif*16
        #print(f1,f2)
        vhex+=LHEX[int(f1)]+LHEX[int(f2)]
        p3=lista_rgb[2]
        raz=p3/16
        f1=math.floor(raz)
        dif=raz-f1
        f2=dif*16
        #print(f1,f2)
        vhex+=LHEX[int(f1)]+LHEX[int(f2)]
        #print(vhex)
        return(vhex)            

    
    delta_mais=[]
    delta_menos=[]
    temp=0
    l_cor_Vermelho=[(255,255,255),(255,204,204),
          (255,153,153),(255,102,102),
          (255,51,51),(255,0,0)]
    l_cor_Verde=[(255,255,255),(204,255,204),
          (153,255,153),(102,255,102),
          (51,255,51),(0,255,0)]


    for y,fx in enumerate(fxmenos):
        if y>0:
            dif=(fx-temp)/51
            delta_menos.append([temp,fx,dif,l_cor_Vermelho[y-1]])
        temp=fx
    for y,fx in enumerate(fxmais):
        if y>0:
            dif=(fx-temp)/51
            delta_mais.append([temp,fx,dif,l_cor_Verde[y-1]])
        temp=fx  
    #print(delta_mais)
    #print(delta_menos)
    df_produf["cor"]=""
    for x,y in df_produf.iterrows():
        per=float(y["perc"])
        #print(per)
        if per<0:
            per=abs(per)
            for dmenos in delta_menos:
                delta=dmenos[2]
                inferior=dmenos[0]
                if per==0.0:
                   df_produf.at[x,"cor"]="#FFFFFF"
                if per>dmenos[0] and per<=dmenos[1]:
                    valor=int((per-inferior)/delta)
                    if dmenos[3]==(255,0,0):
                        lrgb=dmenos[3]
                        r=lrgb[0]
                        g=lrgb[1]
                        b=lrgb[2]
                        r+=-valor
                        lrgb_v=(r,g,b)
                        hexv=rgb_hex(lrgb_v)
                        df_produf.at[x,"cor"]=hexv
                    else:
                        lrgb=dmenos[3]
                        r=lrgb[0]
                        g=lrgb[1]
                        b=lrgb[2]
                        g+=-valor
                        b+=-valor
                        lrgb_v=(r,g,b)
                        hexv=rgb_hex(lrgb_v)
                        df_produf.at[x,"cor"]=hexv

        else:     
            for dmais in delta_mais:
                delta=dmais[2]
                inferior=dmais[0]
                if per==0.0:
                   df_produf.at[x,"cor"]="#FFFFFF"
                if per>dmais[0] and per<=dmais[1]:
                    valor=int((per-inferior)/delta)
                    if dmais[3]==(0,255,0):
                        lrgb=dmais[3]
                        r=lrgb[0]
                        g=lrgb[1]
                        b=lrgb[2]
                        g+=-valor
                        lrgb_v=(r,g,b)
                        hexv=rgb_hex(lrgb_v)
                        df_produf.at[x,"cor"]=hexv
                    else:
                        lrgb=dmais[3]
                        r=lrgb[0]
                        g=lrgb[1]
                        b=lrgb[2]
                        r+=-valor
                        b+=-valor
                        lrgb_v=(r,g,b)
                        hexv=rgb_hex(lrgb_v)
                        df_produf.at[x,"cor"]=hexv
    #print(df_produf.columns)
##    for x,y in df_produf.iterrows():
##        print(y["produto"],y["coduf"],y["perc"],y["cor"])
    return(df_produf)
    
 
