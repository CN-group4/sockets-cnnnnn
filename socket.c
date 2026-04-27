#include <stdio.h>
#include <winsock2.h>
//Misiunea A: Conexiunea TCP (Orientată pe conexiune)
//Studentul A (Server): Creează un socket TCP, realizează operația de Bind pe IP-ul ZeroTier și așteaptă conexiuni (Listen/Accept).
//Studentul B (Client): Inițializează o conexiune (Connect) către IP-ul serverului și transmite un mesaj text.
//Cerință: Utilizați codificarea UTF-8 pentru a asigura compatibilitatea textului între limbaje.

#pragma comment(lib, "ws2_32.lib")

#define PORT 65432

int main() {
    WSADATA wsa;
    SOCKET sock;
    struct sockaddr_in server;
    char *message = "salut!";

    // Inițializează Winsock
    WSAStartup(MAKEWORD(2,2), &wsa);

    // Creează socket
    sock = socket(AF_INET, SOCK_STREAM, 0);

    server.sin_family = AF_INET;
    server.sin_port = htons(PORT);
    server.sin_addr.s_addr = inet_addr("100.90.140.60"); // IP Tailscale

    // Conectare
    if (connect(sock, (struct sockaddr *)&server, sizeof(server)) < 0) {
        printf("Eroare conectare\n");
        return 1;
    }

    printf("Conectat!\n");

    // Trimite mesaj
    send(sock, message, strlen(message), 0);

    // Închidere
    closesocket(sock);
    WSACleanup();

    return 0;
}