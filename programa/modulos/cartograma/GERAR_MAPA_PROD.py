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

    def __init__(self,DF,prod):
        self.prod=prod
        sns.set(style="whitegrid", palette="pastel", color_codes=True)
        sns.mpl.rc("figure", figsize=(10,6))
        self.dirpath=os.getcwd()
        SFILE=self.dirpath+"\\programa\\malhas\\BRUFE250GC_SIR.shp"
        SFILE_UF=self.dirpath+"\\programa\\malhas\\BRUFE250GC_SIR.shp"
        self.sf = shp.Reader(SFILE,encoding="latin1")
        self.sfuf = shp.Reader(SFILE_UF)
        self.comp=len(self.sf.shapes())
        print(self.comp)
        self.variv=prod
        self.dic_uf_cor={}
        for x,y in DF.iterrows():
                self.dic_uf_cor[y["coduf"]]=y["cor"]

        self.Colorir_Poligonos()

    def Colorir_Poligonos(self):
        fig, ax = plt.subplots(figsize=(12,10))
#        fig.suptitle('COMPARATIVO DE PRODUÇÃO - VARIAÇÃO ',fontsize=16)
        ax.set_axis_off()
        indice_s=0
        records = self.sf.records()
        for shape in self.sfuf.shapeRecords():
            npoints=len(shape.shape.points)
            nparts=len(shape.shape.parts)
            if nparts==1:
                x = [i[0] for i in shape.shape.points[:]]
                y = [i[1] for i in shape.shape.points[:]]
                ax.plot(x, y, 'k') 
                shape_ex = self.sfuf.shape(indice_s)
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
            COD=records[indice_s]["CD_GEOCUF"]
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
                    ax.fill(x_lon,y_lat, color=self.dic_uf_cor[int(COD)],linestyle='None')
                except:
                    ax.fill(x_lon,y_lat, color='#ebebe0',linestyle='None')
                   
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
                    ax.fill(x_lon,y_lat, color=self.dic_uf_cor[int(COD)],linestyle='None')
                 except:
                    ax.fill(x_lon,y_lat, color='#ebebe0',linestyle='None')
                    
            indice_s=indice_s+1
        fig.savefig(self.dirpath+"\\programa\\provisórios\\"+self.prod+".png", dpi=100)
        plt.close('all')

  


    

