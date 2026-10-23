import asyncio

async def verificar_rh():
    await asyncio.sleep(1)
    return {"nome": "RH", "status": "OK"}

async def verificar_auth():
    await asyncio.sleep(1)
    return {"nome": "Auth", "status": "OK"}

async def verificar_backup():
    await asyncio.sleep(1)
    return {"nome": "Backup", "status": "OK"}