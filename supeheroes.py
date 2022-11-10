import requests

url = 'https://akabab.github.io/superhero-api/api/all.json'
resp = requests.get(url)
data = resp.json()

class Hero:
    def __init__(self, name):
        self.name = name
        self.id = 0
        self.intelligence = 0

    def search_id_intelligence(self):
        for hero in data:
            if hero['name'] == self.name:
                self.id = hero['id']
                self.intelligence = hero['powerstats']['intelligence']

    def most_intelligence(self, other_1, other_2):
        if self.intelligence > other_1.intelligence:
            if self.intelligence > other_2.intelligence:
                print(f'{self.name} - самый умный супергеров')
            else:
                print(f'{other_2.name} - самый умный супергеров')
        elif self.intelligence > other_2.intelligence:
            if self.intelligence > other_1.intelligence:
                print(f'{self.name} - самый умный супергеров')
            else:
                print(f'{other_1.name} - самый умный супергеров')
        else:
            if other_1.intelligence > other_2.intelligence:
                print(f'{other_1.name} - самый умный супергеров')
            else:
                print(f'{other_2.name} - самый умный супергеров')

Hulk = Hero('Hulk')
Hulk.search_id_intelligence()

Captain_America = Hero('Captain America')
Captain_America.search_id_intelligence()

Thanos = Hero('Thanos')
Thanos.search_id_intelligence()

Hulk.most_intelligence(Thanos, Captain_America)
