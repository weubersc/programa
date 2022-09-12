from programa.modulos.apuracao.estoque_TAB_UF import gerar_tabela as GERATAB
from programa.modulos.apuracao.PREPARAR_LISTA_UF import MONTAR_LISTA as PREPARO

class PROCESSAMENTO:

    def __init__(self,CUF,semes,ano):
        self.PREP=PREPARO(CUF,semes,ano)
        self.semes=semes
        self.ano=int(ano)
        self.cuf=CUF

 

    def TABPROC12(self,LTAB1,LTAB2):
        self.PREP.empresa()
        LISTAB1=self.PREP.ROT1(LTAB1)
        self.PREP.atividade()
        LISTAB2=self.PREP.ROT2(LTAB2)
        TT12=GERATAB(self.semes,self.ano,self.cuf)
        TT12.TAB12(LISTAB1,LISTAB2)

    def TABPROC34(self,LTAB3,LTAB4):
        self.PREP.faixa1()
        LISTATAB3=self.PREP.ROT3(LTAB3)
        self.PREP.faixa2()
        LISTATAB4=self.PREP.ROT4(LTAB4)
        TT34=GERATAB(self.semes,self.ano,self.cuf)
        TT34.TAB34(LISTATAB3,LISTATAB4)

    def TABPROC5(self,LTAB5):
        LISTATAB5=self.PREP.ROT5(LTAB5)
        TT5=GERATAB(self.semes,self.ano,self.cuf)
        TT5.TAB5(LISTATAB5)

    def TABPROC6(self,LTAB6):
        self.PREP.produtos(LTAB6,"emp")
        self.PREP.ROT6()

    def TABPROC7(self,LTAB7):
        self.PREP.produtos(LTAB7,"ativ")
        self.PREP.ROT7()
        
    def TABPROC8(self,LTAB8):
        self.PREP.REGUF(LTAB8)
        LISTATAB8,LISTA_ESPACO=self.PREP.ROT89("emp")
##        for LL in LISTATAB8:
##            print(LL)
##        for LL,item in LISTA_ESPACO.items():
##            print(LL,item)
##        exit()
        TT8=GERATAB(self.semes,self.ano,self.cuf)
        TT8.TAB89(LISTATAB8,LISTA_ESPACO,"emp")

        
    def TABPROC9(self,LTAB9):
        self.PREP.REGUF(LTAB9)
        LISTATAB9,LISTA_ESPACO=self.PREP.ROT89("ativ")
        TT9=GERATAB(self.semes,self.ano,self.cuf)
        TT9.TAB89(LISTATAB9,LISTA_ESPACO,"ativ")

    def TABPROC10(self,LTAB10):
        self.PREP.REGUF10(LTAB10)
        LISTATAB10,LISTA_ESPACO=self.PREP.ROT10()
        TT10=GERATAB(self.semes,self.ano,self.cuf)
        TT10.TAB10(LISTATAB10,LISTA_ESPACO)

    def TABPROC11(self,LTAB11):
        self.PREP.REG11(LTAB11)
        self.PREP.ROT11()


    def TABPROC12B(self,LTAB12):
        LISTATAB12=self.PREP.ROT12(LTAB12)
        TT12=GERATAB(self.semes,self.ano,self.cuf)
        TT12.TAB12B(LISTATAB12)
