import socket
import sdes

clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSock.connect((socket.gethostname(), 1234))

text_file = 'inputtext.txt'

#client to send encrypted text files
with open(text_file, 'rb') as fs:
	data = fs.read()
	
bitString = ''
bits = ''.join('{0:08b}'.format(ord(x), 'b') for x in data)
#print(bits)
#print(len(bits))
#Loop encrypts the read text file before sending it to the server
while len(bits) > 0:
	if len(bits) >= 8:
		bitString = bitString + encrypt(bits)
		bits = bits[8:]	
	else:
		print("ERROR:Padding")
		break
clientSock.send(bitString.encode())
#print(bitString)
clientSock.close()