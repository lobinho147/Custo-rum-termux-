import os
import sys
import random
import string
from datetime import datetime

KEYS_FILE = "keys.txt"
STAFF_PASSWORD = "adm"

# ---------- Funções básicas ----------
def banner(title="LOBO BLOCK - STAFF"):
    os.system("clear")
    print("="*50)
    print(f"       🔥 {title} 🔥")
    print("="*50)

def check_password():
    senha = input("Digite a senha de acesso: ")
    if senha != STAFF_PASSWORD:
        print("❌ Senha incorreta!")
        sys.exit()
    print("✅ Acesso permitido.")
    input("Pressione Enter para continuar...")

# ---------- Funções de Key ----------
def gerar_key(tipo="permanente"):
    numero = random.randint(1000,9999)
    codigos = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    if tipo == "temporaria":
        key = f"Lobo_temp_{numero}_{codigos}"
    else:
        key = f"LoboBlock_{numero}_{codigos}"
    with open(KEYS_FILE, "a") as f:
        f.write(key + "\n")
    print(f"✅ Key gerada: {key}")
    return key

def listar_keys():
    if not os.path.exists(KEYS_FILE):
        print("Nenhuma Key gerada ainda.")
        return
    with open(KEYS_FILE, "r") as f:
        keys = f.read().splitlines()
    print("Keys existentes:")
    for k in keys:
        print(k)

# ---------- Painel Staff ----------
def painel_staff():
    check_password()
    while True:
        banner()
        print("1 - Gerar Key Permanente")
        print("2 - Gerar Key Temporária")
        print("3 - Listar Keys")
        print("0 - Sair")
        choice = input("\n>>> ")

        if choice == "1":
            gerar_key("permanente")
        elif choice == "2":
            gerar_key("temporaria")
        elif choice == "3":
            listar_keys()
        elif choice == "0":
            print("👋 Saindo do Painel Staff...")
            sys.exit()
        else:
            print("❌ Opção inválida!")
            input("Pressione Enter para continuar...")

# ---------- Programa principal ----------
if __name__ == "__main__":
    painel_staff()