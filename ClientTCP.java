import java.io.*;
import java.net.*;
import java.util.Scanner;

public class ClientTCP {
    public static void main(String[] args) throws Exception {
        String host = "IP_SERVER"; // pune IP-ul colegului
        int port = 5000;

        Socket socket = new Socket(host, port);

        BufferedReader in = new BufferedReader(
                new InputStreamReader(socket.getInputStream(), "UTF-8"));
        BufferedWriter out = new BufferedWriter(
                new OutputStreamWriter(socket.getOutputStream(), "UTF-8"));

        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.print("Tu: ");
            String msg = scanner.nextLine();

            out.write(msg + "\n");
            out.flush();

            if (msg.equalsIgnoreCase("exit")) break;

            String response = in.readLine();
            System.out.println("Server: " + response);

            if (response.equalsIgnoreCase("exit")) break;
        }

        socket.close();
    }
}