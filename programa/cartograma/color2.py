from PIL import Image, ImageDraw,ImageFont
import math
import os 

class cores():

    def __init__(self):
        self.dic_rgb={}
        self.dirpath=os.getcwd()
        d_cores={"amarelo":[255,255,0],
                 "laranja":[255,165,0],
                 "vermelho":[255,0,0],
                 "verde":[0,255,0],
                 "azul":[0,0,255],
                 "roxo":[255,0,255],
                 "marron":[255,128,0],
                 "marron2":[153,102,51]}
        d_passo={"amarelo":[[0,0,-25.5],[-25.5,-25.5,0]],
                 "laranja":[[0,-9,-25.5],[-25.5,-16.5,0]],
                 "vermelho":[[0,-25.5,-25.5],[-25.5,0,0]],
                 "verde":[[-25.5,0,-25.5],[0,-25.5,0]],
                 "azul":[[-25.5,-25.5,0],[0,0,-25.5]],
                 "roxo":[[0,-25.5,0],[-25.5,0,-25.5]],
                 "marron":[[0,-12.8,-25.5],[-25.5,-12.8,0]],
                 "marron2":[[-10.2,-15.3,-20.4],[-15.3,-10.2,-5.1]]}
        

        im = Image.new('RGB', (600,600), (255,255,255))
        self.draw = ImageDraw.Draw(im)
        vb=10

        for it,valor in d_cores.items():
            l_temp=[]
            #print(it)
            #print(d_passo[it],valor,sep="--")
            l_temp=self.desenhar(d_passo[it],vb,it)
            self.dic_rgb[it]=l_temp
            vb+=40
        im.save(self.dirpath+'\\programa\provisórios\\cor.jpg', quality=95)

    def desenhar(self,l_passo,vbox,cor):
        lado=20
        lrgb=[255,255,255]
        #print(l_passo)
        l_rgb=[]
        for x in range(1,18):
            if x<11:
                lrgb[0]+=l_passo[0][0]
                lrgb[1]+=l_passo[0][1]
                lrgb[2]+=l_passo[0][2]
                tempcor=(math.ceil(lrgb[0]),
                        math.ceil(lrgb[1]),
                        math.ceil(lrgb[2]))
                #print(lrgb)
                lhex=self.rgb_hex(lrgb)
                l_rgb.append(lhex)
                #print(lhex)
                self.draw.rectangle((20+x*lado, vbox, 20+lado+x*lado,vbox+lado),
                           fill=tempcor,width=1,outline=(255,255,255))
##                lrgb=[255,ccor,ccor]
##                lista_red.append(rgb_hex(lrgb))
            else:
                lrgb[0]+=l_passo[1][0]
                lrgb[1]+=l_passo[1][1]
                lrgb[2]+=l_passo[1][2]
                tempcor=(math.ceil(lrgb[0]),
                        math.ceil(lrgb[1]),
                        math.ceil(lrgb[2]))
                #print(lrgb)
                lhex=self.rgb_hex(lrgb)
                l_rgb.append(lhex)
                #print(lhex)                
                self.draw.rectangle((20+x*lado, vbox, 20+lado+x*lado,vbox+lado),
                           fill=tempcor,width=1,outline=(255,255,255))
##                lrgb=[ccor,0,0]
##                lista_red.append(rgb_hex(lrgb))
        return(l_rgb)

    def rgb_hex(self,lista_rgb):
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


if __name__=="__main__":
    cores()


