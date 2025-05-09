from flask import Flask, request, jsonify
from flask_cors import CORS
from kerykeion import KerykeionChartSVG, AstrologicalSubject

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    '''identify the service'''
    return 'Fernanda Hay - Mapa Astral API'


@app.route('/mapas/natal', methods=['POST'])
def criarmapa() :
    dadosPessoais = request.json

    print ('mapanatal - criando mapa', dadosPessoais['nome'])

    pessoaAstrologica = AstrologicalSubject(
        dadosPessoais['nome'], 
        int(dadosPessoais['ano']), 
        int(dadosPessoais['mes']), 
        int(dadosPessoais['dia']), 
        int(dadosPessoais['hora']), 
        int(dadosPessoais['minuto']), 
        dadosPessoais['local'], 
        dadosPessoais['pais'], 
        tz_str="America/Sao_Paulo"
    )
    
    chart = KerykeionChartSVG(pessoaAstrologica)
    template = chart.makeTemplate()

    print ('mapanatal - finalizado mapa', dadosPessoais['nome'])

    return template

if __name__ == '__main__':
    app.run(debug=True)
