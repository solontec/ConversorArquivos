# ConversorArquivos
Conversor de Arquivos TXT para PDF

Este projeto é um aplicativo simples em Python que converte arquivos .txt em arquivos PDF, salvando automaticamente os PDFs na pasta Downloads do usuário. Ele possui uma interface gráfica feita com Tkinter que permite selecionar múltiplos arquivos e converter todos de uma vez.

Funcionalidades:

Interface gráfica amigável feita com Tkinter

Seleção de múltiplos arquivos .txt

Conversão automática para PDF usando FPDF

Salvamento automático dos arquivos PDF na pasta Downloads

Exibição de mensagens de sucesso e erro

Bibliotecas utilizadas:

tkinter → criação da interface gráfica (janelas, botões e mensagens)

filedialog e messagebox (do tkinter) → seleção de arquivos e exibição de alertas

fpdf → criação e formatação dos arquivos PDF

os → manipulação de caminhos e diretórios do sistema operacional

Instalação:
Antes de executar, instale a biblioteca FPDF com o comando:
pip install fpdf

Como executar:

Salve o arquivo do projeto (por exemplo: conversor_pdf.py).

Execute o comando:
python conversor_pdf.py

Clique no botão “Converter Arquivos” e selecione um ou mais arquivos .txt.

Os arquivos PDF convertidos serão salvos automaticamente na pasta Downloads.

Observações:

Certifique-se de que os arquivos .txt estejam no formato UTF-8 para evitar erros com acentuação ou caracteres especiais.

Caso algum arquivo não possa ser convertido, uma mensagem de erro será exibida com o motivo.
