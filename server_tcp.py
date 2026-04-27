import socket

HOST = '0.0.0.0'
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print("Server pornit, astept conexiune...")

conn, addr = server.accept()
print(f"Conectat cu {addr}")

while True:
    data = conn.recv(1024).decode('utf-8')
    if not data:
        break

    print("Client:", data)

    if data.lower() == "exit":
        break

    msg = input("Tu: ")
    conn.send(msg.encode('utf-8'))

    if msg.lower() == "exit":
        break

conn.close()
server.close()
print("Conexiune inchisa.")