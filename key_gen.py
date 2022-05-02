from Crypto.PublicKey import RSA


def key_gen():
    key = RSA.generate(2048)
    privateKey = key.export_key()
    publicKey = key.publickey().export_key()

    with open('private.pem', 'wb') as f:
        f.write(privateKey)
    with open('private.txt', 'wb') as f:
        f.write(privateKey)

    with open('public.pem', 'wb') as f:
        f.write(publicKey)
    with open('public.txt', 'wb') as f:
        f.write(publicKey)
