from cryptography.hazmat.primitives.asymmetric import padding,rsa
from cryptography.hazmat.primitives import hashes

plik_wejsciowy = input("ktory plik mam podpisac?")
#generowanie klucza prywatnego 
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)
#generowanie klucz publicznego 
public_key = private_key.public_key()


# podpisanie pliku wejsciowego
with open(plik_wejsciowy,'rb') as f:
    data = f.read()

    signature = private_key.sign(
        data,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

#zapisanie podpisu do pliku
with open('signature.txt','wb') as f:
    f.write(signature)

