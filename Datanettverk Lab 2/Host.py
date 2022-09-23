import socket

host = "192.168.5.145"
port = 9798

serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_socket.bind((host, port))

serv_socket.listen()
print("Server: Listening on port " + str(port))

cl_socket, address = serv_socket.accept()
print("Server: Connection established with", address)

run = True
while run:

    text = input("Enter your message (exit to close) \n")
    if text == "exit":
        run = False

    cl_socket.send(text.encode())

print("Server: Closing socket...")
cl_socket.close()
print("Server: Socket closed.")