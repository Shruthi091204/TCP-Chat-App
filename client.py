import socket
import threading

HOST = '127.0.0.1'  # Server IP
PORT = 5000

nickname = input("Enter your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# Receive messages from server
def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print("Connection closed.")
            client.close()
            break

# Send messages to server
def send_messages():
    while True:
        msg = input('')
        if msg.lower() == '/quit':
            client.close()
            print("You left the chat.")
            break
        message = f"{nickname}: {msg}"
        client.send(message.encode('utf-8'))  # <-- Removed the extra print here

# Start threads
threading.Thread(target=receive_messages).start()
threading.Thread(target=send_messages).start()
