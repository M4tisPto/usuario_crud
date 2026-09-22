from mysqlconnection import MySQLConnection

class Usuario:
    def __init__(self, datos):
        self.id = datos['id']
        self.nombre = datos['nombre']
        self.apellido = datos['apellido']
        self.created_at = datos['created_at']
        self.updated_at = datos['updated_at']
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios"
        results = MySQLConnection("usuarios").query_db(query)
        users = []
        for users in results:
            users.append(cls(users))
        return users
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO usuarios (nombre, apellido, created_at, updated_at) VALUES (%(nombre)s, %(apellido), NOW(), NOW());"
        result = MySQLConnection('usuarios').query_db(query, data)
        return result
    @classmethod
    def update_data(cls, data):
        query = "UPDATE usuarios SET (nombre, apellido, updated_at) = (%(nombre)s, %(apellido)s, NOW()) WHERE id = %(id)s;"
        return MySQLConnection('usuarios').query_db(query, data)
