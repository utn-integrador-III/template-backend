import os
import re
from pymongo import MongoClient
from pymongo.collation import Collation


class Connection:
    def __init__(self, collection_name):
        self.collection = None
        self.connect(collection_name)

    def connect(self, collection_name):
        uri = os.getenv('MONGO_URL')
        self.collection = MongoClient(uri)[os.environ["MONGO_DB"]][collection_name]


    def get_all_data(self, values_dict=dict(), lookups=list()):
        lookups_queries = self.lookup_unwind_formating(lookups)
        return self.collection.aggregate([
            *lookups_queries,
            {
                '$match': values_dict
            },
        ])

    def get_data(self, values_dict=dict(), lookups=list()):
        lookups_queries = self.lookup_unwind_formating(lookups)
        data = self.collection.aggregate([
            *lookups_queries,
            {
                '$match': values_dict,
            },
            {
                '$limit': 1,
            }
        ])
        data = list(data)
        if not len(data):
            return None
        return data[0]

    def insert_data(self, values_dict):
        return self.collection.insert_one(values_dict)

    def update_data(self, values_dict, update_dict):
        return self.collection.update_one(values_dict, {'$set': update_dict})

        """ search_exceptions -> {'key': {'values': [], 'replace': []}}"""

    def get_all_data_lazy(self, values_dict=dict(), lookups=list(), search_keys=list(), search_value="", page_size=0, page_num=0, order_by="", sort=0, only_count=False, search_exceptions=dict()):
        lookups_queries = self.lookup_unwind_formating(lookups)
        search_value_escaped = re.escape(search_value)
        pagination = list()
        if page_num and page_size:
            skips = page_size * (page_num - 1)
            pagination = [
                {'$skip': skips},
                {'$limit': page_size},
            ]
        sorting = list()
        if order_by and sort:
            sorting = [{"$sort": {order_by: sort}}]

        expr_statements = []
        or_list = dict()
        if search_value:
            for key in search_keys:
                search_value_escaped_aux = self.map_execeptions(
                    search_exceptions, search_value_escaped, key)
                expr_statements.append({"$expr": {"$regexMatch": {"input": {
                                       "$toString": f"${key}"}, "regex": search_value_escaped_aux, "options": "i"}}})
            or_list = {'$or': expr_statements}
        count = list()
        if only_count:
            count = [{'$count': "total_records"}]
        query = [
            *lookups_queries,
            {
                '$match': {
                    **values_dict,
                    **or_list
                },
            },
            *sorting,
            *pagination,
            *count
        ]
        return self.collection.aggregate(query, collation=Collation(locale="en", strength=1))

    def lookup_unwind_formating(self, lookups):
        lookups_unwinds_list = []
        for lookup in lookups:
            unwind = {
                '$unwind': {
                    'path': f"${lookup['as']}",
                    'preserveNullAndEmptyArrays': True
                },
            }
            lookup_aux = {'$lookup': lookup}
            lookups_unwinds_list.append(lookup_aux)
            lookups_unwinds_list.append(unwind)
        return lookups_unwinds_list

    def map_execeptions(self, exceptions=dict(), search_value="", key=""):
        search_value_aux = search_value.lower()
        if exceptions.get(key):
            if search_value_aux in exceptions[key]['values']:
                index = exceptions[key]['values'].index(search_value_aux)
                search_value_aux = str(exceptions[key]['replace'][index])
        return search_value_aux
