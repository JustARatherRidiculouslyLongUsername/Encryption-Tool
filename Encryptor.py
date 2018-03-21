def encrypt(string, key):
	encrypted_str = ''
	for i in string.encode():
		encrypted_str += chr(i + key)		
	return encrypted_str
    
def decrypt(encrypted_str, key):
	decrypted_str = ''
	for i in encrypted_str.encode():
		decrypted_str += chr(i - key)	
	return decrypted_str
