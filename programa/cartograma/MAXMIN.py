import pandas as pd

def valm(DF,var):
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
         "33":[645,701,1],
         "35":[467,662,0],
         "41":[428,715,0],
         "42":[530,770,1],
         "43":[384,809,0],
         "50":[351,642,0],
         "51":[354,517,0],
         "52":[459,568,0],
         "53":[495,533,0]}

    dic_m={}
    DFM=DF[(DF["produto"]==var)]
    for x,y in DF.iterrows():
         if y["produto"]==var:  
            print(y["produto"],y["coduf"],y["perc"],y["cor"])
            if float(y["perc"])>0:
                perc="+"+str(round(float(y["perc"]),1))
            else:
                perc=str(round(float(y["perc"]),1))
            dic_m[str(y["coduf"])]=perc
    maxx=0.0
    minn=0.0
    ufmax=""
    ufmin=""
    dic_mm={}
    for it,val in dic_m.items():
        #print(it,val,sep="--")
        if float(val)>=maxx:
            ufmax=it
            maxx=float(val)
        if float(val)<minn:
            ufmin=it
            minn=float(val)
    dic_mm[ufmax]=maxx
    dic_mm[ufmin]=minn
    print("Dicionário")
    for it,val in dic_mm.items():
        print(it,val)         

    return(dic,dic_mm)
    
