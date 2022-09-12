import pandas as pd
import os

def maxmin(VAR):
    dirpath=os.getcwd()
    dic={"11":[203,471,0],
         "12":[57,436,0],
         "13":[212,352,0],
         "14":[246,231,0],
         "15":[406,368,0],
         "16":[429,251,0],
         "17":[482,480,0],
         "21":[536,365,0],
         "22":[597,414,0],
         "23":[656,356,0],
         "24":[760,366,1],
         "25":[771,398,1],
         "26":[773,424,1],
         "27":[759,453,1],
         "28":[735,478,1],
         "29":[615,494,0],
         "31":[563,607,0],
         "32":[687,639,1],
         "33":[646,692,1],
         "35":[467,662,0],
         "41":[428,715,0],
         "42":[530,770,1],
         "43":[384,809,0],
         "50":[351,642,0],
         "51":[354,517,0],
         "52":[459,568,0],
         "53":[495,533,0]}


    data=pd.read_json(dirpath+"\\programa\\provisórios\\capacidade_uf.json")

    dic_m={}
    DF=data[["CD_GEOCUF",VAR]]
    for x,y in DF.iterrows():
         cod=str(int(y["CD_GEOCUF"]))
         dic_m[cod]=y[VAR]
    maxx=0.0
    minn=0.0
    ufmax=""
    ufmin=""
    dic_mm={}
    for it,val in dic_m.items():
        #print(it,val,sep="--")
        if float(val)>=maxx:
            ufmax=it
            maxx=round(float(val),1)
        if float(val)<minn:
            ufmin=it
            minn=round(float(val),1)
    dic_mm[ufmax]=maxx
    dic_mm[ufmin]=minn
    #print("Dicionário")
    for it,val in dic_mm.items():
        print(it,val)         


    return(dic,dic_mm)
    
