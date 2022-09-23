import socket

host = "158.39.162.171"
port = 9797

serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_socket.bind((host, port))

serv_socket.listen()
print("Server: Listening on port " + str(port))

cl_socket, address = serv_socket.accept()
print("Server: Connection established with", address)

run = True
while run:
    
    text = input("Enter your message (Type exit to close) \n")
    if text == "exit":
    	run = False
    	break
    
    cl_socket.send(text.encode())
    
    message = cl_socket.recv(1024).decode()
    
    if message == "exit":
    	print("Server: Socket closed")
    	cl_socket.close()
    	run = False
    else:
    	print("Server: ", message)
    

print("Server: Closing socket...")
cl_socket.close()
print("Server: Socket closed.")
