'''TUTORIAL DE IMPLANTAÇÃO DE SISTEMAS'''

'''Utilização do módulo webbrowser na linguagem Python.'''

import subprocess 
import webbrowser

feito = False
print("Projeto: TUTORIAL DE IMPLANTAÇÃO DE SISTEMAS")
while not feito:
    print("Selecione a opção!")
    print("1. Verificar as etapas do processo de implantação de sistemas.")
    print("2. Alguns modelos de governança de TI utilizados em implantações de sistemas.")
    print("3. Visitando as páginas oficiais dos modelos apresentados.")
    print("4. Sair")

    def open_pdf_in_vscode(file_path):
        subprocess.Popen(['code', file_path])

    escolha = input("> ")

    if escolha == "1": 
        #webbrowser.open("http://www.python.org")
        file_path = '/home/luanna/Área de Trabalho/projeto/implantacao_sistemas/tutorial.pdf'
        open_pdf_in_vscode(file_path)

    elif escolha == "2":
        #webbrowser.open("https://docs.python.org/3/py-modindex.html")
        file_path = '/home/luanna/Área de Trabalho/projeto/implantacao_sistemas/modelos.pdf'
        open_pdf_in_vscode(file_path)

    elif escolha == "3":
        opcao = None
        print("Seguem os links das páginas oficiais dos tópicos mencionados.\n")
        while opcao not in [1, 2, 3, 4, 5]:  # Enquanto a opção não estiver na lista de opções válidas
            opcao = int(input("Escolha uma opção (\n1-ITIL\n2-COBIT\n3-ISO/IEC 27001\n4-PMBOK\n5-PRINCE2\n): "))

            if opcao == 1:
                print("Opção 1 escolhida\nITIL (Information Technology Infrastructure Library)")
                webbrowser.open("https://www.axelos.com/best-practice-solutions/itil")
            elif opcao == 2:
                print("Opção 2 escolhida\nCOBIT (Control Objectives for Information and Related Technologies)")
                webbrowser.open("https://www.isaca.org/resources/cobit")
            elif opcao == 3:
                print("Opção 3 escolhida\nISO/IEC 27001")
                webbrowser.open("https://www.iso.org/standard/54534.html")
            elif opcao == 4:
                print("Opção 4 escolhida\nPMBOK (Project Management Body of Knowledge)")
                webbrowser.open("https://www.pmi.org/pmbok-guide-standards")
            elif opcao == 5:
                print("Opção 5 escolhida\nPRINCE2 (Projects IN Controlled Environments)")
                webbrowser.open("https://www.axelos.com/best-practice-solutions/prince2")
            else:
                print("Opção inválida")
            
            print("Os links apresentados direcionam para as páginas oficiais dos respectivos tópicos,\n onde você pode encontrar mais informações e recursos sobre cada um deles.\nBons estudos!\n")
        # Usando um laço de repetição for para iterar sobre as opções
        #for i in range(1, 6):
            #print(f"Opção {i}")


    elif escolha == "4":
        feito = True
    else:
        print("Opção inválida. Escolha uma opção entre 1 a 4")


   