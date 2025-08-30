# TCP Chat App

A simple multi-client chat application built in **Python** using **TCP sockets** by Shruthika Rajan and Vishal Purushothama.

This project allows multiple clients to connect to a server and chat with each other in real-time. Each client has a nickname, and all messages are broadcasted to every connected client.

---

## Features
- Multi-client support (multiple users can chat simultaneously)
- Nickname for each client
- Broadcast messages to all connected clients
- Handles client disconnects gracefully

---

## Technologies Used
- VS Studio Code
- socket (built-in Python library)
- threading (built-in Python library)

---

## How to Run

### 1. Start the Server
Open a terminal in the project folder and run:
```bash
python server.py
