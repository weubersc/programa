#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd
from programa.modulos.apuracao.PDCSVUF import ARQCSVUF as ARQCSV
from programa.modulos.apuracao.eliminar_acentos import Eliminar_Acentos as ORDALF
from listtocsv import listacsv as LCSV



class TABELASUF():

    def __init__(self):
        print("---OK---")
        self.dic_emp_mun={}

    def capacidade(self,LISTA):
        temp=[]
        for LL in LISTA:
            ind19=0
            ind20=0
            ind21=0
            if LL[2]>0:
                ind19=1
            if LL[3]>0:
                ind20=1
            if LL[4]>0:
                ind21=1
            temp.append([LL[0],LL[1],ind19,LL[2],ind20,LL[3],ind21,LL[4]])
        return(temp)
    def TAB12(self,LISTA,LISTA_TIP):
        dBTAB1 = pd.DataFrame(LISTA, columns = ['ID' , 'EMP', 'I_CONV','V_CONV', 'I_GRAN','V_GRAN', 'I_SILO','V_SILO'])    
        v1=dBTAB1['ID'].count()
        v2=dBTAB1[dBTAB1['I_CONV']==1]
        v3=dBTAB1['V_CONV'].sum()
        v4=dBTAB1[dBTAB1['I_GRAN']==1]
        v5=dBTAB1['V_GRAN'].sum()
        v6=dBTAB1[dBTAB1['I_SILO']==1]
        v7=dBTAB1['V_SILO'].sum()
        lista_saida=[]
        print(0,v1,v2['I_CONV'].count(),v3,v4['I_GRAN'].count(),v5,v6['I_GRAN'].count(),v7)
        lista_saida.append([0,v1,v2['I_CONV'].count(),v3,v4['I_GRAN'].count(),
                            v5,v6['I_GRAN'].count(),v7])
        for EMP in LISTA_TIP:
            DBEMP=dBTAB1[dBTAB1['ID']==EMP]
            v1=DBEMP['ID'].count()
            v2=DBEMP[DBEMP['I_CONV']==1]
            v3=DBEMP['V_CONV'].sum()
            v4=DBEMP[DBEMP['I_GRAN']==1]
            v5=DBEMP['V_GRAN'].sum()
            v6=DBEMP[DBEMP['I_SILO']==1]
            v7=DBEMP['V_SILO'].sum()
            print(EMP,v1,v2['I_CONV'].count(),v3,v4['I_GRAN'].count(),v5,v6['I_GRAN'].count(),v7)
            lista_saida.append([EMP,v1,v2['I_CONV'].count(),v3,v4['I_GRAN'].count(),
                                v5,v6['I_GRAN'].count(),v7])
        return(lista_saida)
    def TAB3(self,LISTA,LISTFX):
        dBTAB1 = pd.DataFrame(LISTA, columns = ['ID' , 'EMP', 'I_CONV','V_CONV', 'I_GRAN','V_GRAN', 'I_SILO','V_SILO'])
        lista_saida=[]
        v2=dBTAB1[dBTAB1['I_CONV']==1]
        v3=dBTAB1['V_CONV'].sum()
        print(v2['I_CONV'].count(),v3)
        lista_saida.append([0,v2['I_CONV'].count(),v3])
        il=1
        for fx in range(0,len(LISTFX)):
            if fx==0:
                valor=LISTFX[fx][0]
                DBEMP=dBTAB1[dBTAB1['V_CONV']<valor]
                v2=DBEMP[DBEMP['I_CONV']==1]
                v3=DBEMP['V_CONV'].sum()
                print(v2['I_CONV'].count(),v3)
                lista_saida.append([il,v2['I_CONV'].count(),v3])
                il+=1
            valor1=LISTFX[fx][0]
            valor2=LISTFX[fx][1]
            DPA=dBTAB1[dBTAB1['V_CONV']>=valor1]
            DBEMP=DPA[DPA['V_CONV']<valor2]               
            v2=DBEMP[DBEMP['I_CONV']==1]
            v3=DBEMP['V_CONV'].sum()
            print(v2['I_CONV'].count(),v3)
            lista_saida.append([il,v2['I_CONV'].count(),v3])
            il+=1
            if fx==4:
                valor=LISTFX[fx][1]
                DBEMP=dBTAB1[dBTAB1['V_CONV']>=valor]
                v2=DBEMP[DBEMP['I_CONV']==1]
                v3=DBEMP['V_CONV'].sum()
                print(v2['I_CONV'].count(),v3)
                lista_saida.append([il,v2['I_CONV'].count(),v3])
                il+=1
        return(lista_saida)
    def TAB4(self,LISTA,LISTFX):
        dBTAB1 = pd.DataFrame(LISTA, columns = ['ID' , 'EMP', 'I_CONV','V_CONV', 'I_GRAN','V_GRAN', 'I_SILO','V_SILO'])
        GRANSILO=dBTAB1[(dBTAB1['I_GRAN']==1)|(dBTAB1['I_SILO']==1)]
        v2=dBTAB1[dBTAB1['I_GRAN']==1]
        v3=dBTAB1['V_GRAN'].sum()
        v4=dBTAB1[dBTAB1['I_SILO']==1]
        v5=dBTAB1['V_SILO'].sum()
        lista_saida=[]
        print(GRANSILO['ID'].count(),v3+v5,v2['I_GRAN'].count(),v3,v4['I_SILO'].count(),v5)
        lista_saida.append([0,GRANSILO['ID'].count(),v3+v5,v2['I_GRAN'].count(),v3,v4['I_SILO'].count(),v5])
        il=1
        for fx in range(0,len(LISTFX)):
            if fx==0:
                valor=LISTFX[fx][0]
                GRANSILO=dBTAB1[((dBTAB1['I_GRAN']==1) & (dBTAB1['V_GRAN']<valor))|
                                ((dBTAB1['I_SILO']==1) & (dBTAB1['V_SILO']<valor))]
                GRANSILO1=dBTAB1[(dBTAB1['I_GRAN']==1) & (dBTAB1['V_GRAN']<valor)]
                GRANSILO2=dBTAB1[(dBTAB1['I_SILO']==1) & (dBTAB1['V_SILO']<valor)]
                v2=GRANSILO1[GRANSILO1['I_GRAN']==1]
                v3=GRANSILO1['V_GRAN'].sum()
                v4=GRANSILO2[GRANSILO2['I_SILO']==1]
                v5=GRANSILO2['V_SILO'].sum()
                print(GRANSILO['ID'].count(),v3+v5,v2['I_GRAN'].count(),v3,v4['I_SILO'].count(),v5)
                lista_saida.append([il,GRANSILO['ID'].count(),v3+v5,v2['I_GRAN'].count(),v3,v4['I_SILO'].count(),v5])
                il+=1
            valor1=LISTFX[fx][0]
            valor2=LISTFX[fx][1]
            GRANSILO=dBTAB1[((dBTAB1['I_GRAN']==1) & (dBTAB1['V_GRAN']>=valor1) & (dBTAB1['V_GRAN']<valor2))|
                            ((dBTAB1['I_SILO']==1) & (dBTAB1['V_SILO']>=valor1) & (dBTAB1['V_SILO']<valor2))]
            GRANSILO1=dBTAB1[(dBTAB1['I_GRAN']==1) & (dBTAB1['V_GRAN']>=valor1) & (dBTAB1['V_GRAN']<valor2)]
            GRANSILO2=dBTAB1[(dBTAB1['I_SILO']==1) & (dBTAB1['V_SILO']>=valor1) & (dBTAB1['V_SILO']<valor2)]
            v2=GRANSILO1[GRANSILO1['I_GRAN']==1]
            v3=GRANSILO1['V_GRAN'].sum()
            v4=GRANSILO2[GRANSILO2['I_SILO']==1]
            v5=GRANSILO2['V_SILO'].sum()
            print(GRANSILO['ID'].count(),v3+v5,v2['I_GRAN'].count(),v3,v4['I_SILO'].count(),v5)
            lista_saida.append([il,GRANSILO['ID'].count(),v3+v5,v2['I_GRAN'].count(),v3,v4['I_SILO'].count(),v5])
            il+=1
            if fx==4:
                valor=LISTFX[fx][1]
                GRANSILO=dBTAB1[((dBTAB1['I_GRAN']==1) & (dBTAB1['V_GRAN']>=valor))|
                                ((dBTAB1['I_SILO']==1) & (dBTAB1['V_SILO']>=valor))]
                GRANSILO1=dBTAB1[(dBTAB1['I_GRAN']==1) & (dBTAB1['V_GRAN']>=valor)]
                GRANSILO2=dBTAB1[(dBTAB1['I_SILO']==1) & (dBTAB1['V_SILO']>=valor)]
                v2=GRANSILO1[GRANSILO1['I_GRAN']==1]
                v3=GRANSILO1['V_GRAN'].sum()
                v4=GRANSILO2[GRANSILO2['I_SILO']==1]
                v5=GRANSILO2['V_SILO'].sum()
                print(GRANSILO['ID'].count(),v3+v5,v2['I_GRAN'].count(),v3,v4['I_SILO'].count(),v5)
                lista_saida.append([il,GRANSILO['ID'].count(),v3+v5,v2['I_GRAN'].count(),v3,v4['I_SILO'].count(),v5])
                il+=1
        return(lista_saida)        
  
    def TAB5(self,MERGE,LISTAPROD):
         dBTAB5 = MERGE[['V3' ,'V4_x', 'V5_x','V6','V9']]
         print(dBTAB5.head())
         lista_saida=[]
         for LL in LISTAPROD:
             DPROD=dBTAB5[dBTAB5['V4_x']==LL]
             DMUN=DPROD[["V3","V6","V9"]]
             L_MUN=DMUN.values.tolist()
             temp=[]
             for DD in L_MUN:
                 tam=5-len(str(DD[2]))
                 temp.append(str(DD[1])+tam*"0"+str(DD[2]))
                 self.dic_emp_mun[DD[0]]=str(DD[1])+tam*"0"+str(DD[2])
             nmun=set(temp)
             print(LL,len(nmun),DPROD['V3'].count(),DPROD['V5_x'].sum())
             lista_saida.append([LL,len(nmun),DPROD['V3'].count(),DPROD['V5_x'].sum()])
         return(lista_saida)
    def TAB67(self,PD_MERGE,lista,lprod,EMP,ix):
        PDFIL=PD_MERGE[lista]
        lista_saida=[]
        if ix==1:
            VARP="V15"
        if ix==2:
            VARP="V17"
        for col in PDFIL.columns: 
            print(col)
        for LL in lprod:
            DPTOT=PDFIL[(PDFIL['V4_x']==LL)]
            print(LL,0,DPTOT['V3'].count(),DPTOT['V5_x'].sum())
            lista_saida.append([LL,0,DPTOT['V3'].count(),DPTOT['V5_x'].sum()])
            if ix==1:
                for em in EMP:
                    DPROD=PDFIL[(PDFIL['V4_x']==LL) & (PDFIL[VARP]==em)]
                    print(LL,em,DPROD['V3'].count(),DPROD['V5_x'].sum())
                    lista_saida.append([LL,em,DPROD['V3'].count(),DPROD['V5_x'].sum()])
            if ix==2:
                for at in EMP:
                    DPROD=PDFIL[(PDFIL['V4_x']==LL) & (PDFIL[VARP]==at)]
                    print(LL,at,DPROD['V3'].count(),DPROD['V5_x'].sum())
                    lista_saida.append([LL,at,DPROD['V3'].count(),DPROD['V5_x'].sum()])
        return(lista_saida)
 
    def TAB89(self,PD_MERGE,lista,EMP,ix):
        if ix==1:
            VARP="V15"
        if ix==2:
            VARP="V17"
        PDFIL=PD_MERGE[lista]
        N_TOT=[0]*len(EMP)
        N_MESO=[0]*len(EMP)
        N_MICRO=[0]*len(EMP)
        N_MUNIC=[0]*len(EMP)
        lista_saida=[]
        for col in PDFIL.columns: 
            print(col)
        for em in EMP:
            DPEMP=PDFIL[(PDFIL[VARP]==em) ]
            N_TOT[em-1]=DPEMP['V3'].count()
        #print("Total",PDFIL["V3"].count(),N_TOT)
        lista_saida.append([0,"Total",PDFIL["V3"].count(),N_TOT])
        MESO=PDFIL["V12"].unique()
        ALF=ORDALF(MESO)
        #print(ALF)
        MESO_ORD=ALF.ordenar()
        #print(MESO_ORD)
        for MM in MESO_ORD:
            DPMESO=PDFIL[(PDFIL["V12"]==MM)]
            temp=[]
            for em in EMP:
                DPEMP=DPMESO[(DPMESO[VARP]==em) ]
                N_MESO[em-1]=DPEMP['V3'].count()
            temp=N_MESO[:]
            #print(MM,DPMESO["V3"].count(),N_MESO)
            lista_saida.append([1,MM,DPMESO["V3"].count(),temp])
            MICRO=DPMESO["V14"].unique()
            ALF=ORDALF(MICRO)
            MICRO_ORD=ALF.ordenar()
            for MI in MICRO_ORD:
                DPMICRO=DPMESO[(DPMESO["V14"]==MI)]
                temp=[]
                for em in EMP:
                    DPEMP=DPMICRO[(DPMICRO[VARP]==em) ]
                    N_MICRO[em-1]=DPEMP['V3'].count()
                temp=N_MICRO[:]
                #print(MI,DPMICRO["V3"].count(),N_MICRO)
                lista_saida.append([2,MI,DPMICRO["V3"].count(),temp])
                MUNIC=DPMICRO["V10"].unique()
                ALF=ORDALF(MUNIC)
                MUNIC_ORD=ALF.ordenar()
                for MU in MUNIC_ORD:
                    DPMUNIC=DPMICRO[(DPMICRO["V10"]==MU)]
                    temp=[]
                    for em in EMP:
                        DPEMP=DPMUNIC[(DPMUNIC[VARP]==em) ]
                        N_MUNIC[em-1]=DPEMP['V3'].count()
                    temp=N_MUNIC[:]
                    #print(MU,DPMUNIC["V3"].count(),N_MUNIC)
                    lista_saida.append([3,MU,DPMUNIC["V3"].count(),temp])
        return(lista_saida)

    def TAB10(self,PD_MERGE,lista,CAP):
        PDFIL=PD_MERGE[lista]
        N_TOT=[[0,0]]*len(CAP)
        N_MESO=[[0,0]]*len(CAP)
        N_MICRO=[[0,0]]*len(CAP)
        N_MUNIC=[[0,0]]*len(CAP)
        lista_saida=[]
        for col in PDFIL.columns: 
            print(col)
        il=0
        print(N_TOT)
        for varcp in CAP:
            DPCAP=PDFIL[(PDFIL[varcp]>0)]
            N_TOT[il]=[DPCAP['V3'].count(),PDFIL[varcp].sum()]
            il+=1
        #print(PDFIL["V3"].count(),N_TOT)
        lista_saida.append([0,"Total",PDFIL["V3"].count(),N_TOT])
        MESO=PDFIL["V12"].unique()
        ALF=ORDALF(MESO)
        #print(ALF)
        MESO_ORD=ALF.ordenar()
        #print(MESO_ORD)
        for MM in MESO_ORD:
            DPMESO=PDFIL[(PDFIL["V12"]==MM)]
            il=0
            temp=[]
            for varcp in CAP:
                DPCAP=PDFIL[(PDFIL[varcp]>0) & (PDFIL["V12"]==MM)]
                N_MESO[il]=[DPCAP['V3'].count(),DPCAP[varcp].sum()]
                il+=1
            temp=N_MESO[:]
            #print(MM,DPMESO["V3"].count(),N_MESO)
            lista_saida.append([1,MM,DPMESO["V3"].count(),temp])
            MICRO=DPMESO["V14"].unique()
            ALF=ORDALF(MICRO)
            MICRO_ORD=ALF.ordenar()
            for MI in MICRO_ORD:
                DPMICRO=PDFIL[(PDFIL["V14"]==MI)]
                il=0
                temp=[]
                for varcp in CAP:
                    DPCAP=PDFIL[(PDFIL[varcp]>0) & (PDFIL["V14"]==MI)]
                    N_MICRO[il]=[DPCAP['V3'].count(),DPCAP[varcp].sum()]
                    il+=1
                temp=N_MICRO[:]
                #print(MI,DPMICRO["V3"].count(),N_MICRO)
                lista_saida.append([2,MI,DPMICRO["V3"].count(),temp])
                MUNIC=DPMICRO["V10"].unique()
                ALF=ORDALF(MUNIC)
                MUNIC_ORD=ALF.ordenar()
                for MU in MUNIC_ORD:
                    DPMUNIC=PDFIL[(PDFIL["V10"]==MU)]
                    il=0
                    temp=[]
                    for varcp in CAP:
                        DPCAP=PDFIL[(PDFIL[varcp]>0) & (PDFIL["V10"]==MU)]
                        N_MUNIC[il]=[DPCAP['V3'].count(),DPCAP[varcp].sum()]
                        il+=1
                    #print(MU,DPMUNIC["V3"].count(),N_MUNIC)
                    temp=N_MUNIC[:]
                    lista_saida.append([3,MU,DPMUNIC["V3"].count(),temp])
        return(lista_saida)
    def TAB11(self,PD_MERGE,lista,lprod):
        PDFIL=PD_MERGE[lista]
        for col in PDFIL.columns: 
            print(col)
        lista_saida=[]
        for lp in lprod:
            DPPROD=PDFIL[(PDFIL['V4_x']==lp)]
            #print(lp,0,DPPROD["V3"].count(),DPPROD["V5_x"].sum())
            lista_saida.append([lp,0,DPPROD["V3"].count(),DPPROD["V5_x"].sum()])
            MESO=DPPROD["V12"].unique()
            ALF=ORDALF(MESO)
            MESO_ORD=ALF.ordenar()
            for MM in MESO_ORD:
                DPMESO=DPPROD[(DPPROD["V12"]==MM)]
                #print(lp,"MESO",MM,DPMESO["V3"].count(),DPMESO["V5_x"].sum())
                lista_saida.append([lp,"MESO",MM,DPMESO["V3"].count(),DPMESO["V5_x"].sum()])
                MICRO=DPMESO["V14"].unique()
                ALF=ORDALF(MICRO)
                MICRO_ORD=ALF.ordenar()
                for MI in MICRO_ORD:
                    DPMICRO=DPMESO[(DPMESO["V14"]==MI)]
                    #print(lp,"MICRO",MI,DPMICRO["V3"].count(),DPMICRO["V5_x"].sum())
                    lista_saida.append([lp,"MICRO",MI,DPMICRO["V3"].count(),DPMICRO["V5_x"].sum()])
                    MUNIC=DPMICRO["V10"].unique()
                    ALF=ORDALF(MUNIC)
                    MUNIC_ORD=ALF.ordenar()
                    for MU in MUNIC_ORD:
                        DPMUNIC=DPMICRO[(DPMICRO["V10"]==MU)]
                        #print(lp,"MUNIC",MU,DPMUNIC["V3"].count(),DPMUNIC["V5_x"].sum())
                        lista_saida.append([lp,"MUNIC",MU,DPMUNIC["V3"].count(),
                                            DPMUNIC["V5_x"].sum()])
        return(lista_saida)

    def TAB11B(self,PD_MERGE,lista,lprod):
        PDFIL=PD_MERGE[lista]
        lista_MUN=[]
        for col in PDFIL.columns: 
            print(col)
        lista_saida=[]
        temp=[]
        for lp in lprod:
            DPPROD=PDFIL[(PDFIL['V4_x']==lp)]
            temp.append([DPPROD["V3"].count(),DPPROD["V5_x"].sum()])
        lista_saida.append(["0","Total",temp])
        MESO=PDFIL["V12"].unique()
        ALF=ORDALF(MESO)
        MESO_ORD=ALF.ordenar()
        for MM in MESO_ORD:
            DPMESO=PDFIL[(PDFIL["V12"]==MM)]
            temp=[]
            for lp in lprod:
                DPPROD=DPMESO[(DPMESO['V4_x']==lp)]
                temp.append([DPPROD["V3"].count(),DPPROD["V5_x"].sum()])
            lista_saida.append(["MESO",MM,temp])
            MICRO=DPMESO["V14"].unique()
            ALF=ORDALF(MICRO)
            MICRO_ORD=ALF.ordenar()
            for MI in MICRO_ORD:
                DPMICRO=DPMESO[(DPMESO["V14"]==MI)]
                temp=[]
                for lp in lprod:
                    DPPROD=DPMICRO[(DPMICRO['V4_x']==lp)]
                    temp.append([DPPROD["V3"].count(),DPPROD["V5_x"].sum()])
                lista_saida.append(["MICRO",MI,temp])
                MUNIC=DPMICRO["V10"].unique()
                ALF=ORDALF(MUNIC)
                MUNIC_ORD=ALF.ordenar()
                for MU in MUNIC_ORD:
                    DPMUNIC=DPMICRO[(DPMICRO["V10"]==MU)]
                    temp=[]
                    for lp in lprod:
                        DPPROD=DPMUNIC[(DPMUNIC['V4_x']==lp)]
                        temp.append([DPPROD["V3"].count(),DPPROD["V5_x"].sum()])
                        lista_MUN.append([lp,"MUNIC",MU,DPPROD["V3"].count(),DPPROD["V5_x"].sum()])
                    lista_saida.append(["MUNIC",MU,temp])
        return(lista_saida)
            


    def TAB12_INA(self,L_INAT):
        dBINA = pd.DataFrame(L_INAT, columns = ['ID','V_CONV','V_GRAN','V_SILO'])
        lista_saida=[]
        for col in dBINA.columns: 
            print(col)
        print(dBINA['V_CONV'].sum())
        lista_saida.append(dBINA['V_CONV'].sum())
        print(dBINA['V_GRAN'].sum())
        lista_saida.append(dBINA['V_GRAN'].sum())
        print(dBINA['V_SILO'].sum())
        lista_saida.append(dBINA['V_SILO'].sum())
        print(dBINA['ID'].count())
        lista_saida.append(dBINA['ID'].count())
        DCAP=dBINA[(dBINA['V_CONV']>0) | (dBINA['V_GRAN']>0) |
                   (dBINA['V_SILO']>0)]
        print(DCAP['ID'].count())
        lista_saida.append(DCAP['ID'].count())
        print(dBINA['ID'].count()-DCAP['ID'].count())
        lista_saida.append(dBINA['ID'].count()-DCAP['ID'].count())
        return(lista_saida)
                          
if __name__=="__main__":
    TABELASUF()  
