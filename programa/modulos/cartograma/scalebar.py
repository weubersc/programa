import matplotlib.pyplot as plt
import pandas as pd
import operator
from codigos import Codigos as COD
import os


class SCALE():

    def __init__(self,var,titulo):
        self.titulo=titulo
        self.var=var
        self.dirpath=os.getcwd()
        #print(self.var)
        CODIG=COD()
        self.dic_uf=CODIG.ufsigla
        data=pd.read_json(self.dirpath+"\\programa\\provisórios\\percentual_uf.json")
        dic={}
        for x,y in data.iterrows():
            dic[y["CD_GEOCUF"]]=y[self.var]
        sorted_dic = dict( sorted(dic.items(),
                        key=operator.itemgetter(1),reverse=True))      
        self.dic=sorted_dic
        self.listy=[]
        self.listx=[]
        self.per()
        self.bar()

    def per(self):
        soma=0
        valor=90

        for it,val in self.dic.items():
            soma+=val
            if soma<valor:
                uf=self.dic_uf[str(int(it))]
                self.listx.append(uf)
                self.listy.append(int(round(val,0)))
 

    def bar(self):
  
        plt.figure(figsize = (7,4))
        x=self.listx
        y=self.listy

        x_pos = []
        for i,j in enumerate(self.listx):
            x_pos.append(i)

        #print(x_pos)

        plt.bar(x_pos, y, color='blue')
##        plt.xlabel("Unidades da Federação",fontsize= 12)
##        plt.ylabel("Percentual da Capacidade %",fontsize= 12)
##        plt.title(self.titulo,fontsize= 20)

        plt.yticks(fontsize=14)
        plt.xticks(x_pos, x,fontsize=14)

        #plt.show()

        plt.savefig(self.dirpath+"\\programa\\provisórios\\"+self.var+"_bar.png")

