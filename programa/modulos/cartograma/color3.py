from PIL import Image, ImageDraw,ImageFont
import math
import os

class cores():

    def __init__(self,fxmais,fxmenos):
        font = ImageFont.truetype("arial", size=16)
        self.lista_rgb=[]
        self.fxmais2=[]
        self.fxmenos2=[]
        self.dirpath=os.getcwd()
        for fx in fxmenos:
            self.fxmenos2.append(-1.*float(fx))
        self.fxmenos2.sort()
        for fx in fxmais:
            self.fxmais2.append(float(fx))
        self.fxmais2.sort()
        im = Image.new('RGB', (650,120), (255,255,255))
        self.draw = ImageDraw.Draw(im)
        self.lista_rgb.append(self.desenhar())
        self.lista_rgb.append(self.desenhar2())
        self.draw.rectangle((300,70,370,100),fill="#ebebe0")
        self.draw.text((305,75),"sem. inf.",font=font, fill="black")
        im.save(self.dirpath+'\\programa\\provisórios\\cor3.jpg', quality=95)

    def desenhar(self):
        r=204
        g=0
        b=0
        index=0
        desl=15
        font = ImageFont.truetype("arial", size=16)
        for x in range(1,308):
            temp=[]
            if r<255:
                temp=(r,g,b)
                if r==204:
                   self.draw.line((x+desl,21,x+desl,30),fill=(0,0,0),width=3)
                   self.draw.text((x,35),str(round(self.fxmenos2[index],1)),font=font, fill="black")
                   index+=1
                r+=1
                if r==255:
                   self.draw.line((x+desl,21,x+desl,30),fill=(0,0,0),width=3)
                   self.draw.text((x,35),str(round(self.fxmenos2[index],1)),font=font, fill="black")
                   index+=1
            else:
                temp=(r,g,b)
                if g==204 or g==153 or g==102 or g==51:
                    self.draw.text((x,35),str(round(self.fxmenos2[index],1)),font=font, fill="black")
                    self.draw.line((x+desl,21,x+desl,30),fill=(0,0,0),width=3)
                    index+=1
                g+=1
                b+=1
 
            #print(temp)
            self.draw.rectangle((x+desl,0,x+desl,20),fill=temp)

    def desenhar2(self):
        r=255
        g=255
        b=255
        index=0
        desl=13
        font = ImageFont.truetype("arial", size=16)
        for x in range(308,615):
            temp=[]
            if r!=0:
                temp=(r,g,b)
                if r==255 or r==204 or r==153 or r==102 or r==51:
                    self.draw.line((x+desl,21,x+desl,30),fill=(0,0,0),width=3)
                    self.draw.text((x,35),str(round(self.fxmais2[index],1)),font=font, fill="black")
                    index+=1
                r+=-1
                b+=-1
                if r==0:
                   self.draw.line((x+desl,21,x+desl,30),fill=(0,0,0),width=3)
                   self.draw.text((x,35),str(round(self.fxmais2[index],1)),font=font, fill="black")
                   index+=1
            else:
                temp=(r,g,b)
                g+=-1
                if g==204:
                    self.draw.line((x+desl,21,x+desl,30),fill=(0,0,0),width=3)
                    self.draw.text((x,35),str(round(self.fxmais2[index],1)),font=font, fill="black")
                    index+=1
 
            #print(temp)
            self.draw.rectangle((x+desl,0,x+desl,20),fill=temp)

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
    fx1=["0","1","2","3","4","5","6"]
    cores(fx1,fx1)


