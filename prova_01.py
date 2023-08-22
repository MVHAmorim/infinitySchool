# Sistema de cadastro
#------------------------------------------------------------ 

email = input ('Digite seu e-mail: ')                             
senha = input ('Redigite sua senha: ')

print ('Cadastro efetuado com sucesso.\n-------------------------------------------\n')


# Sistema de Login
#------------------------------------------------------------ 

print("Sistema de Login:\n-------------------------------------------\n")

while True:
    logEmail = input("Digite o seu email: ")
    logSenha = input("Digite sua senha: ")
    
    if senha == logSenha and email == logEmail:
        print("\nLogin efetuado com sucesso!")
        break
    
    else:
        if senha != logSenha and email != logEmail:
            print(f"\nEmail e senha incorretos!.\n")
            
        elif senha != logSenha and email == logEmail:
            print(f"\nSenha incorreta!.\n")

        elif senha == logSenha and email != logEmail:
            print(f"\nEmail incorreto!.\n")