import socket

cl_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "158.39.162.171"
port = 9797

print("Client: Connecting to", host, "on port", port, "...")

cl_socket.connect((host, port))
run = True
while run:
    message = cl_socket.recv(1024).decode()
    if message == "exit":
        run = False
    else:
        print("Server:", message)

    text = input("Enter your message (Type exit to close) \n")
    if text == "exit":
        run = False

    cl_socket.send(text.encode())

print("Server: Socket closed")
cl_socket.close()