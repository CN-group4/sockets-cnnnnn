# Connection TCP între două mașini folosind Tailscale

import socket

# Configurația serverului
HOST = '100.90.140.60'  # Ex: '100.115.92.14'. Pune adresa copiată din aplicația Tailscale!
PORT = 65432                  # Portul pe care ascultăm (Studentul B se va conecta aici)

# Crearea socket-ului TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print(f"Pornire server pe IP-ul Tailscale {HOST}:{PORT}...")
    
    # 1. BIND: Asociem socket-ul cu adresa IP de Tailscale și portul
    s.bind((HOST, PORT))
    
    # 2. LISTEN: Serverul așteaptă conexiuni
    s.listen()
    print("Serverul ascultă și așteaptă conexiunea de la Studentul B...")
    
    # 3. ACCEPT: Acceptăm conexiunea când Studentul B se conectează
    conn, addr = s.accept()
    with conn:
        print(f"Conexiune TCP realizată cu succes! Client conectat de la adresa Tailscale: {addr}")
        
        # Așteptăm să primim date (mesajul) de la client
        data = conn.recv(1024)
        
        if data:
            # 4. DECODIFICARE: Transformăm byții în text folosind UTF-8
            mesaj_text = data.decode('utf-8')
            print(f"Mesaj primit de la client: {mesaj_text}")
        else:
            print("Clientul s-a conectat, dar nu a trimis niciun date.")