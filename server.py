import socket

global respond
respond = False

VERSION = 1

def firstResponder (data):
    if data == "GMNGAME-PN":
        message = "OPEN-PN"
        respond = True
    else:
        message = None

    return message

def secondResponder (data):
    guessNumber = int(data)
    if(guessNumber == number):
        message = "YES"
    elif (guessNumber > int(number)):
        message = "NO-"
    else:
        message = "NO+"
    print(guessNumber)
    return message


def start_server(host='0.0.0.0', port=8724):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((host, port))
    server.listen(1)
    print(f"Server listening on {host}:{port}")
    
    try:
        while True:
            client, addr = server.accept()
            print(f"Connection from {addr}")
            
            try:
                data = client.recv(1024)
                response = firstResponder(data.decode())
                if (response != None):
                    client.send(response.encode())
                while True:
                    data = client.recv(1024)
                    if(not data):
                        start()
                        break
                    response = secondResponder(data.decode())
                    if (response != None):
                        client.send(response.encode())
            finally:
                client.close()
    finally:
        server.close()

def start():
    global number
    number = int(input("\033[43;30mEnter a number:\033[0m "))


if __name__ == "__main__":
    start()
    try:
        start_server()
    except KeyboardInterrupt:
        exit(0)
    except Exception as e:
        print("Error: ", e)