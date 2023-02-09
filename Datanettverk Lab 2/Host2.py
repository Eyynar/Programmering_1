import socket

host = "158.39.162.171"
port = 9797

serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_socket.bind((host, port))

serv_socket.listen()
print("Server: Listening on port " + str(port))

cl_socket, address = serv_socket.accept()
print("Server: Connection established with", address)

# While-løkke som kun kjører mens run = True
run = True
while run:

    # Prompt til meldingen som skal sendes
    text = input("Enter your message (Type exit to close) \n")
    # Skrives det 'exit', vil socketen lukkes, og programmet avsluttes
    if text == "exit":
        run = False
        break

    # Meldingen sendes til socketen på mottagermaskinen
    cl_socket.send(text.encode())

    # Nå sjekkes det om det er noen meldinger som har blitt sendt tilbake
    message = cl_socket.recv(1024).decode()

    # Hvis den mottatte meldingen var 'exit', stenges socketen på denne siden, ellers skrives meldingen ut
    if message == "exit":
        print("Server: Socket closed")
        cl_socket.close()
        run = False
    else:
        print("Server: ", message)

# Socket lukkes
cl_socket.close()
print("Server: Socket closed.")
