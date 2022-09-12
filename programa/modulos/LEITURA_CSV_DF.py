import pandas as pd
import chardet

def LERCSV(ARQ,SEP):
    with open(ARQ, 'rb') as rawdata:
        result = chardet.detect(rawdata.read(10000))
        encod=(result["encoding"])
        DB=pd.read_csv(ARQ,sep=SEP,encoding=encod,header=None)
        return(DB)
    
