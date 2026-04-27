import socket

# Configurația serverului (Folosește același IP de Tailscale de la misiunea precedentă)
HOST = '100.90.140.60'  
PORT = 65432                 

# Crearea socket-ului UDP (AF_INET = IPv4, SOCK_DGRAM = UDP)
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    # BIND: Asociem socket-ul cu adresa și portul
    s.bind((HOST, PORT))
    print(f"Serverul UDP a pornit pe {HOST}:{PORT} și așteaptă mesaje...")
    
    # Buclem la infinit pentru a prinde tot fluxul de mesaje
    while True:
        # Nu mai există s.listen() sau s.accept()!
        # Primim datele direct și adresa celui care le-a trimis
        data, addr = s.recvfrom(1024)
        
        # Decodificăm textul conform cerinței UTF-8
        mesaj_text = data.decode('utf-8')
        print(f"Primit de la {addr}: {mesaj_text}")