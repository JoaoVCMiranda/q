import asyncio
import websockets

from concurrent.futures import ThreadPoolExecutor

# Set of connected clients
connected_clients = set()
input_executor = ThreadPoolExecutor(max_workers=1)

async def get_async_input_executor(prompt: str = "") -> str:
    """
    Asynchronously gets input from the console using loop.run_in_executor.
    """
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(input_executor, input, prompt)

async def chat_client_example_executor():
    print("Welcome to the async chat client (using executor)!")
    while True:
        try:
            message = await get_async_input_executor("Enter message: ")
            print(f"You entered: {message}")
            for client in connected_clients:
                await client.send(message)
            if message.lower() == 'exit':
                break
        except Exception as e:
            print(f"An error occurred during input: {e}")
            break
    # It's good practice to shut down the executor when done
    input_executor.shutdown(wait=True)

# Function to handle each client connection
async def handle_client(websocket):
    # Add the new client to the set of connected clients
    connected_clients.add(websocket)
    try:
        # Listen for messages from the client
        async for message in websocket:
            print(message)
            # Broadcast the message to all other connected clients
            #for client in connected_clients:
            #    if client != websocket:
            #        await client.send(message)
    except websockets.exceptions.ConnectionClosed:
        pass
    finally:
        # Remove the client from the set of connected clients
        connected_clients.remove(websocket)

# Main function to start the WebSocket server
async def start():
    server = await websockets.serve(handle_client, 'localhost', 6789)
    await chat_client_example_executor()
    await server.wait_closed()

# Run the server
if __name__ == "__main__":
    asyncio.run(start())