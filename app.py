import pandas as pd
import re
import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config['DEBUG'] = True

# Dictionary of regex patterns and their corresponding data type.
pattern_dict = {r'^(0?[1-9]|1[012])[- /.](0?[1-9]|[12][0-9]|3[01])[- /.](19|20)?[0-9]{2}$': 'date',   #MM/DD/YY(YY)
                r'^(0?[1-9]|[12][0-9]|3[01])[- /.](0?[1-9]|1[012])[- /.](19|20)?[0-9]{2}$': 'date',   #DD/MM/YY(YY)
                r'^(19|20)?[0-9]{2}[- /.](0?[1-9]|1[012])[- /.](0?[1-9]|[12][0-9]|3[01])$': 'date',   #YY(YY)/MM/DD
                r'^-?[0-9]+$': 'integer',
                #r'^-?[0-9]*\.?[0-9]+$': 'float',
                r'^-?([0-9]+|[0-9]{1,3}([,\ ][0-9]{3})+)((\.|,)[0-9]+)?$': 'float',
                #r'^\ *\$\ *[-+]?[0-9]*\.?[0-9]+\ *$': 'currency',
                r'^\ *(\$|USD|€|EUR|DKK|GBP|£|NOK|SEK)\ *-?([0-9]+|[0-9]{1,3}([,\ ]?[0-9]{3})+)((\.|,)[0-9]+)?\ *$': 'currency'
                }

# Homepage
@app.route('/', methods=['GET'])
def home():
    return "<h1>Content Type Wizard</h1><p>This is an API for returning the content type of a cell.</p>"

# Define 'get' endpoint
@app.route('/api/content_type.json', methods=['GET'])
def get_type():
    # Check if content was provided as part of the URL.
    if 'content' in request.args:
        cell = request.args['content']
    else:
        return 'Error: No content field provided. Please specify an input "content" parameter.'

    # Check if cell is empty and return null if so.
    if pd.isna(cell) or cell==' ':
        return jsonify({'type':''})
    
    # Convert the input into a string.
    content = str(cell)

    # Loop through pattern dictionary and search for patterns in order. 
    # If there is a match, return corresponding data type.
    for pattern, dtype in pattern_dict.items():
        if re.search(pattern, content):
            return jsonify({'type':dtype})
    
    # If there is no other match, return 'string' type.
    return jsonify({'type':'string'})


if __name__ == "__main__":
    app.run()