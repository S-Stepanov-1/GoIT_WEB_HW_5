import asyncio
import logging
import websockets
import json
import main as main_program
from websockets import WebSocketServerProtocol
from websockets.exceptions import ConnectionClosedOK

logging.basicConfig(level=logging.INFO)


class Server:
    clients = set()

    async def register(self, ws: WebSocketServerProtocol):
        self.clients.add(ws)
        logging.info(f'{ws.remote_address} connects')

    async def unregister(self, ws: WebSocketServerProtocol):
        self.clients.remove(ws)
        logging.info(f'{ws.remote_address} disconnects')

    async def send_to_clients(self, message: str):
        if self.clients:
            [await client.send(message) for client in self.clients]

    async def ws_handler(self, ws: WebSocketServerProtocol):
        await self.register(ws)
        try:
            await self.distrubute(ws)
        except ConnectionClosedOK:
            pass
        finally:
            await self.unregister(ws)

    async def distrubute(self, ws: WebSocketServerProtocol):
        async for message in ws:

            #   === Additional task №2 in HW 5 ===
            words = message.split()
            if words[0] == "exchange":
                answer_data_list = await main_program.main(x_days=1)
                await self.send_to_clients(json.dumps(answer_data_list))
            #   =====================================================
            else:
                await self.send_to_clients(message)


async def main():
    server = Server()
    async with websockets.serve(server.ws_handler, 'localhost', 4540):
        await asyncio.Future()  # run forever

if __name__ == '__main__':
    asyncio.run(main())
