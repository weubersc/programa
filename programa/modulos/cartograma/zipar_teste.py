import os
import zipfile

def compactar(SEM,ANO):
    direc=os.getcwd()
    saida=direc+"\\programa\\saida\\"
    os.chdir(saida+"\\cartograma\\")
    print(os.getcwd())
    dirpath=os.getcwd()
    fantasy_zip = zipfile.ZipFile(saida+SEM+"_"+ANO+"_cartogramas.zip", 'w',
                                  zipfile.ZIP_DEFLATED)
     
    for folder, subfolders, files in os.walk(dirpath):
     
        for file in files:
            if file.endswith(SEM+"_"+ANO+"_cartograma.png"):
                print(file)
                fantasy_zip.write(file)
     
    fantasy_zip.close()

    fantasy_zip = zipfile.ZipFile(saida+SEM+"_"+ANO+"_mapas.zip", 'w',
                                  zipfile.ZIP_DEFLATED)
     
    for folder, subfolders, files in os.walk(dirpath):
     
        for file in files:
            if file.endswith(SEM+"_"+ANO+'_'+'municipio_r.png'):
                print(file)
                fantasy_zip.write(file)
     
    fantasy_zip.close()
    print("COMPACTADO")
