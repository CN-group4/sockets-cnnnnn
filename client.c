//Misiunea B: Fluxul UDP (Fără conexiune)
//Modificați scripturile pentru a utiliza socket-uri de tip Datagram (UDP).
//Clientul va transmite un flux rapid de 100 de mesaje numerotate.
//Test de fiabilitate: În timpul transmisiei, unul dintre studenți va dezactiva temporar interfața de rețea pentru a observa pierderea pachetelor la destinație.

#include <stdio.h>
#include <winsock2.h>

#pragma comment(lib, "ws2_32.lib")

#define PORT 65432

int main() {
    WSADATA wsa;
    SOCKET sock;
    struct sockaddr_in server;
    char message[100];

    WSAStartup(MAKEWORD(2,2), &wsa);

    sock = socket(AF_INET, SOCK_DGRAM, 0);

    server.sin_family = AF_INET;
    server.sin_port = htons(PORT);
    server.sin_addr.s_addr = inet_addr("100.90.140.60"); // IP Tailscale server

    for (int i = 1; i <= 100; i++) {
        sprintf(message, "Mesaj %d", i);

        sendto(sock, message, strlen(message), 0,
               (struct sockaddr*)&server, sizeof(server));

        printf("Trimis: %s\n", message);
    }

    closesocket(sock);
    WSACleanup();
    return 0;
}