import csv

def listacsv(ll,nome,delimitador):

    with open(nome, "w") as output:
        writer = csv.writer(output, lineterminator='\n',delimiter=delimitador)
        writer.writerows(ll)
        print("CRIADO CSV---"+str(nome))


