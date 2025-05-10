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

    personal_data = request.json

    print('Creating natal chart for', personal_data['name'])

    astrological_subject = AstrologicalSubject(
        personal_data['name'], 
        int(personal_data['year']), 
        int(personal_data['month']), 
        int(personal_data['day']), 
        int(personal_data['hour']), 
        int(personal_data['minute']), 
        personal_data['location'], 
        personal_data['countryCode'], 
        geonames_username="demo",
        perspective_type="True Geocentric",

    )

    chart = KerykeionChartSVG(astrological_subject, chart_language="PT", chart_type=chartType)
    template = chart.makeTemplate()

    return template

if __name__ == '__main__':
    app.run(debug=True)
