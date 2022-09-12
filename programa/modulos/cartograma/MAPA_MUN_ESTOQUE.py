import pandas as pd
import os
import chardet
from listtocsv import listacsv as LCSV
from openpyxl import Workbook
from openpyxl import load_workbook
from openpyxl.styles import Alignment
from openpyxl.styles import Border, Side, Font
import xlwt
import json
from datetime import datetime
import sqlite3
from programa.modulos.CONSULTA_SQL_DF import DF_SQL_DF as DFSQL




class APURAÇÃO():
    def __init__(self,semestre,ano):
       data_atual = datetime.today()
       self.atual=str(data_atual.year)
       self.ano=str(ano)
       self.ant=str(int(self.ano)-1)
       if semestre=="PRIMEIRO":
           self.sem=1
       if semestre=="SEGUNDO":
           self.sem=2
       print(self.ano,self.ant,self.sem,sep="---")
       self.dirpath=os.getcwd()
       self.ESTAB=(self.dirpath+"\\programa\\arquivos\\ESTAB.csv")
       self.PROD=(self.dirpath+"\\programa\\arquivos\\PROD.csv")
       self.PERG=(self.dirpath+"\\programa\\arquivos\\PERG.csv")
       print("OK")
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

       LISTA_REG_UF=["11","12","13","14","15","16","17",
                  "21","22","23","24","25","26","27","28","29",
                  "31","32","33","35",
                  "41","42","43",
                  "50","51","52","53"]

##       LISTA_REG_UF=["41","42","43"]

       lista_per_uf=[]
       cap_BR=[0,0,0]
       BAR_UF=[]
       cap_uf=[]
       for cuf in LISTA_REG_UF:
           print("----"+cuf+"-----")
           lista_ativo=self.Ativo(self.ESTAB,cuf)
           lista_ativo_ant=self.Ativo_ant(self.ESTAB,cuf)
           cap_at,peruf=self.capuf(lista_ativo,lista_ativo_ant)
           for k in range(0,3):
               cap_BR[k]+=cap_at[k]
           peruf.insert(0,cuf)
           cap_at.insert(0,cuf)
           cap_uf.append(cap_at)
           lista_per_uf.append(peruf)
       lista_per_uf2=[]
       for lpf in lista_per_uf:
           for cp in cap_uf:
               temp=cp[1:4]
               if cp[0]==lpf[0]:
                   temp2=[]
                   temp2=lpf+temp
           lista_per_uf2.append(temp2)
           
       for luf in cap_uf:
           temp=[]
           temp.append(luf[0])
           for k in range(0,3):
               pbr=self.percent(cap_BR[k],luf[k+1])
               temp.append(pbr)
           BAR_UF.append(temp)
       self.DBCAP(lista_per_uf2,BAR_UF)

    def DBCAP(self,lista1,lista2):
        lcol=["CD_GEOCUF",
                "VAR1","VAR2","VAR3",
                "CAP1","CAP2","CAP3"]
        DB1=pd.DataFrame(lista1,columns=lcol)
        print(DB1.shape)
        print(DB1.columns)
        print(DB1.dtypes)
        DB1.to_json(self.dirpath+"\\programa\\provisórios\\capacidade_uf.json",orient="records")
        DB2=pd.DataFrame(lista2,columns=["CD_GEOCUF","VAR1","VAR2","VAR3"])
        print(DB2.shape)
        print(DB2.columns)
        print(DB2.dtypes)
        DB2.to_json(self.dirpath+"\\programa\\provisórios\\percentual_uf.json",orient="records")

               
           
           
    def capuf(self,lista1,lista2):
          cap1=[0]*3
          cap2=[0]*3
          for ll in lista1:
              cap1[0]+=ll[18]
              cap1[1]+=ll[19]
              cap1[2]+=ll[20]
          for ll in lista2:
              cap2[0]+=ll[18]
              cap2[1]+=ll[19]
              cap2[2]+=ll[20]
##          print(cap1)
##          print(cap2)
          puf=self.percentual(cap1,cap2)
          return(cap1,puf)
          
          





    def espaco(self,valor):
        vf=("{:,}".format(valor).replace(",", " "))
        return(vf)

    def percentual(self,som1,som2):
        per=[0,0,0]
        for k in range(0,3):
            try:
                temp=round(((som1[k]-som2[k])/som2[k])*100,1)
                per[k]=temp
            except:
                pass
        return(per)

    def percent(self,som1,som2):
        try:
            temp=round(som2/som1*100,1)
            per=str(temp)
        except:
            per=0
        return(per)

    def Ativo(self,arq,uf):

        DB=pd.read_csv(arq,sep=";",
                                 encoding = "ISO-8859-1",header=None)
 
        tam=(DB.shape)
 
        temp=[]
        for i in range(1,tam[1]+1):
            temp.append("V"+str(i))

        DB.columns = temp
        self.DBCOL=DB

 
        DB_ATIVO=self.DBCOL[((self.DBCOL['V1']==int(self.ano)) &
                         (self.DBCOL['V2']==self.sem) &
                         (self.DBCOL['V6']==int(uf)) &    
                         (self.DBCOL['V23']=='Ativo'))]



        LISTA_ATIVO=DB_ATIVO.values.tolist()
        return(LISTA_ATIVO)


 

    def Ativo_ant(self,arq,uf):

        DB=pd.read_csv(arq,sep=";",
                                 encoding = "ISO-8859-1",header=None)
 
        tam=(DB.shape)

        temp=[]
        for i in range(1,tam[1]+1):
            temp.append("V"+str(i))

        DB.columns = temp
        self.DBCOL=DB


        DB_ATIVO=self.DBCOL[((self.DBCOL['V1']==int(self.ant)) &
                         (self.DBCOL['V2']==self.sem) &
                         (self.DBCOL['V6']==int(uf)) &
                         (self.DBCOL['V23']=='Ativo'))]



        LISTA_ATIVO_ANT=DB_ATIVO.values.tolist()
        return(LISTA_ATIVO_ANT)

    def Prod(self,arq):

        DB=pd.read_csv(arq,sep=";",
                                 encoding = "ISO-8859-1",header=None)
 
        tam=(DB.shape)
        print(tam)
        temp=[]
        for i in range(1,tam[1]+1):
            temp.append("V"+str(i))
        print(temp)
        DB.columns = temp
        self.DBCOL=DB

        for col in self.DBCOL.columns: 
                print(col)

        DB_PROD=self.DBCOL[((self.DBCOL['V1']==int(self.ano)) &
                         (self.DBCOL['V2']==self.sem))]

        print(DB_PROD.shape)
        LISTA_PROD=DB_PROD.values.tolist()
        return(LISTA_PROD)

    def Prod_ant(self,arq):

        DB=pd.read_csv(arq,sep=";",
                                 encoding = "ISO-8859-1",header=None)
 
        tam=(DB.shape)
        print(tam)
        temp=[]
        for i in range(1,tam[1]+1):
            temp.append("V"+str(i))
        print(temp)
        DB.columns = temp
        self.DBCOL=DB

        for col in self.DBCOL.columns: 
                print(col)

        DB_PROD=self.DBCOL[((self.DBCOL['V1']==int(self.ant)) &
                         (self.DBCOL['V2']==self.sem))]

        print(DB_PROD.shape)
        LISTA_PROD=DB_PROD.values.tolist()
        return(LISTA_PROD)
    


    def comparacao(self,listap,lista1,lista2,dicr):
        for lp in listap:
            soma1=0
            contador1=0
            soma2=0
            contador2=0
            L1=[]
            L2=[]
            for l1 in lista1:
                if l1[3]==lp:
                    try:
                       if dicr[l1[2]]==True:
                           L1.append([l1[2],l1[4]])
                           soma1+=int(l1[4])
                           contador1+=1
                    except:
                       pass

            for l2 in lista2:
                if l2[3]==lp:
                    try:
                       if dicr[l2[2]]==True:
                           L2.append([l2[2],l2[4]])
                           soma2+=int(l2[4])
                           contador2+=1
                    except:
                       pass
            tot1=0
            tot2=0
            cont=0
            for m1 in L1:
                for m2 in L2:
                    if m1[0]==m2[0]:
                        tot1+=m1[1]
                        tot2+=m2[1]
                        cont+=1

            print(lp,contador1,contador2,soma1,soma2,sep=";")
            print(lp,cont,tot1,tot2,sep=";")
            try:
                temp=round((tot1-tot2)/tot2*100,1)
                pp=str(temp)
                pp=pp.replace(".",",")
            except:
                pp="0,0"
            self.comp.append([lp,cont,tot1,tot2,pp])
            print("-------------------")
        

class APURAC_MUN():            
    def __init__(self,semestre,ano):
       data_atual = datetime.today()
       self.atual=str(data_atual.year)
       self.ano=str(ano)
       self.ant=str(int(self.ano)-1)
       if semestre=="PRIMEIRO":
           self.sem=1
       if semestre=="SEGUNDO":
           self.sem=2
       print(self.ano,self.ant,self.sem,sep="---")
       self.dirpath=os.getcwd()
       self.ESTAB=(self.dirpath+"\\programa\\arquivos\\ESTAB.csv")
       DF1A=self.Mun_ativo(self.ESTAB)
       DF1A.to_json(self.dirpath+"\\programa\\provisórios\\MUNIC_CAPACIDADE.json",orient="records")
       DF1B=self.Mun_ativo_ant(self.ESTAB)
       DF1B.to_json(self.dirpath+"\\programa\\provisórios\\MUNIC_CAPACIDADE_ANT.json",orient="records") 
    def Mun_ativo(self,arq):

        DB=pd.read_csv(arq,sep=";",
                       encoding = "ISO-8859-1",header=None)
 
        tam=(DB.shape)
 
        temp=[]
        for i in range(1,tam[1]+1):
            temp.append("V"+str(i))

        DB.columns = temp
        self.DBCOL=DB

        DB_1=self.DBCOL[((self.DBCOL['V1']==int(self.ano)) &
                         (self.DBCOL['V2']==self.sem) &
                         (self.DBCOL['V23']=='Ativo'))]
        DB_1["CODMUN"]=""
        for x,y in DB_1.iterrows():
            comp=len(str(y["V9"]))
            CC=str(y["V6"])+(5-comp)*"0"+str(y["V9"])
            DB_1.at[x,"CODMUN"]=CC

        DBA=DB_1[["CODMUN","V19","V20","V21"]]
        conn=sqlite3.connect(self.dirpath+"\\programa\\provisórios\\munic.db")
        DBA.to_sql("MUN",conn,if_exists="replace",index=False)
        conn.close()

        sele="select CODMUN,sum(V19) as CONV,sum(V20) as GRAN,sum(V21) as SILO from MUN group by CODMUN"
        conn=sqlite3.connect(self.dirpath+"\\programa\\provisórios\\munic.db")
        DF1=pd.read_sql_query(sele,conn)
        conn.close()
        return(DF1)
        

                             
                             


 

    def Mun_ativo_ant(self,arq):

        DB=pd.read_csv(arq,sep=";",
                                 encoding = "ISO-8859-1",header=None)
 
        tam=(DB.shape)

        temp=[]
        for i in range(1,tam[1]+1):
            temp.append("V"+str(i))

        DB.columns = temp
        self.DBCOL=DB

        DB_2=self.DBCOL[((self.DBCOL['V1']==(int(self.ant)-1)) &
                         (self.DBCOL['V2']==self.sem) &
                         (self.DBCOL['V23']=='Ativo'))]

        DB_2["CODMUN"]=""
        for x,y in DB_2.iterrows():
            comp=len(str(y["V9"]))
            CC=str(y["V6"])+(5-comp)*"0"+str(y["V9"])
            DB_2.at[x,"CODMUN"]=CC

        DBB=DB_2[["CODMUN","V19","V20","V21"]]
        conn=sqlite3.connect('munic.db')
        DBB.to_sql("MUN",conn,if_exists="replace",index=False)
        conn.close()

        sele="select CODMUN,sum(V19) as CONV,sum(V20) as GRAN,sum(V21) as SILO from MUN group by CODMUN"
        conn=sqlite3.connect('munic.db')
        DF2=pd.read_sql_query(sele,conn)
        conn.close()
        return(DF2)
     
class Produto():
      def __init__(self,semestre,ano):
        data_atual = datetime.today()
        self.atual=str(data_atual.year)
        self.ano=str(ano)
        self.ant=str(int(self.ano)-1)
        if semestre=="PRIMEIRO":
           self.sem=1
        if semestre=="SEGUNDO":
           self.sem=2
        #print(self.ano,self.ant,self.sem,sep="---")
        self.dirpath=os.getcwd()
        self.ESTAB=(self.dirpath+"\\programa\\arquivos\\ESTAB.csv")
        self.PROD=(self.dirpath+"\\programa\\arquivos\\PROD.csv")
        self.PERG=(self.dirpath+"\\programa\\arquivos\\PERG.csv")
        #print("OK")
        LISTA_PROD=['Algodão (em pluma)',
                 'Algodão (em caroço)',
                 'Caroço de Algodão',
                 'Arroz (em casca)',
                 'Arroz Beneficiado',
                 'Café Arábica (em grão)',
                 'Café Canephora (em grão)',
                 'Café (em grão)',
                 'Feijão Preto (em grão)',
                 'Feijão de Cor (em grão)',
                 'Feijão (em grão)',
                 'Milho (em grão)',
                 'Soja (em grão)',
                 'Trigo (em grão)',
                 ]

        LISTA_REG_UF=["11","12","13","14","15","16","17",
                  "21","22","23","24","25","26","27","28","29",
                  "31","32","33","35",
                  "41","42","43",
                  "50","51","52","53"]

        DB_ATUAL=self.ATUAL(self.ESTAB,self.PROD)
        DB_ANTERIOR=self.ANTERIOR(self.ESTAB,self.PROD)
        DB_CAFE_ATUAL=self.cafe(DB_ATUAL,LISTA_REG_UF)
        DB_CAFE_ANTERIOR=self.cafe(DB_ANTERIOR,LISTA_REG_UF)
        DB_FEIJAO_ATUAL=self.feijao(DB_ATUAL,LISTA_REG_UF)
        DB_FEIJAO_ANTERIOR=self.feijao(DB_ANTERIOR,LISTA_REG_UF)
        DF_CONCAT0=pd.concat([DB_ATUAL,DB_CAFE_ATUAL])
        DF_CONCAT1=pd.concat([DB_ANTERIOR,DB_CAFE_ANTERIOR])
        DB_ATUAL=pd.concat([DF_CONCAT0,DB_FEIJAO_ATUAL])
        DB_ANTERIOR=pd.concat([DF_CONCAT1,DB_FEIJAO_ANTERIOR])
        DB_PROD_UF1=self.PRODUTOxUF(DB_ATUAL)
        DB_PROD_UF2=self.PRODUTOxUF(DB_ANTERIOR)
        lista_uf_prod=[]
        lista_br_prod=[]
        for LP in LISTA_PROD:
            DF1=DB_PROD_UF1[((DB_PROD_UF1['PRODT']==LP))]
            soma1=DF1["quant"].sum()
            DF2=DB_PROD_UF2[((DB_PROD_UF2['PRODT']==LP))]
            soma2=DF2["quant"].sum()
            for ff in LISTA_REG_UF:
                DF1=DB_PROD_UF1[((DB_PROD_UF1['CODUF']==int(ff)) &
                                 (DB_PROD_UF1['PRODT']==LP))]
                x1,y1=(DF1.shape)
                DF2=DB_PROD_UF2[((DB_PROD_UF2['CODUF']==int(ff)) &
                                 (DB_PROD_UF2['PRODT']==LP))]
                x2,y2=(DF2.shape)
                perc,prod1,prod2=self.PROCUF(DF1,DF2)
                try:
                    varbr1=str(round(float(prod1)/float(soma1)*100,4))
                    varbr2=str(round(float(prod2)/float(soma2)*100,4))
                except:
                    varbr1="-"
                    varbr2="-"
                lista_uf_prod.append([ff,LP,perc,varbr1,prod1,varbr2,prod2])
            try:
                percbr=str(round((float(soma1)/float(soma2)-1)*100,4))
            except:
                print(LP,soma1,soma2)
            lista_br_prod.append([LP,soma1,soma2,percbr])
        DFUF=pd.DataFrame(lista_uf_prod,columns=["uf","prod","var","per","quant","per_ant","quant_ant"])
        DFBR=pd.DataFrame(lista_br_prod,columns=["prod","BRA","BRANT","per"])
##        for ll in lista_uf_prod:
##            print(ll)
##        for ll in lista_br_prod:
##            print(ll)        
        DFUF.to_json(self.dirpath+"\\programa\\provisórios\\produto_UF.json",orient="records")
        DFBR.to_json(self.dirpath+"\\programa\\provisórios\\produto_BR.json",orient="records")
        DB_MUN_SQL=DB_ATUAL[["V4_x","V5_x","V6","V9"]]
        sql_query="select V4_x,sum(V5_x) as V5_x,"
        sql_query+="V6,V9 from MUNIC group by V4_x,V6,V9"
        DB_MUN=DFSQL(DB_MUN_SQL,sql_query,"MUNIC")
        #print(DB_MUN.shape)
        DB_MUN=DB_MUN.rename(columns = {"V4_x":"produto",
                                       "V5_x":"produc",
                                       "V6":"coduf"})
        #print(DB_MUN.shape)
        DB_MUN["CODMUN"]=""
        
        for x,y in DB_MUN.iterrows():
            comp=len(str(y["V9"]))
            cod=str(y["coduf"])+(5-comp)*"0"+str(y["V9"])
            DB_MUN.at[x,"CODMUN"]=cod
        DB_MUN2=DB_MUN[["produto","produc","coduf","CODMUN"]]    
        DB_MUN2.to_json(self.dirpath+"\\programa\\provisórios\\produto_mun.json",orient="records")
        

       
      def ATUAL(self,arqe,arqp):
        
        DBE=pd.read_csv(arqe,sep=";",
                                 encoding = "ISO-8859-1",header=None)

        DBP=pd.read_csv(arqp,sep=";",
                                 encoding = "ISO-8859-1",header=None)
 
        tam=(DBE.shape)
 
        temp=[]
        for i in range(1,tam[1]+1):
            temp.append("V"+str(i))

        DBE.columns = temp
        self.DBCOL=DBE

 
        DBE_ATIVO=self.DBCOL[((self.DBCOL['V1']==int(self.ano)) &
                         (self.DBCOL['V2']==self.sem) &
                         (self.DBCOL['V23']=='Ativo'))]

        DBP=pd.read_csv(arqp,sep=";",
                                 encoding = "ISO-8859-1",header=None)
 
        tam=(DBP.shape)
 
        temp=[]
        for i in range(1,tam[1]+1):
            temp.append("V"+str(i))

        DBP.columns = temp
        self.DBCOL=DBP

 
        DBP_ATIVO=self.DBCOL[((self.DBCOL['V1']==int(self.ano)) &
                         (self.DBCOL['V2']==self.sem))]


        DBmerge=pd.merge(DBP_ATIVO,DBE_ATIVO,on="V3",how="left")

        #print(DBmerge.shape)
        #print(DBmerge.columns)
        return(DBmerge)

      def ANTERIOR(self,arqe,arqp):
        
        DBE=pd.read_csv(arqe,sep=";",
                                 encoding = "ISO-8859-1",header=None)

        DBP=pd.read_csv(arqp,sep=";",
                                 encoding = "ISO-8859-1",header=None)
 
        tam=(DBE.shape)
 
        temp=[]
        for i in range(1,tam[1]+1):
            temp.append("V"+str(i))

        DBE.columns = temp
        self.DBCOL=DBE

 
        DBE_ATIVO=self.DBCOL[((self.DBCOL['V1']==(int(self.ano)-1)) &
                         (self.DBCOL['V2']==self.sem) &
                         (self.DBCOL['V23']=='Ativo'))]

        DBP=pd.read_csv(arqp,sep=";",
                                 encoding = "ISO-8859-1",header=None)
 
        tam=(DBP.shape)
 
        temp=[]
        for i in range(1,tam[1]+1):
            temp.append("V"+str(i))

        DBP.columns = temp
        self.DBCOL=DBP

 
        DBP_ATIVO=self.DBCOL[((self.DBCOL['V1']==(int(self.ano)-1)) &
                         (self.DBCOL['V2']==self.sem))]


        DBmerge=pd.merge(DBP_ATIVO,DBE_ATIVO,on="V3",how="left")

        #print(DBmerge.shape)
        #print(DBmerge.columns)
        return(DBmerge)
    
      def PRODUTOxUF(self,DF):
          conn=sqlite3.connect('produto')
          DF.to_sql("tabela",conn,if_exists='replace',index=False)
          conn.close()

          conn=sqlite3.connect('produto')
          selecao="select v6 as CODUF,v7 as SIGLAUF,v4_x as PRODT,sum(v5_x) as quant from tabela "
          selecao+="group by v6,v7,v4_x"
          DFS=pd.read_sql_query(selecao,conn)
          conn.close()

          return(DFS)
        
      def PROCUF(self,DFA,DFB):
          var1=0
          var2=0
          for x,y in DFA.iterrows():
              var1=float(y["quant"])
          for x,y in DFB.iterrows():
              var2=float(y["quant"])
          #print(var1,var2)
          try:
                temp=str(round(((float(var1)-float(var2))/float(var2))*100,4))
          except:
                temp="-"
          
          return(temp,var1,var2)

    
      def cafe(self,DF,LUF):
          lcafe=['Café Arábica (em grão)',
                 'Café Canephora (em grão)']
          DF0=DF[(DF["V4_x"]==lcafe[0])]
          DF1=DF[(DF["V4_x"]==lcafe[1])]
          for x,y in DF0.iterrows():
              DF0.at[x,"V4_x"]="Café (em grão)"
          for x,y in DF1.iterrows():
              DF1.at[x,"V4_x"]="Café (em grão)"
          DF_CONCAT=pd.concat([DF0,DF1])
          #print(DF0.columns)
          #print(DF1.columns)
          #print(DF_CONCAT.columns)
          #print(DF0.shape)
          #print(DF1.shape)
          #print(DF_CONCAT.shape)

          conn=sqlite3.connect("cafe.db")
          DF_CONCAT.to_sql("PROD",conn,if_exists="replace",index=False)
          conn.close()

          conn=sqlite3.connect("cafe.db")
          sql_query="select V1_x, V2_x, V3, V4_x, sum(V5_x) as V5_x, V1_y, V2_y, V4_y, V5_y,"
          sql_query+="V6, V7, V8, V9, V10, V11, V12, V13, V14, V15, V16,"
          sql_query+="V17, V18, sum(V19) as V19, sum(V20) as V20, sum(V21) as V21, V22, V23, V24 from PROD group by V3"
          DF_CAFE=pd.read_sql_query(sql_query,conn)
          conn.close()
          #print(DF_CAFE.columns)
          #print(DF_CAFE.shape)
          sum0=DF0["V5_x"].sum()
          sum1=DF1["V5_x"].sum()
          sumt=DF_CAFE["V5_x"].sum()
          sum10=sum0+sum1
          #print(sum0,sum1,sum10,sumt,sep="--")
          somabr0=0
          somabr1=0
          somabrc=0
          somabr10=0
          for luf in LUF:
              DUF0=DF0[(DF0["V6"]==int(luf))]
              DUF1=DF1[(DF1["V6"]==int(luf))]
              DUF_CAFE=DF_CAFE[(DF_CAFE["V6"]==int(luf))]
              sum0=DUF0["V5_x"].sum()
              somabr0+=sum0
              sum1=DUF1["V5_x"].sum()
              somabr1+=sum1
              sumt=DUF_CAFE["V5_x"].sum()
              somabrc+=sumt
              sum10=sum0+sum1
              somabr10+=sum10
              #print(sum0,sum1,sum10,sumt,sep="--")
          #print(somabr0,somabr1,somabr10,somabrc,sep="--")
          return(DF_CAFE)

      def feijao(self,DF,LUF):
          lfeijao=['Feijão Preto (em grão)',
                 'Feijão de Cor (em grão)']
          DF0=DF[(DF["V4_x"]==lfeijao[0])]
          DF1=DF[(DF["V4_x"]==lfeijao[1])]
          for x,y in DF0.iterrows():
              DF0.at[x,"V4_x"]="Feijão (em grão)"
          for x,y in DF1.iterrows():
              DF1.at[x,"V4_x"]="Feijão (em grão)"
          DF_CONCAT=pd.concat([DF0,DF1])
          #print(DF0.columns)
          #print(DF1.columns)
          #print(DF_CONCAT.columns)
          #print(DF0.shape)
          #print(DF1.shape)
          #print(DF_CONCAT.shape)

          conn=sqlite3.connect("feijao.db")
          DF_CONCAT.to_sql("PROD",conn,if_exists="replace",index=False)
          conn.close()

          conn=sqlite3.connect("feijao.db")
          sql_query="select V1_x, V2_x, V3, V4_x, sum(V5_x) as V5_x, V1_y, V2_y, V4_y, V5_y,"
          sql_query+="V6, V7, V8, V9, V10, V11, V12, V13, V14, V15, V16,"
          sql_query+="V17, V18, sum(V19) as V19, sum(V20) as V20, sum(V21) as V21, V22, V23, V24 from PROD group by V3"
          DF_FEIJAO=pd.read_sql_query(sql_query,conn)
          conn.close()
          #print(DF_FEIJAO.columns)
          #print(DF_FEIJAO.shape)
          sum0=DF0["V5_x"].sum()
          sum1=DF1["V5_x"].sum()
          sumt=DF_FEIJAO["V5_x"].sum()
          sum10=sum0+sum1
          #print(sum0,sum1,sum10,sumt,sep="--")
          somabr0=0
          somabr1=0
          somabrc=0
          somabr10=0
          for luf in LUF:
              DUF0=DF0[(DF0["V6"]==int(luf))]
              DUF1=DF1[(DF1["V6"]==int(luf))]
              DUF_FEIJAO=DF_FEIJAO[(DF_FEIJAO["V6"]==int(luf))]
              sum0=DUF0["V5_x"].sum()
              somabr0+=sum0
              sum1=DUF1["V5_x"].sum()
              somabr1+=sum1
              sumt=DUF_FEIJAO["V5_x"].sum()
              somabrc+=sumt
              sum10=sum0+sum1
              somabr10+=sum10
              #print(sum0,sum1,sum10,sumt,sep="--")
          #print(somabr0,somabr1,somabr10,somabrc,sep="--")
          return(DF_FEIJAO)
          
          
          
