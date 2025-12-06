import socket

VERSION = 1

def connect_to_server(host='127.0.0.1', port=8724):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    print(f"Connected to {host}:{port}")
    
    try:
        message = "GMNGAME-PN"
        client.send(message.encode())
        response = client.recv(1024)
        if response.decode() != "OPEN-PN":
            client.close()
            return
        while True:
            guess = input("Guess a number: ")
            client.send(guess.encode())
            response = client.recv(1024)
            if response.decode() == "YES":
                print("\U0001f44d Great job!")
                client.close()
                break
            elif response.decode() == "NO-":
                print("To high.")
            else:
                print("To low")
    finally:
        client.close()

if __name__ == "__main__":
    ip = input("IP address (port 8724): ")
    connect_to_server(ip)