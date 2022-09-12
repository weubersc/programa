import zipfile
import os
import glob
import shutil

dirpath=os.getcwd()
print(dirpath)



l_arq=[glob.glob('**/*SEGUNDO-semestre_2021.pdf')]

l_nome=[]
for larq in l_arq:
    for lq in larq:
        arq_out=lq.split("\\")
        shutil.move(dirpath+"\\"+lq,arq_out[1])
        l_nome.append(arq_out[1])

with zipfile.ZipFile("apuração.zip", mode="w") as archive:
    for ln in l_nome:
            print(ln)
            path = os.path.join(dirpath, ln)
            archive.write(ln)
            os.remove(path)
