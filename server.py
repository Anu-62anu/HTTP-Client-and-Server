import socket

def handle_client(client_socket):
    request = client_socket.recv(1024).decode()
    print(f"Received request: {request}")

    if "GET" in request:
        response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"
        response += "<html><body><h1>Hello, World!</h1></body></html>"
    elif "POST" in request:
        response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"
        response += "<html><body><h1>POST request received!</h1></body></html>"
    else:
        response = "HTTP/1.1 405 Method Not Allowed\r\nContent-Type: text/html\r\n\r\n"
        response += "<html><body><h1>Method Not Allowed</h1></body></html>"

    client_socket.send(response.encode())
    client_socket.close()


def start_server(host='localhost', port=9091):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"Server listening on {host}:{port}")
    
    while True:
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr}")
        handle_client(client_socket)

if __name__ == "__main__":
    start_server()
