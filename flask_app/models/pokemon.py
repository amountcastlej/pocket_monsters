from flask_app.config.mysqlconnection import connectToMySQL 

db = "pokemon_db"
class Pokemon:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.type = data['type']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def all_pokemon(cls):
        query = "SELECT * FROM pokemon;"
        results = connectToMySQL(db).query_db(query)
        pokemons = []
        for pokemon in results:
            pokemons.append(cls(pokemon))
        return pokemons

    @classmethod
    def create_pokemon(cls, form_data):
        query = """
        INSERT INTO pokemon (name, type, email) 
        VALUES (%(name)s, %(type)s, %(email)s);
        """
        return connectToMySQL(db).query_db(query, form_data)

    @classmethod
    def update(cls, data, id):
        query = f"UPDATE pokemon SET name = %(name)s, type= %(type)s, email= %(email)s WHERE id = {id};"
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def one_pokemon(cls, data):
        query="SELECT * FROM pokemon WHERE id = %(id)s;"
        results = connectToMySQL(db).query_db(query, data)
        return cls(results[0])

    @classmethod
    def destroy_pokemon(cls, data):
        query = "DELETE FROM pokemon WHERE id = %(id)s"
        return connectToMySQL(db).query_db(query, data)


