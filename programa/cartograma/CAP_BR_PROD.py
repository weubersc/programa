import json
import pandas as pd
import os

def CAPBR(var):
    dirpath=os.getcwd()
    data1=pd.read_json(dirpath+"\\programa\\provisórios\\produto_BR.json")
    for x,y in data1.iterrows():
        CAP=float(y["per"])
        PER=str(round(CAP,1))
        if var==y["prod"]:
            PERC=PER.replace(".",",")+ " (%)"
            PRODBR=y["BRA"]
    return(PRODBR,PERC)
    

    

