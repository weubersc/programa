import json
import pandas as pd
import os

def CAPBR(var):
    dirpath=os.getcwd()
    data1=pd.read_json(dirpath+"\\programa\\provisórios\\MUNIC_CAPACIDADE.json")
    data2=pd.read_json(dirpath+"\\programa\\provisórios\\MUNIC_CAPACIDADE_ANT.json")

    CAP1=data1[var].sum()
    CAP2=data2[var].sum()
    PER=str(round((CAP1-CAP2)/CAP2*100,1))
    PERC=PER.replace(".",",")+ " (%)"
    return(CAP1,PERC)
    

    

