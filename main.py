import requests
from datetime import datetime

USERNAME = "nome_usuario"
TOKEN = "crie_seu_token"
GRAPH_ID = "graph1"

BASE_URL = "https://pixe.la/v1/users"
HEADERS = {"X-USER-TOKEN": TOKEN}

def criar_usuario():
    user_params = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }
    res = requests.post(url=BASE_URL, json=user_params)
    print(res.text)

def criar_grafico():
    graph_config = {
        "id": GRAPH_ID,
        "name": "Programing",
        "unit": "Min",
        "type": "int",
        "color": "shibafu"
    }
    url = f"{BASE_URL}/{USERNAME}/graphs"
    res = requests.post(url=url, json=graph_config, headers=HEADERS)
    print(res.text)

def adicionar_pixel():
    quantidade = input("Quantidade de minutos programando hoje: ")
    data = datetime.now().strftime("%Y%m%d")
    pixel_data = {
        "date": data,
        "quantity": quantidade
    }
    url = f"{BASE_URL}/{USERNAME}/graphs/{GRAPH_ID}"
    res = requests.post(url=url, json=pixel_data, headers=HEADERS)
    print(res.text)

def atualizar_pixel():
    data = input("Data a atualizar (formato YYYYMMDD): ")
    quantidade = input("Nova quantidade: ")
    url = f"{BASE_URL}/{USERNAME}/graphs/{GRAPH_ID}/{data}"
    new_data = {"quantity": quantidade}
    res = requests.put(url=url, json=new_data, headers=HEADERS)
    print(res.text)

def deletar_pixel():
    data = input("Data do pixel a deletar (formato YYYYMMDD): ")
    url = f"{BASE_URL}/{USERNAME}/graphs/{GRAPH_ID}/{data}"
    res = requests.delete(url=url, headers=HEADERS)
    print(res.text)

def menu():
    while True:
        print("\n--- MENU PIXELA ---")
        print("1. Criar usuário")
        print("2. Criar gráfico")
        print("3. Adicionar pixel")
        print("4. Atualizar pixel")
        print("5. Deletar pixel")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_usuario()
        elif opcao == "2":
            criar_grafico()
        elif opcao == "3":
            adicionar_pixel()
        elif opcao == "4":
            atualizar_pixel()
        elif opcao == "5":
            deletar_pixel()
        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()