import os

##Variavel receberá valor do arquivo .txt
emails_cadastrados = "emails_cadastrados.txt"

#1 - Coleta de Dados-------------------------------------------------------------------------------------------------------------------------------------
print("Preencha os campos sem acentos")
nome = input("Informe o nome do funcionario: \n").strip().lower()
sobrenome = input("Informe o sobrenome do funcionario: \n").strip().lower()
empresa = input("Informe a Empresa que o funcionario trabalha: \n").strip(" ").lower().replace(" ","")
#.strip e .lower garantem que a entrada estará sem espaços e com caracteres minusculos

#1.1 - Variaveis recebenbem o valor das entradas do usuário
nomeCompleto = f"{nome} {sobrenome}"
email_gerado = f"{nome}.{sobrenome}@{empresa}.com.br"

#Atribui valor de falso na variavel booleana
verificarRepetido = False

#2- Conferencia------------------------------------------------------------------------------------------------------------------------------------------
if os.path.exists(emails_cadastrados):                #Nessa linha precisei de ajuda pois tive de mexer na biblioteca SO, ainda não tenho dominio dela
    with open(emails_cadastrados , "r") as arquivo:   #'with' garante que o arquivo .txt será aberto e lido ("r") e levará o nome de 'arquivo'
        for linha in arquivo:                         #arquivo entra no  loop for para conferir
            if nomeCompleto in linha.lower():         #Se nossa entrada de usuario ja esta no arquivo .txt
                verificarRepetido = True              #caso sim o verificarRepetido fica com valor verdadeiro
                break                                 #Termina o sistema e acusa que a entrada já existe


if verificarRepetido:                                                            #Tentei colocar um ELIF no lugar do IF: Não retornou o print
    print(f"\n[AVISO] {nomeCompleto.title()} Já possui cadastro no sistema!")    #Com if o resposta veio como eu previa
else:
    with open(emails_cadastrados, "a") as arquivo:                               #No Else, como não está igual, ele salva normal
        arquivo.write(f"Nome: {nomeCompleto.title()} | Email: {email_gerado}")   #Abre o arquivo.txt e salva a nova entrada

    print("-" * 30)
    print(f"E-mail {email_gerado} salvo com sucesso!")
    print("-" * 30)

# 4. Leitura do arquivo para mostrar todos os e-mails atuais--------------------------------------------------------------------------------------------
print("\nLista de e-mails no sistema:")                         #Ao final o sistema me te retorna uma lista com os e-mail já cadastrados
if os.path.exists(emails_cadastrados):
    with open(emails_cadastrados, "r") as arquivo:
        print(arquivo.read())


