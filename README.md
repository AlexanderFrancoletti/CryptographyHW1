# CryptographyHW1

To run the program, run the server and then run the client on another terminal. The server itself doesn't actually edit any file currently, but the client takes the "inputtext.txt" file as input to send to the server. The client encrypts the file using a toy DES, and then sends the file over to the server, which receives the encrypted file and then decrypts it.

The DES algorithm and functions are all contained in a single file name "sdes.py". Initially it sets all the keys for each step that it's going to take during encryption, such as the initial permutation keys and substitution matrices. The process of encryption begins with the permutation of the input byte according to the initial permutation key. After that, it goes into the fk function, which does the following steps in order after a key is generated: split the byte into left and right halves, permutate the right half using the expansion/permutation key, performs an xor operation on the resulting byte with the known key, then transforms that string by checking the left and right halves of itself into a substitution matrix, doing a permutation with the initial permutation 4 bit key, and finally performing as xor operation with the initial left half.

Key generation happens twice during the encryption algorithm, one time for each fk function call. The first key that is generated is made using a byte shift after a permutation using the initial 10 bit key, followed by a single left bit shift and then a permutation using the inital 8 bit key. The second key is generated in an identical matter, except it is left shifted 3 times as opposed to 1.

After the second fk function call has been made using the 2nd generated key, the byte goes through one last shift using the initial permutation inverse key declared earlier. After that, the byte is now encrypted, and can be sent safely to the server without concern. The only way for the now encrypted byte to be read by a human is to call the decrypt.
