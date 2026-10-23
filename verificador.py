import asyncio
from fastapi import FastAPI
from sistema import verificar_rh, verificar_auth, verificar_backup

app = FastAPI()

@app.get("/saude")
async def verificar_saude():
    resultado = await asyncio.gather(verificar_rh(), verificar_auth(), verificar_backup())
    return {"sistemas": resultado}