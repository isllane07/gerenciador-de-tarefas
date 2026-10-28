
import tkinter as tk
from tkinter import messagebox
import json
import os

ARQUIVO = "tarefas.json"
tarefas = []


def carregar_tarefas():
    if os.path.exists(ARQUIVO):
        try:
            with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)

            if isinstance(dados, list):
                return dados

        except (json.JSONDecodeError, OSError):
            messagebox.showerror(
                "Erro",
                "Não foi possível ler o arquivo de tarefas."
            )

    return []


def salvar_tarefas():
    try:
        with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
            json.dump(
                tarefas,
                arquivo,
                ensure_ascii=False,
                indent=4
            )
    except OSError:
        messagebox.showerror(
            "Erro",
            "Não foi possível salvar as tarefas."
        )


def atualizar_lista():
    lista_tarefas.delete(0, tk.END)

    for tarefa in tarefas:
        if tarefa["concluida"]:
            texto = f"✔  {tarefa['nome']} - Concluída"
        else:
            texto = f"○  {tarefa['nome']} - Pendente"

        lista_tarefas.insert(tk.END, texto)

    total = len(tarefas)
    concluidas = sum(1 for tarefa in tarefas if tarefa["concluida"])

    contador.config(
        text=f"{concluidas} de {total} tarefas concluídas"
    )


def adicionar_tarefa():
    nome = campo_tarefa.get().strip()

    if nome == "":
        messagebox.showwarning("Atenção", "Digite o nome da tarefa!")
        return

    tarefas.append({
        "nome": nome,
        "concluida": False
    })

    salvar_tarefas()
    campo_tarefa.delete(0, tk.END)
    atualizar_lista()


def concluir_tarefa():
    selecionada = lista_tarefas.curselection()

    if not selecionada:
        messagebox.showwarning(
            "Atenção",
            "Selecione uma tarefa na lista!"
        )
        return

    indice = selecionada[0]
    tarefas[indice]["concluida"] = True

    salvar_tarefas()
    atualizar_lista()


def remover_tarefa():
    selecionada = lista_tarefas.curselection()

    if not selecionada:
        messagebox.showwarning(
            "Atenção",
            "Selecione uma tarefa para remover!"
        )
        return

    indice = selecionada[0]
    tarefas.pop(indice)

    salvar_tarefas()
    atualizar_lista()


# Carrega os dados antes de montar a interface
tarefas = carregar_tarefas()

janela = tk.Tk()
janela.title("Gerenciador de Tarefas")
janela.geometry("600x650")
janela.configure(bg="#1e1e2e")

titulo = tk.Label(
    janela,
    text="Minhas tarefas",
    font=("Arial", 24, "bold"),
    bg="#1e1e2e",
    fg="#cba6f7"
)
titulo.pack(pady=(25, 5))

subtitulo = tk.Label(
    janela,
    text="Organize seu dia, uma tarefa por vez.",
    font=("Arial", 11),
    bg="#1e1e2e",
    fg="#cdd6f4"
)
subtitulo.pack(pady=(0, 15))

campo_tarefa = tk.Entry(janela, font=("Arial", 12), width=35)
campo_tarefa.pack(pady=5)

lista_tarefas = tk.Listbox(
    janela,
    font=("Arial", 12),
    width=45,
    height=12,
    bg="#313244",
    fg="#cdd6f4",
    selectbackground="#cba6f7",
    selectforeground="#1e1e2e",
    borderwidth=0
)
lista_tarefas.pack(pady=15)

contador = tk.Label(
    janela,
    text="",
    font=("Arial", 10),
    bg="#1e1e2e",
    fg="#a6adc8"
)
contador.pack(pady=5)

tk.Button(
    janela,
    text="+ Adicionar tarefa",
    font=("Arial", 10, "bold"),
    bg="#cba6f7",
    fg="#1e1e2e",
    relief="flat",
    padx=12,
    pady=7,
    command=adicionar_tarefa
).pack(pady=4)

tk.Button(
    janela,
    text="✔ Marcar como concluída",
    font=("Arial", 10, "bold"),
    bg="#a6e3a1",
    fg="#1e1e2e",
    relief="flat",
    padx=12,
    pady=7,
    command=concluir_tarefa
).pack(pady=4)

tk.Button(
    janela,
    text="Remover tarefa",
    font=("Arial", 10, "bold"),
    bg="#f38ba8",
    fg="#1e1e2e",
    relief="flat",
    padx=12,
    pady=7,
    command=remover_tarefa
).pack(pady=4)

atualizar_lista()
janela.mainloop()
