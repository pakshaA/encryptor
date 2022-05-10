from cryptography.fernet import Fernet


def write_key(curr_dir):
    key = Fernet.generate_key()
    with open(curr_dir + '/simmetric_key.txt', 'wb')\
            as key_file:
        key_file.write(key)

    with open(curr_dir + '/simmetric_key', 'wb') as key_file:
        key_file.write(key)


def load_key(curr_dir):
    return open(curr_dir + '/simmetric_key', 'rb').read()


def encrypt(filename, curr_dir):
    f = Fernet(load_key(curr_dir))
    with open(filename, 'rb') as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(curr_dir + '/data_encrypted.txt', 'wb') as file:
        file.write(encrypted_data)


def decrypt(filename, curr_dir):
    key = load_key(curr_dir)
    f = Fernet(key)
    with open(filename, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(curr_dir + '/data_decrypted.txt', 'wb') as file:
        file.write(decrypted_data)
