'''
Created on 8 de nov de 2016

@author: ze
'''
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, jsonify, Response, send_from_directory
import json


app = Flask(__name__)
app.config['DEBUG'] = True
app.config.from_object(__name__)

# Configuracoes do Banco de Dados
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'pedidos.db')))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

#########################################################
##### INICIO DO BLOCO DAS FUNCOES DO BANCO DE DADOS #####
#########################################################
def bd_conecta():
    """Conecta ao banco de dados especificado."""
    if not hasattr(g, 'sqlite_db'):
        rv = sqlite3.connect(app.config['DATABASE'])
        rv.row_factory = sqlite3.Row
        g.sqlite_db = rv
    return g.sqlite_db

@app.teardown_appcontext
def bd_fechar(error):
    """Fecha o Banco de Dados ao Fim da Requisicao."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@app.cli.command('initdb')
def bd_iniciar():
    """Inicia a Conexao com o Banco de Dados."""
    db = bd_conecta()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

def bd_adicionar_mensagem(lanche,mesa):
    db = bd_conecta()
    
    db.execute("insert into pedidos values(NULL,\'"+lanche+"\',\'"+mesa+"\');")
    db.commit()
    
###SITE##

@app.route('/adicionar')
def adiciona_mensagem():
    if 'lanche' in request.args and 'bebida' in request.args and 'adicional' in request.args and 'mesa' in request.args:
        
        gerenciador(request.args['lanche'], request.args['bebida'], request.args['adicional'],request.args['mesa'])
        return "SIM"
    else:
        return "NAO"
    


def gerenciador(lanche,bebida,adicional,mesa):
    if "$" in adicional:
        novo=adicional.split("$")
        
        for i in novo:
            if "lanche" in i:
                Gerencia_Lanche(lanche,mesa,i)
            if "porcao" in i:
                Gerenciador_Adicional_Porcao(i,mesa)
    else:
        if "lanche" in adicional:
            Gerencia_Lanche(lanche,mesa,adicional)
        elif "porcao" in adicional:
            Gerenciador_Adicional_Porcao(adicional,mesa)
            Gerencia_Lanche(lanche,mesa,adicional)
        
    
def Gerencia_Lanche(lanche,mesa,adicional):
    quantidade_de_tipos_lanche=1
    Mqntd={}
    if "$"in lanche:
        for i in lanche:
            if i == "$":
                quantidade_de_tipos_lanche+=1
    if quantidade_de_tipos_lanche == 1:
        qntd=lanche.split("_")
        Mqntd[qntd[0]]=qntd[1]
    if quantidade_de_tipos_lanche >=2:
        ale=lanche.split("$")
        for i in range(len(ale)):
            g=ale[i]
            novo=g.split("_")
            Mqntd[novo[0]]=novo[1]
    
    Adiciona_Lanche(Mqntd,mesa,adicional)
        
def Gerenciador_Adicional_Lanche(adicional):
    adic="i"
    print adicional
    if "lanche"in adicional:
        novo= adicional.split("!")
        mesa=novo[0].split("-")
        lanche=novo[1]
        mesa=mesa[0]
        adicio=novo[2]
        adicio=adicio.split("_")
        adic=adicio[0]+" em "+adicio[1]+" lanche."
    else:
        lanche=" "
    return adic,lanche


    
def Adiciona_Lanche(dics,mesa,adicional):
    adic,lc=Gerenciador_Adicional_Lanche(adicional)
    a=" "
    if adic != "i":
        a=adic
    for i in dics:
        if lc == i:
            lanche= dics[i]+"x"+ " de "+i + " "+a
            bd_adicionar_mensagem(lanche,mesa)
        else:
            lanche= dics[i]+"x"+ " de "+i
            bd_adicionar_mensagem(lanche,mesa)



def Gerenciador_Adicional_Porcao(adicional,mesa):
    quantidade_de_tipos_porc=0
    Mqntd={}
    for i in adicional:
        if i == "!":
            quantidade_de_tipos_porc+=1
    
    if "porcao" in adicional:
        if quantidade_de_tipos_porc==1:
            novo= adicional.split("!")
            mesa=novo[0].split("-")
            mesa=mesa[0]    
            porc=novo[1]
            porcao=porc.split("_")
            tamanho=porcao[1]
            qntd=porcao[2]
            porcao=porcao[0]
            
            adic=porcao+" Tamanho: "+tamanho
            Mqntd[adic]=qntd
            Adiciona_porc(Mqntd,mesa)
        if quantidade_de_tipos_porc>=2:
            novo= adicional.split("!")
            mesa=novo[0].split("-")
            mesa=mesa[0]
            for i in novo:
                if "porcao" not in i:
                    porcao=i.split("_")
                    tamanho=porcao[1]
                    qntd=porcao[2]
                    porcao=porcao[0]
                    adic=porcao+" Tamanho: "+tamanho
                    Mqntd[adic]=qntd
            
            Adiciona_porc(Mqntd,mesa)
         
def Adiciona_porc(dics,mesa):
    for i in dics:
        print i," cxhjsdbngklsdabgjkasdbvsdjkvbsd"
        lanche= dics[i]+"x"+ " de "+i
        
        bd_adicionar_mensagem(lanche,mesa)
        
 
        
            
        
        

            
        
        
                        
if __name__ == "__main__":
    app.run(host='10.42.0.1', port=80)

