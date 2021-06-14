#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   app.py
@Time    :   2021/06/11 16:54:02
@Author  :   xianglun xu 
@Contact :   xianglun918@qq.com
'''

# logging is safe for concurrent computing 
import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime
from aiohttp import web

# Define the HTML page 
def index(request):
    return web.Response(body=b'<h1>Awesome</h1>', content_type='text/html')

# Changed from old version @asyncio.coroutine to async def 
async def init(loop):
    app = web.Application(loop=loop)  # Removed loop=loop (is deprecated.) Not chnaged now for safety. (will update after all project finished.)
    app.router.add_route('GET', '/', index)
    appRunner = web.AppRunner(app)
    # Changed from old version yield from to await
    await appRunner.setup()
    srv = await loop.create_server(appRunner.server, '127.0.0.1', 9000)
    logging.info('Server started at http://127.0.0.1:9000')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()