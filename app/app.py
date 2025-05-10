from flask import Flask, request
from flask_cors import CORS
from kerykeion import KerykeionChartSVG, AstrologicalSubject

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    '''identify the service'''
    return 'Ceu Interior - API Lua'


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
        geonames_username="andreideholte",
        perspective_type="True Geocentric"
    )

    chart = KerykeionChartSVG(pessoaAstrologica, chart_language="PT")
    template = chart.makeTemplate()

    return template

if __name__ == '__main__':
    app.run(debug=True)
