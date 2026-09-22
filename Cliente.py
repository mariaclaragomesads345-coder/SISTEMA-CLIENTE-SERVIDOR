import socket
import tkinter as tk
from tkinter import messagebox

def conectar_ao_serviimportdor():
    try:
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.connect(('localhost', 5000))

        cliente.send("Ola´, sou o cliente visual!".encode('utf-8'))

        resposta = cliente.recv(1024).decode('utf-8')
        cliente.close()

        messagebox.showinfo("Sucesso", f"Resposta do servidor: {resposta}")

    except Exception as e:

        messagebox.showerror("Erro", f"Não foi possível conectar ao servidor: {e}")

janela = tk.Tk()
janela.title("meu sistema cliente")
janela.geometry("300x200")

texto = tk.Label(janela, text="Clique no botão para conectar ao servidor", font=("Arial", 10))
texto.pack(pady=20)

botao = tk.Button(janela, text="Conectar", command=conectar_ao_servidor, bg="green", fg="white", font=("Arial", 11, "bold"))
botao.pack(pady=20)
tk.Label(janela, text="Mensageiro (janela)", font=("Arial", 12, "bold")).pack(pady=5)

campo_texto = tk.Entry(janela, width=30, font=("Arial", 11))
campo_texto.pack(pady=5)

janela.mainloop()
