from flask import Flask, render_template,request
import programa.CAPACIDADE as CAP
import programa.RANKING_MUNICIPIO as RANK
import programa.SILO_BAG as SILO
import programa.WEB as WEB
import programa.CARTOGRAMA as CART
import programa.BRASIL as BR
import programa.UFS as UFS




lista_ano=["2017","2018",
           "2019","2020",
           "2021","2022",
           "2023","2024",
           "2025","2026",
           "2027","2028"]

lista_mes=["janeiro","fevereiro","março",
           "abril","maio","junho",
           "julho","agosto","setembro",
           "outubro","novembro","dezembro"]

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


app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tabulacao")
def tabulacao():
    return render_template("tabulacao.html")

@app.route("/apuracao")
def apuracao():
    return render_template("apuração.html")

@app.route("/brasil", methods=["GET","POST"])
def brasil():
    return render_template("brasil.html",lano=lista_ano)

@app.route("/uf", methods=["GET","POST"])
def uf():
    return render_template("uf.html",lano=lista_ano,lgeo=lista_geo)

@app.route("/tufs", methods=["GET","POST"])
def tufs():
    return render_template("tufs.html",lano=lista_ano)

@app.route("/ufcheck", methods=["GET","POST"])
def ufcheck():
    return render_template("ufcheck.html",lano=lista_ano,lgeo=lista_geo)

@app.route("/ufcheck_exec", methods=["GET","POST"])
def ufcheck_exec():
     sem= request.form.get('SEMES')
     ano= request.form.get('SANO')
     l_geo=request.form.getlist('SCHECK')
     for gg in l_geo:
         UFS.UF_GERADOR(gg,dufnome[gg],ano,sem)
     return("Apurado "+sem+" Semestre de "+ano+" nas UFs escolhidas")

@app.route("/brasil_exec", methods=["GET","POST"])
def brasil_exec():
     sem= request.form.get('SEMES')
     ano= request.form.get('SANO')
     BR.BR_GERENCIAR(ano,sem)
     return("Apurado "+sem+" Semestre de "+ano+" em nível Brasil")

@app.route("/uf_exec", methods=["GET","POST"])
def uf_exec():
     sem= request.form.get('SEMES')
     ano= request.form.get('SANO')
     geo= request.form.get('SGEO')
     UFS.UF_GERADOR(geo,dufnome[geo],ano,sem)
     return("Apurado "+sem+" Semestre de "+ano+" em nível de UF:"+geo)

@app.route("/tufs_exec", methods=["GET","POST"])
def tufs_exec():
     sem= request.form.get('SEMES')
     ano= request.form.get('SANO')
     for k,it in dufnome.items():
         UFS.UF_GERADOR(k,it,ano,sem)
     return("Apurado "+sem+" Semestre de "+ano+" em todas as UFs")

@app.route("/provisoria")
def provisoria():
        return render_template("provisoria.html",lmes=lista_mes,lano=lista_ano)

@app.route("/provisoria_exec", methods=["GET","POST"])
def provisoria_exec():
     sem= request.form.get('SEMES')
     ano= request.form.get('SANO')
     mes= request.form.get('SMES')
     CAP.APURAÇÃO(sem,int(ano),mes)
     return("Apurado "+sem+" Semestre de "+ano+" referente ao mês de "+mes)

@app.route("/ranking")
def ranking():
    return render_template("ranking.html",lano=lista_ano)

@app.route("/ranking_exec", methods=["GET","POST"])
def ranking_exec():
     sem= request.form.get('SEMES')
     ano= request.form.get('SANO')
     if sem=="Primeiro":
         sem_num=1
     elif sem=="Segundo":
         sem_num=2
     RANK.ARQCSVUF(sem_num,int(ano))
     return("Ranking Apurado para o "+sem+" Semestre de "+ano)



@app.route("/silo_bag")
def silo_bag():
    return render_template("silo_bag.html",lano=lista_ano)

@app.route("/silo_bag_exec", methods=["GET","POST"])
def silo_bag_exec():
     sem= request.form.get('SEMES')
     ano= request.form.get('SANO')
     SILO.APURAÇÃO(sem,int(ano))
     return("Capacidade Silo Bag apurada para o "+sem+" Semestre de "+ano)

@app.route("/mapas")
def mapas():
    return render_template("mapas.html",lano=lista_ano)

@app.route("/mapas_exec", methods=["GET","POST"])
def mapas_exec():
     sem= request.form.get('SEMES')
     ano= request.form.get('SANO')
     CART.GERAR(int(ano),sem)
     return("Cartogramas gerados para o "+sem+" Semestre de "+ano)

@app.route("/web")
def web():
    return render_template("web.html",lano=lista_ano)

@app.route("/web_exec", methods=["GET","POST"])
def web_exec():
     sem= request.form.get('SEMES')
     ano= request.form.get('SANO')
     if sem=="Primeiro":
         sem_num=1
     elif sem=="Segundo":
         sem_num=2
     WEB.APUR(int(ano),sem_num)
     return("Questionário WEB apurados para o "+sem+" Semestre de "+ano)



app.run()

    
    
