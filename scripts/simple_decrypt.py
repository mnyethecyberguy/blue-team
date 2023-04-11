import os
from cryptography.fernet import Fernet
#Note: Must have cryptography instlaled via "pip3 install cryptography"

def load_key():
    return open("key.key", "rb").read()

def decrypt(filename, key):
    f = Fernet(key)
    new_name = filename[:-10]
    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # write the original file
    with open(new_name, "wb") as file:
        file.write(decrypted_data)

def main(folder_path):
    for path, subdirs, files in os.walk(folder_path):
        for name in files:
            file_path = os.path.join(path,name)
            decrypt(file_path, key)
            os.remove(file_path)

# Driver Code
if __name__ == '__main__':
    # Calling main() function
    key = load_key()
    decrypt_path = "/tmp/criticalfiles"
    main(decrypt_path)
