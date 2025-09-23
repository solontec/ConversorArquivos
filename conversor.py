import tkinter as tk
from tkinter import filedialog, messagebox
from fpdf import FPDF
import os

def converter_para_pdf():
    #aqui abre uma janela pra o user selecionar arquivo 
    caminho_arquivo_txt = filedialog.askopenfilename(
        title="Selecione um arquivo para converter",
        filetypes=[("Arquivos de texto", "*.txt")]
    )

    if not caminho_arquivo_txt:
        #se o usuario cancelar a selecao do arquivo aqui nao faz absloutamente nada
        return
    
    try:
        # Extrai apenas o nome do arquivo original (sem o caminho e a extensão)
        nome_arquivo_sem_extensao = os.path.splitext(os.path.basename(caminho_arquivo_txt))[0]

        # --- Alteração para salvar na pasta Downloads ---
        # 1. Obtém o caminho da pasta principal do usuário (ex: C:\Users\Nome)
        caminho_pasta_usuario = os.path.expanduser("~")
        
        # 2. Constrói o caminho completo para a pasta Downloads
        caminho_pasta_downloads = os.path.join(caminho_pasta_usuario, "Downloads")
        
        # 3. Combina o caminho da pasta com o nome do novo arquivo PDF
        caminho_completo_pdf = os.path.join(caminho_pasta_downloads, f"{nome_arquivo_sem_extensao}.pdf")

        # Cria um objeto FPDF da biblioteca
        pdf = FPDF('P', 'mm', 'A4') 
        pdf.add_page()
        pdf.set_font("Arial", size=14)

        # Lê o conteúdo do arquivo
        with open(caminho_arquivo_txt, "r", encoding="utf-8") as arquivo_txt:
            conteudo = arquivo_txt.read()

        # Adiciona todo o conteúdo lido no PDF
        pdf.multi_cell(0, 5, txt=conteudo)

        # Salva o arquivo no novo local especificado (pasta Downloads)
        pdf.output(caminho_completo_pdf)

        messagebox.showinfo(
            "Sucesso",
            f"O arquivo foi convertido para PDF e salvo em '{caminho_completo_pdf}'."
        )

    except FileNotFoundError:
            messagebox.showerror("Erro", "Arquivo não encontrado.")
    except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {e}")


# aqui vou configurar a janela com tkinter

janela = tk.Tk()
janela.title("Conversor de Arquivos para PDF")
janela.geometry("400x150") 
janela.resizable(False, False)

# Adiciona um rótulo (texto) à janela
label_titulo = tk.Label(janela, text="Clique no botão para converter um arquivo .txt para PDF", font=("Arial", 10))
label_titulo.pack(pady=20)

# Adiciona um botão à janela
btn_converter = tk.Button(janela, text="Converter Arquivo", command=converter_para_pdf)
btn_converter.pack()

# Inicia o loop da interface gráfica
janela.mainloop()






