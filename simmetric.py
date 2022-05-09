from cryptography.fernet import Fernet


def write_key():
    key = Fernet.generate_key()
    with open('C:\\Users\\paksh\\Desktop\\test_text\\simmetric\\simmetric_key.txt', 'wb')\
            as key_file:
        key_file.write(key)

    with open('C:\\Users\\paksh\\Desktop\\test_text\\simmetric\\simmetric_key', 'wb') as key_file:
        key_file.write(key)


def load_key():
    return open('C:\\Users\\paksh\\Desktop\\test_text\\simmetric\\simmetric_key', 'rb').read()


def encrypt(filename):
    f = Fernet(load_key())
    with open(filename, 'rb') as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open('C:\\Users\\paksh\\Desktop\\test_text\\simmetric\\data_encrypted.txt', 'wb') as file:
        file.write(encrypted_data)


def decrypt(filename):
    key = load_key()
    f = Fernet(key)
    with open(filename, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open('C:\\Users\\paksh\\Desktop\\test_text\\simmetric\\data_decrypted.txt', 'wb') as file:
        file.write(decrypted_data)
