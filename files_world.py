from user_class import User
from sing_in_class import SingIn
from session_class import Session
from user_info_generator_class import UserInfoGenerator
from find_user_bynick_class import FindUser

class FilesWorld():
    def __init__(self):
        self.users = {}
        self.groups = {}

    def session_init(self, ouser):
        osession = Session(self.users, self.groups, ouser)

        sair_da_rede = False
        while sair_da_rede == False:
                
            command = input("comando : ")
            if command == 'lista_de_comandos':
                osession.commands()
            elif command == 'editar_usuario':
                ouser.edit(self.users)
            elif command == 'acessar_perfil':
                a_user = osession.find_user()
                ouser.access_perfil(a_user)
            elif command == 'add_amigo':
                a_user = osession.find_user()
                ouser.add_amigo(a_user)
            elif command == 'subir_arquivo':
                PerfilFilesManager().uploading(self.user.nickname)
                
            elif command == 'criar_grupo':
                GrupoCreator().creation(self.groups, self.user)

            elif command == 'entrar_grupo':
                name = input("\nNome do grupo em que se deseja entrar: ")
                group = GroupFinder().find(self.groups, name)
                if group == None:
                    print("Esse grupo não existe")
                else:
                    if group not in self.user.groups:
                        print("Você não eh membro do grupo.")
                    else:
                        GroupSession(self.users, group, self.user).session()

            elif command == 'sair':
                sair_da_rede = True
                print("Desconectando...\n")
            
            elif command == 'show':
                print(self.user)

    def singning_in(self):
        osing_in = SingIn(self.users)
        
        ouser = osing_in.signing_in()
        if ouser:
            self.session_init(ouser)

    def majority_verification(self):
        print("Você tem mais de 18 anos? Digite sua respota no seguinte formato:\n")
        print("'sim' - caso tenha idade maior ou igual a 18 anos.")
        print("'nao' - caso seja menor de idade.\n")
        return input("Resposta: ")

    def singning_up(self):
        """Cria um novo usuário"""
        majority = self.majority_verification()
        
        if majority == 'nao':
            print("Você não tem idade suficiente para ser um usuário dessa rede.\n\n")
        elif majority == 'sim':
            ouser_info_generator = UserInfoGenerator(self.users)
            
            login, nickname, password = ouser_info_generator.generate_info()
            
            ouser = User(login, nickname, password)
            self.users[login] = ouser

    def show(self):
        print("***Users Info***")
        for ouser in self.users.values():
            print(f"    login: {ouser.login}\n    nickname: {ouser.nickname}\n    password: {ouser.password}\n") 

    def exit(self):
        exit()

    


    