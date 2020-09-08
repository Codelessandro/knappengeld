import numpy as np

class Match():

    def get_random_10_values():
        return np.random.uniform(0,4,10);

    def __init__(self):

    def x(self):
        _ = [
            'Bayern München',
            'Borussia Dortmund',
            'Markus Merk',
             get_random_10_values()
        ]

        return _


    def y(self):


class DataLoader():
    def __init__(self, nr_games):
        games = map(lambda game: Match(game), np.arange(nr_games));


dl = DataLoader(20)

