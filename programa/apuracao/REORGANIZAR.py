import pandas as pd

class FORMATAR():

    def __init__(self,LISTA):

        self.lista=LISTA
        self.GRUPO=[]
        self.GRUPO.append(['Algodão (em pluma)',
                 'Algodão (em caroço)',
                 'Caroço de Algodão'
                 ])
        self.GRUPO.append(['Semente de Algodão',
                 'Arroz (em casca)',
                 'Arroz Beneficiado'
                 ])
        self.GRUPO.append(['Semente de Arroz',
                 'Café Arábica (em grão)',
                 'Café Canephora (em grão)'])
        self.GRUPO.append(['Feijão Preto (em grão)',
                 'Feijão de Cor (em grão)',
                 'Milho (em grão)'])

        self.GRUPO.append(['Semente de Milho',
                           'Soja (em grão)',
                             'Semente de Soja'])
        self.GRUPO.append(['Trigo (em grão)',
                 'Semente de Trigo',
                 'Outros Grãos e Sementes'])

    def TRANSFORMAR(self):
        
        dBTRANS = pd.DataFrame(self.lista,columns = ['v1','v2','v3','v4','v5'])
        tam=(dBTRANS.shape)
        print(tam)
        temp=[]

##        for index, row in dBTRANS.iterrows():
##            print(row[0],row[1])
        for gr in self.GRUPO:
            GRUPO1=gr
            print(GRUPO1)
            DBGRUPO1=dBTRANS[(dBTRANS['v1']==GRUPO1[0])|(dBTRANS['v1']==GRUPO1[1])|
                             (dBTRANS['v1']==GRUPO1[2])]
            tam=(DBGRUPO1.shape)
            print(tam)
            DBMUN=dBTRANS["v3"].unique()
        for index, row in DBGRUPO1.iterrows():
                print(row[0],row[2])


       


        

                
            
        

if __name__=="__main__":
    LISTA=[0,0]
    FORMATAR(LISTA) 
