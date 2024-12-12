import cv2
import socket
import struct
import pickle

# Initialize webcam
cap = cv2.VideoCapture(0)

# Create socket for data transmission
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 9999))  # Bind to all interfaces on port 9999
server_socket.listen(5)
print("Waiting for connection...")

conn, addr = server_socket.accept()
print(f"Connected by: {addr}")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Serialize the frame
    data = pickle.dumps(frame)
    # Send the frame size followed by the frame data
    conn.sendall(struct.pack("Q", len(data)) + data)

cap.release()
server_socket.close()
