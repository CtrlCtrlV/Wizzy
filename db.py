import os
import json
from utils import *
from airtable import Airtable
BASEID = os.environ['DBKEY']
BASEKEY = os.environ['DBPASS']
at = Airtable(BASEID, "main",BASEKEY)

async def fetch(keysValue, path="", getRec=False):
    log("DBCall [FETCH] > received")
    log("DBCall [FETCH] > tapping into database")
    results = at.get_all(view="Grid view")
    log("DBCall [FETCH] > data received")
    """
    [
    {
        'id':'recfxTLjmeboQGHVE',
        'fields':{
            'values':"{'tapOn':'hello'}",
            'keys':'tap'
        },
        'createdTime':'2021-06-15T03:44:28.000Z'
    },
    {
        'id':'recPSxGVr6tNHCO6w',
        'fields':{
            'values':'{"verboseConsole":"false"}',
            'keys':'configs'
        },
        'createdTime':'2021-06-15T03:44:28.000Z'
    },
    {
        'id':'reczPepwpiSLl4OrD',
        'fields':{
            'values':'{"wizVersion":"WD1.0.0", "plugins":[ { "name":"defaultPlugin", "version":"1.0.0", "referral":"rec123434" } ] }',
            'keys':'versionControl'
        },
        'createdTime':'2021-06-15T03:44:28.000Z'
    }
]
    """
    for i in results:
        x = i
        if x['fields']['keys']==keysValue:
            if getRec:
                log("DBCall [FETCH] > formatting data for ID")
                log("DBCall [FETCH] > successfully handled")
                return x['id']
            if path !="":
                log("DBCall [FETCH] > formatting data for given path")
                log("DBCall [FETCH] > successfully handled")
                return json.loads(i['fields']['values'])[path]
            else:
                log("DBCall [FETCH] > skipping data formatting (no path provided)")
                log("DBCall [FETCH] > successfully handled")
                return x['fields']['values']

async def update(keysValue, valuesValue):
    log("DBCall [UPDATE] > received")
    compFields = {
        'values':valuesValue,
    }
    log("DBCall [UPDATE] > tapping into database")
    at.update(await fetch(keysValue,'',True),compFields)
    log("DBCall [UPDATE] > database responsive")
    log("DBCall [UPDATE] > successfully handled")

async def create(keysValue, valuesValue):
    log("DBCall [CREATE] > received")
    compFields = {
        'keys':keysValue,
        'values':valuesValue
    }
    log("DBCall [CREATE] > tapping into database")
    at.insert(compFields)
    log("DBCall [CREATE] > database responsive")
    log("DBCall [CREATE] > successfully handled")

async def destroy(keysValue):
    log("DBCall [DESTROY] > received")
    log("DBCall [DESTROY] > tapping into database")
    at.delete(await fetch(keysValue,'',True))
    log("DBCall [DESTROY] > database responsive")
    log("DBCall [DESTROY] > successfully handled")