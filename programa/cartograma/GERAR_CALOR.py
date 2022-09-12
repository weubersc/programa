import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import shapefile as shp
import seaborn as sns
import json


class PLOTAR():

    def __init__(self):
        sns.set(style="whitegrid", palette="pastel", color_codes=True)
        sns.mpl.rc("figure", figsize=(10,6))
##        data = pd.read_csv(arquivo,encoding='latin-1',dtype={variv1:'str',variv2:'str'})
##        data=data.rename(columns = {variv1:'CD_GEOCMU'})
##        print(data.head())
        SFILE="55mu2500gsd.shp"
        self.sf = shp.Reader(SFILE,encoding="latin1")
        self.comp=len(self.sf.shapes())
        print(self.comp)
        self.df = self.read_shapefile()
        print(self.df.dtypes)
        print(self.df.head())
        print(self.df.columns)
        lista_coords=[]
        for x,y in self.df.iterrows():
            temp=[]
            temp=set(y["coords"])
            cx,cy=self.centroid(temp)
            lista_coords.append([y["codig"],cx,cy])
        with open("centroide.json",'w') as fout:
           json.dump(lista_coords,fout)

    def centroid(self,points):
        x_coords = [p[0] for p in points]
        y_coords = [p[1] for p in points]
        _len = len(points)
        centroid_x = sum(x_coords)/_len
        centroid_y = sum(y_coords)/_len
        return(centroid_x, centroid_y)
            
        
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
    

