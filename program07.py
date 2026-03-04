#file integrity checker
import hashlib

def file_hash(filename):
    h = hashlib.md5()
    with open(filename, "rb") as file: 
        while chunk :=file.read(4096): 
            h.update(chunk)
    return h.hexdigest()

filel = input("Enter file: ")
print("Hash:", file_hash (filel))