from mysqlconnection import MySQLConnection

class Usuario:
    def __init__(self, datos):
        self.id = datos['id']
        self.nombre = datos['nombre']
        self.apellido = datos['apellido']
        self.email = datos['email']
        self.created_at = datos['created_at']
        self.updated_at = datos['updated_at']
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios"
        results = MySQLConnection("usuario").query_db(query)
        users = []
        for u in results:
            users.append(cls(u))
        
        return users
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO usuarios (nombre, apellido, email, created_at, updated_at) VALUES (%(nombre)s, %(apellido)s, %(email)s, NOW(), NOW());"
        result = MySQLConnection('usuario').query_db(query, data)
        return result
    @classmethod
    def update_data(cls, data):
        query = "UPDATE usuarios SET nombre = %(nombre)s, apellido = %(apellido)s,email = %(email)s, updated_at = NOW() WHERE id = %(id)s;"
        return MySQLConnection('usuario').query_db(query, data)
    @classmethod
    def delete_user(cls, data):
        query = "DELETE FROM usuarios WHERE id = %(id)s;"
        return MySQLConnection('usuario').query_db(query, data)
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM usuarios WHERE id = %(id)s"
        return MySQLConnection('usuario').query_db(query, data)