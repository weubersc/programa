import pandas as pd
import os
import chardet

class ARQCSVUF():
    def __init__(self):
       self.dirpath=os.getcwd()
       self.ESTAB=(self.dirpath+"\\programa\\arquivos\\ESTAB.csv")
       self.PROD=(self.dirpath+"\\programa\\arquivos\\PROD.csv")
       self.PERG=(self.dirpath+"\\programa\\arquivos\\PERG.csv")
       print("OK")
#       self.filtercsv(2018,1,["V15","V16"])

    def pdcsv(self,arq):

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

   

    def filtercsv(self,ano,sem,lista,situa,cuf):
        print(type(ano))
        print(type(sem))
        print(type(cuf))
        print("FILTRO")
        if situa==1:
            PROV=self.DBCOL[((self.DBCOL['V1']==int(ano)) &
                         (self.DBCOL['V2']==sem) & 
                         (self.DBCOL['V6']==int(cuf)) &
                         (self.DBCOL['V23']=='Ativo'))]
        if situa==0:
             PROV=self.DBCOL[((self.DBCOL['V1']==int(ano)) &
                         (self.DBCOL['V2']==sem))]
        if situa==2:
             print(self.DBCOL["V23"].unique())
             PROV=self.DBCOL[((self.DBCOL['V1']==int(ano)) &
                         (self.DBCOL['V2']==sem) & 
                         (self.DBCOL['V23']=='Paralisado') &
                          (self.DBCOL['V6']==int(cuf)))]
        self.LL=PROV[lista]
        gg=self.LL.values.tolist()
        return(gg)


    def Merge_ESTAB_PROD(self,arq1,arq2,ano,sem):
        self.pdcsv(arq1)
        DB1A=self.DBCOL
        DB1=DB1A[((DB1A['V1']==int(ano)) &
                         (DB1A['V2']==sem))]
        print(DB1.head())

#        DB1.rename(columns={'V3':'COD_IBGE'}, inplace=True)
        self.pdcsv(arq2)
        DB2A=self.DBCOL
        DB2=DB2A[((DB2A['V1']==int(ano)) &
                         (DB2A['V2']==sem) & 
                         (DB2A['V23']=='Ativo')) ]
 
        print( DB2.head())
#        DB2.rename(columns={'V3':'COD_IBGE'}, inplace=True)
        DBM = pd.merge(DB1,DB2,left_on='V3', right_on='V3')
        print( DBM.head())
        print(DB1["V3"].count(),DB2["V3"].count(),DBM["V3"].count())
        print("--------")
        
        return(DBM,DB1,DB2)
    
                        
       
if __name__=="__main__":
    ARQCSVUF()       
      
