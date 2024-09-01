import os

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa','ativo':False},
                {'nome':'Pizza Suprema', 'categoria':'Pizza','ativo':True},
                {'nome':'Cantina', 'categoria':'Italiano','ativo':False},
                ]

def exibir_nome_do_programa():
    '''Exibe o nome estilizado do programa na tela'''

    print("""      
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      """)

def exibir_opcoes():
    '''E função e reponsavel por exibir as opções'''
    print('1. Cadastrar restaurante')
    print('2. Lista restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    '''Essa função e responsavel por finalizar o app'''
    exibir_subtitulo('Finalizando app')

def voltar_ao_menu_principal():
    '''Essa função e responsavel por volta o app para o menu principal'''
    input('\nDigite uma tecla para voltar ao menu principal')
    main()    

def opcao_invalida():
    '''Essa e responsavel para avisa quando a opção que foi digitada e invalida'''
    print('Opção inválida!!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    '''Essa  função é responsavel por exibir o subtitulo'''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    '''Essa função é reponsavel por cadastrar um novo restaurante

    Inputs:
    - Nome do restaurante
    - Categoria


    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes  
        
    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!!\n')
    voltar_ao_menu_principal()

def listar_restaurantes():
    '''Essa função e responsavel por lista o restaurante do app'''
    exibir_subtitulo('listando os restaurantes')
    #para cada restaurante na lista restaurantes:nome
    print(f'{'Nome do restaurante'.ljust(23)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativo' if restaurante['ativo'] else 'desativado'
        print(f' - {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    '''Essa função e resposavel por alterna o estado do restarante '''
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja altenar o estado: ')
    restaurante_encotrado = False

    for restaurante  in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encotrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encotrado:
        print('O restaurante não foi encontrado') 
    voltar_ao_menu_principal()

def escolher_opcoes():
    '''Essa função e responsavel por escolher as opções do menu principal'''
    try:
        opcao_escolhida = int(input('escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()   
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    '''Função principal que inicia o programa'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()