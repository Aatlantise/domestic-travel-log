from flask import Flask
from datetime import datetime
import json


app = Flask(__name__)

def retrieve_records():
    '''
    Read user records from .tsv or .json file
    '''
    with open('hyun.log', 'r') as myfile:
        data=myfile.read()

    # parse file
    obj = json.loads(data)

    out_text = '&#9;'.join(["Datetime", "Type", "Number", "Origin", "Destination", "Duration", "Cost"])
    out_text += "<br/>"

    for item in obj["items"]:
        #item["datetime"] = datetime.strptime(item["datetime"], '%b %d %Y %I:%M%p')

        out_text += '&#9;'.join([v for k, v in item.items()])
        out_text += "<br/>"

    return out_text


def add_record():
    '''
    Add travel item
    '''

def remove_record():
    '''
    Remove travel item
    '''

def edit_record():
    '''
    edit travel item
    '''

@app.route("/")
def main():
    obj = retrieve_records()
    return obj
    
if __name__ == "__main__":
    app.run(debug=True)