import os

restaurantes = [{'nome':'toyotomi', 'categoria': 'Sushi', 'ativo': False},{'nome': 'Pizza Rex', 'categoria': 'Pizza', 'ativo': True},{'nome':'cantina', 'categoria': 'Italiana', 'ativo': False}]

def exibir_nome_do_programa():
    '''Exibe o nome do programa na tela'''
    print(""" 
██████████████████████████████████████████████████████████████████████████
█─▄▄▄▄██▀▄─██▄─▄─▀█─▄▄─█▄─▄▄▀███▄─▄▄─█▄─▀─▄█▄─▄▄─█▄─▄▄▀█▄─▄▄─█─▄▄▄▄█─▄▄▄▄█
█▄▄▄▄─██─▀─███─▄─▀█─██─██─▄─▄████─▄█▀██▀─▀███─▄▄▄██─▄─▄██─▄█▀█▄▄▄▄─█▄▄▄▄─█
▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀▀▀▄▄▄▄▄▀▄▄█▄▄▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀""")

def exibir_opcoes():
    '''Eixibe as opções que o usuário pode escolher'''
    print('1. Cadastrar restaurante\n2. listar restaurante\n3. Alternar estado do restaurante \n4. Sair\n')

def finalizar_app():
    '''Exibe a mensagem de finalização do app'''
    exibir_subtitulo('encerrando o app')
    

def voltar_ao_menu_principal():
    '''Volta para o menu principal após o usuário digitar qualquer tecla

    Outputs:
    - Volta ao menu principal
    '''

    input('\nDigite uma tecla para voltar ao menu principal ')
    main()

def opcao_invalida():
    '''Exibe uma mensagem de opção invalida e volta ao menu principal

        Outputs:
        - volta ao menu principal
    '''
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    '''Exibe o subtitulo pré-formatado para cada opção escolhida

        Inputs:
        - texto: string - o texto do subtítulo
    '''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    '''Essa função é responsável por cadastrar um novo restaurante

        Inputs:
        - Nome do Restaurante;
        - Categoria

        Outputs:
        - Adiciona um novo restaurante a lista de restaurantes
    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    
    nome_do_restaurante = input("digite o nome do restaurante que deseja cadastrar: ")
    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'o restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()

def listar_restaurantes():
    '''Lista os restaurantes presentes la lista restaurantes
    
        Ouputs:
        - Exibe a lista de restaurantes
    '''
    exibir_subtitulo('Listando os restaurantes')
    
    print(f' {'Nome_do_restaurante'.ljust(23)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(22)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    '''Altera o estado dos restaurantes entre ativo e inativo
    
        Inputs:
        - Nome do restaurante que se deseja alterar o estado

        Outputs:
        - Exibe mensagem de sucesso ou de restaurante não encontrado
    '''
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
        
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado.')
    
    voltar_ao_menu_principal()

def escolher_opcao():
    '''Pede para o usuário escolher uma opção dentre as disponíveis e executa a função respectiva
    
        Inputs: 
        - numero de escolha da opção

        Outputs:
        - Executa a opção escolhida
    '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        #print(f'voce escolheu a opção {opcao_escolhida}')
        '''match opcao_escolhida:
            case 1:
                print('cadastrar restaurante')
            case 2:
                print('listar restaurante')
            case 3:
                print('ativar restaurante')
            case 4:
                finalizar_app()
            case _:
                print('opção inválida')'''

        #fazer versão com match
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
    '''Inicia o programa'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()