import os
import pandas as pd
import numpy as np
import string

class MICROMUN():

    def __init__(self,sem,ano,uf):
        self.dirpath=os.getcwd()
        self.ano=ano
        self.sem=sem
        self.cuf=uf
        self.dic_mun={}
        self.lista_micro=[]
        self.arq=(self.dirpath+"\\programa\\arquivos\\ESTAB.csv")
        self.DICMUN()

    def DICMUN(self):
        DB=pd.read_csv(self.arq,sep=";",
                                 encoding = "ISO-8859-1",header=None) 
        tam=(DB.shape)
        temp=[]
        for i in range(1,tam[1]+1):
            temp.append("V"+str(i))
        DB.columns = temp
        tt=DB["V6"]
        PROV=DB[((DB['V1']==int(self.ano)) &
                         (DB['V2']==int(self.sem)) & 
                         (DB['V6']==int(self.cuf)) &
                         (DB['V23']=='Ativo'))]
        DBM=PROV[["V10","V14"]]
        MUN=DBM["V10"].unique()
        MIC=DBM["V14"].unique()
        gg=DBM.values.tolist()
        for MM in MIC:
            self.lista_micro.append(MM)
        for g in gg:
            self.dic_mun[g[0]]=g[1]
 

       
        
        
        
        
 


if __name__=="__main__":
    MICROMUN("2","2018","41")
