import tkinter as tk
from tkinter import filedialog, messagebox
from fpdf import FPDF
import os


class ConversorPDF:
    def __init__(self, master):
        """Inicializa a interface"""
        self.master = master
        self.master.title("Conversor de arquivos para PDF")
        self.master.geometry("600x300")
        self.master.resizable(False, False)

        # abaixo crio de fato aq interface configurada com o tkinter 
        self._criar_widgets()

    def _criar_widgets(self): #crio a janela com o texto, fontes e tamanho
        """Organiza os widgets na janela"""
        label_titulo = tk.Label(
            self.master,
            text="Clique no botão para converter arquivos .txt para PDF",
            font=("Arial", 10)
        )
        label_titulo.pack(pady=20)

        btn_converter = tk.Button(
            self.master,
            text="Converter Arquivos",
            command=self.converter_para_pdf  # interface e botao
        )
        btn_converter.pack()

    #funcao para converter de fato para pdf
    def converter_para_pdf(self):
        """Abre seleção de arquivos e faz a conversão"""  
        arquivos_txt = filedialog.askopenfilenames(
            #askopenfilename apenas um arquivo por vez, ja com o "S", podemos mobilizar mellhor eles, util para varias tafeas entao coloquei isso.
            title="Selecione arquivos para converter",
            filetypes=[("Arquivos de texto", "*.txt")]
        )

        if not arquivos_txt:
            return  # caso cancelem ele nao retorna nada

        sucesso = 0
        erros = []

        for caminho_arquivo_txt in arquivos_txt:
            try:
                # pega só  o nome do arquivo original 
                nome_arquivo_sem_extensao = os.path.splitext(
                    os.path.basename(caminho_arquivo_txt)
                )[0]

                # manda de fato pra dowloads quiando converter
                caminho_pasta_usuario = os.path.expanduser("~")
                caminho_pasta_downloads = os.path.join(caminho_pasta_usuario, "Downloads")

                # Cgera o caminho final com nome do arquivo que já era
                caminho_completo_pdf = os.path.join(
                    caminho_pasta_downloads, f"{nome_arquivo_sem_extensao}.pdf"
                )

                # chamo o metodo para criar que irei fazer 
                self._gerar_pdf(caminho_arquivo_txt, caminho_completo_pdf)
                sucesso += 1

            except Exception as e:
                erros.append(f"{caminho_arquivo_txt}: {e}")

        # mensagens finais
        if sucesso > 0:
            messagebox.showinfo(
                "Sucesso",
                f"{sucesso} arquivo(s) foram convertidos para PDF e salvos na pasta Downloads." #msg se der bom
            )
        if erros:
            messagebox.showerror("Erros", "\n".join(erros))

     
    def _gerar_pdf(self, caminho_arquivo_txt, caminho_completo_pdf): #cofigura o documento, como ele sera de fato e como vai ser a leitura
    
        pdf = FPDF()  
        pdf.add_page()
        pdf.set_font("Helvetica", size=14)  # fontes básicas já aceitam UTF-8

        with open(caminho_arquivo_txt, "r", encoding="utf-8") as arquivo_txt:
            conteudo = arquivo_txt.read()

        pdf.multi_cell(0, 10, conteudo)  # agora aceita emojis, acentos e caracteres especiais
        pdf.output(caminho_completo_pdf)
    #emabixo verifico se o bloco está rodando certo, se sim ele gera um loop executando o codigo todo acima
if __name__ == "__main__":
    root = tk.Tk()
    app = ConversorPDF(root)  
    root.mainloop()
