import asyncio
import socketio

# Allow connections from 'http://localhost:8080'
sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins=['http://localhost:8080'])
app = socketio.ASGIApp(sio)

# Initialize your chess game interface

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
    # Process the move in your chess game
    # result = chess_game.process_move(move)
    # Implement your logic here

# Entry point for running the server
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=5000)
