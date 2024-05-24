from db.mongo_client import Connection


class UserDBConnection:

    def __init__(self, collection):
        self.connection = Connection(collection)

    def create_data(self, data):
        return ""

    def update_data(self, id, user_updated_data):
        return ""

    def get_all_data(self):
        return []
    
    def get_by_id(self, id):
        return {}

    def delete_user(self,id):
        return ""