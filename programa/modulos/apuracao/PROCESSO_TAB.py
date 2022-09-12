from programa.modulos.apuracao.estoque_TAB_BR import gerar_tabela as GERATAB
from programa.modulos.apuracao.PREPARAR_LISTA import MONTAR_LISTA as PREPARO
from listtocsv import listacsv as SAIDA

class PROCESSAMENTO:

    def __init__(self,ano,sem):
        print("-----"+str(ano)+"----"+str(sem))
        self.ano=ano
        self.sem=sem
        self.PREP=PREPARO(self.ano,self.sem)

        
    def TABPROC12(self,LTAB1,LTAB2):
        self.PREP.empresa()
        LISTAB1=self.PREP.ROT1(LTAB1)
        self.PREP.atividade()
        LISTAB2=self.PREP.ROT2(LTAB2)
        TT12=GERATAB(self.sem,self.ano)
        TT12.TAB12(LISTAB1,LISTAB2)

    def TABPROC34(self,LTAB3,LTAB4):
        self.PREP.faixa1()
        LISTATAB3=self.PREP.ROT3(LTAB3)
        self.PREP.faixa2()
        LISTATAB4=self.PREP.ROT4(LTAB4)
        TT34=GERATAB(self.sem,self.ano)
        TT34.TAB34(LISTATAB3,LISTATAB4)

    def TABPROC5(self,LTAB5):
        LISTATAB5=self.PREP.ROT5(LTAB5)
        TT5=GERATAB(self.sem,self.ano)
        SAIDA(LISTATAB5,"tabela5.csv",";")
        TT5.TAB5(LISTATAB5)
    


    def TABPROC6(self,LTAB6):
        self.PREP.produtos(LTAB6,"emp")
        self.PREP.ROT6()

    def TABPROC7(self,LTAB7):
        self.PREP.produtos(LTAB7,"ativ")
        self.PREP.ROT7()
        
    def TABPROC8(self,LTAB8):
        self.PREP.REGUF(LTAB8)
        LISTATAB8=self.PREP.ROT89("emp")
        TT8=GERATAB(self.sem,self.ano)
        TT8.TAB89(LISTATAB8,"emp")
        
    def TABPROC9(self,LTAB9):
        self.PREP.REGUF(LTAB9)
        LISTATAB9=self.PREP.ROT89("ativ")
        TT9=GERATAB(self.sem,self.ano)
        TT9.TAB89(LISTATAB9,"ativ")

    def TABPROC10(self,LTAB10):
        self.PREP.REGUF10(LTAB10)
        LISTATAB10=self.PREP.ROT10()
        TT10=GERATAB(self.sem,self.ano)
        TT10.TAB10(LISTATAB10)

    def TABPROC11(self,LTAB11):
        self.PREP.REG11(LTAB11)
        LISTATAB11=self.PREP.ROT11()

    def TABPROC12B(self,LTAB12):
        print("FIM DA PROG.")
        LISTATAB12=self.PREP.ROT12(LTAB12)
        TT12=GERATAB(self.sem,self.ano)
        TT12.TAB12B(LISTATAB12)
