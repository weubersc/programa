import pandas as pd
from programa.modulos.apuracao.PDCSV import ARQCSV
from programa.modulos.apuracao.PROCESSO_TAB import PROCESSAMENTO as PROCESS
from programa.modulos.apuracao.MERGE_PDFs import TABULACAO as MONTAR


def BR_GERENCIAR(selano,SEM):

    ANO=int(selano)
    if SEM=="PRIMEIRO":
        semestre=1
    if SEM=="SEGUNDO":
        semestre=2
    PANDAS=ARQCSV()
    PANDAS.pdcsv(PANDAS.ESTAB)
    L_EMP=PANDAS.filtercsv(ANO,semestre,["V15","V16","V19","V20","V21"],1)
    L_ATIV=PANDAS.filtercsv(ANO,semestre,["V17","V18","V19","V20","V21"],1)
    L_INATIVO=PANDAS.filtercsv(ANO,semestre,["V3","V19","V20","V21"],2)
    PANDAS.pdcsv(PANDAS.PROD)
    L_PROD=PANDAS.filtercsv(ANO,semestre,["V3","V4","V5"],0)
    PD_PROD_MERGE=PANDAS.Merge_ESTAB_PROD(PANDAS.PROD,PANDAS.ESTAB,ANO,semestre)
    DF_MERGE,DF_PROD,DF_ESTAB=PD_PROD_MERGE
    soma=0
    TIPO_EMP=[1,2,3,4]

    TIPO_ATIV=[1,2,3,4,5]
    LISTA_FAIXA1=[[2000,5000],[5000,10000],[10000,50000],[50000,100000],[100000,200000]]
    LISTA_FAIXA2=[[1200,5000],[5000,10000],[10000,50000],[50000,100000],[100000,200000]]
    LISTA_CAP=["V19","V20","V21"]
    LISTA_EMP=[]
    LISTA_ATIV=[]
    LISTA_PROD5=['Algodão (em pluma)',
                 'Algodão (em caroço)',
                 'Caroço de Algodão',
                 'Semente de Algodão',
                 'Arroz (em casca)',
                 'Arroz Beneficiado',
                 'Semente de Arroz',
                 'Café Arábica (em grão)',
                 'Café Canephora (em grão)',
                 'Feijão Preto (em grão)',
                 'Feijão de Cor (em grão)',
                 'Milho (em grão)',
                 'Semente de Milho',
                 'Soja (em grão)',
                 'Semente de Soja',
                 'Trigo (em grão)',
                 'Semente de Trigo',
                 'Outros Grãos e Sementes'
                 ]

    LISTA_REG_UF=[["11","12","13","14","15","16","17"],
                  ["21","22","23","24","25","26","27","28","29"],
                  ["31","32","33","35"],
                  ["41","42","43"],
                  ["50","51","52","53"]]

    def capacidade(LISTA):
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
            

    def TAB12(LISTA,LISTA_TIP):
        dBTAB1 = pd.DataFrame(LISTA, columns = ['ID' , 'EMP', 'I_CONV','V_CONV', 'I_GRAN','V_GRAN', 'I_SILO','V_SILO'])
        v1=dBTAB1['ID'].count()
        v2=dBTAB1[dBTAB1['I_CONV']==1]
        v3=dBTAB1['V_CONV'].sum()
        v4=dBTAB1[dBTAB1['I_GRAN']==1]
        v5=dBTAB1['V_GRAN'].sum()
        v6=dBTAB1[dBTAB1['I_SILO']==1]
        v7=dBTAB1['V_SILO'].sum()
        LISTA_SAIDA=[]
        tot=0
        #print(0,v1,v2['I_CONV'].count(),v3,v4['I_GRAN'].count(),v5,v6['I_GRAN'].count(),v7)
        LISTA_SAIDA.append([tot,v1,v2['I_CONV'].count(),v3,v4['I_GRAN'].count(),v5,v6['I_GRAN'].count(),v7])
        for EMP in LISTA_TIP:
            DBEMP=dBTAB1[dBTAB1['ID']==EMP]
            v1=DBEMP['ID'].count()
            v2=DBEMP[DBEMP['I_CONV']==1]
            v3=DBEMP['V_CONV'].sum()
            v4=DBEMP[DBEMP['I_GRAN']==1]
            v5=DBEMP['V_GRAN'].sum()
            v6=DBEMP[DBEMP['I_SILO']==1]
            v7=DBEMP['V_SILO'].sum()
            #print(EMP,v1,v2['I_CONV'].count(),v3,v4['I_GRAN'].count(),v5,v6['I_GRAN'].count(),v7)
            LISTA_SAIDA.append([EMP,v1,v2['I_CONV'].count(),v3,v4['I_GRAN'].count(),v5,v6['I_GRAN'].count(),v7])
        return(LISTA_SAIDA)

    def TAB3(LISTA,LISTFX):
        dBTAB1 = pd.DataFrame(LISTA, columns = ['ID' , 'EMP', 'I_CONV','V_CONV', 'I_GRAN','V_GRAN', 'I_SILO','V_SILO'])
        v2=dBTAB1[dBTAB1['I_CONV']==1]
        v3=dBTAB1['V_CONV'].sum()
        LISTA_SAIDA=[]
        #print(0,v2['I_CONV'].count(),v3)
        LISTA_SAIDA.append([0,v2['I_CONV'].count(),v3])
        il=1
        for fx in range(0,len(LISTFX)):
            if fx==0:
                valor=LISTFX[fx][0]
                DBEMP=dBTAB1[dBTAB1['V_CONV']<valor]
                v2=DBEMP[DBEMP['I_CONV']==1]
                v3=DBEMP['V_CONV'].sum()
                #print(il,v2['I_CONV'].count(),v3)
                LISTA_SAIDA.append([il,v2['I_CONV'].count(),v3])
                il+=1
            valor1=LISTFX[fx][0]
            valor2=LISTFX[fx][1]
            DPA=dBTAB1[dBTAB1['V_CONV']>=valor1]
            DBEMP=DPA[DPA['V_CONV']<valor2]               
            v2=DBEMP[DBEMP['I_CONV']==1]
            v3=DBEMP['V_CONV'].sum()
            #print(il,v2['I_CONV'].count(),v3)
            LISTA_SAIDA.append([il,v2['I_CONV'].count(),v3])
            il+=1
            if fx==4:
                valor=LISTFX[fx][1]
                DBEMP=dBTAB1[dBTAB1['V_CONV']>=valor]
                v2=DBEMP[DBEMP['I_CONV']==1]
                v3=DBEMP['V_CONV'].sum()
                #print(il,v2['I_CONV'].count(),v3)
                LISTA_SAIDA.append([il,v2['I_CONV'].count(),v3])
                il+=1
        return(LISTA_SAIDA)
                
    def TAB4(LISTA,LISTFX):
        dBTAB1 = pd.DataFrame(LISTA, columns = ['ID' , 'EMP', 'I_CONV','V_CONV', 'I_GRAN','V_GRAN', 'I_SILO','V_SILO'])
        GRANSILO=dBTAB1[(dBTAB1['I_GRAN']==1)|(dBTAB1['I_SILO']==1)]
        v2=dBTAB1[dBTAB1['I_GRAN']==1]
        v3=dBTAB1['V_GRAN'].sum()
        v4=dBTAB1[dBTAB1['I_SILO']==1]
        v5=dBTAB1['V_SILO'].sum()
        LISTA_SAIDA=[]
        #print(0,GRANSILO['ID'].count(),v3+v5,v2['I_GRAN'].count(),v3,v4['I_SILO'].count(),v5)
        LISTA_SAIDA.append([0,GRANSILO['ID'].count(),v3+v5,v2['I_GRAN'].count(),v3,v4['I_SILO'].count(),v5])
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
                #print(il,GRANSILO['ID'].count(),v3+v5,v2['I_GRAN'].count(),v3,v4['I_SILO'].count(),v5)
                LISTA_SAIDA.append([il,GRANSILO['ID'].count(),v3+v5,v2['I_GRAN'].count(),v3,v4['I_SILO'].count(),v5])
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
            #print(il,GRANSILO['ID'].count(),v3+v5,v2['I_GRAN'].count(),v3,v4['I_SILO'].count(),v5)
            LISTA_SAIDA.append([il,GRANSILO['ID'].count(),v3+v5,v2['I_GRAN'].count(),v3,v4['I_SILO'].count(),v5])
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
                #print(il,GRANSILO['ID'].count(),v3+v5,v2['I_GRAN'].count(),v3,v4['I_SILO'].count(),v5)
                LISTA_SAIDA.append([il,GRANSILO['ID'].count(),v3+v5,v2['I_GRAN'].count(),v3,v4['I_SILO'].count(),v5])
                il+=1
        return(LISTA_SAIDA)
    def MUNEMP():         
        PANDAS.pdcsv(PANDAS.ESTAB)
        LISTA_MUNEMP=PANDAS.filtercsv(ANO,semestre,["V3","V6","V7","V9","V10","V15","V17"],1)
        dic_emp_mun={}
        for LL in LISTA_MUNEMP:
            tamanho=5-len(str(LL[3]))
            zero=tamanho*"0"
            dic_emp_mun[LL[0]]=str(LL[1])+zero+str(LL[3])
        return(dic_emp_mun)
         

    def TAB5(LISTA,LISTAPROD):
         dBTAB5 = pd.DataFrame(LISTA, columns = ['COD' , 'PROD', 'QUANT'])
         DICEMP=MUNEMP()
         LISTA_SAIDA=[]
         for LL in LISTAPROD:
             DPROD=dBTAB5[dBTAB5['PROD']==LL]
             temp=[]
             for DD in DPROD['COD']:
                 try:
                     temp.append(DICEMP[DD])
                 except:
                     pass
             mun_prod=set(temp)
             PP=DPROD['COD'].unique()
             #print(LL,len(mun_prod),DPROD['COD'].count(),DPROD['QUANT'].sum())
             LISTA_SAIDA.append([LL,len(mun_prod),DPROD['COD'].count(),DPROD['QUANT'].sum()])
         return(LISTA_SAIDA)
                      
             

                 
     
    def TAB67(PD_MERGE,lista,lprod,EMP,ix):
        PDFIL=PD_MERGE[lista]
        if ix==1:
            VARP="V15"
        if ix==2:
            VARP="V17"
##        for col in PDFIL.columns: 
##            print(col)
        LISTA_SAIDA=[]
        for LL in lprod:
            DPTOT=PDFIL[(PDFIL['V4_x']==LL)]
            #print(LL,0,DPTOT['V3'].count(),DPTOT['V5_x'].sum())
            LISTA_SAIDA.append([LL,0,DPTOT['V3'].count(),DPTOT['V5_x'].sum()])
            if ix==1:
                for em in EMP:
                    DPROD=PDFIL[(PDFIL['V4_x']==LL) & (PDFIL[VARP]==em)]
                    #print(LL,em,DPROD['V3'].count(),DPROD['V5_x'].sum())
                    LISTA_SAIDA.append([LL,em,DPROD['V3'].count(),DPROD['V5_x'].sum()])
            if ix==2:
                for at in EMP:
                    DPROD=PDFIL[(PDFIL['V4_x']==LL) & (PDFIL[VARP]==at)]
                    LISTA_SAIDA.append([LL,at,DPROD['V3'].count(),DPROD['V5_x'].sum()])
            
        return(LISTA_SAIDA)

    def TAB89(PD_MERGE,lista,lreguf,EMP,ix):
        if ix==1:
            VARP="V15"
        if ix==2:
            VARP="V17"
        PDFIL=PD_MERGE[lista]
        N_EST=[0]*len(EMP)
        N_REG=[0]*len(EMP)
        N_UF=[0]*len(EMP)
        lista_saida=[]
##        for col in PDFIL.columns: 
##            print(col)
        for em in EMP:
            DPEMP=PDFIL[(PDFIL[VARP]==em) ]
            N_EST[em-1]=DPEMP['V3'].count()
        #print("00",PDFIL["V3"].count(),N_EST)
        lista_saida.append(["00",PDFIL["V3"].count(),N_EST])
        for reg  in range(0,len(lreguf)):
            DPREG=PDFIL[(PDFIL['V4']==reg+1) ]
            for em in EMP:
                temp=[]
                DPPROV=DPREG[(PDFIL['V4']==reg+1) & (DPREG[VARP]==em)]       
                N_REG[em-1]=DPPROV['V3'].count()
                temp=N_REG[:]
            #print(str(reg+1),DPREG["V3"].count(),N_REG)
            lista_saida.append([str(reg+1),DPREG["V3"].count(),temp])
            for uf in lreguf[reg]:
                DPUF=DPREG[(DPREG['V6']==int(uf))]
                temp=[]
                for em in EMP:
                    DPPROV=DPUF[(DPREG['V6']==int(uf)) & (DPUF[VARP]==em)]       
                    N_UF[em-1]=DPPROV['V3'].count()
                    temp=N_UF[:]
                #print(str(uf),DPUF["V3"].count(),temp)
                lista_saida.append([str(uf),DPUF["V3"].count(),temp])
        return(lista_saida)

    def TAB10(PD_MERGE,lista,lreguf,CAP):
        PDFIL=PD_MERGE[lista]
        N_TOT=[[0,0]]*len(CAP)
        N_REG=[[0,0]]*len(CAP)
        N_UF=[[0,0]]*len(CAP)    
##        for col in PDFIL.columns: 
##            print(col)
        il=0
    #    print(N_TOT)
        lista_saida=[]
        for varcp in CAP:
            DPCAP=PDFIL[(PDFIL[varcp]>0)]
            N_TOT[il]=[DPCAP['V3'].count(),PDFIL[varcp].sum()]
            il+=1
        #print(PDFIL["V3"].count(),N_TOT)
        lista_saida.append(["00",PDFIL["V3"].count(),N_TOT])
        for reg  in range(0,len(lreguf)):
            DPREG=PDFIL[(PDFIL['V4']==reg+1) ]
            il=0
            temp=[]
            for varcp in CAP:
                DPPROV=PDFIL[(PDFIL['V4']==reg+1) & (PDFIL[varcp]>0)]       
                N_REG[il]=[DPPROV['V3'].count(),DPPROV[varcp].sum()]
                il+=1
            temp=N_REG[:]
            #print(DPREG["V3"].count(),temp)
            lista_saida.append([str(reg+1),DPREG["V3"].count(),temp])
            for uf in lreguf[reg]:
                DPUF=PDFIL[(PDFIL['V6']==int(uf)) ]
                iluf=0
                temp=[]
                for varcp in CAP:
                    DPPROV=PDFIL[(PDFIL['V6']==int(uf)) & (PDFIL[varcp]>0)]       
                    N_UF[iluf]=[DPPROV['V3'].count(),DPPROV[varcp].sum()]
                    iluf+=1
                temp=N_UF[:]
                #print(uf,DPUF["V3"].count(),temp)
                lista_saida.append([str(uf),DPUF["V3"].count(),temp])

        return(lista_saida)
    def TAB11(PD_MERGE,lista,lprod,lreguf):
        PDFIL=PD_MERGE[lista]
##        for col in PDFIL.columns: 
##            print(col)
        lista_saida=[]
        for lp in lprod:
            DPPROD=PDFIL[(PDFIL['V4_x']==lp)]
    #        print(lp,"00",DPPROD["V3"].count(),DPPROD["V5_x"].sum())
            lista_saida.append([lp,"00",DPPROD["V3"].count(),DPPROD["V5_x"].sum()])
            for reg  in range(0,len(lreguf)):
                DPREG=DPPROD[(PDFIL['V4_y']==reg+1)]
    #            print(lp,str(reg+1),DPREG["V3"].count(),DPREG["V5_x"].sum())
                lista_saida.append([lp,str(reg+1),DPREG["V3"].count(),
                                    DPREG["V5_x"].sum()])
                for uf in lreguf[reg]:
                    DPUF=DPPROD[(DPPROD['V6']==int(uf))]
    #                print(lp,str(uf),DPUF["V3"].count(),DPUF["V5_x"].sum())
                    lista_saida.append([lp,str(uf),DPUF["V3"].count(),
                                        DPUF["V5_x"].sum()])
        return(lista_saida)

    def TAB12_INA(L_INAT):
        dBINA = pd.DataFrame(L_INAT, columns = ['ID','V_CONV','V_GRAN','V_SILO'])
        for col in dBINA.columns: 
            print(col)
        lista_saida=[]
        #print(dBINA['V_CONV'].sum())
        lista_saida.append(dBINA['V_CONV'].sum())
        #print(dBINA['V_GRAN'].sum())
        lista_saida.append(dBINA['V_GRAN'].sum())
        #print(dBINA['V_SILO'].sum())
        lista_saida.append(dBINA['V_SILO'].sum())
        #print(dBINA['ID'].count())
        lista_saida.append(dBINA['ID'].count())
        DCAP=dBINA[(dBINA['V_CONV']>0) | (dBINA['V_GRAN']>0) |
                   (dBINA['V_SILO']>0)]
        #print(DCAP['ID'].count())
        lista_saida.append(DCAP['ID'].count())
        #print(dBINA['ID'].count()-DCAP['ID'].count())
        lista_saida.append(dBINA['ID'].count()-DCAP['ID'].count())
        return(lista_saida)
        

      

        
    LISTA_EMP=capacidade(L_EMP)
    LISTA_ATIV=capacidade(L_ATIV)
    LISTA_PRODUTO=L_PROD[:]
    PROCESSO=PROCESS(ANO,semestre)
    LISTA_TAB1=TAB12(LISTA_EMP,TIPO_EMP)
##    for lx in LISTA_TAB1:
##        print(lx)
    LISTA_TAB2=TAB12(LISTA_ATIV,TIPO_ATIV)
##    for lx in LISTA_TAB2:
##        print(lx)
    PROCESSO.TABPROC12(LISTA_TAB1,LISTA_TAB2)
    LISTA_TAB3=TAB3(LISTA_EMP,LISTA_FAIXA1)
    ##print(LISTA_TAB3)
    LISTA_TAB4=TAB4(LISTA_EMP,LISTA_FAIXA2)
    ##print(LISTA_TAB4)
    PROCESSO.TABPROC34(LISTA_TAB3,LISTA_TAB4)
    LISTA_TAB5=TAB5(LISTA_PRODUTO,LISTA_PROD5)
    ##print(LISTA_TAB5)
    PROCESSO.TABPROC5(LISTA_TAB5)
    LISTA_TAB6=TAB67(DF_MERGE,["V3","V4_x","V5_x","V15","V16"],LISTA_PROD5,
         TIPO_EMP,1)
    ##print(LISTA_TAB6)
    PROCESSO.TABPROC6(LISTA_TAB6)
    LISTA_TAB7=TAB67(DF_MERGE,["V3","V4_x","V5_x","V17","V18"],LISTA_PROD5,
          TIPO_ATIV,2)
    ##print(LISTA_TAB7)
    PROCESSO.TABPROC7(LISTA_TAB7)
    LISTA_TAB8=TAB89(DF_ESTAB,["V3","V4","V6","V15","V16"],LISTA_REG_UF,
              TIPO_EMP,1)
    ###print(LISTA_TAB8)
    PROCESSO.TABPROC8(LISTA_TAB8)
    LISTA_TAB9=TAB89(DF_ESTAB,["V3","V4","V6","V17","V18"],LISTA_REG_UF,
            TIPO_ATIV,2)
    ####print(LISTA_TAB9)
    PROCESSO.TABPROC9(LISTA_TAB9)
    LISTA_TAB10=TAB10(DF_ESTAB,["V3","V4","V6","V19","V20","V21"],LISTA_REG_UF,
          LISTA_CAP)
    ####print(LISTA_TAB10)
    PROCESSO.TABPROC10(LISTA_TAB10)
    LISTA_TAB11=TAB11(DF_MERGE,["V3","V4_x","V5_x","V4_y","V6"],LISTA_PROD5,
          LISTA_REG_UF)
    ###print(LISTA_TAB11)
    PROCESSO.TABPROC11(LISTA_TAB11)
    LISTA_TAB12=TAB12_INA(L_INATIVO)
    #print(LISTA_TAB12)
    PROCESSO.TABPROC12B(LISTA_TAB12)
    #exit()
    MONTAR(selano,SEM)
