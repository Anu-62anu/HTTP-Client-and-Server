import socket

def send_request(host='localhost', port=9091, method='GET'):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    
    request = f"{method} / HTTP/1.1\r\nHost: localhost\r\n\r\n"
    client.send(request.encode())
    
    response = client.recv(4096).decode()
    print(f"Received response: {response}")

    client.close()

if __name__ == "__main__":
    send_request(method='POST')
