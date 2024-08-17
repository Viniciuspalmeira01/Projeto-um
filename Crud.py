from nwe import perfil , Anuncio , db
import random, time

db.connect()
db.create_tables([perfil, Anuncio])

def criar_perfil():#cria perfis aleatórios no banco
    senha = random.randint(1,1000)
    pr = random.randint(0,1000)#deferencia A de B
    npc = {'pessoa':f'pessoa{pr}', 'Email':f'pessoa{pr}@gmail', 'senha':senha }#dicionário indicando
    usuario = perfil.create(nome = npc[f'pessoa'],email =npc['Email'],senha = npc['senha'] )
    return usuario.save()

def gerador_de_perfis(n =int):#apartir de um valor inteiro, você cria um determinado número de perfis
    for x in range(0,n):
        try:
            criar_perfil()
        except :#caso já exista aquele Id, ele retorna um erro 
            print('Usuário já existente!!')

def exibir_perfis():
    lista_usuarios = perfil.select()
    for x in lista_usuarios:
        print('-', x.id , x.nome)
def delete(nome_antigo):
    usuário = perfil.get(perfil.nome == nome_antigo)
    return usuário.delete()
    
def new_update():
    N = int(input('Digite o Id que deseja saber :\n'))
    pessoo_escolhida = perfil.get(perfil.id == N)
    print('A pessoa escolhida foi :' , pessoo_escolhida.nome)
    novo_nome = input('Novo nome:\n')
    pessoo_escolhida.nome = novo_nome

    return pessoo_escolhida.save()

def run():
    n = input('Digite a função requerida : \n')
    if n =='gerar perfis':
        x = int(input('quantos perfis? :\n'))
        gerador_de_perfis(x)
        time.sleep(5)
        exibir_perfis()
    elif n == 'trocar nomes':
        new_update()
    elif n == 'deletar usuário':
       nome = input('Digite o nome do usuário')
       delete(nome_antigo= nome)
       time.sleep(4)
       exibir_perfis()
    else:
        print('Não entendi')
run()