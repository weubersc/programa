from programa.modulos.apuracao.estoque_TAB_BR import gerar_tabela as GERATAB
from programa.modulos.apuracao.FORMATO_NUMERO import inteiro as formato
from programa.modulos.apuracao.FORMATO_NUMERO import flutuante as tonelada
from programa.modulos.apuracao.INVERSAO import INVERTER
from programa.modulos.apuracao.INVERSAO import FORMATAR
import pandas as pd
from códigos import Codigos as COD
from programa.modulos.apuracao.formatlista import FORMATAR_LISTA as FORTRACO

class MONTAR_LISTA:

    def __init__(self,ano,sem):
        self.ano=str(ano)
        self.sem=str(sem)
        DATA1="30/06/"+str(self.ano)
        DATA2="31/12/"+str(self.ano)
        if sem==1:
            self.DATA=DATA1
        if sem==2:
            self.DATA=DATA2
        self.emp={}
        self.ativ={}
        self.fx1={}
        self.fx2={}
        self.lista_chave=[]
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
        print(self.fx1)

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
        print(self.fx2)

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
        CC=COD()
        codig=CC.codigo
        self.lista89=[]
        for ll in lista:
            temp=[]
            espaco=""
            if len(ll[0])!=1:
                espaco="     "
            temp.append(espaco+"  "+codig[ll[0]])
            temp.append(formato(ll[1]))
            for lz in ll[2]:
                temp.append(formato(lz))
            self.lista89.append(temp)

    def REGUF10(self,lista):
        CC=COD()
        codig=CC.codigo
        self.lista10=[]
        for ll in lista:
            temp=[]
            espaco=""
            if len(ll[0])!=1:
                espaco="     "
            temp.append(espaco+"  "+codig[ll[0]])
            temp.append(formato(ll[1]))
            for lz in ll[2]:
                for lw in lz:
                    temp.append(formato(lw))
            self.lista10.append(temp)

##        for ll in self.lista10:
##            print(ll)

    def REG11(self,lista):
        CC=COD()
        codig=CC.codigo
        lista_cod=[]
        self.lista11=[]
        for ll in lista:
            if ll[0]=='Algodão (em caroço)':
                lista_cod.append(ll[1])

        for vv in lista_cod:
            temp=[]
            if len(vv)==1:
                temp.append(codig[vv])
            else:
                string="      "+codig[vv]
                temp.append(string)
            for cc in self.prod:
                for ll in lista:
                  if ll[0]==cc and vv==ll[1]:
                     temp.append(formato(ll[2]))
                     temp.append(tonelada(ll[3]))
            self.lista11.append(temp)



    
        



    def ROT1(self,listad):
        LINHA1=["Pesquisa de Estoques - "+ self.sem+"º " + "semestre de "+self.ano+" - BRASIL",
                "","","","","","",""]
        string="1. Unidades Armazenadoras, com indicação do número de informantes e capacidade útil \n"
        string+=" dos armazéns e dos silos, segundo os tipos de propriedade da empresa"
        LINHA2=[string,"","","","","","",""]
        
        LINHA3=["Tipos de \n propriedade \n da \n empresa",
                "Total de \n  estabele- \n cimentos",
                "Unidades armazenadoras","","","","",""]
        print(len( LINHA3))
        LINHA4=["","","Armazéns convencionais, \n estruturais e infláveis",
                "","Armazéns graneleiros  \n e granelizados","","Silos",""]
        LINHA5=["","","Número \n  de \n  informantes",
                "Capacidade \n  útil \n  (m³)",
                "Número \n  de \n de informantes",
                "Capacidade \n  útil \n  (t)",
                "Número \n  de \n  informantes",
                "Capacidade \n  útil \n  (t)"]
        FONTE="Fonte: IBGE, Diretoria de Pesquisas, Coordenação de Estatísticas Agropecuárias, "
        FONTE=FONTE+"Pesquisa de Estoques " + self.sem +"º "+ "semestre de "+self.ano
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
        for lk in LISTA:
            print(lk)
        return(LISTA)
        
 
    def ROT2(self,listad):
        LINHA1=["Pesquisa de Estoques - " + self.sem +"º "+  "semestre de "+self.ano+" - BRASIL",
                "","","","","","",""]
        string="2. Unidades Armazenadoras, com indicação do número de informantes e capacidade útil \n"
        string+=" dos armazéns e dos silos, segundo os tipos de atividade do estabelecimento"
        LINHA2=[string,"","","","","","",""]
        
        LINHA3=["Tipos de \n atividade \n do \n estabelecimento",
                "Total de \n  estabele- \n cimentos",
                "Unidades armazenadoras","","","","",""]
        print(len( LINHA3))
        LINHA4=["","","Armazéns convencionais, \n estruturais e infláveis",
                "","Armazéns graneleiros  \n e granelizados","","Silos",""]
        LINHA5=["","","Número \n  de \n  informantes",
                "Capacidade \n  útil \n  (m³)",
                "Número \n  de \n  informantes",
                "Capacidade \n  útil \n  (t)",
                "Número \n  de \n  informantes",
                "Capacidade \n  útil \n de (t)"]
        FONTE="Fonte: IBGE, Diretoria de Pesquisas, Coordenação de Estatísticas Agropecuárias, "
        FONTE=FONTE+"Pesquisa de Estoques " + self.sem +"º "+ "semestre de "+self.ano
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
        for lk in LISTA:
            print(lk)
        return(LISTA)

    def ROT3(self,listad):
        LINHA1=["Pesquisa de Estoques - " + self.sem +"º "+ "semestre de "+self.ano+" - BRASIL",
                "",""]
        string="3. Armazéns convencionais, estruturais e infláveis com indicação do número de \n"
        string+="estabelecimentos e capacidade útil, segundo os grupos de capacidade útil"
        LINHA2=[string,"",""]
        
        LINHA3=["Grupos de capacidade útil \n (m³)",
                "Armazéns convencionais, estruturais e infláveis",
                ""]
        
        print(len( LINHA3))
        LINHA4=["","Número de estabelecimentos",
                 "Capacidade útil  \n (m³)"]
        
        FONTE="Fonte: IBGE, Diretoria de Pesquisas, Coordenação de Estatísticas Agropecuárias, "
        FONTE=FONTE+"Pesquisa de Estoques " + self.sem +"º "+ "semestre de "+self.ano
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
        for lk in LISTA:
            print(lk)
        return(LISTA)

    def ROT4(self,listad):
        LINHA1=["Pesquisa de Estoques - " + self.sem +"º "+ "semestre de "+self.ano+" - BRASIL",
                "","","","","",""]
        string="4. Armazéns e silos para produtos a granel, com indicação do número de informantes\n"
        string+="e capacidade útil, segundo os grupos de capacidade útil"
        LINHA2=[string,"","","","","",""]
        
        LINHA3=["Grupos de \n capacidade útil \n (m³)",
                "Armazéns e silos para produtos a granel",
                "","","","",""]
        print(len( LINHA3))
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
        FONTE=FONTE+"Pesquisa de Estoques "+self.sem+"º " + "semestre de "+self.ano
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
        for lk in LISTA:
            print(lk)
        return(LISTA) 

    def ROT5(self,listad):
        LINHA1=["Pesquisa de Estoques - "+self.sem+"º " + "semestre de "+self.ano+" - BRASIL",
                "","",""]
        string="5. Número de municípios, de informantes e estoque declarado em " +self.DATA+ " , \n"
        string+="segundo os produtos"
        LINHA2=[string,"","",""]
        
        LINHA3=["Produtos",
                "Número \n de \n municípios",
                "Número \n de \n informantes",
                "Estoque em " +self.DATA+ "  \n (t)"]
        
        print(len( LINHA3))        
        FONTE="Fonte: IBGE, Diretoria de Pesquisas, Coordenação de Estatísticas Agropecuárias, "
        FONTE=FONTE+"Pesquisa de Estoques " + self.sem +"º "+ "semestre de "+self.ano
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
        LINHA1=["Pesquisa de Estoques - " + self.sem +"º "+ "semestre de "+self.ano+" - BRASIL",
                "","","","","","","","","","","",""]
        string="6. Produtos estocados, com indicação do número de informantes e da \n"
        string+="quantidade existente em " +self.DATA+ ", segundo os tipos de propriedade da empresa"
        LINHA2=[[string,"","","","","","","","","","","","(continua)"],
                [string,"","","","","","","","","","","","(conclusão)"]]
        print("!---LINHA12---")
        for jj in LINHA2:
            print(jj)
        print("-----")
        print(len(self.prod))
        LINHA3=[]
        for i in range(0,18,6):
            LINHA3.append(["Tipos de \n propriedade da \n empresa",self.prod[i],"",
                   self.prod[i+1],"",self.prod[i+2],"",
                   self.prod[i+3],"",
                   self.prod[i+4],"",
                   self.prod[i+5],""])
        for kk in LINHA3:
            print(kk)
        LINHA4=["","Número \n de \n informantes","Quantidade \n (t)",
                   "Número \n de \n informantes","Quantidade \n (t)",
                   "Número \n de \n informantes","Quantidade \n (t)",
                   "Número \n de \n informantes","Quantidade \n (t)",
                   "Número \n de \n informantes","Quantidade \n (t)",
                   "Número \n de \n informantes","Quantidade \n (t)"]
    
        FONTE="Fonte: IBGE, Diretoria de Pesquisas, Coordenação de Estatísticas Agropecuárias, "
        FONTE=FONTE+"Pesquisa de Estoques " + self.sem +"º "+ "semestre de "+self.ano
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
        TT6=GERATAB(int(self.sem),int(self.ano))
        TT6.TAB6(LISTA,"emp")
            
    def ROT7(self):
        LINHA1=["Pesquisa de Estoques - " + self.sem +"º "+ "semestre de "+self.ano+" - BRASIL",
                "","","","","","","","","","","",""]
        string="7. Produtos estocados, com indicação do número de informantes e da \n"
        string+="quantidade existente em " +self.DATA+ " , segundo os tipos de atividade do estabelecimento"
        LINHA2=[[string,"","","","","","","","","","","","(continua)"],
                [string,"","","","","","","","","","","","(conclusão)"]]
        print("-----")
        print(len(self.prod))
        LINHA3=[]
        for i in range(0,18,6):
            LINHA3.append(["Tipos de \n atividade do \n estabelecimento",self.prod[i],"",
                   self.prod[i+1],"",self.prod[i+2],"",
                   self.prod[i+3],"",
                   self.prod[i+4],"",
                   self.prod[i+5],""])
        for kk in LINHA3:
            print(kk)
        LINHA4=["","Número \n de \n informantes","Quantidade \n (t)",
                   "Número \n de \n informantes","Quantidade \n (t)",
                   "Número \n de \n informantes","Quantidade \n (t)",
                   "Número \n de \n informantes","Quantidade \n (t)",
                   "Número \n de \n informantes","Quantidade \n (t)",
                   "Número \n de \n informantes","Quantidade \n (t)"]
    
        FONTE="Fonte: IBGE, Diretoria de Pesquisas, Coordenação de Estatísticas Agropecuárias, "
        FONTE=FONTE+"Pesquisa de Estoques " + self.sem +"º "+ "semestre de "+self.ano
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
        for ll in LISTA:
            print(len(ll))
            print(ll)
        TT7=GERATAB(int(self.sem),int(self.ano))
        TT7.TAB6(LISTA,"ativ")
            
    def ROT89(self,tipo):
        LINHA1=["Pesquisa de Estoques - " + self.sem +"º "+ "semestre de "+self.ano+" - BRASIL",
                "","","","",""]
        if tipo=="ativ":
            string="9. Estabelecimentos, por tipos de atividade, segundo\n"
            string+=" as grandes regiões e as unidades da federação"
            LINHA2=[string,"","","","",""]
            LINHA3=["Grandes Regiões \n e \n Unidades da Federação","Estabelecimentos","","","",""]
            LINHA4=["","Total","Atividade do estabelecimento","","",""]
            LINHA5=["","","Comércio \n (exceto \n supermercado)","Indústria",
                    "Serviço de \n Armazenagem",
                    "Produção \n Agropecuária"]
        if tipo=="emp":
            string="8. Estabelecimentos, por tipos de propriedade da empresa, segundo \n"
            string+=" as grandes regiões e as unidades da federação"
            LINHA2=[string,"","","","",""]
            LINHA3=["Grandes Regiões \n e \n Unidades da Federação","Estabelecimentos","","","",""]
            LINHA4=["","Total","Propriedade da empresa","","",""]
            LINHA5=["","","Governo","Iniciativa \n Privada \n (exceto cooperativa)","Cooperativa",
                    "Economia \n Mista"]  
        FONTE="Fonte: IBGE, Diretoria de Pesquisas, Coordenação de Estatísticas Agropecuárias, "
        FONTE=FONTE+"Pesquisa de Estoques " + self.sem +"º "+ "semestre de "+self.ano
        LINHAF=[FONTE,"","","","",""]
        LISTA=[]
        LISTA.append(LINHA1)
        LISTA.append(LINHA2)
        LISTA.append(LINHA3)
        LISTA.append(LINHA4)
        LISTA.append(LINHA5)
        FTRACO=FORTRACO(self.lista89)
        lista_f=FTRACO.TRACO()
        for ll in lista_f:
            if tipo=="emp":
                LISTA.append(ll)
            if tipo=="ativ":
                transport=ll[:]
                lista_ativ=transport[0:6]
                LISTA.append(lista_ativ)             
        LISTA.append(LINHAF)
        return(LISTA)

    def ROT10(self):
        LINHA1=["Pesquisa de Estoques - " + self.sem +"º "+ "semestre de "+self.ano+" - BRASIL",
                "","","","","","",""]
        string="10. Armazéns convencionais, estruturais e infláveis, armazéns graneleiros e granelizados e silos, com indicação \n"
        string+="do número de informantes e capacidade útil,segundo as grandes regiões e as unidades da federação"
        LINHA2=[string,"","","","","","",""]
        LINHA3=["Grandes Regiões \n e \n Unidades da Federação",
                " Total de \n estabelecimentos",
                "Armazéns convencionais, \n estruturais e infláveis","",
                "Armazéns graneleiros \n e granelizados","",
                "Silos",""]
        LINHA4=["","","Número \n de \n informantes","Capacidade \n  útil (m³)",
                   "Número \n de \n informantes","Capacidade \n  útil (t)",
                   "Número \n de \n informantes","Capacidade \n  útil (t)"]
  
    
        FONTE="Fonte: IBGE, Diretoria de Pesquisas, Coordenação de Estatísticas Agropecuárias, "
        FONTE=FONTE+"Pesquisa de Estoques " + self.sem +"º "+ "semestre de "+self.ano
        LINHAF=[FONTE,"","","","","","",""]
        LISTA=[]
        LISTA.append(LINHA1)
        LISTA.append(LINHA2)
        LISTA.append(LINHA3)
        LISTA.append(LINHA4)
        FTRACO=FORTRACO(self.lista10)
        lista_f=FTRACO.TRACO()
        for ll in lista_f:
            LISTA.append(ll) 
        LISTA.append(LINHAF)
        for ll in LISTA:
            print(len(ll))
            print(ll)
        return(LISTA)

    def ROT11(self):
        LINHA1=["Pesquisa de Estoques - " + self.sem +"º "+  "semestre de "+self.ano+" - BRASIL",
                "","","","","",""]
        string="11. Produtos estocados, com indicação do número de informantes e da quantidade \n"
        string+="existente em " +self.DATA+ ", segundo as grandes regiões e as unidades da federação"
        LINHA2=[[string,"","","","","","(continua)"],
                [string,"","","","","","(conclusão)"]]
        print("-----")
        print(len(self.prod))
        LINHA4=["","Número \n de \n informantes","Quantidade \n (t)",
                   "Número \n de \n informantes","Quantidade \n (t)",
                   "Número \n de \n informantes","Quantidade \n (t)"]
        FONTE="Fonte: IBGE, Diretoria de Pesquisas, Coordenação de Estatísticas Agropecuárias, "
        FONTE=FONTE+"Pesquisa de Estoques " + self.sem +"º "+ "semestre de "+self.ano
        LINHAF=[FONTE,"","","","","",""]
        indice=0
        FTRACO=FORTRACO(self.lista11)
        lista_f=FTRACO.TRACO67()
        lista_x=FTRACO.DESINT11()
        for i in range(0,18,3):
            indice+=1
            print("-----"+str(i)+"-------")
            LISTA=[]
            LISTA.append(LINHA1)
            if i < 15:
                LISTA.append(LINHA2[0])
            else:
                LISTA.append(LINHA2[1])
            LINHA3=["Grandes Regiões \n e \n Unidades da Federação",self.prod[i],"",
                   self.prod[i+1],"",self.prod[i+2],""]
            LISTA.append(LINHA3)
            LISTA.append(LINHA4)
            indi=i*2+1
            indf=indi+5
            for m11 in lista_x:
                temp=[]
                temp.append(m11[0])
                for ix in range(indi,indf+1):
                    temp.append(m11[ix])
                LISTA.append(temp)
            LISTA.append(LINHAF)
            print("DATA_STAR_TREK")
            for tt in LISTA:
                print(tt)
            TT11=GERATAB(int(self.sem),int(self.ano))
            TT11.TAB11(LISTA,indice)

                
    def ROT12(self,lista):
        LISTA_SAIDA=[]
        LINHA1=["Pesquisa de Estoques - " + self.sem +"º "+ "semestre de "+self.ano+" - BRASIL",
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
        FONTE=FONTE+"Pesquisa de Estoques " + self.sem +"º "+ "semestre de "+self.ano
        LINHAF=[FONTE,""]
        LISTA_SAIDA.append(LINHAF)
        return(LISTA_SAIDA)
       
        

   

        
if __name__=="__main__":
     MONTAR_LISTA(1,2018)                
            
            
            
