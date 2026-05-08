import time

CodSecret = 123

def apresentacao():
    print("Boas vindas ao serviço de streaming de filmes da FEI")
    print()
    print("1 - Entrar com Login")
    print("2 - Cadastrar-se")
    print()
    numApresentacao = int(input())
    if numApresentacao == 1:
        execLogin()
    elif numApresentacao == 2:
        execCadastro()
    else:
        print()
        print("O número digitado não possui uma função atrelada. Tente novamente")
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
        insertCodSecreto = int(input("Insira o código de acesso de Admnistrador: "))
        if insertCodSecreto == CodSecret:
            acesso_liberado()
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
                    print("O número digitado não possui uma função atrelada. Tente novamente")
                    print()
                    print("1 - Tentar Novamente")
                    print("2 - Voltar para o menu")
                    print()
    else:
        print("Usuário não encontrado. Tente novamente ou cadastre um novo Usuário")
        print()
        print("1 - Tentar novamente")
        print("2 - Cadastrar novo usuário")
        while True:
            insertTenteDenovo = int(input())
            if insertTenteDenovo == 1:
                return LoginADM()
            elif insertTenteDenovo == 2:
                return execCadastro()
            else:
                print()
                print("O número digitado não possui uma função atrelada. Tente novamente")
                print()
                print("1 - Tentar Novamente")
                print("2 - Cadastrar novo usuário")
                print()
def LoginUsuario():
    insertNomeUsu = str(input("Insira seu nome de Usuário: ").strip())
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
        AposLoginUsuario()
    else:
        print("Usuário não encontrado. Tente novamente ou cadastre um novo Usuário")
        print()
        print("1 - Tentar novamente")
        print("2 - Cadastrar novo usuário")
        while True:
            insertTenteDenovo = int(input())
            if insertTenteDenovo == 1:
                return LoginUsuario()
            elif insertTenteDenovo == 2:
                return execCadastro()
            else:
                print()
                print("O número digitado não possui uma função atrelada. Tente novamente")
                print()
                print("1 - Tentar Novamente")
                print("2 - Cadastrar novo Usuario")
                print()

def execLogin():
    print()
    print("Deseja logar com que tipo de conta?")
    print()
    print("1 - Login de Admnistrador")
    print("2 - Login de Usuário")
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
        print("O número digitado não possui uma função atrelada. Tente novamente")
        print()
        execLogin()

def CadastroUsu():
    NovoNomeUsu = str(input("Insira seu nome de Usuário: ").strip())
    NovaSenhaUsu = str(input("Insira uma senha para sua conta: ").strip())
    if ";" in NovoNomeUsu:
        print("Erro: O nome de usuário não pode conter ponto e vírgula (;)")
        print()
        return CadastroUsu()
    elif NovoNomeUsu == "" or NovaSenhaUsu == "":
        print("Digite um nome de usuário ou senha válido")
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
        print("Este nome de usuário já está em uso, tente outro")
        print()
        return CadastroUsu()
    else:
        bdUsuario = open("usuario.txt", "a")
        bdUsuario.write(f"{NovoNomeUsu};{NovaSenhaUsu}\n")
        bdUsuario.close()
        print("Cadastro concluído, você pode logar agora mesmo.")
        print()
        apresentacao()
def CadastroADM():
    insertCodSecret = int(input("Insira o código ultra secreto da FEI: "))
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
        print("Código Validado")
        print()
        NovoNomeADM = str(input("Insira seu nome de usuário: ").strip())
        NovaSenhaADM = str(input("Insira uma senha para sua conta: ").strip())
        if ";" in NovoNomeADM:
            print("Erro: O nome de usuário não pode conter ponto e vírgula (;)")
            print()
            return CadastroADM()
        elif NovoNomeADM == "" or NovaSenhaADM == "":
            print("Digite um nome de usuário ou senha válido")
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
                print("Este nome de usuário já está em uso, tente outro")
                print()
                return CadastroADM()
            else:
                bdADM = open("admnistrador.txt", "a")
                bdADM.write(f"{NovoNomeADM};{NovaSenhaADM}\n")
                bdADM.close()
                print("Cadastro concluído, você pode logar agora mesmo.")
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
                print("O número digitado não possui uma função atrelada. Tente novamente")
                print()


def execCadastro():
    print()
    print("Deseja se cadastrar como um novo ADM ou Usuário?")
    print()
    print("1 - Novo Usuário")
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
        print("O número digitado não possui uma função atrelada. Tente novamente")
        print()
        execCadastro
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
apresentacao()
def AposLoginUsuario():
    print("O que deseja fazer?")
    print()
    print("1 - Buscar filme por nome")
    print("2 - Curtir filmes assistidos")
    print("3 - Favoritar filmes assistidos")
    print("4 - Acessar filmes curtidos e favoritos")
