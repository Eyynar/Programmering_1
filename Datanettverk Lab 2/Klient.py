import socket

cl_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "158.39.162.171"
port = 9797

print("Client: Connecting to", host, "on port", port, "...")

cl_socket.connect((host, port))

# While-løkke som kjører mens run = True
run = True
while run:
    # Henter melding som er sendt til socket
    message = cl_socket.recv(1024).decode()
    # Hvis meldingen er 'exit', avsluttes while-løkken
    if message == "exit":
        run = False
    else:
        # Ellers printes meldingen
        print("Server:", message)

    # Prompt for melding som skal sendes
    text = input("Enter your message (Type exit to close) \n")
    # Hvis meldingen som sendes er 'exit', avsluttes løkken
    if text == "exit":
        run = False

    # Medingen sendes til mottagermaskin
    cl_socket.send(text.encode())

# Når løkken er avsluttet, lukkes socketen.
print("Server: Socket closed")
cl_socket.close()
