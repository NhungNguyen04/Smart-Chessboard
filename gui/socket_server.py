import asyncio
import socketio
import aiohttp

sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins=['http://localhost:8080'])
app = socketio.ASGIApp(sio)

@sio.event
async def connect(sid, environ):
    print(f'Client connected: {sid}')

@sio.event
async def disconnect(sid):
    print(f'Client disconnected: {sid}')

@sio.event
async def opponentMove(sid, data):
    game_id = data.get('gameId')
    move = data.get('move')
    print(f'Received move from client {sid}: Game ID: {game_id}, Move: {move}')
    
    # Send move to GUI using HTTP POST request
    async with aiohttp.ClientSession() as session:
        async with session.post('http://localhost:8000/move', json={'move': move}) as response:
            if response.status == 200:
                print("Move sent to GUI successfully")
            else:
                print("Failed to send move to GUI")

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=5000)

