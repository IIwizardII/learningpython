import os
import asyncio
import time

async def func():
    print("started: ", time.strftime('%X'))
    print("something")
    await asyncio.sleep(1)
    print("else")
    print("started: ", time.strftime('%X'))
    
    
def random_function():
    print("inside random function")
    asyncio.run(func())
    print("ending")

random_function()



