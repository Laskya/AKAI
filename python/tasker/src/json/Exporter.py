import json


class Exporter:

    def __init__(self):
        pass

    def save_tasks(self, tasks):
        file = open('taski.json', 'w', encoding='utf-8')
        json.dump(tasks, file, indent=2, ensure_ascii=False)
        file.close()
        pass
