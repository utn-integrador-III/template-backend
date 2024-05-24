from db.user_db_connection import UserDBConnection
from decouple import config
from utils.commons import Commons

connection = UserDBConnection(config("USERS_COLLECTION"))


class User:
    id =" ",
    userName = " ",
    userPassword=" ",

    def __init__(
            self,
            id,
            userName,
            userPassword,
    ):
        self.id = id,
        self.userName = userName,
        self.userPassword = userPassword


    @classmethod
    def get_by_id(self, id):  
        return connection.get_by_id(id)
    
    @classmethod
    def get_all(self):
        return connection.get_all_data()

    def create_user(self):
        new_user = { }
        return connection.create_data(new_user)

    def update(self, id):
        return connection.update_data(id, { })

    @classmethod
    def delete(self, id):
        return connection.delete_user(id)

        

