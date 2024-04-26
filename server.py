# Server program for messaging service
# usage: python3 server.py <svr_port>


import socket
import sys
import threading

def client_handle(cli_socket, cli_address):

def client_join(cli_socket, parts):
	#handle when a client joins

def client_list(cli_socket):
	#list all clients

def client_mesg(cli_socket, parts):
	#send message to one client

def client_bcst(cli_socket, parts):
	#send message to all clients

def client_quit(cli_socket):
	#disconnect

def create_server(port):
	svr_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	svr_socket.bind(("0.0.0.0", port))
	svr_socket.listen(10)
	print("Server listening on port :", port)

	while True:
        	cli_socket, cli_address = svr_socket.accept()
        	print("Accepted connection from ", cli_address)

		#threading setup


def main():

	#invalid server call
	if len(sys.argv) != 2:
		print("usage: python server.py <svr_port>")
		sys.exit(1)

	port = int(sys.argv[1])
	create_server(port)

if __name__ == "__main__":
	main()
