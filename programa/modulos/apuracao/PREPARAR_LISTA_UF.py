from programa.modulos.apuracao.estoque_TAB_UF import gerar_tabela as GERATAB
from programa.modulos.apuracao.FORMATO_NUMERO import inteiro as formato
from programa.modulos.apuracao.FORMATO_NUMERO import flutuante as tonelada
from programa.modulos.apuracao.INVERSAO import INVERTER
from programa.modulos.apuracao.INVERSAO import FORMATAR
import pandas as pd
from códigos import Codigos as COD
from programa.modulos.apuracao.formatlista_uf import FORMATAR_LISTA as FORTRACO
from listtocsv import listacsv as SAIDA
from programa.modulos.apuracao.limador import corretor as CORLIM

class MONTAR_LISTA():

    def __init__(self,NUF,semes,ano):
        self.ano=ano
        DATA1="30/06/"+str(self.ano)
        DATA2="31/12/"+str(self.ano)
        if semes==1:
            self.DATA=DATA1
        if semes==2:
            self.DATA=DATA2
        self.emp={}
        self.cuf=NUF
        self.semes=semes
        self.ativ={}
        self.fx1={}
        self.fx2={}
        self.lista_chave=[]
        CC=COD()
        self.ufnome=CC.codigo
        self.nomeuf=self.ufnome[NUF]
        #print(self.nomeuf)
        self.prod=['Algodão (em pluma)',
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
         'Outros Grãos e Sementes']
        self.prod2=['Algodão \n (em pluma)',
         'Algodão \n (em caroço)',
         'Caroço de \n  Algodão',
         'Semente de \n Algodão',
         'Arroz \n (em casca)',
         'Arroz \n Beneficiado',
         'Semente de \n Arroz',
         'Café Arábica \n (em grão)',
         'Café Canephora \n (em grão)',
         'Feijão Preto \n (em grão)',
         'Feijão de Cor \n (em grão)',
         'Milho \n (em grão)',
         'Semente de \n Milho',
         'Soja \n (em grão)',
         'Semente de \n Soja',
         'Trigo \n (em grão)',
         'Semente de \n Trigo',
         'Outros Grãos e \n Sementes']
        self.tab6_inv=[]
#        self.empresa()
#        self.ROT1()
##        self.faixa1()
##        self.ROT3()
        
    def empresa(self):
        lista_emp=[0,1,2,3,4]
        lista_rot=["     Total",
                   "Governo",
                   "Iniciativa Privada\n(exceto cooperativa)",
                   "Cooperativa",
                   "Economia Mista"]
        il=0
        for e in lista_emp:
            self.emp[e]=lista_rot[il]
            il+=1

    def atividade(self):
        lista_ativ=[0,1,2,3,4]
        lista_rot=["      Total",
                   "Comércio \n (exceto supermercado)",
                   "Indústria",
                   "Serviço de Armazenagem",
                   "Produção Agropecuária"]
        il=0
        for a in lista_ativ:
            self.ativ[a]=lista_rot[il]
            il+=1
            
    def faixa1(self):
        lista_fx1=[0,1,2,3,4,5,6,7]
        lista_rot=["      Total",
                   "Menos de 2 000",
                   "2 000 a menos de 5 000",
                   "5 000 a menos de 10 000",
                   "10 000 a menos de 50 000",
                   "50 000 a menos de 100 000",
                   "100 000 a menos de 200 000",
                   "200 000 e mais"]
        il=0
        for x1 in lista_fx1:
            self.fx1[x1]=lista_rot[il]
            il+=1
        #print(self.fx1)

    def faixa2(self):
        lista_fx2=[0,1,2,3,4,5,6,7]
        lista_rot=["      Total",
                   "Menos de 1 200",
                   "1 200 a menos de 5 000",
                   "5 000 a menos de 10 000",
                   "10 000 a menos de 50 000",
                   "50 000 a menos de 100 000",
                   "100 000 a menos de 200 000",
                   "200 000 e mais"]
        il=0
        for x2 in lista_fx2:
            self.fx2[x2]=lista_rot[il]
            il+=1
        #print(self.fx2)

    def produtos(self,listad,tipo):
        self.empresa()
        self.atividade()

        if tipo=="emp":
            temporario=INVERTER(listad,self.prod,self.emp)
            self.tab6_inv=FORMATAR(temporario,self.prod,self.emp,12)

        if tipo=="ativ":
            temporario=INVERTER(listad,self.prod,self.ativ)
            self.tab7_inv=FORMATAR(temporario,self.prod,self.ativ,12)        


##        for inv in self.tab6_inv:
##            for ix in inv:
##                for bb in ix:
##                    print(bb)
            

    def REGUF(self,lista):
        self.lista89=[]
        self.nomereg={}
        for ll in lista:
            temp=[]
            espaco=""
            self.nomereg[ll[1]]=ll[0]
            if ll[0]==0:
                espaco="     "
                temp.append(espaco+"     "+ll[1])
                temp.append(formato(ll[2]))
            if ll[0]==1:
                espaco=""
                temp.append(ll[1])
                temp.append(formato(ll[2]))
            if ll[0]==2:
                espaco="  "
                temp.append(espaco+ll[1])
                temp.append(formato(ll[2]))
            if ll[0]==3:
                espaco="      "
                temp.append(espaco+ll[1])
                temp.append(formato(ll[2]))
            for lz in ll[3]:
                temp.append(formato(lz))
            self.lista89.append(temp)

    def REGUF10(self,lista):
        self.lista10=[]
        self.nomereg={}
        for ll in lista:
            temp=[]
            espaco=""
            self.nomereg[ll[1]]=ll[0]
            if ll[0]==0:
                espaco="     "
                temp.append(espaco+"     "+ll[1])
                temp.append(formato(ll[2]))
            if ll[0]==1:
                espaco=""
                temp.append(ll[1])
                temp.append(formato(ll[2]))
            if ll[0]==2:
                espaco="  "
                temp.append(espaco+ll[1])
                temp.append(formato(ll[2]))
            if ll[0]==3:
                espaco="      "
                temp.append(espaco+ll[1])
                temp.append(formato(ll[2]))
            for lz in ll[3]:
                for lw in lz:
                    temp.append(formato(lw))
            self.lista10.append(temp)

##        for ll in self.lista10:
##            print(ll)

    def REG11(self,lista):
        servico=lista[:]
        self.lista11=[]
        self.nomereg={}
        provisorio=[]
        for ll in servico:
            temp=[]
            espaco=""
            self.nomereg[ll[1]]=ll[0]
            if str(ll[0])=="0":
                espaco="     "
                temp.append(espaco+"     "+ll[1])
            if ll[0]=="MESO":
                espaco=""
                temp.append(ll[1])
            if ll[0]=="MICRO":
                espaco="  "
                temp.append(espaco+ll[1])
            if ll[0]=="MUNIC":
                espaco="      "
                temp.append(espaco+ll[1])
            for lz in ll[2]:
                    temp.append(formato(lz[0]))
                    temp.append(tonelada(lz[1]))
            provisorio.append(temp)
        #print(len(provisorio[0]))
        #print(provisorio[0])
        lista_prov1=[]
        lista_prov2=[]
        lista_prov3=[]
        for pp in provisorio:
            lista_prov1.append([pp[0],pp[1],pp[2],pp[3],pp[4],pp[5],pp[6],
                                pp[7],pp[8],pp[9],pp[10],pp[11],pp[12]])
            lista_prov2.append([pp[0],pp[13],pp[14],pp[15],pp[16],pp[17],pp[18],
                                pp[19],pp[20],pp[21],pp[22],pp[23],pp[24]])
            lista_prov3.append([pp[0],pp[25],pp[26],pp[27],pp[28],pp[29],pp[30],
                                pp[31],pp[32],pp[33],pp[34],pp[35],pp[36]])
        self.lista11.append(lista_prov1)
        self.lista11.append(lista_prov2)
        self.lista11.append(lista_prov3)
##        K=1
##        for ss in self.lista11:
##            print(K)
##            print(len(ss))
##            print("--------------")
##            K=K+1
##        exit()
            



    
        



    def ROT1(self,listad):
        LINHA1=["Pesquisa de Estoques - "+str(self.semes)+"º semestre de "+ str(self.ano) +" - "+self.nomeuf,
                "","","","","","",""]
        string="1. Unidades Armazenadoras, com indicação do número de informantes e capacidade útil \n"
        string+=" dos armazéns e dos silos, segundo os tipos de propriedade da empresa"
        LINHA2=[string,"","","","","","",""]
        
        LINHA3=["Tipos de \n propriedade \n da \n empresa",
                "Total de \n  estabele- \n cimentos",
                "Unidades armazenadoras","","","","",""]
        #print(len( LINHA3))
        LINHA4=["","","Armazéns convencionais, \n estruturais e infláveis",
                "","Armazéns graneleiros  \n e granelizados","","Silos",""]
        LINHA5=["","","Número \n  de \n  informantes",
                "Capacidade \n  útil \n  (m³)",
                "Número \n  de \n  informantes",
                "Capacidade \n  útil \n  (t)",
                "Número \n  de \n  informantes",
                "Capacidade \n  útil \n  (t)"]
        FONTE="Fonte: IBGE, Diretoria de Pesquisas, Coordenação de Estatísticas Agropecuárias, "
        FONTE=FONTE+"Pesquisa de Estoques "+str(self.semes)+"º semestre de "+ str(self.ano)
        LINHAF=[FONTE,"","","","","","",""]
        LISTA=[]
        LISTA.append(LINHA1)
        LISTA.append(LINHA2)
        LISTA.append(LINHA3)
        LISTA.append(LINHA4)
        LISTA.append(LINHA5)
        FTRACO=FORTRACO(listad)
        lista_f=FTRACO.TRACO()  
        for ld in lista_f:
            temp=[]
            temp.append(self.emp[ld[0]])
            for j in range(1,len(ld)):
                temp.append(formato(ld[j]))
            LISTA.append(temp)
        LISTA.append(LINHAF)
        print("----")
        for lk in LISTA:
            print(lk)
        print("----")
        return(LISTA)

 
    def ROT2(self,listad):
        LINHA1=["Pesquisa de Estoques - "+str(self.semes)+"º semestre de "+ str(self.ano) +" - "+self.nomeuf,
                "","","","","","",""]
        string="2. Unidades Armazenadoras, com indicação do número de informantes e capacidade útil \n"
        string+=" dos armazéns e dos silos, segundo os tipos de atividade do estabelecimento"
        LINHA2=[string,"","","","","","",""]
        
        LINHA3=["Tipos de \n atividade \n do \n estabelecimento",
                "Total de \n  estabele- \n cimentos",
                "Unidades armazenadoras","","","","",""]
        #print(len( LINHA3))
        LINHA4=["","","Armazéns convencionais, \n estruturais e infláveis",
                "","Armazéns graneleiros  \n e granelizados","","Silos",""]
        LINHA5=["","","Número \n  de \n  informantes",
                "Capacidade \n  útil \n  (m³)",
                "Número \n  de \n  informantes",
                "Capacidade \n  útil \n  (t)",
                "Número \n  de \n  informantes",
                "Capacidade \n  útil \n  (t)"]
        FONTE="Fonte: IBGE, Diretoria de Pesquisas, Coordenação de Estatísticas Agropecuárias, "
        FONTE=FONTE+"Pesquisa de Estoques "+str(self.semes)+"º semestre de "+ str(self.ano)
        LINHAF=[FONTE,"","","","","","",""]
        LISTA=[]
        LISTA.append(LINHA1)
        LISTA.append(LINHA2)
        LISTA.append(LINHA3)
        LISTA.append(LINHA4)
        LISTA.append(LINHA5)
        FTRACO=FORTRACO(listad)
        lista_f=FTRACO.TRACO()
        for ld in lista_f:
            temp=[]
            if ld[0]!=5:
                temp.append(self.ativ[ld[0]])
                for j in range(1,len(ld)):
                    temp.append(formato(ld[j]))
                LISTA.append(temp)

        LISTA.append(LINHAF)
##        for lk in LISTA:
##            print(lk)
        return(LISTA)

    def ROT3(self,listad):
        LINHA1=["Pesquisa de Estoques - "+str(self.semes)+"º semestre de "+ str(self.ano) +" - "+self.nomeuf,
                "",""]
        string="3. Armazéns convencionais, estruturais e infláveis com indicação do número de \n"
        string+="estabelecimentos e capacidade útil, segundo os grupos de capacidade útil"
        LINHA2=[string,"",""]
        
        LINHA3=["Grupos de capacidade útil \n (m³)",
                "Armazéns convencionais, estruturais e infláveis",
                ""]
        
        #print(len( LINHA3))
        LINHA4=["","Número de estabelecimentos",
                 "Capacidade útil  \n (m³)"]
        
        FONTE="Fonte: IBGE, Diretoria de Pesquisas, Coordenação de Estatísticas Agropecuárias, "
        FONTE=FONTE+"Pesquisa de Estoques "+str(self.semes)+"º semestre de "+ str(self.ano)
        LINHAF=[FONTE,"",""]
        LISTA=[]
        LISTA.append(LINHA1)
        LISTA.append(LINHA2)
        LISTA.append(LINHA3)
        LISTA.append(LINHA4)
        FTRACO=FORTRACO(listad)
        lista_f=FTRACO.TRACO()
        for ld in lista_f:
            temp=[]
            temp.append(self.fx1[ld[0]])
            for j in range(1,len(ld)):
                temp.append(formato(ld[j]))
            LISTA.append(temp)

        LISTA.append(LINHAF)
##        for lk in LISTA:
##            print(lk)
        return(LISTA)

    def ROT4(self,listad):
        LINHA1=["Pesquisa de Estoques - "+str(self.semes)+"º semestre de "+ str(self.ano) +" - "+self.nomeuf,
                "","","","","",""]
        string="4. Armazéns e silos para produtos a granel, com indicação do número de informantes\n"
        string+="e capacidade útil, segundo os grupos de capacidade útil"
        LINHA2=[string,"","","","","",""]
        
        LINHA3=["Grupos de \n capacidade útil \n (m³)",
                "Armazéns e silos para produtos a granel",
                "","","","",""]
        #print(len( LINHA3))
        LINHA4=["","Total","",
                "Armazéns \n graneleiros e granelizados","",
                "Silos",""]
        LINHA5=["","Número \n de \n informantes",
                 "Capacidade útil  \n (t)",
                "Número \n de \n informantes",
                 "Capacidade útil  \n (t)",
                "Número \n de \n informantes",
                 "Capacidade útil  \n (t)"]
        
        FONTE="Fonte: IBGE, Diretoria de Pesquisas, Coordenação de Estatísticas Agropecuárias, "
        FONTE=FONTE+"Pesquisa de Estoques "+str(self.semes)+"º semestre de "+ str(self.ano)
        LINHAF=[FONTE,"","","","","",""]
        LISTA=[]
        LISTA.append(LINHA1)
        LISTA.append(LINHA2)
        LISTA.append(LINHA3)
        LISTA.append(LINHA4)
        LISTA.append(LINHA5)        
        FTRACO=FORTRACO(listad)
        lista_f=FTRACO.TRACO()
        for ld in lista_f:
            temp=[]
            temp.append(self.fx2[ld[0]])
            for j in range(1,len(ld)):
                temp.append(formato(ld[j]))
            LISTA.append(temp)

        LISTA.append(LINHAF)
##        for lk in LISTA:
##            print(lk)
        return(LISTA) 

    def ROT5(self,listad):
        LINHA1=["Pesquisa de Estoques - "+str(self.semes)+"º semestre de "+ str(self.ano) +" - "+self.nomeuf,
                "","",""]
        string="5. Número de municípios, de informantes e estoque declarado em "+self.DATA+", \n"
        string+="segundo os produtos"
        LINHA2=[string,"","",""]
        
        LINHA3=["Produtos",
                "Número \n de \n municípios",
                "Número \n de \n informantes",
                "Estoque em "+self.DATA+" \n (t)"]
        
        #print(len( LINHA3))        
        FONTE="Fonte: IBGE, Diretoria de Pesquisas, Coordenação de Estatísticas Agropecuárias, "
        FONTE=FONTE+"Pesquisa de Estoques "+str(self.semes)+"º semestre de "+ str(self.ano) 
        LINHAF=[FONTE,"",""]
        LISTA=[]
        LISTA.append(LINHA1)
        LISTA.append(LINHA2)
        LISTA.append(LINHA3)
        FTRACO=FORTRACO(listad)
        lista_f=FTRACO.TRACO()
        lista_x=FTRACO.DESINT5()
        for ld in lista_x:
            temp=[]
            temp.append(ld[0])
            temp.append(formato(ld[1]))
            temp.append(formato(ld[2]))
            temp.append(tonelada(ld[3]))
            LISTA.append(temp)

        LISTA.append(LINHAF)
        for lk in LISTA:
            print(lk)
        return(LISTA)

    def ROT6(self):
        LINHA1=["Pesquisa de Estoques - "+str(self.semes)+"º semestre de "+ str(self.ano) +" - "+self.nomeuf,
                "","","","","","","","","","","",""]
        string="6. Produtos estocados, com indicação do número de informantes e da \n"
        string+="quantidade existente em "+self.DATA+", segundo os tipos de propriedade da empresa"
        LINHA2=[[string,"","","","","","","","","","","","(continua)"],
                [string,"","","","","","","","","","","","(conclusão)"]]
##        print("-----")
##        print(len(self.prod))
        LINHA3=[]
        for i in range(0,18,6):
            LINHA3.append(["Tipos de \n propriedade \n da \n empresa",self.prod[i],"",
                   self.prod[i+1],"",self.prod[i+2],"",
                   self.prod[i+3],"",
                   self.prod[i+4],"",
                   self.prod[i+5],""])
##        for kk in LINHA3:
##            print(kk)
        LINHA4=["","Número \n de \n informantes","Quantidade \n (t)",
                   "Número \n de \n informantes","Quantidade \n (t)",
                   "Número \n de \n informantes","Quantidade \n (t)",
                   "Número \n de \n informantes","Quantidade \n (t)",
                   "Número \n de \n informantes","Quantidade \n (t)",
                   "Número \n de \n informantes","Quantidade \n (t)"]
    
        FONTE="Fonte: IBGE, Diretoria de Pesquisas, Coordenação de Estatísticas Agropecuárias, "
        FONTE=FONTE+"Pesquisa de Estoques "+str(self.semes)+"º semestre de "+ str(self.ano)
        LINHAF=[FONTE,"","","","","","","","","","","",""]
        LISTA=[]
        for k in range(0,3):
            if k!=1:
                LISTA.append(LINHA1)
                if k==0:
                    LISTA.append(LINHA2[0])
                if k==2:
                    LISTA.append(LINHA2[1])
            LISTA.append(LINHA3[k])
            LISTA.append(LINHA4)
            FTRACO=FORTRACO(self.tab6_inv[k])
            lista_f=FTRACO.TRACO67()
            for y6 in lista_f:
                LISTA.append(y6)
            if k>0:    
                LISTA.append(LINHAF)
        for ll in LISTA:
            print(len(ll))
            print(ll)
        TT6=GERATAB(int(self.semes),int(self.ano),self.cuf)
        TT6.TAB6(LISTA,"emp")
            
    def ROT7(self):
        LINHA1=["Pesquisa de Estoques - "+str(self.semes)+"º semestre de "+ str(self.ano) +" - "+self.nomeuf,
                "","","","","","","","","","","",""]
        string="7. Produtos estocados, com indicação do número de informantes e da \n"
        string+="quantidade existente em "+self.DATA+", segundo os tipos de atividade do estabelecimento"
        LINHA2=[[string,"","","","","","","","","","","","(continua)"],
                [string,"","","","","","","","","","","","(conclusão)"]]
##        print("-----")
##        print(len(self.prod))
        LINHA3=[]
        for i in range(0,18,6):
            LINHA3.append(["Tipos de \n atividade do \n estabelecimento",self.prod[i],"",
                   self.prod[i+1],"",self.prod[i+2],"",
                   self.prod[i+3],"",
                   self.prod[i+4],"",
                   self.prod[i+5],""])
##        for kk in LINHA3:
##            print(kk)
        LINHA4=["","Número \n de \n informantes","Quantidade \n (t)",
                   "Número \n de \n informantes","Quantidade \n (t)",
                   "Número \n de \n informantes","Quantidade \n (t)",
                   "Número \n de \n informantes","Quantidade \n (t)",
                   "Número \n de \n informantes","Quantidade \n (t)",
                   "Número \n de \n informantes","Quantidade \n (t)"]
    
        FONTE="Fonte: IBGE, Diretoria de Pesquisas, Coordenação de Estatísticas Agropecuárias, "
        FONTE=FONTE+"Pesquisa de Estoques "+str(self.semes)+"º semestre de "+ str(self.ano)
        LINHAF=[FONTE,"","","","","","","","","","","",""]
        LISTA=[]
        for k in range(0,3):
            if k!=1:
                LISTA.append(LINHA1)
                if k==0:
                    LISTA.append(LINHA2[0])
                if k==2:
                    LISTA.append(LINHA2[1])
            LISTA.append(LINHA3[k])
            LISTA.append(LINHA4)
            FTRACO=FORTRACO(self.tab7_inv[k])
            lista_f=FTRACO.TRACO67()
            for y7 in lista_f:
                LISTA.append(y7)
            if k>0:    
                LISTA.append(LINHAF)
##        for ll in LISTA:
##            print(len(ll))
##            print(ll)
        TT7=GERATAB(int(self.semes),int(self.ano),self.cuf)
        TT7.TAB6(LISTA,"ativ")
            
    def ROT89(self,tipo):
        #TAMANHO DA LISTA PARA SE SABER O NÚMERO DE PÁGINAS"
        TAMANHO=len(self.lista89)
        NUMPAG=TAMANHO//38
##        print(TAMANHO,"___",NUMPAG)
        if NUMPAG==0:
            lista_ALT89,nomereg=self.ALT89(tipo)
            return(lista_ALT89,nomereg)
        else:
            lista_ALT89,nomereg=self.PAG89(tipo)
            return(lista_ALT89,nomereg)
 
    def PAG89(self,tipo):
       #TAMANHO DA LISTA PARA SE SABER O NÚMERO DE PÁGINAS"
        TAMANHO=len(self.lista89)
        NUMPAG=TAMANHO//38
##        print(TAMANHO,"___",NUMPAG)
        lista_saida_89=[]
        FTRACO=FORTRACO(self.lista89)
        lista_f=FTRACO.TRACO()
        for pag in range(0,NUMPAG):
            LINHA1=["Pesquisa de Estoques - "+str(self.semes)+"º semestre de "+ str(self.ano) +" - "+self.nomeuf,
                    "","","","",""]
            if tipo=="ativ":
                string="9. Estabelecimentos, por tipos de atividade, segundo\n"
                string+="as mesorregiões, as microrregiões e os municípios "
                LINHA2=[string,"","","","","(continua)"]
                LINHA3=["Mesorregiões, Microrregiões \n e \n Municípios","Estabelecimentos","","","",""]
                LINHA4=["","Total","Atividade do estabelecimento","","",""]
                LINHA5=["","","Comércio \n (exceto \n supermercado)","Indústria",
                        "Serviço de \n Armazenagem",
                        "Produção \n Agropecuária"]
            if tipo=="emp":
                string="8. Estabelecimentos, por tipos de propriedade da empresa, segundo \n"
                string+=" as mesorregiões, as microrregiões e os municípios"
                LINHA2=[string,"","","","","(continua)"]
                LINHA3=["Mesorregiões, Microrregiões \n e \n Municípios","Estabelecimentos","","","",""]
                LINHA4=["","Total","Propriedade da empresa","","",""]
                LINHA5=["","","Governo","Iniciativa \n Privada \n (exceto cooperativa)","Cooperativa",
                        "Economia \n Mista"]  

            LISTA=[]
            LISTA.append(LINHA1)
            LISTA.append(LINHA2)
            LISTA.append(LINHA3)
            LISTA.append(LINHA4)
            LISTA.append(LINHA5)
            for fatiar in range(pag*38,(pag+1)*38):
                if tipo=="emp":
                    LISTA.append(lista_f[fatiar])
                if tipo=="ativ":
                    transport=lista_f[fatiar][:]
                    lista_ativ=transport[0:6]
                    LISTA.append(lista_ativ)                
                N_prov=fatiar
            lista_saida_89.append(LISTA)
        LINHA1=["Pesquisa de Estoques - "+str(self.semes)+"º semestre de "+ str(self.ano) +" - "+self.nomeuf,
                "","","","",""]
        if tipo=="ativ":
                string="9. Estabelecimentos, por tipos de atividade, segundo\n"
                string+="as mesorregiões, as microrregiões e os municípios "
                LINHA2=[string,"","","","","(conclusão)"]
                LINHA3=["Mesorregiões, Microrregiões \n e \n Municípios","Estabelecimentos","","","",""]
                LINHA4=["","Total","Atividade do estabelecimento","","",""]
                LINHA5=["","","Comércio \n (exceto \n supermercado)","Indústria",
                        "Serviço de \n Armazenagem",
                        "Produção \n Agropecuária"]
        if tipo=="emp":
            string="8. Estabelecimentos, por tipos de propriedade da empresa, segundo \n"
            string+=" as mesorregiões, as microrregiões e os municípios"
            LINHA2=[string,"","","","","(conclusão)"]
            LINHA3=["Mesorregiões, Microrregiões \n e \n Municípios","Estabelecimentos","","","",""]
            LINHA4=["","Total","Propriedade da empresa","","",""]
            LINHA5=["","","Governo","Iniciativa \n Privada \n (exceto cooperativa)","Cooperativa",
                    "Economia \n Mista"]  
        LISTA=[]
        LISTA.append(LINHA1)
        LISTA.append(LINHA2)
        LISTA.append(LINHA3)
        LISTA.append(LINHA4)
        LISTA.append(LINHA5)
        for fatiar in range(N_prov+1,len(lista_f)):
            if tipo=="emp":
                    LISTA.append(lista_f[fatiar])
            if tipo=="ativ":
                    transport=lista_f[fatiar][:]
                    lista_ativ=transport[0:6]
                    LISTA.append(lista_ativ)    
        FONTE="Fonte: IBGE, Diretoria de Pesquisas, Coordenação de Estatísticas Agropecuárias, "
        FONTE=FONTE+"Pesquisa de Estoques "+str(self.semes)+"º semestre de "+ str(self.ano)
        LINHAF=[FONTE,"","","","",""]
        LISTA.append(LINHAF)
        lista_saida_89.append(LISTA)
##        for ll in lista_saida_89:
##            for xx in ll:
##                print(xx)
        return(lista_saida_89,self.nomereg)

    
    def ALT89(self,tipo):
        lista_saida_89=[]
        LINHA1=["Pesquisa de Estoques - "+str(self.semes)+"º semestre de "+ str(self.ano) +" - "+self.nomeuf,
                "","","","",""]
        if tipo=="ativ":
                string="       9. Estabelecimentos, por tipos de atividade, segundo\n"
                string+="     as mesorregiões, as microrregiões e os municípios "
                LINHA2=[string,"","","","",""]
                LINHA3=["Mesorregiões, Microrregiões \n e \n Municípios","Estabelecimentos","","","",""]
                LINHA4=["","Total","Atividade do estabelecimento","","",""]
                LINHA5=["","","Comércio \n (exceto \n supermercado)","Indústria",
                        "Serviço de \n Armazenagem",
                        "Produção \n Agropecuária"]
        if tipo=="emp":
            string="   8. Estabelecimentos, por tipos de propriedade da empresa, segundo \n"
            string+="    as mesorregiões, as microrregiões e os municípios"
            LINHA2=[string,"","","","",""]
            LINHA3=["Mesorregiões, Microrregiões \n e \n Municípios","Estabelecimentos","","","",""]
            LINHA4=["","Total","Propriedade da empresa","","",""]
            LINHA5=["","","Governo","Iniciativa \n Privada \n (exceto cooperativa)","Cooperativa",
                    "Economia \n Mista"]  
        LISTA=[]
        LISTA.append(LINHA1)
        LISTA.append(LINHA2)
        LISTA.append(LINHA3)
        LISTA.append(LINHA4)
        LISTA.append(LINHA5)
        FTRACO=FORTRACO(self.lista89)
        lista_f=FTRACO.TRACO()
        for fatiar in range(0,len(lista_f)):
            if tipo=="emp":
                    LISTA.append(lista_f[fatiar])
            if tipo=="ativ":
                    transport=lista_f[fatiar][:]
                    lista_ativ=transport[0:6]
                    LISTA.append(lista_ativ)                   
        FONTE="Fonte: IBGE, Diretoria de Pesquisas, Coordenação de Estatísticas Agropecuárias, "
        FONTE=FONTE+"Pesquisa de Estoques "+str(self.semes)+"º semestre de "+ str(self.ano)
        LINHAF=[FONTE,"","","","",""]
        LISTA.append(LINHAF)
        lista_saida_89.append(LISTA)
        return(lista_saida_89,self.nomereg)

    def ROT10(self):
        TAMANHO=len(self.lista10)           
        NUMPAG=TAMANHO//38
##        print(TAMANHO,"___",NUMPAG)
        if NUMPAG==0:
            lista_ALT10,nomereg=self.ALT10()
            return(lista_ALT10,nomereg)
        else:
            lista_ALT10,nomereg=self.PAG10()
            return(lista_ALT10,nomereg)
 
    def ALT10(self):
        lista_saida_10=[]
        LISTA=[]
        LINHA1=["Pesquisa de Estoques - "+str(self.semes)+"º semestre de "+ str(self.ano) +" - "+self.nomeuf,
                "","","","","","",""]
        LISTA.append(LINHA1)
        string="       10. Armazéns convencionais, estruturais e infláveis, armazéns graneleiros e granelizados e silos, com indicação \n"
        string+="       do número de informantes e capacidade útil, segundo as mesorregiões, as microrregiões e os municípios"
        LINHA2=[string,"","","","","","",""]
        LINHA3=["Mesorregiões, Microrregiões \n e \n Municípios",
                    " Total de \n estabelecimentos",
                    "Armazéns convencionais, \n estruturais e infláveis","",
                    "Armazéns graneleiros \n e granelizados","",
                    "Silos",""]
        LINHA4=["","","Número \n de \n informantes","Capacidade \n útil (m³)",
                       "Número \n de \n informantes","Capacidade \n útil (t)",
                       "Número \n de \n informantes","Capacidade \n útil (t)"]
        LISTA.append(LINHA2)
        LISTA.append(LINHA3)
        LISTA.append(LINHA4)
        FTRACO=FORTRACO(self.lista10)
        lista_f=FTRACO.TRACO()
        for ll in lista_f:
            print(ll)
        for fatiar in range(0,len(lista_f)):
            LISTA.append(lista_f[fatiar])                
        FONTE="Fonte: IBGE, Diretoria de Pesquisas, Coordenação de Estatísticas Agropecuárias, "
        FONTE=FONTE+"Pesquisa de Estoques "+str(self.semes)+"º semestre de "+ str(self.ano)
        LINHAF=[FONTE,"","","","","","",""]
        LISTA.append(LINHAF)
        lista_saida_10.append(LISTA)
##        for ll in lista_saida_10:
##            for xx in ll:
##                print(xx)
        return(lista_saida_10,self.nomereg)

    def PAG10(self):
        TAMANHO=len(self.lista10)           
        NUMPAG=TAMANHO//38
##        print(TAMANHO,"___",NUMPAG)
        lista_saida_10=[]
        FTRACO=FORTRACO(self.lista10)
        lista_f=FTRACO.TRACO()
        for pag in range(0,NUMPAG):
            LINHA1=["Pesquisa de Estoques - "+str(self.semes)+"º semestre de "+ str(self.ano) +" - "+self.nomeuf,
                    "","","","","","",""]
            string="   10. Armazéns convencionais, estruturais e infláveis, armazéns graneleiros e granelizados e silos, com indicação \n"
            string+="   do número de informantes e capacidade útil, segundo as mesorregiões, as microrregiões e os municípios"
            LINHA2=[string,"","","","","","","(continua)"]
            LINHA3=["Mesorregiões, Microrregiões \n e \n Municípios",
                    " Total de \n estabelecimentos",
                    "Armazéns convencionais, \n estruturais e infláveis","",
                    "Armazéns graneleiros \n e granelizados","",
                    "Silos",""]
            LINHA4=["","","Número \n de \n informantes","Capacidade \n útil (m³)",
                       "Número \n de \n informantes","Capacidade \n útil (t)",
                       "Número \n de \n informantes","Capacidade \n útil (t)"]
            LISTA=[]
            LISTA.append(LINHA1)
            LISTA.append(LINHA2)
            LISTA.append(LINHA3)
            LISTA.append(LINHA4)
            for fatiar in range(pag*38,(pag+1)*38):
                LISTA.append(lista_f[fatiar])
                N_prov=fatiar
            lista_saida_10.append(LISTA)
        LISTA=[]
        LISTA.append(LINHA1)
        string="   10. Armazéns convencionais, estruturais e infláveis, armazéns graneleiros e granelizados e silos, com indicação \n"
        string+="   do número de informantes e capacidade útil, segundo as mesorregiões, as microrregiões e os municípios"
        LINHA2=[string,"","","","","","","(conclusão)"]
        LISTA.append(LINHA2)
        LISTA.append(LINHA3)
        LISTA.append(LINHA4)
        for fatiar in range(N_prov+1,len(lista_f)):
            LISTA.append(lista_f[fatiar])                
        FONTE="Fonte: IBGE, Diretoria de Pesquisas, Coordenação de Estatísticas Agropecuárias, "
        FONTE=FONTE+"Pesquisa de Estoques "+str(self.semes)+"º semestre de "+ str(self.ano)
        LINHAF=[FONTE,"","","","","","",""]
        LISTA.append(LINHAF)
        lista_saida_10.append(LISTA)
##        for ll in lista_saida_10:
##            for xx in ll:
##                print(xx)
        return(lista_saida_10,self.nomereg)
        

    def ROT11(self):
        m=0
        SAIDA(self.lista11,"lista11.csv",";")
        varlabel="(continua)"
        for ss in self.lista11:
            FTRACO=FORTRACO(ss)
            lista_f=FTRACO.TRACO67()
            lista_x=FTRACO.DESINT11(self.semes,self.ano,self.cuf)
            lista_saida_11=[]
            TAMANHO=len(ss)
            NUMPAG=TAMANHO//38
            #print(NUMPAG)
            for pag in range(0,NUMPAG):
                #print(pag)
                varlabel="(continua)"
                LINHA1=["Pesquisa de Estoques - "+str(self.semes)+"º semestre de "+ str(self.ano) +" - "+self.nomeuf,
                        "","","","","","","","","","","",""]
                string="   11. Produtos estocados, com indicação do número de informantes e da quantidade \n"
                string+="    existente em "+self.DATA+", segundo as mesorregiões, as microrregiões e os municípios"
                LINHA2=[string,"","","","","","","","","","","","(continua)"]
                indice=m*6
                LINHA3=["Mesorregiões , Microrregiões \n e \n Municípios",self.prod2[indice],"",
                       self.prod2[indice+1],"",self.prod2[indice+2],"",self.prod2[indice+3],"",
                       self.prod2[indice+4],"",self.prod2[indice+5],""]
                LINHA4=["","Núm. \n de \n inf.","Quant.\n (t)",
                   "Núm. \n de \n inf.","Quant.\n (t)",
                   "Núm. \n de \n inf.","Quant.\n (t)",
                   "Núm. \n de \n inf.","Quant.\n (t)",
                   "Núm. \n de \n inf.","Quant.\n (t)",
                   "Núm. \n de \n inf.","Quant.\n (t)"]
                FONTE="Fonte: IBGE, Diretoria de Pesquisas, Coordenação de Estatísticas Agropecuárias, "
                FONTE=FONTE+"Pesquisa de Estoques "+str(self.semes)+"º semestre de "+ str(self.ano)
                LISTA=[]
                LISTA.append(LINHA1)
                LISTA.append(LINHA2)
                LISTA.append(LINHA3)
                LISTA.append(LINHA4)
                
                for fatiar in range(pag*38,(pag+1)*38):
                    LISTA.append(lista_x[fatiar])
                    N_prov=fatiar
                lista_saida_11.append(LISTA)
            LISTA=[]
            varlabel="(continua)"
            LINHA1=["Pesquisa de Estoques - "+str(self.semes)+"º semestre de "+ str(self.ano) +" - "+self.nomeuf,
                        "","","","","","","","","","","",""]
            string="   11. Produtos estocados, com indicação do número de informantes e da quantidade \n"
            string+="    existente em "+self.DATA+", segundo as mesorregiões, as microrregiões e os municípios"
            LINHA2=[string,"","","","","","","","","","","","(continua)"]
            indice=m*6
            LINHA3=["Mesorregiões , Microrregiões \n e \n Municípios",self.prod2[indice],"",
                   self.prod2[indice+1],"",self.prod2[indice+2],"",self.prod2[indice+3],"",
                   self.prod2[indice+4],"",self.prod2[indice+5],""]
            LINHA4=["","Núm. \n de \n inf.","Quant.\n (t)",
               "Núm. \n de \n inf.","Quant.\n (t)",
               "Núm. \n de \n inf.","Quant.\n (t)",
               "Núm. \n de \n inf.","Quant.\n (t)",
               "Núm. \n de \n inf.","Quant.\n (t)",
               "Núm. \n de \n inf.","Quant.\n (t)"]
            LISTA.append(LINHA1)
            if m==2:
                LINHA2=[string,"","","","","","","","","","","","(conclusão)"]
                varlabel="(conclusão)"
            LISTA.append(LINHA2)
            LISTA.append(LINHA3)
            LISTA.append(LINHA4)
            try:
                for fatiar in range(N_prov+1,len(ss)):
                    LISTA.append(lista_x[fatiar])
            except:
                for fatiar in range(0,len(ss)):
                    LISTA.append(lista_x[fatiar])            
            FONTE="Fonte: IBGE, Diretoria de Pesquisas, Coordenação de Estatísticas Agropecuárias, "
            FONTE=FONTE+"Pesquisa de Estoques "+str(self.semes)+"º semestre de "+ str(self.ano)
            LINHAF=[FONTE,"","","","","","",""]
            LISTA.append(LINHAF)
            lista_saida_11.append(LISTA)
            m=m+1
            TT11=GERATAB(int(self.semes),int(self.ano),self.cuf)
            corr=CORLIM(lista_saida_11,11,varlabel)
            lista1=corr.saida
##            for lx in lista1:
##                print(lx)
##                
            TT11.TAB11(lista1,self.nomereg,m)
  
                
    def ROT12(self,lista):
        LISTA_SAIDA=[]
        LINHA1=["Pesquisa de Estoques - "+str(self.semes)+"º semestre de "+ str(self.ano) +" - "+self.nomeuf,
                ""]
        string="Informações suplementares \n"
        string+="Capacidade útil dos estabelecimentos inativos"
        LINHA2=[string,""] 
        LINHA3=['Unidades armazenadoras',"Capacidade útil"]
        LISTA_COL=["                Armazém convencional, estrutural e inflável",
                   "                Armazém graneleiro e granelizado",
                   "                Silo (para grãos)",
                   "Total de estabelecimentos inativos:",
                   "Total de estabelecimentos inativos com informações de capacidade útil:",
                   "Total de estabelecimentos inativos sem informações de capacidade útil:"]
        LISTA_SAIDA.append(LINHA1)
        LISTA_SAIDA.append(LINHA2)
        LISTA_SAIDA.append(LINHA3)
        for i in range(0,6):
            try:
                resul=float(0/int(lista[i]))
                resultado=formato(lista[i])
            except:
                resultado="-"
            if i==0:
                resultado=resultado+" m³"
            if i==1 or i==2:
                resultado=resultado+" (t)"
            LISTA_SAIDA.append([LISTA_COL[i],resultado])                   
        FONTE="Fonte: IBGE, Diretoria de Pesquisas, Coordenação de Estatísticas Agropecuárias, "
        FONTE=FONTE+"Pesquisa de Estoques "+str(self.semes)+"º semestre de "+ str(self.ano)
        LINHAF=[FONTE,""]
        LISTA_SAIDA.append(LINHAF)
        return(LISTA_SAIDA)
       
        

   

        
if __name__=="__main__":
     MONTAR_LISTA("41",2,2018)                
            
            
            
