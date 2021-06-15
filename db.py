import os
from airtable import airtable
at = airtable.Airtable('BASE_ID', 'API_KEY')
BASEID = os.environ['DBKEY']
BASEKEY = os.environ['DBPASS']

def fetch(keysValue, path=""):
    return at.get("main")['fields'][keysValue]

def update(keysValue, valuesValue):
    
    at.update("main")

def create(keysValue, valuesValue):
    pass

def destroy(keysValue):
    pass