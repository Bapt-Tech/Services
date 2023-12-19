###ModChatServer
###19/12/2023
###15:57
###Bapt-Tech

import socket
import threading
import re


def ChatServer_Main():
    
    def handle_client(client_socket, client_address):
        try:
            username = client_socket.recv(1024).decode('utf-8')

            print(f"{username} a rejoint le chat depuis {client_address[0]}:{client_address[1]}")

            # Demander à l'utilisateur de choisir un salon
            client_socket.send("Liste des salons : Salon1, Salon2".encode('utf-8'))
            selected_channel = client_socket.recv(1024).decode('utf-8')
            usernames.append(username)

            if selected_channel not in channels:
                channels[selected_channel] = []

            channels[selected_channel].append((username, client_socket))
            broadcast_message(f"{username} a rejoint le salon {selected_channel}", client_socket, selected_channel)

            while True:
                message = client_socket.recv(1024).decode('utf-8')
                if not message:
                    break
                if message.lower() == '/exit':
                    break
                if message.lower() == '/salonlist':
                    STRchannels = ' '.join(channels)
                    client_socket.send(f"{STRchannels}".encode('utf-8'))
                if message.lower() == '/users':
                    STRusernames = ' '.join(usernames)
                    client_socket.send(f"{STRusernames}".encode('utf-8'))
                elif message.startswith('/join'):
                    new_channel = message.split()[1]
                    if new_channel in channels:
                        channels[selected_channel].remove((username, client_socket))
                        selected_channel = new_channel
                        channels[selected_channel].append((username, client_socket))
                        client_socket.send(f"Vous avez rejoint le salon {selected_channel}".encode('utf-8'))
                    else:
                        client_socket.send(f"Le salon {new_channel} n'existe pas.".encode('utf-8'))
                elif message.startswith('@'):
                    recipient, _, message = message.partition(' ')
                    recipient = recipient[1:]  # Supprimer le @ du nom d'utilisateur du destinataire
                    send_private_message(username, recipient, message)
                else:
                    print(f"{username} ({selected_channel}): {message}")
                    broadcast_message(f"{username} ({selected_channel}): {message}", client_socket, selected_channel)
        except:
            print(f"Connexion perdue avec {client_address[0]}:{client_address[1]}")
        finally:
            if selected_channel in channels:
                channels[selected_channel].remove((username, client_socket))
            client_socket.close()

    def broadcast_message(message, sender_socket, channel):
        if channel in channels:
            for _, client_socket in channels[channel]:
                if client_socket != sender_socket:
                    try:
                        client_socket.send(message.encode('utf-8'))
                    except:
                        print("Erreur lors de l'envoi du message")

    def send_private_message(sender_username, recipient_username, message):
        recipient_socket = None
        for channel in channels.values():
            for username, client_socket in channel:
                if username == recipient_username:
                    recipient_socket = client_socket
                    break

        if recipient_socket is not None:
            private_message = f"(Message privé de {sender_username}): {message}"
            try:
                recipient_socket.send(private_message.encode('utf-8'))
            except:
                print("Erreur lors de l'envoi du message privé")

    def server_shutdown():
        for channel in channels:
            for client in channels[channel]:
                client[1].send("Le serveur s'arrête. À bientôt !".encode('utf-8'))
                client[1].close()

        server.close()
        exit()

    def start_server():
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('0.0.0.0', 12345))
        server.listen(5)
        print("Serveur en attente de connexions...")

        while True:
            client_socket, client_address = server.accept()
            print(f"Connexion acceptée de {client_address[0]}:{client_address[1]}")
            clients.append(client_socket)
            client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
            client_thread.start()

    clients = []
    usernames = []
    channels = {
        "Salon1": [],
        "Salon2": []
    }

    if __name__ == "__main__":
        start_server()