import pandas as pd
import os
import chardet
from listtocsv import listacsv as LCSV
import programa.modulos.ler_encod as LER
import programa.modulos.LEITURA_CSV_DF as CSV_DF
import programa.modulos.CONSULTA_SQL_DF as SQL
import sqlite3

class ARQCSVUF():
    def __init__(self,semes,ano):
       self.dirpath=os.getcwd()
       self.ESTAB=(self.dirpath+"\\programa\\arquivos\\ESTAB.csv")
       self.PROD=(self.dirpath+"\\programa\\arquivos\\PROD.csv")
       self.PERG=(self.dirpath+"\\programa\\arquivos\\PERG.csv")
       encod=LER.LER_ENCOD(self.ESTAB)
       ANO=ano
       SEMESTRE=semes
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

       # Converter CSV para DF
       DF_ESTAB=CSV_DF.LERCSV(self.ESTAB,";")
       DF_PROD=CSV_DF.LERCSV(self.PROD,";")
       x,y=DF_ESTAB.shape
       print(x,y)
       lista_col=[]
       for k in range(1,y+1):
           lista_col.append("W"+str(k))
       DF_ESTAB.columns=lista_col
       x,y=DF_PROD.shape
       print(x,y)
       lista_col=[]
       for k in range(1,y+1):
           lista_col.append("V"+str(k))
       DF_PROD.columns=lista_col
       
       # CALCULAR O RANKING POR TIPO DE CAPACIDADE E TOTAL
       sql="select W6,W7,W9,W10,sum(W19) as CONV,sum(W20) as GRAN,sum(W21) as SILO "
       sql+="from tabela where W1="+str(ANO)+" and W2="+str(SEMESTRE) +" and W22=1"
       sql+=" group by W6,W7,W9,W10"
       print(sql)
       DF_EST=SQL.DF_SQL_DF(DF_ESTAB,sql,"tabela")
       L_ESTAB=DF_EST.values.tolist()
       L_TOTAL=[]
       for ll in L_ESTAB:
           total=ll[4]+ll[5]+ll[6]
           codmun=str(ll[0])+(5-len(str(ll[2])))*"0"+str(ll[2])
           L_TOTAL.append([ll[1],codmun,ll[3],total,ll[4],ll[5],ll[6]])
       colunas=["SIGLA_UF","COD_MUN","MOME_MUN","TOTAL",
                "CONV","GRAN","SILO"]
       DATA_ESTAB=pd.DataFrame(L_TOTAL,columns=colunas)
       DATA_ESTAB_SORT=DATA_ESTAB.sort_values("TOTAL", ascending=False)
       # writing to Excel
       datatoexcel = pd.ExcelWriter(self.dirpath+"\\programa\\saida\\Ranking.xlsx")
  
       # write DataFrame to excel
       DATA_ESTAB_SORT.to_excel(datatoexcel,sheet_name='CAPACIDADE', index=False)

       # CALCULAR O RANKING POR PRODUTO
       DF_EST=DF_ESTAB[(DF_ESTAB["W1"]==ANO) &
                          (DF_ESTAB["W2"]==SEMESTRE) &
                          (DF_ESTAB["W22"]==1)]

       DF_PRODUTO=DF_PROD[(DF_PROD["V1"]==ANO) &
                          (DF_PROD["V2"]==SEMESTRE)]
       print(DF_PRODUTO.shape)
       DF_soma=(DF_PRODUTO.groupby("V4")["V5"]
               .sum()
               .sort_values(ascending=False)
               .reset_index()
               )
       colunas=["Produto","ARMZ(kg)"]
       DF_soma.columns=colunas
       
       DF_soma.to_excel(datatoexcel,sheet_name="PRODUTO", index=False)

       for pp in LISTA_PROD5:
           DF_PRODUTO=DF_PROD[(DF_PROD["V4"]==pp) &
                                  (DF_PROD["V1"]==ANO) &
                                  (DF_PROD["V2"]==SEMESTRE)]
           print(pp)
           DF_MERGE=pd.merge(DF_PRODUTO,DF_EST, left_on='V3',right_on='W3',how='left')
           print(DF_MERGE.shape)
           sql="select W6,W7,W9,W10,sum(V5) as ARMZ "
           sql+="from tabela group by W6,W7,W9,W10"
           #print(sql)
           DF_PP=SQL.DF_SQL_DF(DF_MERGE,sql,"tabela")
           #print(DF_PP.shape)
           L_PROD=DF_PP.values.tolist()
           L_TOTAL=[]
           for ll in L_PROD:
               codmun=str(ll[0])+(5-len(str(ll[2])))*"0"+str(ll[2])
               L_TOTAL.append([ll[1],codmun,ll[3],ll[4]])
           colunas=["SIGLA_UF","COD_MUN","MOME_MUN","ARMZ(kg)"]
           DATA_PROD=pd.DataFrame(L_TOTAL,columns=colunas)
           DATA_PROD_SORT=DATA_PROD.sort_values("ARMZ(kg)", ascending=False)
           # write DataFrame to excel
           DATA_PROD_SORT.to_excel(datatoexcel,sheet_name=pp, index=False)       


       # save the excel
       datatoexcel.save()
           
       

                 
       
if __name__=="__main__":
    ARQCSVUF(2,2021)       
      
