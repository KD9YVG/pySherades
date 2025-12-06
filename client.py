import socket

def connect_to_server(host='0.0.0.0', port=8724):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    print(f"Connected to {host}:{port}")
    
    try:
        while True:
            message = input("Enter message (or 'quit' to exit): ")
            if message.lower() == 'quit':
                break
            client.send(message.encode())
            response = client.recv(1024)
            print(f"Server response: {response.decode()}")
    finally:
        client.close()

if __name__ == "__main__":
    connect_to_server()