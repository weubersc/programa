import os
import glob

dufnome={"Brasil":"00",
               "Rondônia":"11",
               "Acre":"12",
               "Amazonas":"13",
               "Roraima":"14",
               "Pará":"15",
               "Amapá":"16",
               "Tocantins":"17",
               "Maranhão":"21",
               "Piauí":"22",
               "Ceará":"23",
               "Rio Grande do Norte":"24",
               "Paraíba":"25",
               "Pernambuco":"26",
               "Alagoas":"27",
               "Sergipe":"28",
               "Bahia":"29",
               "Minas Gerais":"31",
               "Espírito Santo":"32",
               "Rio de Janeiro":"33",
               "São Paulo":"35",
               "Paraná":"41",
               "Santa Catarina":"42",
               "Rio Grande do Sul":"43",
               "Mato Grosso do Sul":"50",
               "Mato Grosso":"51",
               "Goiás":"52",
               "Distrito Federal":"53",
               }

lista_geo=[]
for key,item in dufnome.items():
    if key!="Brasil":
        lista_geo.append(key)
lista_geo.sort()

dirpath=os.getcwd()

for uf in lista_geo:
    path=dirpath+"\\"+uf
    os.mkdir(path)
