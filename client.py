from socket import *
server_name = 'localhost'
server_port = 5069
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_name,server_port))
while True:
  sentence = input("Enter Your message to server :")
  client_socket.send(sentence.encode())
  message = client_socket.recv(2049)
  print ("From Server -> ", message.decode())
  if(sentence == 'bye'):
    client_socket.close()