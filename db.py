import os
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
        if getRec:
            return i['id']
        if i['fields']['keys']==keysValue:
            if path !="":
                return keysValue[path]
            else:
                return i['fields']['values']

async def update(keysValue, valuesValue):
    
    at.update("main")

async def create(keysValue, valuesValue):
    at.create("main",{
    "fields": {
      "keys": keysValue,
      "values": str(valuesValue)
    }
  })

async def destroy(keysValue):
    pass