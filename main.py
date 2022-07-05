from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
  return render_template('index.html')
  
@app.route('/<materia>')
def assuntos(materia):
  if materia == '1':
     return jsonify({'Matematica':'Funcoes-Nocoes basicas de estatistica-Probabilidade-Analise Combinatoria-Circunferencias-Equacoes do segundo grau e inequacoes-Logaritmos'})
  elif materia == '2':
    return jsonify({'Fisica':'Energia-Mecanica-Eletricidade-Optica-Termofisica-Leis de Newton-Correntes e potencia eletrica-Fenomenos ondulatorios'})
  elif materia == '3':
    return jsonify({'Biologia':'Moleculas, celulas e tecidos-Hereditariedade e diversidade da vida-Identidade dos seres vivos-Ecologia e ciencias ambientais-Origem e evolucao da vida-Qualidade de vida das populacoes humanas'})
  elif materia == '4':
    return jsonify({'Sociologia':'Cultura-Cidadania-Movimentos Sociais-Politica, Estado e Governo-Revolucao Cientifica e Industrial-Sociedade Contemporanea-Teorias Sociologicas'})
  elif materia == '5':
    return jsonify({'Filosofia':'Filosofia Antiga-Filosofia Medieval/Crista-Filosofia Moderna-Filosofia Contemporanea'})
  elif materia == '6':
    return jsonify({'Historia':'Organizacao social-Movimentos sociais-Pensamento politico e acao do Estado-Fordismo, toyotismo, as novas tecnicas de producao e seus impactos-Industrializacao brasileira, urbanizacao e transformacoes sociais e trabalhistas-Globalizacao e tecnologias de comunicacao'})
  elif materia == '7':
    return jsonify({'Geografia':'Questoes Ambientais-Urbanizacao-Globalizacao-Geografia Agraria-Industrializacao-Climatologia-Cartografia'})
  elif materia == '8':
    return jsonify({'Literatura':'O Cortico-Dom Casmurro-Vidas Secas-Iracema-Memorias Postumas de Bras Cubas-Grande Sertao: Veredas-A Moreninha'})

app.run(host='0.0.0.0')