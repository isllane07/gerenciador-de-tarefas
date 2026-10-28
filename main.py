
import json
import os

ARQUIVO = "tarefas.json"


def carregar_tarefas():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)

    return []


def salvar_tarefas():
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(tarefas, arquivo, ensure_ascii=False, indent=4)


tarefas = carregar_tarefas()

print("=== GERENCIADOR DE TAREFAS ===")
print(f"{len(tarefas)} tarefa(s) carregada(s).")

while True:
    print()
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Remover tarefa")
    print("4. Marcar tarefa como concluída")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    # ADICIONAR TAREFA
    if opcao == "1":
        nome_tarefa = input("Digite a tarefa: ").strip()

        if nome_tarefa == "":
            print("O nome da tarefa não pode ficar vazio!")
        else:
            tarefa = {
                "nome": nome_tarefa,
                "concluida": False
            }

            tarefas.append(tarefa)
            salvar_tarefas()

            print("Tarefa cadastrada e salva com sucesso!")

    # LISTAR TAREFAS
    elif opcao == "2":
        print("=== SUAS TAREFAS ===")

        if len(tarefas) == 0:
            print("Você ainda não tem tarefas cadastradas.")
        else:
            for numero, tarefa in enumerate(tarefas, start=1):
                nome = tarefa["nome"]
                status = tarefa["concluida"]

                if status:
                    print(f"{numero}. {nome} - Concluída")
                else:
                    print(f"{numero}. {nome} - Pendente")

    # REMOVER TAREFA
    elif opcao == "3":
        if len(tarefas) == 0:
            print("Não há tarefas para remover.")
        else:
            print("=== SUAS TAREFAS ===")

            for numero, tarefa in enumerate(tarefas, start=1):
                print(f"{numero}. {tarefa['nome']}")

            try:
                numero = int(
                    input("Digite o número da tarefa que deseja remover: ")
                )

                if 1 <= numero <= len(tarefas):
                    tarefa_removida = tarefas.pop(numero - 1)
                    salvar_tarefas()

                    print(f"Tarefa removida: {tarefa_removida['nome']}")
                else:
                    print("Número inválido!")

            except ValueError:
                print("Digite um número inteiro válido!")

    # MARCAR COMO CONCLUÍDA
    elif opcao == "4":
        if len(tarefas) == 0:
            print("Não há tarefas para concluir.")
        else:
            print("=== SUAS TAREFAS ===")

            for numero, tarefa in enumerate(tarefas, start=1):
                nome = tarefa["nome"]
                status = tarefa["concluida"]

                if status:
                    print(f"{numero}. {nome} - Concluída")
                else:
                    print(f"{numero}. {nome} - Pendente")

            try:
                numero = int(
                    input("Digite o número da tarefa concluída: ")
                )

                if 1 <= numero <= len(tarefas):
                    tarefas[numero - 1]["concluida"] = True
                    salvar_tarefas()

                    print("Tarefa concluída e salva com sucesso!")
                else:
                    print("Número inválido!")

            except ValueError:
                print("Digite um número inteiro válido!")

    # SAIR
    elif opcao == "5":
        print("Encerrando o programa. Até mais!")
        break

    # OPÇÃO INVÁLIDA
    else:
        print("Opção inválida! Tente novamente.")
