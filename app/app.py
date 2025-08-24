from flask import Flask, request, jsonify
from flask_cors import CORS
from kerykeion import KerykeionChartSVG, AstrologicalSubject
import re
from pathlib import Path

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    '''identify the service'''
    return 'Ceu Interior - API Lua'

def is_chart_type_valid(var):
  """
  Checks if a chart type is considered "valid" in this context.
  This might include checking for None or empty strings.
  """
  if var is None:
      return False
  if not isinstance(var, str):
      return False
  return True

@app.route('/chart/<chartType>', methods=['POST'])
def create_map(chartType):
    if not is_chart_type_valid(chartType):
        return jsonify({"error": "The 'chartType' parameter is missing or invalid."}), 400

    if chartType not in ['Natal'] : 
        return jsonify({"error": "Sorry, the 'chartType' parameter is not supported yet."}), 404

    #print(request.json)
    
    fields = request.json['fields']
    
    # Encontrar os campos pelos seus IDs
    name = None
    date = None
    fullHour = None
    location = None
    country = None
    
    for field in fields:
        if field['fieldName'] == 'nome_completo':
            name = field['fieldValue']
        elif field['fieldName'] == 'data_nascimento':
            # Formato esperado: "1993-01-24T02: 00: 00.000Z"
            date_str = field['fieldValue'].replace(' ', '')
            date = date_str.split('T')[0]  # Pega apenas a parte da data
        elif field['fieldName'] == 'Hora de Nascimento':
            # Formato esperado: "07: 35: 00.000"
            fullHour = field['fieldValue'].replace(' ', '')
        elif field['fieldName'] == 'local_nascimento':
            location_data = field['fieldValue']
            location = location_data['formatted']
            country = location_data['country']
    
    print('Creating natal chart for', name)

    # Extrair ano, mês e dia da data
    [year, month, day] = date.split('-')
    
    # Extrair hora e minuto
    hour_parts = fullHour.split(':')
    hour = hour_parts[0]
    minute = hour_parts[1]

    astrological_subject = AstrologicalSubject(
        name,
        int(year),
        int(month),
        int(day),
        int(hour),
        int(minute),
        location,
        country,
        geonames_username="andreideholte",
        perspective_type="True Geocentric",
    )

    chart = KerykeionChartSVG(
        astrological_subject,
        chart_language="PT",
        chart_type=chartType,
        new_settings_file=Path(Path(__file__).parent / "custom_settings.json")
    )
    template = chart.makeTemplate()
    
    # Pós-processamento do SVG para remover "Pontos para <nome>"
    template = re.sub(r'<text[^>]*>Pontos para [^<]*</text>', '', template)
    template = re.sub('Saturn_comp-mees4pd8o', 'Saturno', template)
    
    return jsonify({'chart': template})

if __name__ == '__main__':
    app.run(debug=True)
