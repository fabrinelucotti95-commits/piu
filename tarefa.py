import tkinter as tk

def principal():
    janela = tk.Tk()
    janela.title("Encanto Perfumaria")
    janela.geometry("1000x650")
    janela.configure(bg="#fdf8f3")
    janela.resizable(False, False)

    # ==========================
    # CABEÇALHO
    # ==========================

    try:
        imagem = tk.PhotoImage(file="assets/perfumaria.png")

        banner = tk.Label(
            janela,
            image=imagem,
            bg="#fdf8f3"
        )
        banner.image = imagem
        banner.pack(pady=10)

    except:
        banner = tk.Label(
            janela,
            text="🌹 ENCANTO PERFUMARIA 🌹",
            font=("Segoe UI", 24, "bold"),
            bg="#fdf8f3",
            fg="#6d214f"
        )
        banner.pack(pady=20)

    titulo = tk.Label(
        janela,
        text="Encanto Perfumaria",
        font=("Segoe UI", 28, "bold"),
        bg="#fdf8f3",
        fg="#6d214f"
    )
    titulo.pack()

    subtitulo = tk.Label(
        janela,
        text="Perfumes nacionais e importados",
        font=("Segoe UI", 12),
        bg="#fdf8f3",
        fg="#8c6f7a"
    )
    subtitulo.pack(pady=(0, 20))

    # ==========================
    # CATÁLOGO
    # ==========================

    frame_produtos = tk.Frame(
        janela,
        bg="#fdf8f3"
    )
    frame_produtos.pack()

    produtos = [
        ("🌹 La Vie Est Belle", "R$ 399,90"),
        ("✨ Egeo Dolce", "R$ 129,90"),
        ("💎 Malbec Gold", "R$ 189,90"),
        ("🌸 Floratta Red", "R$ 149,90"),
        ("🖤 212 VIP", "R$ 449,90"),
        ("🥇 Chanel Nº 5", "R$ 799,90"),
    ]

    linha = 0
    coluna = 0

    for nome, preco in produtos:

        card = tk.Frame(
            frame_produtos,
            bg="white",
            width=250,
            height=180,
            bd=1,
            relief="solid"
        )

        card.grid(
            row=linha,
            column=coluna,
            padx=15,
            pady=15
        )

        card.grid_propagate(False)

        tk.Label(
            card,
            text="🧴",
            font=("Segoe UI", 42),
            bg="white"
        ).pack(pady=10)

        tk.Label(
            card,
            text=nome,
            bg="white",
            font=("Segoe UI", 11, "bold")
        ).pack()

        tk.Label(
            card,
            text=preco,
            bg="white",
            fg="#c2185b",
            font=("Segoe UI", 12, "bold")
        ).pack(pady=5)

        tk.Button(
            card,
            text="Comprar",
            bg="#c2185b",
            fg="white",
            bd=0,
            width=15,
            cursor="hand2"
        ).pack(pady=10)

        coluna += 1

        if coluna > 2:
            coluna = 0
            linha += 1

    rodape = tk.Label(
        janela,
        text="© 2026 Encanto Perfumaria - Todos os direitos reservados",
        bg="#fdf8f3",
        fg="#8c6f7a",
        font=("Segoe UI", 9)
    )
    rodape.pack(side="bottom", pady=10)

    janela.mainloop()

if __name__ == "__main__":
    principal()