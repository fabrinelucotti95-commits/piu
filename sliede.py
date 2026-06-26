import tkinter as tk


def principal():
    # Inicializa a janela principal do Tkinter
    janela_principal = tk.Tk()
    janela_principal.title("NovaMarket")

    # Define o tamanho da janela e impede o redimensionamento
    largura_janela = 900
    altura_janela = 550
    janela_principal.resizable(False, False)

    # Centraliza a janela na tela
    largura_tela = janela_principal.winfo_screenwidth()
    altura_tela = janela_principal.winfo_screenheight()

    posicao_x = (largura_tela - largura_janela) // 2
    posicao_y = (altura_tela - altura_janela) // 2

    janela_principal.geometry(
        f"{largura_janela}x{altura_janela}+{posicao_x}+{posicao_y}"
    )

    # Paleta de cores
    COR_FUNDO = "#0a0f1d"
    COR_PAINEL = "#161e35"
    COR_TEXTO = "#ffffff"
    COR_SECUNDARIA = "#8a99ad"

    janela_principal.configure(bg=COR_FUNDO)

    # ==================================================
    # PAINEL ESQUERDO
    # ==================================================

    painel_esquerdo = tk.Frame(
        janela_principal,
        width=450,
        height=550,
        bg=COR_FUNDO,
        bd=0,
        highlightthickness=0
    )

    painel_esquerdo.pack(side="left", fill="both")
    painel_esquerdo.pack_propagate(False)

    # Logo
    logo = tk.Label(
        painel_esquerdo,
        text="NovaMarket",
        fg=COR_TEXTO,
        bg=COR_FUNDO,
        font=("Segoe UI", 28, "bold")
    )
    logo.pack(pady=(35, 5))

    # Subtítulo da marca
    subtitulo_logo = tk.Label(
        painel_esquerdo,
        text="Marketplace Premium",
        fg=COR_SECUNDARIA,
        bg=COR_FUNDO,
        font=("Segoe UI", 11)
    )
    subtitulo_logo.pack()

    # Área da imagem
    try:
        ilustracao = tk.PhotoImage(file="assets/marketplace.png")

        imagem_label = tk.Label(
            painel_esquerdo,
            image=ilustracao,
            bg=COR_FUNDO,
            bd=0
        )

        imagem_label.image = ilustracao
        imagem_label.pack(expand=True)

    except Exception:
        marcador_imagem = tk.Label(
            painel_esquerdo,
            text="[Adicione assets/marketplace.png]",
            fg=COR_SECUNDARIA,
            bg=COR_FUNDO,
            font=("Helvetica", 12, "italic")
        )

        marcador_imagem.pack(expand=True)

    # ==================================================
    # PAINEL DIREITO
    # ==================================================

    painel_direito = tk.Frame(
        janela_principal,
        width=450,
        height=550,
        bg=COR_PAINEL,
        bd=0,
        highlightthickness=0
    )

    painel_direito.pack(side="right", fill="both")
    painel_direito.pack_propagate(False)

    # Container central
    container_login = tk.Frame(
        painel_direito,
        bg=COR_PAINEL
    )

    container_login.place(
        relx=0.5,
        rely=0.35,
        anchor="center"
    )

    # Título
    titulo = tk.Label(
        container_login,
        text="Bem-vindo de volta",
        fg=COR_TEXTO,
        bg=COR_PAINEL,
        font=("Segoe UI", 24, "bold")
    )

    titulo.pack(pady=(0, 10))

    # Subtítulo
    subtitulo = tk.Label(
        container_login,
        text="Faça login para continuar",
        fg=COR_SECUNDARIA,
        bg=COR_PAINEL,
        font=("Segoe UI", 11)
    )

    subtitulo.pack()

    # Linha decorativa
    linha = tk.Frame(
        container_login,
        bg="#7c4dff",
        width=80,
        height=3
    )

    linha.pack(pady=20)

    # Espaço reservado para a próxima etapa
    placeholder_formulario = tk.Label(
        container_login,
        text="Campos de login serão adicionados na Etapa 3",
        fg=COR_SECUNDARIA,
        bg=COR_PAINEL,
        font=("Segoe UI", 10, "italic")
    )

    placeholder_formulario.pack()

    # Executa interface
    janela_principal.mainloop()


if __name__ == "__main__":
    principal()
