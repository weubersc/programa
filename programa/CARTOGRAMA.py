import pandas as pd
import json
from programa.modulos.cartograma.MAPA_MUN_ESTOQUE import APURAÇÃO as APUR
from programa.modulos.cartograma.MAPA_MUN_ESTOQUE import APURAC_MUN as APURAC
from programa.modulos.cartograma.MAPA_MUN_ESTOQUE import Produto 
from programa.modulos.cartograma.GERAR_MAPA import PLOTTING as PLOT
from programa.modulos.cartograma.GERAR_MAPA_MUN import PLOTTING as PLOT_MUN
from programa.modulos.cartograma.GERAR_MAPA_PROD import PLOTTING as PLOT_PROD
from programa.modulos.cartograma.GERAR_MAPA_MUN_PROD import PLOTTING as PLOT_MUN_PROD
from programa.modulos.cartograma.scalebar import SCALE as BAR
from programa.modulos.cartograma.scalebar_produto import SCALE as BARPROD
from programa.modulos.cartograma.GERAR_CALOR import PLOTAR as PL
from programa.modulos.cartograma.municipio_latlon import munic_centroide
from programa.modulos.cartograma.CONTOURF import contorno
from programa.modulos.cartograma.natural_breaks import getJenksBreaks as jenks
from programa.modulos.cartograma.drawing import legenda_per as LEGPER
from programa.modulos.cartograma.drawing import legenda_cap as LEGCAP
from programa.modulos.cartograma.drawing import legenda_cap_vertical as LEGCAP_VERTICAL
from programa.modulos.cartograma.drawing import legenda_prod as LEGPROD
from programa.modulos.cartograma.drawing import legenda_prod_vertical as LEGPROD_VERTICAL
from programa.modulos.cartograma.MONTAGEM_CAP import APRESENTACAO as MONTAR
from programa.modulos.cartograma.MONTAGEM_CAP_PROD import APRESENTACAO as MONTAR_PROD
from programa.modulos.cartograma.CAP_BR import CAPBR
from programa.modulos.cartograma.CAP_BR_PROD import CAPBR as CAPBRPROD
from programa.modulos.cartograma.color2 import cores as cores12
from programa.modulos.cartograma.color3 import cores as cores13
from programa.modulos.cartograma.perc_rotulo import rotulo
from programa.modulos.cartograma.jenks_mais_menos import valores
from programa.modulos.cartograma.produto_cor import DFCORES as PROD_COR
from programa.modulos.cartograma.PRODUTO_MUN_JENKS import PROD_MUN_JENKS as PMUM_JENKS
from programa.modulos.cartograma.zipar_teste import compactar as ZIPPAR

class GERAR():

    def __init__(self,ANNO,SEMES):
        ANO=ANNO
        ANO_ANT=ANO-1
        SS=SEMES.upper()
        SEM=SS.lower()
        if SEM=="primeiro":
            semt="Primeiro"
        if SEM=="segundo":
            semt="Segundo"

        ## GERAÇÃO DOS MAPAS DE PRODUTO
        ##----------------------------------
        Produto(SS,ANO)

        cor=cores12()
        dic_cores={}
        for x,y in cor.dic_rgb.items():
            dic_cores[x]=[y[1],y[3],y[6],y[8],y[10],y[14]]

        df_produf=rotulo()
        #print(df_produf.columns)
        ##for x,y in df_produf.iterrows():
        ##    print(y['produto'],y['coduf'],y['perc'])
        fxmais,lmais,fxmenos,lmenos=valores(df_produf)
        cores13(fxmais,fxmenos)
        DF_PROD_COR=PROD_COR(df_produf,lmais,lmenos,fxmais,fxmenos)

        l_prod=["Algodão (em pluma)",
                "Algodão (em caroço)",
                "Caroço de Algodão",
                "Arroz (em casca)",
                "Arroz Beneficiado",
                "Café Arábica (em grão)",
                "Café Canephora (em grão)",
                "Café (em grão)",
                "Feijão Preto (em grão)",
                "Feijão de Cor (em grão)",
                "Feijão (em grão)",
                "Milho (em grão)",
                "Soja (em grão)",
                "Trigo (em grão)"]

        #l_prod=["Algodão (em pluma)"]
        print(DF_PROD_COR.columns)
        for ll in l_prod:
            DFP=DF_PROD_COR[(DF_PROD_COR["produto"]==ll)]
            PLOT_PROD(DFP,ll)
            BARPROD(ll)
            DF,lfx,color=PMUM_JENKS(ll)
            PLOT_MUN_PROD(DF,lfx,dic_cores[color],"produc",ll)
            LEGPROD(dic_cores[color],lfx,ll)
            LEGPROD_VERTICAL(dic_cores[color],lfx,ll)
            TOTBR,PERC=CAPBRPROD(ll)
            MONTAR_PROD(semt,str(ANO),ll,TOTBR,PERC,DFP)

        ##----------------------------------
        ## FIM DA GERAÇÃO DOS MAPAS DE PRODUTO    

        ## GERAÇÃO DAS MAPAS DE CAPACIDADE
        ##----------------------------------
        APUR(SS,ANO)
        APURAC(SS,ANO)


        LVAL=[-20,-10,-5,0,5,10,15,20]
        LCORES={0:"#B40404",
                1:"#FE2E2E",
                2:"#F78181",
                3:"#F6CECE",
                99:"#A4A4A4",
                77:"#FFFFFF",
                4:"#BCF5A9",
                5:"#5FC006",
                6:"#4FA003",
                7:'#037503',
               }

        LCORES_V={99:"#FFFFFF",         
                 0:"#F1F8E0",
                 1:"#BCF5A9",
                 2:"#82FA58",
                 3:'#00FF00',
                 4:'#31B404',
                 5:'#21610B'}

        LCORES_B={99:"#FFFFFF",
                  0:'#eff3ff',
                  1:'#c6dbef',
                  2:'#9ecae1',
                  3:'#6baed6',
                  4:'#3182bd',
                  5:'#08519c'}

        LCORES_P={99:"#FFFFFF",         
                  0:'#f1eef6',
                  1:'#d4b9da',
                  2:'#c994c7',
                  3:'#df65b0',
                  4:'#dd1c77',
                  5:'#980043'}
                
        PLOT(LVAL,LCORES,"VAR1","CAP1")
        PLOT(LVAL,LCORES,"VAR2","CAP2")
        PLOT(LVAL,LCORES,"VAR3","CAP3")
        tit1=("Capacidade (m³) de armazéns convencionais," 
                          "estruturais e infláveis")
        tit2=("Capacidade (t) de armazéns graneleiros e granalizados")
        tit3=("Capacidade (t) de silos")

        BAR("VAR1",tit1)
        BAR("VAR2",tit2)
        BAR("VAR3",tit3)

        DATA_CENTRO_MUN=munic_centroide()
        DZ=DATA_CENTRO_MUN["CONV"]
        z=DZ.values.tolist()
        faixa1=jenks(z,6)
        DZ=DATA_CENTRO_MUN["GRAN"]
        z=DZ.values.tolist()
        faixa2=jenks(z,6)
        DZ=DATA_CENTRO_MUN["SILO"]
        z=DZ.values.tolist()
        faixa3=jenks(z,6)
        PLOT_MUN(faixa1,LCORES_V,"CONV","V1")
        PLOT_MUN(faixa2,LCORES_B,"GRAN","V2")
        PLOT_MUN(faixa3,LCORES_P,"SILO","V3")
        LEGPER(LCORES,str(ANO_ANT),SEM)
        LEGCAP(LCORES_V,faixa1,"CONV",1)
        LEGCAP(LCORES_B,faixa2,"GRAN",2)
        LEGCAP(LCORES_P,faixa3,"SILO",2)
        LEGCAP_VERTICAL(LCORES_V,faixa1,"CONV",1)
        LEGCAP_VERTICAL(LCORES_B,faixa2,"GRAN",2)
        LEGCAP_VERTICAL(LCORES_P,faixa3,"SILO",2)
        V1,PER=CAPBR("CONV")
        MONTAR(semt,str(ANO),"VAR1","CONV",tit1,V1,PER)
        V2,PER=CAPBR("GRAN")
        MONTAR(semt,str(ANO),"VAR2","GRAN",tit2,V2,PER)
        V3,PER=CAPBR("SILO")
        MONTAR(semt,str(ANO),"VAR3","SILO",tit3,V3,PER)

        ##----------------------------------
        ## FIM DA GERAÇÃO DAS MAPAS DE CAPACIDADE

        ##----------------------------------
        ##------COMPACTAR-------
        ZIPPAR(semt,str(ANO))

