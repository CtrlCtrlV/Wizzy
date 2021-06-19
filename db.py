import os
import json
from airtable import Airtable
BASEID = os.environ['DBKEY']
BASEKEY = os.environ['DBPASS']
at = Airtable(BASEID, "main",BASEKEY)

async def fetch(keysValue, path="", getRec=False):
    results = at.get_all(view="Grid view")
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
                return x['id']
            if path !="":
                return json.loads(i['fields']['values'])[path]
            else:
                return x['fields']['values']

async def update(keysValue, valuesValue):
    compFields = {
        'values':valuesValue,
    }
    at.update(await fetch(keysValue,'',True),compFields)

async def create(keysValue, valuesValue):
    compFields = {
        'keys':keysValue,
        'values':valuesValue
    }
    at.insert(compFields)

async def destroy(keysValue):
    at.delete(await fetch(keysValue,'',True))