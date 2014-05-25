import suds
import hashlib
url = "http://localhost:8080/server/soap/description"
client = suds.client.Client(url)
print client
# while True:
#     print "========================HASHING================================\n"
#     print "Masukan nama algoritma hash berikut.\nAlgoritma : md5, sha1, sha224, sha256, sha384, sha512\nContoh masukan: md5"
#     algoritmaHash = raw_input("Nama algoritma : ")
#     plaintext = raw_input("Masukan kata : ")
#     if(str.lower(algoritmaHash) == "md5"):
#         print "\nPlaintext : "+plaintext
#         print "Ciphertext : "+client.service.md5(plaintext)+"\n===============================================================\n"
#     elif(str.lower(algoritmaHash) == "sha1"):
#         print "\nPlaintext : "+plaintext
#         print "Ciphertext : "+client.service.sha1(plaintext)+"\n===============================================================\n"
#     elif(str.lower(algoritmaHash) == "sha224"):
#         print "\nPlaintext : "+plaintext
#         print "Ciphertext : "+client.service.sha224(plaintext)+"\n===============================================================\n"
#     elif(str.lower(algoritmaHash) == "sha256"):
#         print "\nPlaintext : "+plaintext
#         print "Ciphertext : "+client.service.sha256(plaintext)+"\n===============================================================\n"
#     elif(str.lower(algoritmaHash) == "sha384"):
#         print "\nPlaintext : "+plaintext
#         print "Ciphertext : "+client.service.sha384(plaintext)+"\n===============================================================\n"
#     elif(str.lower(algoritmaHash) == "sha512"):
#         print "\nPlaintext : "+plaintext
#         print "Ciphertext : "+client.service.sha512(plaintext)+"\n===============================================================\n"
#     else:
#         print "Masukan nama algoritma salah\n===============================================================\n"
#         break