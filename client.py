#importing libraries
import socket
import cv2
import pickle
import struct
from skimage.metrics import structural_similarity as ssim
import numpy as np

base_img = cv2.imread("base.png")

capture = cv2.VideoCapture(1)
fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
videoWriter = cv2.VideoWriter('video_capture.avi', fourcc, 8, (640,480))


client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_ip = '192.168.0.123'
port = 10050 

client_socket.connect((host_ip,port)) 

data = b""

payload_size = struct.calcsize("Q")
while True:
    while len(data) < payload_size:
        packet = client_socket.recv(4*1024)
        if not packet: break
        data+=packet
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("Q",packed_msg_size)[0]
    while len(data) < msg_size:
        data += client_socket.recv(4*1024)
    frame_data = data[:msg_size]
    data  = data[msg_size:]
    frame = pickle.loads(frame_data)
    
    cv2.imshow("Receiving...",frame)
    s = ssim(base_img,frame,multichannel=True)
    if(s <0.7):
        videoWriter.write(frame)
    print(s)
    key = cv2.waitKey(10) 
    if key  == 13:
        break
client_socket.close()
 
 
 