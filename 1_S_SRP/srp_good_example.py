'''
SINGLE RESPONSABILITY PRINCIPLE

Note que nessa classe, temos várias ações e responsabilidades. O que torna a manutenção, usabilidade e até a performance ruins.

Seguindo o conceito do Princípio da Responsabilidade única, organize essa classe e, se necessário, crie outras 
classes com suas devidas responsabilidades.

'''
class ConnectionApi:
    def conect_api(self):
        pass

class Notification:
    def send_notification(self):
        pass

class GenerationReport:

    def generate_report(self):
        pass

    def send_report(self):
        pass
    
class Tasks:

    def create_task(self):
        pass

    def update_task(self):
        pass

    def remove_task(self):
        pass

    