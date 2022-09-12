from programa.modulos.cartograma.natural_breaks import getJenksBreaks as jenks
import json
import pandas as pd
import os

def PROD_MUN_JENKS(prod):
        dirpath=os.getcwd()
        dic_cores={"Algodão (em pluma)":"laranja",
                   "Algodão (em caroço)":"roxo",
                   "Caroço de Algodão":"amarelo",
                   "Arroz (em casca)":"vermelho",
                   "Arroz Beneficiado":"azul",
                   "Café Arábica (em grão)":"verde",
                   "Café Canephora (em grão)":"laranja",
                   "Café (em grão)":"marron",
                   "Feijão Preto (em grão)":"roxo",
                   "Feijão de Cor (em grão)":"amarelo",
                   "Feijão (em grão)":"marron2",
                   "Milho (em grão)":"vermelho",
                   "Soja (em grão)":"azul",
                   "Trigo (em grão)":"verde"}
        data=pd.read_json(dirpath+"\\programa\\provisórios\\produto_mun.json")
        data=data.rename(columns={"CODMUN":"codig"})
        data["codig"]=data.codig.astype("object")
        data2=data[(data["produto"]==prod)]
        DZ=data2["produc"]
        z=DZ.values.tolist()
        faixa=jenks(z,6)
        return(data2,faixa,dic_cores[prod])

        
