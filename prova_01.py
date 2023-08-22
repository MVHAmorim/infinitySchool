# Sistema de cadastro
#------------------------------------------------------------ 

while True:
    
    senha = input ('Digite sua senha: ')                             
    confSenha = input ('Redigite sua senha: ')
    
    if senha == confSenha:
        print ('Senha cadastrada com sucesso!\n-------------------------------------------\n')
        break
    
    elif senha != confSenha:
        print ('Senhas não coincidem! \nReinicie o processo de cadastro.\n-------------------------------------------\n')


# Sistema de Login
#------------------------------------------------------------ 

print("Sistema de Login:\n-------------------------------------------\n")

while True:
    confSenha = input("Digite a senha cadastrada: ")
    if senha == confSenha:
        print("Login efetuado com sucesso!")
        break
    
    else:
        print(f"Senha incorreta!.\n")