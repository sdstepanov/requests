import requests

hero_name_list = ['Hulk', 'Captain America', 'Thanos']


class Super_hero:

    def __init__(self, hero_name):
        self.hero_name = hero_name
        self.super_hero_list = []

    def get_intelligence_hero(self):
        id_hero_list = self.get_id_super_hero()
        for id_hero in id_hero_list:
            power_stats = requests.get(f'https://superheroapi.com/api/2619421814940190/{id_hero}/powerstats').json()
            name_superhero = str(power_stats['name'])
            intelligence_superhero = int(power_stats['intelligence'])
            self.super_hero_list += [(name_superhero, intelligence_superhero)]
        answer = self.get_max_intelligence()
        return f'Самый умный - {answer}'

    def get_id_super_hero(self):
        id_hero_list = []
        for name in self.hero_name:
            super_hero = requests.get(f'https://superheroapi.com/api/2619421814940190/search/{name}').json()
            id_hero_list += [super_hero['results'][0]['id']]
        return id_hero_list

    def get_max_intelligence(self):
        self.super_hero_list.sort(key=lambda intelligence: intelligence[1])
        max_intelligence = self.super_hero_list[-1]
        ans = max_intelligence[0]
        return ans


if __name__ == '__main__':
    hero = Super_hero(hero_name_list)
    print(hero.get_intelligence_hero())
