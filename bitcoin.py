import random

def simulate_bitcoin_mining():
    count = 0
    bitcoin = 0
    while True:
        print(f"[Bitcoins encontrados {bitcoin}] Buscando por bitcoin... ({count} tentativas)")
        if random.randint(1, 100000000) == 1:
            bitcoin += 1
            print(f"1 bitcoin encontrado! Total: {bitcoin} bitcoin(s)")
        count += 1

simulate_bitcoin_mining()