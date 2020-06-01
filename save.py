import os
import json


class Save:
    def save(self, gamer, clocks, directory='saves'):

        file_path = directory + '/' + gamer.name + '.json'
        with open(file_path, "w") as write_file:
            data = {'health': gamer.statistics['health'],
                    'fatigue': gamer.statistics['fatigue'],
                    'grades': gamer.statistics['grades'],
                    'money': gamer.statistics['money'],
                    'alcohol': gamer.statistics['alcohol'],
                    'name': gamer.name,
                    'days': clocks.days + 1
                    }
            json.dump(data, write_file, indent=2)

    def load(self, gamer, clocks, directory='saves'):

        file_path = directory + '/' + gamer.name + '.json'
        with open(file_path, "r") as read_file:
            data = json.load(read_file)
            gamer.name = data['name']
            clocks.days = data['days']
            for characteristics in gamer.statistics:
                gamer.statistics[characteristics] = data[characteristics]


    def dir_is_empty(self, directory='saves'):

        dir_name = directory;
        if not os.listdir(dir_name):
            return True
        else:
            return False
