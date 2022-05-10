from Crypto.PublicKey import RSA


def key_gen(curr_dirr):
    key = RSA.generate(2048)
    privateKey = key.export_key()
    publicKey = key.publickey().export_key()

    with open(curr_dirr + '\\private.pem', 'wb') as f:
        f.write(privateKey)

    with open(curr_dirr + '\\public.pem', 'wb') as f:
        f.write(publicKey)
