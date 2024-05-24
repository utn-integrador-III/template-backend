from datetime import date


class Commons:
    @staticmethod
    def convertIds(list_result):
        try:
            for item in list_result:
                item['_id'] = str(item['_id'])
            return list_result
        except TypeError:
            return None

    @staticmethod
    def get_time():
        from datetime import datetime
        try:
            dt_string = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
            return dt_string
        except:
            return 0