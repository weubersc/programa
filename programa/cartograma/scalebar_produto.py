import matplotlib.pyplot as plt
import pandas as pd
import operator
from codigos import Codigos as COD
import os


class SCALE():

    def __init__(self,var):
        self.var=var
        print(self.var)
        CODIG=COD()
        self.dic_uf=CODIG.ufsigla
        self.dirpath=os.getcwd()
        data=pd.read_json(self.dirpath+"\\programa\\provisórios\\produto_UF.json")
        print(data.columns)
        DFP=data[(data["prod"]==var)]
        dic={}
        for x,y in DFP.iterrows():
            dic[y["uf"]]=float(y["per"])
        sorted_dic = dict( sorted(dic.items(),
                        key=operator.itemgetter(1),reverse=True))      
        self.dic=sorted_dic
        self.listy=[]
        self.listx=[]
        self.per()
        self.bar()

    def per(self):
        soma=0
        valor=95

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

        print(x_pos)

        plt.bar(x_pos, y, color='green')
##        plt.xlabel("Unidades da Federação",fontsize= 12)
##        plt.ylabel("Percentual da Capacidade %",fontsize= 12)
##        plt.title(self.titulo,fontsize= 20)

        plt.yticks(fontsize=14)
        plt.xticks(x_pos, x,fontsize=14)

        #plt.show()

        plt.savefig(self.dirpath+"\\programa\\provisórios\\"+self.var+"_bar.png")

