import db
import plugins

async def tap(args, msObject):
    await msObject.channel.send(args)
