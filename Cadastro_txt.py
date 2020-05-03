from desafio115arq import sistema


arq='cursoemvideo.txt'
if sistema.arquivoExiste(arq):
    print('Arquivo encontrado com sucesso!')
else:
    print('Arquivo nāo encontrado.')
    sistema.criarArquivo(arq)

sistema.menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
