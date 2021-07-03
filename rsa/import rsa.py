import rsa
  
# generate public and private keys with 
# rsa.newkeys method,this method accepts 
# key length as its parameter
# key length should be atleast 16
publicKey, privateKey = rsa.newkeys(2048)
a= repr(privateKey)
b = repr(publicKey)
a = bytes(a, 'ascii')
b = bytes(b, 'ascii')
#save keys in files 
file_out = open("public.txt",'wb')
file_out.write(b)
file_out.close()

file_out = open("private.txt",'wb')
file_out.write(a)
file_out.close() 
# this is the string that we will be encrypting
message = input("Enter Message:")

  
# rsa.encrypt method is used to encrypt 
# string with public key string should be 
# encode to byte string before encryption 
# with encode method
encMessage = rsa.encrypt(message.encode(), 
                         publicKey)
  
print("original string: ", message)
print("encrypted string: ", encMessage)
  
# the encrypted message can be decrypted 
# with ras.decrypt method and private key
# decrypt method returns encoded byte string,
# use decode method to convert it to string
# public key cannot be used for decryption
decMessage = rsa.decrypt(encMessage, privateKey).decode()
  
print("decrypted string: ", decMessage)