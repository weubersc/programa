import os
import pandas as pd
import numpy as np
import string
from códigos import Codigos as COD

class FORMATAR_LISTA:

    def __init__(self,listax):
        self.lista=listax
        self.ltraco=[]
        self.Xlista=[]
        self.diff1=[]
    def TRACO(self):
        for ll in self.lista:
            temp=[]
            for lx in ll:
                var=lx
                if var=="0":
                    var=lx.replace('0', '-')
                temp.append(var)
            self.ltraco.append(temp)
        for ll in self.ltraco:
            print(ll)
        return(self.ltraco)
 
    def TRACO67(self):
        for ll in self.lista:
            temp=[]
            temp.append(ll[0])
            for ik in range(1,len(ll),2):
                print("--IK--")
                print(ik)
                if ll[ik]=="0":
                   temp.append("-")
                   temp.append("-")
                if ll[ik]!="0" and ll[ik+1]=="0":
                   temp.append(ll[ik])
                   temp.append("0")
                if ll[ik]!="0" and ll[ik+1]!="0":
                   temp.append(ll[ik])
                   temp.append(ll[ik+1])
            self.ltraco.append(temp)
        for ll in self.ltraco:
            print(ll)
        return(self.ltraco)
    
    def DESINT5(self):
        for ss in self.ltraco:
            temp=[]
            temp.append(ss[0])
            temp.append(ss[1])
            try:
                ninf=int(ss[2])
                if ninf<=2:
                    temp.append("x")
                    temp.append("x")
                else:
                    temp.append(ss[2])
                    temp.append(ss[3])
            except:
                temp.append(ss[2])
                temp.append(ss[3])
            self.Xlista.append(temp)
        return(self.Xlista)

    def DESINT11(self):
        for ss in self.ltraco:
            temp=[]
            print(ss)
            temp.append(ss[0])
            bolreg=False
            reg=["Norte","Nordeste","Centro-Oeste","Sul","Sudeste"]
            treg=ss[0].strip()
            for rr in reg:
                if treg==rr:
                    print("---reg--")
                    print(rr,treg)
                    bolreg=True
            for idx in range(1,len(ss),2):
                try:
                    ninf=int(ss[idx])
                    if ninf<=2 and bolreg==False:
                        temp.append("x")
                        temp.append("x")
                    else:
                        temp.append(ss[idx])
                        temp.append(ss[idx+1])
                except:
                    temp.append(ss[idx])
                    temp.append(ss[idx+1])
            self.Xlista.append(temp)
        L_X=self.DIFER()
        LISTA_MENOR=[]
        print("AS LONG AS")
        print(L_X)
        for ss in self.Xlista:
            zz=ss[:]
            valor=(ss[0]).lstrip()
            flag=False
            for lx in L_X:
                if valor==lx[0]:
                   zz[lx[1]]="x"
                   zz[lx[1]+1]="x"
            LISTA_MENOR.append(zz)
        return(LISTA_MENOR)

    def DIFER(self,):
        CC=COD()
        codig=CC.codigo
        codig_inv={}
        for key, value in codig.items():
            codig_inv[value]=key
##        for chave,valor in codig_inv.items():
##            print(chave)
        prov=[]
        for pp in self.Xlista:
            temp=[]
            temp.append(codig_inv[pp[0].lstrip()])
            for ix in range(1,len(pp)):
                temp.append(pp[ix])
            prov.append(temp)
            lista_x_menos1=[]
        for reg in range(1,6):
            lista_reg=[]
            lista_uf=[]
            for ss in prov:
                tempreg=[]
                tempuf=[]
                var0=ss[0]
                reguf=var0[0]
                if var0==str(reg):
                    tempreg.append(ss[0])
                    for ik in range(1,len(ss),2):
                        tempreg.append(ss[ik])
                    lista_reg.append(tempreg)
                if reguf==str(reg):
                    tempuf.append(ss[0])
                    for ik in range(1,len(ss),2):
                        tempuf.append(ss[ik])
                    lista_uf.append(tempuf)
            for mm in range(1,len(lista_uf[0])):
                tot=self.sumColumn(lista_uf[1:],mm)
                try:
                    dif=int(lista_reg[0][mm])-int(tot)
                    if dif==1 and int(lista_reg[0][mm])!=1:
                        mr=2*(mm-1)+1
                        lista_x_menos1.append([reg,mr])
                except:
                    pass
        #print(lista_x_menos1)
        lista_X2=[]
        for lemos in lista_x_menos1:
            temp=[]
            tempuf=[]
            for pp in prov:
                ruf=pp[0]
                #print(ruf,lemos[0],ruf[0])
                if lemos[0]==int(ruf[0]) and len(str(ruf))==2:
##                    print("-----")
##                    print(lemos[1],pp[lemos[1]])
                    tempuf.append(pp[0])
                    temp.append(pp[lemos[1]+1])
##            print(tempuf)
##            print(temp)
            VX,INDX=self.menorx(temp)
##            print(VX,INDX)
            lista_X2.append([codig[str(tempuf[INDX])],lemos[1]])
##        for vv in lista_X2:
##            print(vv)
        return(lista_X2)
            
        
            
        


       
##            dBTAB1 = pd.DataFrame(lista_reg)
##            tam=(dBTAB1.shape)
##            temp=[]
##            for i in range(1,tam[1]+1):
##                temp.append("V"+str(i))
##            dBTAB1.columns = temp
##            print(dBTAB1.describe())
##            print(dBTAB1.sum(axis = 0, skipna = True))
             

    def sumColumn(self,mlista, column):
        total = 0
        for row in range(len(mlista)):
            try:
                total += int(mlista[row][column])
            except:
                pass
        return(total)
            


    
    def menorx(self,lista):
        menor=0
        pos=0
        flag=False
        for ix in range(0,len(lista)):
            try:
                tt=(lista[ix]).replace(' ','')
##                print(tt)
                valor=int(tt)
                if flag==False:
                    menor=valor
                    pos=ix
                    flag=True
                if flag==True and valor<menor:
                    menor=valor
                    pos=ix
            except:
                pass
        return(menor,pos)
            
       
        

        
if __name__=="__main__":
     lista=[["0","12"],["13","12"],["11","0"]]
     FORMATAR_LISTA(lista)          
        
