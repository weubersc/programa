import pandas as pd
from programa.modulos.cartograma.natural_breaks import getJenksBreaks as jenks

def valores(df_produf):
    l_mais=[]
    l_menos=[]
    cmais=0
    cmenos=0
    for x,y in df_produf.iterrows():
        #print(y["produto"],y["coduf"],y["perc"])
        if float(y["perc"])>=0:
            l_mais.append(float(y["perc"]))
            cmais+=1
        if float(y["perc"])<0:
            l_menos.append(-1*float(y["perc"]))
            cmenos+=1
##    for l1 in l_mais:
##        print(l1)
    #print("total de positivos :{1} ",cmais)
##    for l2 in l_menos:
##        print(l2)
    #print("total de negativos :{1} ",cmenos)
    faixa_mais=jenks(l_mais,6)
    faixa_menos=jenks(l_menos,6)
    #print(faixa_mais)
    #print(faixa_menos)
    temp1=[]
    temp2=[]
    temp3=[]
    temp4=[]
    temp5=[]
    temp6=[]
    for ll in l_mais:
        if ll<=faixa_mais[1]:
            temp1.append(ll)
        if ll>faixa_mais[1] and ll<=faixa_mais[2] :
            temp2.append(ll)
        if ll>faixa_mais[2] and  ll<=faixa_mais[3] :
            temp3.append(ll)
        if ll>faixa_mais[3] and ll<=faixa_mais[4] :
            temp4.append(ll)
        if ll>faixa_mais[4] and  ll<=faixa_mais[5] :
            temp5.append(ll)
        if ll>faixa_mais[5] and  ll<=faixa_mais[6] :
            temp6.append(ll)
    l_mais.append(temp1)
    l_mais.append(temp2)
    l_mais.append(temp3)
    l_mais.append(temp4)
    l_mais.append(temp5)
    l_mais.append(temp6)
    temp1=[]
    temp2=[]
    temp3=[]
    temp4=[]
    temp5=[]
    temp6=[]    
    for ll in l_menos:
        if ll<=faixa_menos[1]:
            temp1.append(ll)
        if ll>faixa_menos[1] and ll<=faixa_menos[2] :
            temp2.append(ll)
        if ll>faixa_menos[2] and  ll<=faixa_menos[3] :
            temp3.append(ll)
        if ll>faixa_menos[3] and ll<=faixa_menos[4] :
            temp4.append(ll)
        if ll>faixa_menos[4] and  ll<=faixa_menos[5] :
            temp5.append(ll)
        if ll>faixa_menos[5] and  ll<=faixa_menos[6] :
            temp6.append(ll)
    l_menos.append(temp1)
    l_menos.append(temp2)
    l_menos.append(temp3)
    l_menos.append(temp4)
    l_menos.append(temp5)
    l_menos.append(temp6)
    return(faixa_mais,l_mais,faixa_menos,l_menos)
