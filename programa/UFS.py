import pandas as pd
from programa.modulos.apuracao.TAB_UF import TABELASUF as TABUF
from programa.modulos.apuracao.PDCSVUF import ARQCSVUF as ARQCSV
from programa.modulos.apuracao.PROCESSO_TAB_UF import PROCESSAMENTO as PROCESS
from programa.modulos.apuracao.REORGANIZAR import FORMATAR as REORG
from programa.modulos.apuracao.MERGE_PDFs_UF import TABULACAO as MONTAR_UF

class UF_GERADOR():

    def __init__(self,NOMEUF,NUF,ano,sem):
        ANO=ano
        if sem=="PRIMEIRO":
            semestre=1
        if sem=="SEGUNDO":
            semestre=2
        UF=NUF
        PANDAS=ARQCSV()
        PANDAS.pdcsv(PANDAS.ESTAB)
        L_EMP=PANDAS.filtercsv(ANO,semestre,["V15","V16","V19","V20","V21"],1,UF)
    ##    print(len(L_EMP))
        L_ATIV=PANDAS.filtercsv(ANO,semestre,["V17","V18","V19","V20","V21"],1,UF)
        L_INATIVO=PANDAS.filtercsv(ANO,semestre,["V3","V19","V20","V21"],2,UF)
        PANDAS.pdcsv(PANDAS.PROD)
        L_PROD=PANDAS.filtercsv(ANO,semestre,["V3","V4","V5"],0,UF)
        PD_PROD_MERGE=PANDAS.Merge_ESTAB_PROD(PANDAS.PROD,PANDAS.ESTAB,ANO,semestre)
        DF_MERGEUF,DF_PROD,DF_ESTABUF=PD_PROD_MERGE
        DF_MERGE=DF_MERGEUF[DF_MERGEUF["V6"]==int(UF)]
        DF_ESTAB=DF_ESTABUF[DF_ESTABUF["V6"]==int(UF)]
    ##    print("XXXXXXX")
    ##    print(DF_MERGE["V3"].count())
    ##    print(DF_ESTAB["V3"].count())
    ##    print("XXXXXXX")                    
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
        GERAUF=TABUF()
        LISTA_EMP=GERAUF.capacidade(L_EMP)
        LISTA_ATIV=GERAUF.capacidade(L_ATIV)
        LISTA_PRODUTO=L_PROD[:]
        PROCESSO=PROCESS(UF,semestre,ANO)
        LISTA_TAB1=GERAUF.TAB12(LISTA_EMP,TIPO_EMP)
        LISTA_TAB2=GERAUF.TAB12(LISTA_ATIV,TIPO_ATIV)
        ##print(LISTA_TAB1)
        ##print(LISTA_TAB2)
        PROCESSO.TABPROC12(LISTA_TAB1,LISTA_TAB2)
        LISTA_TAB3=GERAUF.TAB3(LISTA_EMP,LISTA_FAIXA1)
        LISTA_TAB4=GERAUF.TAB4(LISTA_EMP,LISTA_FAIXA2)
        ##for ll in LISTA_TAB3:
        ##    print(ll)
        ##for ll in LISTA_TAB4:
        ##    print(ll)
        PROCESSO.TABPROC34(LISTA_TAB3,LISTA_TAB4)
        LISTA_TAB5=GERAUF.TAB5(DF_MERGE,LISTA_PROD5)
        ##print(LISTA_TAB5)
        PROCESSO.TABPROC5(LISTA_TAB5)
        LISTA_TAB6=GERAUF.TAB67(DF_MERGE,["V3","V4_x","V5_x","V15","V16"],LISTA_PROD5,
                     TIPO_EMP,1)
        ##print(LISTA_TAB6)
        PROCESSO.TABPROC6(LISTA_TAB6)

        LISTA_TAB7=GERAUF.TAB67(DF_MERGE,["V3","V4_x","V5_x","V17","V18"],LISTA_PROD5,
                     TIPO_ATIV,2)
        ##print(LISTA_TAB7)
        PROCESSO.TABPROC7(LISTA_TAB7)
        LISTA_TAB8=GERAUF.TAB89(DF_ESTAB,["V3","V10","V12","V14","V15","V16"],
                     TIPO_EMP,1)
        LISTA_TAB9=GERAUF.TAB89(DF_ESTAB,["V3","V10","V12","V14","V17","V18"],
                     TIPO_ATIV,2)
        PROCESSO.TABPROC8(LISTA_TAB8)
        PROCESSO.TABPROC9(LISTA_TAB9)
        ##for ll in LISTA_TAB9:
        ##    print(ll)
        LISTA_TAB10=GERAUF.TAB10(DF_ESTAB,["V3","V10","V12","V14","V19","V20","V21"],
                                LISTA_CAP)
        PROCESSO.TABPROC10(LISTA_TAB10)
        LISTA_TAB11=GERAUF.TAB11B(DF_MERGE,["V3","V4_x","V5_x","V10","V12","V14"],LISTA_PROD5)
        PROCESSO.TABPROC11(LISTA_TAB11)
        LISTA_TAB12B=GERAUF.TAB12_INA(L_INATIVO)
        PROCESSO.TABPROC12B(LISTA_TAB12B)
        MONTAR_UF(sem,ano,NOMEUF)

if __name__=="__main__":
    UF_GERADOR("Goiás",52,2021,"Primeiro")
