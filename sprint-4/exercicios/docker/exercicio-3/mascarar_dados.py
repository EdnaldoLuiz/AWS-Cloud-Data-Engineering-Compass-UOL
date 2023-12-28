import hashlib

while True:
    input_string = input("Digite uma string para mascarar (ou 'sair' para sair): ")

    if input_string.lower() == 'sair':
        break

    sha1_hash = hashlib.sha1(input_string.encode()).hexdigest()

    print(f"Hash SHA-1 da string '{input_string}': {sha1_hash}")
