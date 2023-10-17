import json


class Importer:

    def __init__(self):
        pass

    def read_tasks(self):
        file = open('taski.json', 'r', encoding='utf-8')
        self.data = json.load(file)
        file.close()
        pass

    def get_tasks(self):
        return self.data