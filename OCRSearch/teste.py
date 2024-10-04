import os
from PyPDF2 import PdfReader
import tkinter as tk
from tkinter import *
import threading


def create_info_rectangle(canvas, x, y, width, height, vezes, paginas, titulo,Keyword, margin):
    # Desenhar o retângulo
    canvas.create_rectangle(x, y, x + width, y + height, fill="lightblue", outline="black")
    
    # Adicionar o texto dentro do retângulo
    text = f"SUA KEYWORD: {Keyword}\n FOI ENCONTRADO(A): {vezes} VEZES\nNA PAGINA: {paginas}\nDO PDF: {titulo}"
    canvas.create_text(x + margin, y + margin, anchor="nw", text=text, font=("Arial", 10))




def search(pdf, keyword, canvas, margin):
    print('\n--------------------------------------------------------------------\n')
    path = os.getcwd()
    pdfs = [archive for archive in pdf if archive.endswith('.pdf')]
    folder = [folder for folder in pdf if not folder.count('.')]
    print(f"{folder}\n -------------------------------------------------------\n")
    print(pdfs)
    y = margin
    for i in range(len(folder)):
        pasta = folder[i]
        for i in range(len(pdfs)):
            arquivo = pdfs[i]
            pdf = f'{pasta}\{arquivo}'
            if (os.path.exists(pdf)):
                print(pdf)
                print('\n-------------------\nsim este caminho é valido')
            else:
                print(pdf)
                print('\n-------------------\nnão, este caminho não é valido')
    #for i in range(len(pdfs)):
        #print(pdfs[i])
        #pdfpath = f"{path}\{pdfs[i]}"
        #print(pdfpath)
        #read = PdfReader(pdfpath)
        #print(read)
        #numpages = len(read.pages)
        #for i in range(numpages):
            #pages = read.pages[i]
            #AllPDF = pages.extract_text()
            #UpperPDF = AllPDF.upper()
            #count = UpperPDF.count(keyword.upper())
            #if count > 0:
                #print('Valor Encontrado')
                #create_info_rectangle(canvas, margin, y, 400, 100, count, i+1, pdf, keyword, margin)
                #y += 100 + margin

def newsearch(path, key, canvas, margin):
    rootpath = path
    print(rootpath)
    archivespdf = []
    archives = os.listdir(rootpath)
    for i in range(len(archives)):
        if (archives[i].count('.')):
            print(archives[i]+"\n")
            print("--------- > Arquivo\n")
            archivespdf.append(archives[i])
        else:
            print(archives[i]+"\n")
            print("--------- > Pasta\n")
            PathF = f"{path}\{archives[i]}"
            archivespdf.append(archives[i])
            print(f' -------> {PathF}')
            listarchives = os.listdir(PathF)
            for i in range(len(listarchives)):
                print(listarchives[i])

                archivespdf.append(listarchives[i])
    print(archivespdf)
    threading.Thread(target=search, args=(archivespdf, key, canvas, margin)).start()
    

def result(keyword):           
    def on_mouse_wheel(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    # Configuração da janela principal
    root = tk.Tk()
    root.title("Overflow Example")

    # Configuração do frame com scrollbar
    frame = tk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=1)

    canvas = tk.Canvas(frame, bg="white")
    scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
    # Função para ajustar a barra de rolagem ao conteúdo
    def on_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    canvas.bind("<Configure>", on_configure)

    # Vincular o evento de rolagem do mouse à função on_mouse_wheel
    root.bind_all("<MouseWheel>", on_mouse_wheel)

    # Iniciar a aplicação
    newsearch(os.getcwd(), keyword, canvas, 5)
    root.mainloop()
def Main():
    def keyword():
        value = E1.get()
        result(value)
    root = tk.Tk()
    root.title("Overflow Example")
    L1 = Label(root, text="Por favor digite a palavra-chave \n no qual deseja pesquisar:")
    L1.pack( side=TOP)
    E1 = Entry(root, bd=5)
    E1.pack(side = (BOTTOM))
    B1 = Button(root, text="Procurar", command=keyword)
    B1.pack(side=LEFT)
    
    root.mainloop()
Main()
