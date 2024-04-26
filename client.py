

# Client program used for messaging service
# usage : python3 client.py <server_ip> <server_port>

import socket
import sys

def create_client(svr_ip, svr_port):
	#initialize socket
	cli_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	cli_socket.connect((svr_ip, svr_port))

	#create username and join server
	username = input("Enter JOIN followed by your username: ");
	join_message = f"JOIN {username}"
	cli_socket.send(join_message.encode())

	#recieve and decode response from server
	svr_response = cli_socket.recv(1024)
	print(svr_response.decode())

	while True:
		#put some logic here for all the commands

	#close socket
	cli_socket.close()

def main():
	#incorrect program call
	if len(sys.argv) != 3:
		print("Usage: python client.py <server_ip> <server_port>")
		sys.exit(1)

	svr_ip = sys.argv[1]
	svr_port = int(sys.argv[2])
	create_client(svr_ip, svr_port)

if __name__ == "__main__":
	main()
