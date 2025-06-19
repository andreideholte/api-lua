from flask import Flask, request, jsonify
from flask_cors import CORS
from kerykeion import KerykeionChartSVG, AstrologicalSubject

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

    personal_data = request.json['data']

    name = personal_data['field:comp-mbwmkwa1']
    date = personal_data['field:comp-mbwn9mp2']
    fullHour = personal_data['field:comp-mc3i8u21']

    # some situations country may come in stateCountry variable, in this case we check if country is empty
    [ location, stateCountry, country ] = personal_data['field:comp-mbwmrv73'].split(',')

    if (country == ''):
        country = stateCountry

    if (country == 'Brasil'):
        country = 'BR'
    elif (country == 'EUA'):
        country = 'US'

    print('Creating natal chart for', name)

    [ year, month, day ] = date.split('-')
    [ hour, minute ] = fullHour.split(':')

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

    chart = KerykeionChartSVG(astrological_subject, chart_language="PT", chart_type=chartType)
    template = chart.makeTemplate()

    return jsonify({'chart': template})

if __name__ == '__main__':
    app.run(debug=True)
