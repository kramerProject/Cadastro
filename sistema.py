pessoas=[]

def tit(msg):
    print('-'*30)
    print(msg.center(30))
    print('-' * 30)

def menu(lista):

    while True:
        tit('MENU PRINCIPAL')
        c=1
        for item in lista:
            print(f'\033[0;33m{c} - \033[0;34m{item}\033[m')
            c+=1
        print('-'*30)

        op = leia('\033[0;33mSua opçāo: \033[m')

        if op == 2:
            cadastrar()
        elif op == 1:
            ver()
        elif op == 3:
            tit('SAINDO DO SISTEMA! ATÉ LOGO.')
            break


def cadastrar():

    tit('NOVO CADASTRO')
    nome=str(input('Digite o nome da pessoa: '))
    idade=int(input('Digite a idade: '))
    try:
        a=open('cursoemvideo.txt','at')
    except:
        print('Houve um erro na abertura do arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na hora de escrever os dados')
        else:
            print(f'Novo Registro de {nome} adicionado')
            a.close()



def ver():
    try:
        arquivo=open('cursoemvideo.txt','rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        tit('PESSOAS CADASTRADAS')
        for linha in arquivo:
            dado=linha.split(';')
            dado[1]=dado[1].replace('\n','')
            print(f'{dado[0]:<23}{dado[1]} anos')
    finally:
        arquivo.close()

def leia(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mErro: digite um número inteiro válido\033[m')
        except KeyboardInterrupt:
            print('\n\033[0;31mErro: Usuário optou por nāo digitar um número\033[m')
            return 0
        else:
            return n


def arquivoExiste(nome):
    try:
        a=open(nome,'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a=open(nome,'wt+')
        a.close()
    except:
        print('Houve na criaçāo do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')





