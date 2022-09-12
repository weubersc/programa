import os
import pandas as pd
import numpy as np
import string
from códigos import Codigos as COD
from programa.modulos.apuracao.MICRO_MUN import MICROMUN
import re

class FORMATAR_LISTA:

    def __init__(self,listax):
        self.lista=listax
        self.ltraco=[]
        self.Xlista=[]
        self.diff1=[]
    def TRACO(self):
        for ll in self.lista:
            temp=[]
            for idx in range(0,len(ll)):
               if idx==0:
                  temp.append(ll[idx])
               if idx>0:
                    var=str(ll[idx])
                    if var=="0":
                        temp.append("-")
                    else:
                        temp.append(var)
            self.ltraco.append(temp)
        return(self.ltraco)
 
    def TRACO67(self):
        for ll in self.lista:
            temp=[]
            temp.append(ll[0])
            for ik in range(1,len(ll),2):
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

    def DESINT11(self,sem,ano,uf):
        for ss in self.ltraco:
            temp=[]
            temp.append(ss[0])
            tokens = re.findall('\s+',ss[0])
            try:
                #print(ss[0],len(tokens[0]))
                esp=len(tokens[0])
            except:
                esp=0
            for idx in range(1,len(ss),2):
                try:
                    ninf=int(ss[idx])
                    if ninf<=2 and esp==6:
                        temp.append("x")
                        temp.append("x")
                    else:
                        temp.append(ss[idx])
                        temp.append(ss[idx+1])
                except:
                    temp.append(ss[idx])
                    temp.append(ss[idx+1])
            self.Xlista.append(temp)
        L_X=self.DIFER(sem,ano,uf)
        print(L_X)
        LISTA_MENOR=[]
        print("AS LONG AS")
        for ss in self.Xlista:
            zz=ss[:]
            valor=(ss[0])
            for lx in L_X:
                if valor==lx[0]:
                   zz[lx[1]]="x"
                   zz[lx[1]+1]="x"
            LISTA_MENOR.append(zz)
        return(LISTA_MENOR)

    def DIFER(self,sem,ano,cuf):
        print("DIFER")
        MICMUN=MICROMUN(sem,ano,cuf)
        MICMUN.DICMUN()
        DIC_MUN=MICMUN.dic_mun
        LIST_MIC=MICMUN.lista_micro
        tempmic=[]
        for mic in LIST_MIC:
            ntemp=mic.lstrip()
            tempmic.append(ntemp)
        listmic=set(tempmic)
        LISTA_MENOS=[]
        for MM in listmic:
            #print(MM)
            temp1=[]
            tempM=[]
            teste=False
            for ss in self.Xlista:
                prov=ss[:]  
                try:
                    nome_mun=ss[0].lstrip()
                    mnome=DIC_MUN[nome_mun]
                    if MM==mnome and teste==True:
                       tempM.append(prov)
                       #print(MM,nome_mun,"MUN")
                    if MM==mnome and teste==False:
                       teste=True
                       temp1=prov[:]
                       #print(MM,nome_mun)
                except:
                    pass
            temp=[]
            for ids in range(1,12,2):
                valor=self.sumColumn(tempM,ids)
                try:
                    if int(temp1[ids])!=1:
                        temp.append(int(temp1[ids])-valor)
                    else:
                        temp.append(0)
                except:
                    temp.append(0)
            m=0
            for tt in temp:
                if tt==1:
                   indx=(m)*2+2
                   tempw=[]
                   tnome=[]
                   for mun in tempM:
                       tempw.append(mun[indx])
                       tnome.append(mun[0])
                   menor,pos=self.menorx(tempw)
                   LISTA_MENOS.append([tnome[pos],(m)*2+1])
                m+=1
        return(LISTA_MENOS)

             

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
        
