import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import shapefile as shp
import seaborn as sns
import json
import os

class PLOTTING():

    def __init__(self,LISTAFX,LISTACORES,V1,C1):
        self.dirpath=os.getcwd()
        self.LISTAFX=LISTAFX
        self.color_sq=LISTACORES
        sns.set(style="whitegrid", palette="pastel", color_codes=True)
        sns.mpl.rc("figure", figsize=(10,6))
##        data = pd.read_csv(arquivo,encoding='latin-1',dtype={variv1:'str',variv2:'str'})
##        data=data.rename(columns = {variv1:'CD_GEOCMU'})
##        print(data.head())
        SFILE=self.dirpath+"\\programa\\malhas\\BRUFE250GC_SIR.shp"
        self.sf = shp.Reader(SFILE)
        self.comp=len(self.sf.shapes())
        #print(self.comp)
        self.df = self.read_shapefile()
        #print(self.df.dtypes)
        #print(self.df.head())
        self.df["CD_GEOCUF"]=self.df.CD_GEOCUF.astype("int64")
##        for x,y in self.df.iterrows():
##            print(y["CD_GEOCUF"])
        data=pd.read_json(self.dirpath+"\\programa\\provisórios\\capacidade_uf.json")
        data["CD_GEOCUF"]=data.CD_GEOCUF.astype("int64")
##        for x,y in data.iterrows():
##            print(y["CD_GEOCUF"])
        self.varlabel="CD_GEOCUF"
        self.dfuf = pd.merge(self.df, data, on="CD_GEOCUF")
        self.dfuf[V1]=self.dfuf[V1].astype(float)
        self.variv=V1
        self.valor=C1
        self.DIC_FILTRO={}
        self.selecao_fx()
        self.Colorir_Poligonos()


    def Colorir_Poligonos(self):
        fig, ax = plt.subplots(figsize=(12,10))
#        fig.suptitle('COMPARATIVO DE PRODUÇÃO - VARIAÇÃO ',fontsize=16)
        ax.set_axis_off()
        indice_s=0
        records = self.sf.records()
        for shape in self.sf.shapeRecords():
            npoints=len(shape.shape.points)
            nparts=len(shape.shape.parts)
            if nparts==1:
                x = [i[0] for i in shape.shape.points[:]]
                y = [i[1] for i in shape.shape.points[:]]
                ax.plot(x, y, 'k') 
                shape_ex = self.sf.shape(indice_s)
            else: # loop over parts of each shape, plot separately
               for ip in range(nparts): # loop over parts, plot separately
                 i0=shape.shape.parts[ip]
                 if ip < nparts-1:
                      i1 = shape.shape.parts[ip+1]-1
                 else:
                      i1 = npoints
                 seg=shape.shape.points[i0:i1+1]
                 x_lon = np.zeros((len(seg),1))
                 y_lat = np.zeros((len(seg),1))
                 for ip in range(len(seg)):
                     x_lon[ip] = seg[ip][0]
                     y_lat[ip] = seg[ip][1]
                 ax.plot(x_lon,y_lat,'k')
        for shape in self.sf.shapeRecords():
            COD=records[indice_s][self.varlabel]
            npoints=len(shape.shape.points)
            nparts=len(shape.shape.parts)
            if nparts==1:
                x = [i[0] for i in shape.shape.points[:]]
                y = [i[1] for i in shape.shape.points[:]]
                #ax.plot(x, y, 'k') 
                shape_ex = self.sf.shape(indice_s)
                x_lon = np.zeros((len(shape_ex.points),1))
                y_lat = np.zeros((len(shape_ex.points),1))
                for ip in range(len(shape_ex.points)):
                    x_lon[ip] = shape_ex.points[ip][0]
                    y_lat[ip] = shape_ex.points[ip][1]
                try:
                    ax.fill(x_lon,y_lat, color=self.color_sq[self.DIC_FILTRO[int(COD)]],linestyle='None')
                except:
                    ax.fill(x_lon,y_lat, color='white',linestyle='None')
                   
            else: # loop over parts of each shape, plot separately
               for ip in range(nparts): # loop over parts, plot separately
                 i0=shape.shape.parts[ip]
                 if ip < nparts-1:
                      i1 = shape.shape.parts[ip+1]-1
                 else:
                      i1 = npoints
                 seg=shape.shape.points[i0:i1+1]
                 x_lon = np.zeros((len(seg),1))
                 y_lat = np.zeros((len(seg),1))
                 for ip in range(len(seg)):
                     x_lon[ip] = seg[ip][0]
                     y_lat[ip] = seg[ip][1]
                 #ax.plot(x_lon,y_lat,'k', color='white',linestyle='None')
                 for ip in range(len(seg)):
                     x_lon[ip] = seg[ip][0]
                     y_lat[ip] = seg[ip][1]
                 try:
                    ax.fill(x_lon,y_lat, color=self.color_sq[self.DIC_FILTRO[int(COD)]],linestyle='None')
                 except:
                    ax.fill(x_lon,y_lat, color='white',linestyle='None')
                    
            indice_s=indice_s+1
        fig.savefig(self.dirpath+"\\programa\\provisórios\\"+self.variv+".png", dpi=100)

    def selecao_fx(self):
        for ix in range(0,len(self.LISTAFX)):
            if ix==0:
                 selecao=self.variv+'<'+str(self.LISTAFX[ix])
            elif ix==len(self.LISTAFX)-1:
                 selecao=self.variv+'>'+str(self.LISTAFX[ix])
            else:
                selecao=self.variv+'<'+str(self.LISTAFX[ix])
                selecao=selecao+ ' & '+self.variv+'>='+str(self.LISTAFX[ix-1])
            #print(selecao)
            FILTRO=self.dfuf.query(selecao)
            FILTRO=FILTRO[self.varlabel]
            for FF in FILTRO:
                self.DIC_FILTRO[FF]=ix
        for x,y in self.dfuf.iterrows():
            if y[self.variv]==0:
                self.DIC_FILTRO[y[self.varlabel]]=99
            if y[self.valor]==0:
                self.DIC_FILTRO[y[self.varlabel]]=77
                
        
    def read_shapefile(self):
        """
        Read a shapefile into a Pandas dataframe with a 'coords' 
        column holding the geometry information. This uses the pyshp
        package
        """
        fields = [x[0] for x in self.sf.fields][1:]
        records = self.sf.records()
        shps = [s.points for s in self.sf.shapes()]
        df = pd.DataFrame(columns=fields, data=records)
        df = df.assign(coords=shps)
        return(df)

##if  __name__ =='__main__':
##    LCOR=['#ECE7F2', '#A6BDDB', '#74A9CF', '#0570B0', '#023858']
##    LVAL=[0.0, 51.34703082, 102.69406164,
##          154.04109246000002, 205.38812328, 256.7351541]
##    var1='GEOCMU'
##    var2='raz13'
##    caminho='D:/Users/weuber/PPM/arquivos/trimestral/bov102.csv'
##    PLOTTING(LVAL,LCOR,caminho,var1,var2)
    

