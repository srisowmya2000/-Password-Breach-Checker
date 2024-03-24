#  Password Breach Checker

**_Introduction: _**
This project aims to check if a given set of passwords has been breached by comparing their MD5 hashes with a list of hashed passwords from a data file. The code uses Python and the Hashlib library to perform the hashing and comparison.

**Features:**
Password Hashing: Utilizes the Hashlib library to hash passwords using the MD5 algorithm.
File Input: Reads passwords to check from a file containing weak passwords.
Hash Comparison: Compares the hashed passwords with a list of hashed passwords from another file.
Output: Indicates whether each password is safe or has been breached.

**Execution:**
The script reads passwords from the weak passwords file and hashes them using MD5.
It then compares each hashed password with the hashed passwords from the Hashes file.
If a match is found, it indicates that the password has been breached. Otherwise, it marks it as safe.

**Note: **
This educational project should not be used for real-world password management without proper security measures.


