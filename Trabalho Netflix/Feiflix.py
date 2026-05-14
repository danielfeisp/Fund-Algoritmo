import time

CodSecret = 123

try:
    open("usuario.txt", "a").close()
    open("admnistrador.txt", "a").close()
    open("filmes.txt", "a").close()
    open("favoritos.txt", "a").close()
except:
    pass

def apresentacao():
    print("Boas vindas ao servico de streaming de filmes da FEI")
    print()
    print("1 - Entrar com Login")
    print("2 - Cadastrar-se")
    print("3 - Sair")
    print()
    numApresentacao = int(input())
    if numApresentacao == 1:
        execLogin()
    elif numApresentacao == 2:
        execCadastro()
    elif numApresentacao == 3:
        exit()
    else:
        print()
        print("O numero digitado nao possui uma funcao atrelada. Tente novamente")
        print()
        apresentacao()

def LoginADM():
    insertNomeADM = str(input("Insira seu nome de Admnistrador: ").strip())
    insertSenhaADM = str(input("Insira sua senha: ").strip())
    ADM_achado = False
    bdADM = open("admnistrador.txt", "r")
    for linha in bdADM:
        dadosADM = linha.strip().split(";")
        if len(dadosADM) == 2:
            ADMcerto, senhaADMcerto = dadosADM
            if ADMcerto == insertNomeADM and senhaADMcerto == insertSenhaADM:
                ADM_achado = True
                break
    bdADM.close()
    if ADM_achado:
        insertCodSecreto = int(input("Insira o codigo de acesso de Admnistrador: "))
        if insertCodSecreto == CodSecret:
            acesso_liberado()
            AposLoginAdmin(insertNomeADM)
        else:
            acesso_negado()
            while True:
                insertTryAgain = int(input())
                if insertTryAgain == 1:
                    return LoginADM()
                elif insertTryAgain == 2:
                    return apresentacao()
                else:
                    print()
                    print("O numero digitado nao possui uma funcao atrelada. Tente novamente")
                    print()
                    print("1 - Tentar Novamente")
                    print("2 - Voltar para o menu")
                    print()
    else:
        print("Usuario nao encontrado. Tente novamente ou cadastre um novo Usuario")
        print()
        print("1 - Tentar novamente")
        print("2 - Cadastrar novo usuario")
        while True:
            insertTenteDenovo = int(input())
            if insertTenteDenovo == 1:
                return LoginADM()
            elif insertTenteDenovo == 2:
                return execCadastro()
            else:
                print()
                print("O numero digitado nao possui uma funcao atrelada. Tente novamente")
                print()
                print("1 - Tentar Novamente")
                print("2 - Cadastrar novo usuario")
                print()

def LoginUsuario():
    insertNomeUsu = str(input("Insira seu nome de Usuario: ").strip())
    insertSenhaUsu = str(input("Insira sua senha: ").strip())
    usuario_achado = False
    bdUsuario = open("usuario.txt", "r")
    for linha in bdUsuario:
        dadosUsu = linha.strip().split(";")
        if len(dadosUsu) == 2:
            Usucerto, senhaUsucerto = dadosUsu
            if Usucerto == insertNomeUsu and senhaUsucerto == insertSenhaUsu:
                usuario_achado = True
                break
    bdUsuario.close()
    if usuario_achado:
        acesso_liberado()
        AposLoginUsuario(insertNomeUsu)
    else:
        print()
        print("Usuario nao encontrado. Tente novamente ou cadastre um novo Usuario")
        print()
        print("1 - Tentar novamente")
        print("2 - Cadastrar novo usuario")
        while True:
            insertTenteDenovo = int(input())
            if insertTenteDenovo == 1:
                return LoginUsuario()
            elif insertTenteDenovo == 2:
                return execCadastro()
            else:
                print()
                print("O numero digitado nao possui uma funcao atrelada. Tente novamente")
                print()
                print("1 - Tentar Novamente")
                print("2 - Cadastrar novo Usuario")
                print()

def execLogin():
    print()
    print("Deseja logar com que tipo de conta?")
    print()
    print("1 - Login de Admnistrador")
    print("2 - Login de Usuario")
    print("3 - Voltar para o menu")
    print()
    numLogin = int(input())
    if numLogin == 1:
        print()
        LoginADM()
    elif numLogin == 2:
        print()
        LoginUsuario()
    elif numLogin == 3:
        print()
        apresentacao()
    else:
        print()
        print("O numero digitado nao possui uma funcao atrelada. Tente novamente")
        print()
        execLogin()

def CadastroUsu():
    NovoNomeUsu = str(input("Insira seu nome de Usuario: ").strip())
    NovaSenhaUsu = str(input("Insira uma senha para sua conta: ").strip())
    if ";" in NovoNomeUsu or "|" in NovoNomeUsu:
        print("Erro: O nome de usuario nao pode conter caracteres invalidos")
        print()
        return CadastroUsu()
    elif NovoNomeUsu == "" or NovaSenhaUsu == "":
        print("Digite um nome de usuario ou senha valido")
        print()
        return CadastroUsu()
    else:
        usuariojaexiste = False
        bdUsuario = open("usuario.txt", "r")
        for linha in bdUsuario:
            dadosU = linha.strip().split(";")
            if len(dadosU) == 2:
                if dadosU[0] == NovoNomeUsu:
                    usuariojaexiste = True
                    break
        bdUsuario.close()

    if usuariojaexiste:
        print("Este nome de usuario ja esta em uso, tente outro")
        print()
        return CadastroUsu()
    else:
        bdUsuario = open("usuario.txt", "a")
        bdUsuario.write(f"{NovoNomeUsu};{NovaSenhaUsu}\n")
        bdUsuario.close()
        print("Cadastro concluido, voce pode logar agora mesmo.")
        print()
        apresentacao()

def CadastroADM():
    insertCodSecret = int(input("Insira o codigo ultra secreto da FEI: "))
    if insertCodSecret == CodSecret:
        print()
        print("Carregando")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print()
        print("Codigo Validado")
        print()
        NovoNomeADM = str(input("Insira seu nome de usuario: ").strip())
        NovaSenhaADM = str(input("Insira uma senha para sua conta: ").strip())
        if ";" in NovoNomeADM or "|" in NovoNomeADM:
            print("Erro: O nome de usuario nao pode conter caracteres invalidos")
            print()
            return CadastroADM()
        elif NovoNomeADM == "" or NovaSenhaADM == "":
            print("Digite um nome de usuario ou senha valido")
            return CadastroADM()
        else:
            ADMjaexiste = False
            bdADM = open("admnistrador.txt", "r")
            for linha in bdADM:
                dadosU = linha.strip().split(";")
                if len(dadosU) == 2:
                    if dadosU[0] == NovoNomeADM:
                        ADMjaexiste = True
                        break
            bdADM.close()
            
            if ADMjaexiste:
                print("Este nome de usuario ja esta em uso, tente outro")
                print()
                return CadastroADM()
            else:
                bdADM = open("admnistrador.txt", "a")
                bdADM.write(f"{NovoNomeADM};{NovaSenhaADM}\n")
                bdADM.close()
                print("Cadastro concluido, voce pode logar agora mesmo.")
                print()
                apresentacao()
    else:
        acesso_negado()
        while True:
            insertNovaTentativa = int(input())
            if insertNovaTentativa == 1:
                print()
                return CadastroADM()
            elif insertNovaTentativa == 2:
                print()
                return apresentacao()
            else:
                print()
                print("O numero digitado nao possui uma funcao atrelada. Tente novamente")
                print()

def execCadastro():
    print()
    print("Deseja se cadastrar como um novo ADM ou Usuario?")
    print()
    print("1 - Novo Usuario")
    print("2 - Novo Admnistrador")
    print("3 - Voltar para o menu")
    print()
    numCadastro = int(input())
    if numCadastro == 1:
        print()
        CadastroUsu()
    elif numCadastro == 2:
        print()
        CadastroADM()
    elif numCadastro == 3:
        print()
        apresentacao()
    else:
        print()
        print("O numero digitado nao possui uma funcao atrelada. Tente novamente")
        print()
        execCadastro()

def acesso_liberado():
    print()
    print("Carregando")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print()
    print("Acesso Liberado")
    print()

def acesso_negado():
    print()
    print("Carregando")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print()
    print("Acesso Negado")
    print()
    print("1 - Tentar Novamente")
    print("2 - Voltar para o menu")
    print()

def AposLoginUsuario(usuarioLogado):
    while True:
        print("O que deseja fazer?")
        print()
        print("1 - Buscar filme por nome")
        print("2 - Curtir ou descurtir filmes")
        print("3 - Gerenciar listas de favoritos")
        print("4 - Voltar para o menu inicial")
        print()
        opcao = int(input())
        
        if opcao == 1:
            print()
            busca = input("Digite o nome do filme: ").strip().lower()
            achou = False
            bdFilmes = open("filmes.txt", "r")
            for linha in bdFilmes:
                dados = linha.strip().split("|")
                if len(dados) >= 9:
                    if busca in dados[0].lower():
                        print()
                        print("Titulo: " + dados[0])
                        print("Sinopse: " + dados[1])
                        print("Duracao: " + dados[2])
                        print("Atores: " + dados[3])
                        print("Diretor: " + dados[4])
                        print("Lancamento: " + dados[5])
                        print("Premios: " + dados[6])
                        print("Baseado em livro: " + dados[7])
                        print("Curtidas: " + dados[8])
                        print()
                        achou = True
            bdFilmes.close()
            if not achou:
                print("Nenhum filme encontrado.")
                print()
                
        elif opcao == 2:
            print()
            busca = input("Digite o nome exato do filme: ").strip()
            filmes = []
            achou = False
            ja_curtido = False
            ja_descurtido = False
            bdCurtidas = open("curtidas.txt", "r")
            for linha in bdCurtidas:
                if f"{usuarioLogado}|{busca}" == linha.strip():
                    ja_curtido = True
                    break
            bdCurtidas.close()
            bdDescurtidas = open("descurtidas.txt", "r")
            for linha in bdDescurtidas:
                if f"{usuarioLogado}|{busca}" == linha.strip():
                    ja_descurtido = True
                    break
            bdDescurtidas.close()
            bdFilmes = open("filmes.txt", "r")
            for linha in bdFilmes:
                dados = linha.strip().split("|")
                if len(dados) >= 9:
                    if dados[0] == busca:
                        achou = True
                        print("Curtidas atuais: " + dados[8])
                        print()
                        print("1 - Curtir")
                        print("2 - Descurtir")
                        print()
                        acao = int(input())
                        curtidas = int(dados[8])
                        if acao == 1:
                            if ja_curtido:
                                print("Você já curtiu esse filme")
                                print()
                                AposLoginUsuario(usuarioLogado)
                            elif ja_descurtido or (not ja_curtido and not ja_descurtido):
                                curtidas = curtidas + 1
                                bdCurtidas = open("curtidas.txt", "a")
                                bdCurtidas.write(f"{usuarioLogado}|{busca}\n")
                                bdCurtidas.close()
                                if ja_descurtido:
                                    bdDescurtidas = open("descurtidas.txt", "r")
                                    linha_descurtidas = bdDescurtidas.readlines()
                                    bdDescurtidas.close()
                                    bdDescurtidas = open("descurtidas.txt", "w")
                                    for linha in linha_descurtidas:
                                        if linha.strip() == f"{usuarioLogado}|{busca}":
                                            continue
                                        bdDescurtidas.write(linha)
                                    bdDescurtidas.close()
                                print()
                                print("Filme curtido!")
                        elif acao == 2:
                            if ja_descurtido:
                                print("Você já descurtiu esse filme")
                                print()
                                AposLoginUsuario(usuarioLogado)
                            elif ja_curtido or (not ja_curtido and not ja_descurtido):
                                if curtidas > 0:
                                    curtidas = curtidas - 1
                                bdDescurtidas = open("descurtidas.txt", "a")
                                bdDescurtidas.write(f"{usuarioLogado}|{busca}\n")
                                bdDescurtidas.close()
                                if ja_curtido:
                                    bdCurtidas = open("curtidas.txt", "r")
                                    linha_curtidas = bdCurtidas.readlines()
                                    bdCurtidas.close()
                                    bdCurtidas = open("curtidas.txt", "w")
                                    for linha in linha_curtidas:
                                        if linha.strip() == f"{usuarioLogado}|{busca}":
                                            continue
                                        bdCurtidas.write(linha)
                                    bdCurtidas.close()
                                print()
                                print("Filme Descurtido!")
                        dados[8] = str(curtidas)
                filmes.append("|".join(dados) + "\n")
            bdFilmes.close()
            
            if achou:
                bdFilmes = open("filmes.txt", "w")
                for f in filmes:
                    bdFilmes.write(f)
                bdFilmes.close()
                print()
            else:
                print()
                print("Filme nao encontrado.")
                print()
                
        elif opcao == 3:
            print()
            gerenciarFavoritos(usuarioLogado)
            
        elif opcao == 4:
            print()
            apresentacao()
            break

def gerenciarFavoritos(usuarioLogado):
    while True:
        print()
        print("1 - Ver minhas listas")
        print("2 - Criar nova lista")
        print("3 - Adicionar filme na lista")
        print("4 - Remover filme da lista")
        print("5 - Excluir lista")
        print("6 - Voltar")
        print()
        opcao = int(input())
        
        if opcao == 1:
            bdFav = open("favoritos.txt", "r")
            for linha in bdFav:
                dados = linha.strip().split("|")
                if len(dados) >= 2:
                    if dados[0] == usuarioLogado:
                        print()
                        print("Lista: " + dados[1])
                        if len(dados) == 3 and dados[2] != "":
                            print("Filmes: " + dados[2])
                        else:
                            print("Filmes: Nenhum")
            bdFav.close()
            
        elif opcao == 2:
            print()
            nomeLista = input("Nome da nova lista: ").strip()
            bdFav = open("favoritos.txt", "r")
            lista_duplicada = False
            for linha in bdFav:
                if usuarioLogado in linha and nomeLista in linha:
                    lista_duplicada = True
                    break
            bdFav.close()
            if lista_duplicada:
                print()
                print(f"Já existe uma lista chamada {nomeLista} para este perfil")
                print()
                gerenciarFavoritos(usuarioLogado)
            else:
                bdFav = open("favoritos.txt", "a")
                bdFav.write(f"{usuarioLogado}|{nomeLista}|\n")
                bdFav.close()
                print("Lista criada com sucesso.")
                print()
            
        elif opcao == 3 or opcao == 4:
            print()
            nomeLista = input("Nome da lista: ").strip()
            nomeFilme = input("Nome exato do filme: ").strip()
            linhas = []
            achouLista = False
            bdFav = open("favoritos.txt", "r")
            for linha in bdFav:
                dados = linha.strip().split("|")
                if len(dados) >= 2 and dados[0] == usuarioLogado and dados[1] == nomeLista:
                    achouLista = True
                    filmes = []
                    if len(dados) == 3 and dados[2] != "":
                        filmes = dados[2].split(",")
                        
                    if opcao == 3:
                        if nomeFilme not in filmes:
                            filmes.append(nomeFilme)
                            print("Filme adicionado.")
                        else:
                            print("O filme ja esta na lista.")
                    elif opcao == 4:
                        if nomeFilme in filmes:
                            filmes.remove(nomeFilme)
                            print("Filme removido.")
                        else:
                            print("O filme nao esta na lista.")
                            
                    novaLinha = f"{dados[0]}|{dados[1]}|{','.join(filmes)}\n"
                    linhas.append(novaLinha)
                else:
                    linhas.append(linha)
            bdFav.close()
            
            if achouLista:
                bdFav = open("favoritos.txt", "w")
                for l in linhas:
                    bdFav.write(l)
                bdFav.close()
            else:
                print("Lista nao encontrada.")
            print()
            
        elif opcao == 5:
            nomeLista = input("Nome da lista para excluir: ").strip()
            linhas = []
            achouLista = False
            bdFav = open("favoritos.txt", "r")
            for linha in bdFav:
                dados = linha.strip().split("|")
                if len(dados) >= 2 and dados[0] == usuarioLogado and dados[1] == nomeLista:
                    achouLista = True
                else:
                    linhas.append(linha)
            bdFav.close()
            
            if achouLista:
                bdFav = open("favoritos.txt", "w")
                for l in linhas:
                    bdFav.write(l)
                bdFav.close()
                print("Lista excluida.")
            else:
                print("Lista nao encontrada.")
            print()
            
        elif opcao == 6:
            print()
            break

def AposLoginAdmin(adminLogado):
    while True:
        print()
        print("O que deseja fazer?")
        print()
        print("1 - Cadastrar novo video")
        print("2 - Excluir video")
        print("3 - Consultar usuarios")
        print("4 - Visualizar estatisticas do sistema")
        print("5 - Buscar filme por nome")
        print("6 - Curtir ou descurtir filmes")
        print("7 - Gerenciar listas de favoritos")
        print("8 - Voltar para o menu inicial")
        print()
        opcao = int(input())
        
        if opcao == 1:
            nome = input("Titulo do Filme: ").strip()
            sinopse = input("Sinopse: ").strip()
            duracao = input("Duracao: ").strip()
            atores = input("3 Atores principais: ").strip()
            diretor = input("Diretor: ").strip()
            data = input("Ano e Mes de Lancamento: ").strip()
            premios = input("Premios: ").strip()
            baseado = input("Baseado em um livro: ").strip()
            bdFilmes = open("filmes.txt", "a")
            bdFilmes.write(f"{nome}|{sinopse}|{duracao}|{atores}|{diretor}|{data}|{premios}|{baseado}|0\n")
            bdFilmes.close()
            print("Video cadastrado.")
            print()
            
        elif opcao == 2:
            busca = input("Digite o Titulo exato do filme a ser excluido: ").strip().lower()
            filmes = []
            excluido = False
            bdFilmes = open("filmes.txt", "r")
            for linha in bdFilmes:
                dados = linha.strip().split("|")
                if len(dados) > 0 and dados[0].lower() == busca:
                    excluido = True
                else:
                    filmes.append(linha)
            bdFilmes.close()
            
            if excluido:
                bdFilmes = open("filmes.txt", "w")
                for f in filmes:
                    bdFilmes.write(f)
                bdFilmes.close()
                print("Video excluido com sucesso.")
            else:
                print("Video nao encontrado.")
            print()
            
        elif opcao == 3:
            print()
            print("Usuarios do sistema:")
            bdUsuario = open("usuario.txt", "r")
            for linha in bdUsuario:
                dados = linha.strip().split(";")
                if len(dados) >= 1:
                    print(dados[0])
            bdUsuario.close()
            print()
            
        elif opcao == 4:
            totUsu = 0
            bdUsuario = open("usuario.txt", "r")
            for linha in bdUsuario:
                totUsu = totUsu + 1
            bdUsuario.close()
            
            filmesEst = []
            bdFilmes = open("filmes.txt", "r")
            for linha in bdFilmes:
                dados = linha.strip().split("|")
                if len(dados) >= 9:
                    filmesEst.append([dados[0], int(dados[8])])
            bdFilmes.close()
            print()
            print("Total de usuarios: " + str(totUsu))
            print("Total de videos: " + str(len(filmesEst)))
            print("Top 5 videos mais curtidos:")
            
            filmesEst.sort(key=lambda x: x[1], reverse=True)
            
            limite = 5
            if len(filmesEst) < 5:
                limite = len(filmesEst)
                
            for i in range(limite):
                print(str(i+1) + " - " + filmesEst[i][0] + " com " + str(filmesEst[i][1]) + " curtidas")
            print()

        elif opcao == 5:
            print()
            busca = input("Digite o nome do filme: ").strip().lower()
            achou = False
            bdFilmes = open("filmes.txt", "r")
            for linha in bdFilmes:
                dados = linha.strip().split("|")
                if len(dados) >= 9:
                    if busca in dados[0].lower():
                        print()
                        print("Titulo: " + dados[0])
                        print("Sinopse: " + dados[1])
                        print("Duracao: " + dados[2])
                        print("Atores: " + dados[3])
                        print("Diretor: " + dados[4])
                        print("Lancamento: " + dados[5])
                        print("Premios: " + dados[6])
                        print("Baseado em livro: " + dados[7])
                        print("Curtidas: " + dados[8])
                        achou = True
            bdFilmes.close()
            if not achou:
                print("Nenhum filme encontrado.")
                
        elif opcao == 6:
            print()
            busca = input("Digite o nome exato do filme: ").strip()
            filmes = []
            achou = False
            ja_curtido = False
            ja_descurtido = False
            bdCurtidas = open("curtidas.txt", "r")
            for linha in bdCurtidas:
                if f"{adminLogado}|{busca}" == linha.strip():
                    ja_curtido = True
                    break
            bdCurtidas.close()
            bdDescurtidas = open("descurtidas.txt", "r")
            for linha in bdDescurtidas:
                if f"{adminLogado}|{busca}" == linha.strip():
                    ja_descurtido = True
                    break
            bdDescurtidas.close()
            bdFilmes = open("filmes.txt", "r")
            for linha in bdFilmes:
                dados = linha.strip().split("|")
                if len(dados) >= 9:
                    if dados[0] == busca:
                        achou = True
                        print("Curtidas atuais: " + dados[8])
                        print()
                        print("1 - Curtir")
                        print("2 - Descurtir")
                        print()
                        acao = int(input())
                        curtidas = int(dados[8])
                        if acao == 1:
                            if ja_curtido:
                                print("Você já curtiu esse filme")
                                print()
                                AposLoginUsuario(adminLogado)
                            elif ja_descurtido or (not ja_curtido and not ja_descurtido):
                                curtidas = curtidas + 1
                                bdCurtidas = open("curtidas.txt", "a")
                                bdCurtidas.write(f"{adminLogado}|{busca}\n")
                                bdCurtidas.close()
                                if ja_descurtido:
                                    bdDescurtidas = open("descurtidas.txt", "r")
                                    linha_descurtidas = bdDescurtidas.readlines()
                                    bdDescurtidas.close()
                                    bdDescurtidas = open("descurtidas.txt", "w")
                                    for linha in linha_descurtidas:
                                        if linha.strip() == f"{adminLogado}|{busca}":
                                            continue
                                        bdDescurtidas.write(linha)
                                    bdDescurtidas.close()
                                print()
                                print("Filme curtido!")
                        elif acao == 2:
                            if ja_descurtido:
                                print("Você já descurtiu esse filme")
                                print()
                                AposLoginUsuario(adminLogado)
                            elif ja_curtido or (not ja_curtido and not ja_descurtido):
                                if curtidas > 0:
                                    curtidas = curtidas - 1
                                bdDescurtidas = open("descurtidas.txt", "a")
                                bdDescurtidas.write(f"{adminLogado}|{busca}\n")
                                bdDescurtidas.close()
                                if ja_curtido:
                                    bdCurtidas = open("curtidas.txt", "r")
                                    linha_curtidas = bdCurtidas.readlines()
                                    bdCurtidas.close()
                                    bdCurtidas = open("curtidas.txt", "w")
                                    for linha in linha_curtidas:
                                        if linha.strip() == f"{adminLogado}|{busca}":
                                            continue
                                        bdCurtidas.write(linha)
                                    bdCurtidas.close()
                                print()
                                print("Filme Descurtido!")
                        dados[8] = str(curtidas)
                filmes.append("|".join(dados) + "\n")
            bdFilmes.close()
            
            if achou:
                bdFilmes = open("filmes.txt", "w")
                for f in filmes:
                    bdFilmes.write(f)
                bdFilmes.close()
                print()
            else:
                print()
                print("Filme nao encontrado.")
                print()
        elif opcao == 7:
            gerenciarFavoritos(adminLogado)
        elif opcao == 8:
            apresentacao()
            break

if __name__ == "__main__":
    apresentacao()