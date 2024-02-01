import hashlib
#creating variables and assign them with the local files that is stored in the system. 
hashfile ="/home/kali/Desktop/Hashes"
leakpwd ="/home/kali/Desktop/weakpasswords"
#we are opening the weakpassword file and reading it line by line.
with open(leakpwd, 'r') as file:
weakpassword = file.readlines()
#we are using iteration as the list in the text file the passwords have to be hashed. If 
we don’t use the for loop the file will be hashed.
for line in weakpassword:
password = line.strip()
#performing hashing of the passwords.
password_hash = hashlib.md5(password.encode()).hexdigest()
#Similarly opening and reading the contents in hash text file 
with open(hashfile, 'r') as file:
hash_lines = file.readlines()
for hash_line in hash_lines:
hash_line = hash_line.strip()
#using the condition if the hashline hashes are equal to password hashes then it is 
breached else it is safe. 
if hash_line == password_hash:
print("the password is breached")
break
else:
print("the password is safe"
