import socket
import binascii
import sdes

##############I DID NOT WRITE THIS FUNCTION, I FOUND THIS CODE HERE################ 
#https://stackoverflow.com/questions/7396849/convert-binary-to-ascii-and-vice-versa
def int2bytes(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))

def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return int2bytes(n).decode(encoding, errors)
###################################################################################
serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSock.bind((socket.gethostname(), 1234))
serverSock.listen(1)
conn, addr = serverSock.accept()

#While loop starts the server read/write waiting
decryptedMess = ''
message = ''
data = conn.recv(1024).decode()
print(data)
while len(data) > 0:
	if len(data) >= 8:
		decryptedMess = decryptedMess + decrypt(data)
		data = data[8:]
	else:
		print("Padding error")
		break
print(text_from_bits(decryptedMess))