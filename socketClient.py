#!/usr/bin/env python3
# Link to tutorial I followed http://danielhnyk.cz/simple-server-client-aplication-python-3/

import socket
import sys

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

soc.connect(("127.0.0.1", 12345))

print("Please wait while I calculate the Fibonnaci number you've requested")
clients_arg = sys.argv[1]
soc.sendall(bytes(clients_arg, "utf8"))  # we must encode the string to bytes
result_bytes = soc.recv(4096)  # the number means how the response can be in bytes
result_string = result_bytes.decode("utf8")  # the return will be in bytes, so decode

print("The Fibonacci number corresponding to your input is {}".format(result_string))
