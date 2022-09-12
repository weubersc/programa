import csv

def listacsv(ll,nome,delimitador):
   try:
     with open(nome, "w") as output:
        writer = csv.writer(output, lineterminator='\n',delimiter=delimitador)
        writer.writerows(ll)
        print("CRIADO CSV")
   except:
     with open(nome, "w", encoding='utf-8') as output:
        writer = csv.writer(output, lineterminator='\n',delimiter=delimitador)
        writer.writerows(ll)
        print("CRIADO CSV")

