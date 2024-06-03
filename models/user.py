class UserModel(object):
    def __init__(self, user: dict):
        self.nome = user.get('nome')
        self.email = user.get('email')
        self.telefone = user.get('telefone')
        self.idade = user.get('idade')
    
    def to_dict(self):
        return {
            'nome': self.nome,
            'email': self.email,
            'telefone': self.telefone,
            'idade': self.idade,
        }