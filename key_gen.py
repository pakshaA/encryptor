from Crypto.PublicKey import RSA


def key_gen():
    key = RSA.generate(2048)
    privateKey = key.export_key()
    publicKey = key.publickey().export_key()

    with open('C:\\Users\\paksh\\PycharmProjects\\encryptor\\for_asimmetric\\private.pem', 'wb') as f:
        f.write(privateKey)

    with open('C:\\Users\\paksh\\PycharmProjects\\encryptor\\for_asimmetric\\public.pem', 'wb') as f:
        f.write(publicKey)
