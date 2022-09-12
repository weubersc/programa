import json
import pandas as pd
from programa.modulos.cartograma.natural_breaks import getJenksBreaks as jenks
import os

def rotulo():
    dirpath=os.getcwd()
    DF_perc=pd.read_json(dirpath+"\\programa\\provisórios\\produto_UF.json")

    LISTA_PROD=['Algodão (em pluma)',
                     'Algodão (em caroço)',
                     'Caroço de Algodão',
                     'Arroz (em casca)',
                     'Arroz Beneficiado',
                     'Café Arábica (em grão)',
                     'Café Canephora (em grão)',
                     'Café (em grão)',
                     'Feijão Preto (em grão)',
                     'Feijão de Cor (em grão)',
                     'Feijão (em grão)',
                     'Milho (em grão)',
                     'Soja (em grão)',
                     'Trigo (em grão)',
                     ]

    lista_prod_uf=[]

    for lprod in LISTA_PROD:
        DF_UF=DF_perc[(DF_perc["prod"]==lprod)]
        soma_ant=DF_UF["quant_ant"].sum()
        for x,y in DF_UF.iterrows():
            if y["var"]=="-" and y["quant"]>0:
                perc=round((y["quant"]/soma_ant)*100,4)
                lista_prod_uf.append([lprod,y["uf"],perc])
                
            if y["var"]!="-":
                perc=round(float(y["var"])*float(y["per_ant"])/100,4)
                lista_prod_uf.append([lprod,y["uf"],perc])


    DF_prod_uf=pd.DataFrame(lista_prod_uf,columns=["produto","coduf","perc"])
    return(DF_prod_uf)
    
    
    
      
