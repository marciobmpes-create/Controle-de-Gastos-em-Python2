import json
import os

ARQUIVO = "gastos.json"

def carregar_gastos():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    return []

def salvar_gastos(gastos):
    with open(ARQUIVO, "w") as f:
        json.dump(gastos, f, indent=4)

def adicionar_gasto(gastos):
    descricao = input("Descrição do gasto: ")
    valor = float(input("Valor: R$ "))
    categoria = input("Categoria (ex: comida, transporte, lazer): ")

    gasto = {
        "descricao": descricao,
        "valor": valor,
        "categoria": categoria
    }

    gastos.append(gasto)
    salvar_gastos(gastos)
    print("Gasto adicionado com sucesso!\n")

def listar_gastos(gastos):
    if not gastos:
        print("Nenhum gasto registrado.\n")
        return

    print("\nLista de Gastos:")
    for i, g in enumerate(gastos, 1):
        print(f"{i}. {g['descricao']} - R$ {g['valor']:.2f} ({g['categoria']})")
    print()

def total_gasto(gastos):
    total = sum(g["valor"] for g in gastos)
    print(f"\nTotal gasto: R$ {total:.2f}\n")

def total_por_categoria(gastos):
    categorias = {}

    for g in gastos:
        cat = g["categoria"]
        categorias[cat] = categorias.get(cat, 0) + g["valor"]

    print("\nGastos por categoria:")
    for cat, total in categorias.items():
        print(f"{cat}: R$ {total:.2f}")
    print()

def menu():
    gastos = carregar_gastos()

    while True:
        print("==== CONTROLE DE GASTOS ====")
        print("1 - Adicionar gasto")
        print("2 - Listar gastos")
        print("3 - Ver total gasto")
        print("4 - Ver total por categoria")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_gasto(gastos)
        elif opcao == "2":
            listar_gastos(gastos)
        elif opcao == "3":
            total_gasto(gastos)
        elif opcao == "4":
            total_por_categoria(gastos)
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!\n")

if __name__ == "__main__":
    menu()
