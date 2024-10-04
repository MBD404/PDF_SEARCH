# Este passo deverá fazer o mesmo que o passo anterior
# porém agora os arquivos devem ser pdfs, haverão
# 4 Senhas e 5 Arquivos pdf para poder abrir dentro do programa

# -- !!!  DESAFIO  !!! --
# ESTE DESÁFIO CONSISTE EM PESQUISAR UMA PALAVRA CHAVE DENTRO DE TODOS OS PDFS 

# --------- COLINHAS ------- 
# EXEMPLO DE COUNT: 

#frase = 'O roeu a roupa do rei de Roma'
#found = frase.count('rat')
#if found:
    #print(f'esta frase foi encontrada {found} Vezes')
#else:
    #print('frase não encontrada')

from pypdf import PdfReader
import os
from time import sleep


class App:
    def Start():
        path = os.getcwd()
        print('BEM VINDO\nAO MEU LEITOR DE PDF')
        print('Porfavor insira a Key Correta:')
        arquivos = os.listdir(path)
        for i, arquivo in enumerate(arquivos, start=1):
                print(f"{i} - {arquivo}")
        print('Escolha\n---------------------------')
        choice = int(input('/> '))
        if choice == 0000:
             return False
        else:
             choice = choice - 1
             arquivo = arquivos[choice]
             App.Get_Pdf(arquivo)
    def Get_Pdf(pdf):
         pdf = pdf
         App.get_password(pdf)
    def get_password(pdf):
         Key = PdfReader(pdf)
         Correct_Key = PdfReader('password-4.pdf')
         Key_Content = {}
         CKey_Content = {}
         for i, pages1 in enumerate(Key.pages):
              Key_Content[i + 1] = pages1.extract_text()
         for i, pages2 in enumerate(Correct_Key.pages):
              CKey_Content[i + 1] = pages2.extract_text()
        
         print(f'Chave Escolhida : {Key_Content[1]}')
         App.Verify_Password(Key_Content[1], CKey_Content[1])

    def Verify_Password(Key,CKey):
        username = os.environ.get('USERNAME')
        if Key == CKey:
              print(f"""
            
 ##                                             ##                 ###
 ##       ######   ##  ##            ##  ##            ######       ##   ######
 ######   ##  ##   ######            ##  ##    ###     ##  ##   ######   ##  ##
 ##  ##   ######   ######            ##  ##     ##     ##  ##   ##  ##   ##  ##
 ##  ##   ##       ## ###             ####      ##     ##  ##   ##  ##   ##  ##
 ######   #####    ## ###              ##     ######   ##  ##   ######   ######          

                Seja Bem-vind@ {username}
                """)
              sleep(2)
        else:
            print('Senha Incorret... Tente Novamente')
            sleep(2)
            App.Start()
    

# ------- PARTE PARA LER OS PDFs ------------


App.Start()
