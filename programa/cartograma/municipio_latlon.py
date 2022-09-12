import json
import pandas as pd
import os

def munic_centroide():
    dirpath=os.getcwd()
    data_cent=pd.read_json(dirpath+"\\programa\\arquivos\\centroide.json")        
    data_CAP=pd.read_json(dirpath+"\\programa\\provisórios\\MUNIC_CAPACIDADE.json")

    data_cent=data_cent.rename(columns={0:"CODMUN",1:"LAT",2:"LON"})

    data_merge=pd.merge(data_CAP,data_cent,on="CODMUN",how="left")
    return(data_merge)


