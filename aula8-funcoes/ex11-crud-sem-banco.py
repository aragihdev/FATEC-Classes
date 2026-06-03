produtos = []

def mostrar_opcoes():
    print("1 - Cadastar produto")
    print("2 - Remover produto")
    print("3 - Listar produtos")
    print("4 - Procurar produto")
    print("5 - Editar produto")
    print("6 - Encerrar sessão")
def novo_produto():
    nome_produto = input("Qual o nome do produto? ")
    while True:
        valor_produto = float(input("Qual o valor do produto? "))
        if valor_produto > 0:
            break
        else:
            print("Valor inválido.")
    while True:
        quantidade_produto = int(input(f"Quantos {nome_produto} serão adicionados? "))
        if quantidade_produto > 0:
            break
        else:
            print("Quantidade inválida.")
    produto = {"nome": nome_produto,
               "preço": valor_produto,
               "quantidade": quantidade_produto}
    produtos.append(produto)

def listar_produtos():
    if len(produtos) == 0:
        print("Não há produtos cadastros ainda.")
    else:
        print("LISTA DE PRODUTOS")
        for i, produto in enumerate(produtos):
            print()
            print(f"Código:{i}\nNome: {produto['nome']}\nPreço: {produto['preço']}\nQuantidade: {produto['quantidade']}")
        print()

def remover_produto():
    listar_produtos()
    if len(produtos) < 0:
        print("Não há produtos para serem removidos.")
    else:
        codigo_remover = int(input("Digite o código do produto que deseja remover: "))
        if 0 <= codigo_remover < len(produtos):
            produto_removido = produtos.pop(codigo_remover)
            print(f"Produto: {produto_removido['nome']} removido com sucesso.")
        else:
            print("Código inválido.")
def buscar_produtos():
    nome_buscar = input("Qual o nome do produto que deseja buscar? ").lower()
    for i, produto in enumerate(produtos):
        if produto['nome'] == nome_buscar:
            print()
            print("PRODUTO ENCONTRADO!")
            print()
            print(f"Código:{i}\nNome: {produto['nome']}\nPreço: {produto['preço']}\nQuantidade: {produto['quantidade']}")
            print()
        else:
            print("Produto não encontrado.")
def editar_produto():
    codigo_editar = int(input("Qual o código do produto que será editado? "))
    for i, produto in enumerate(produtos):
        if i == codigo_editar:
            print()
            print(f"PRODUTO A SER EDITADO: {produto['nome']}")
            print()
            produtos[i]['nome'] = input(f"Qual será o novo nome? ")
            produtos[i]['preço'] = input(f"Qual será o novo preço? ")
            produtos[i]['quantidade'] = input(f"Qual será a nova quantidade? ")
            print()
while True:
    mostrar_opcoes()
    usuario_escolhe = input("O que deseja fazer?")
    if usuario_escolhe == "1":
        novo_produto()
    elif usuario_escolhe == "2":
        remover_produto()
    elif usuario_escolhe == "3":
        listar_produtos()
    elif usuario_escolhe == "4":
        buscar_produtos()
    elif usuario_escolhe == "5":
        editar_produto()
    elif usuario_escolhe == "6":
        break
    else:
        print("Opção inválida")