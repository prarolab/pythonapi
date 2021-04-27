#!/usr/bin/env python
# encoding: utf-8
from flask import Flask, request 
from flask_restful import Api, Resource
import unicodedata

app = Flask(__name__)
api = Api(app)

api.app.config['RESTFUL_JSON'] = {
    'ensure_ascii': False
}

dicts = {}
company_char= chr(169)
#c= unicodedata.lookup('Copyright sign')

company = ["Microsoft", "Oracle","Google", "Amazon", "Deloitte"]
for k in company:
    company_symbol = k + company_char
    dicts[k] = company_symbol

class replace_string(Resource):
    def get(self,text):
        for i, j in dicts.items():
            text = text.replace(i, j)
        return {"data": text}

api.add_resource(replace_string,"/replace/<string:text>")
if __name__ == "__main__":
    app.run(debug=True)


