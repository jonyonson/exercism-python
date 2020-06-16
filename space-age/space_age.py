class SpaceAge:

    def __init__(self, seconds):
        self.seconds = seconds
        self.seconds_in_year = 31557600
        self.orbits_per_earth_year = {
            'earth': 1,
            'mercury': 0.2408467,
            'venus': 0.61519726,
            'mars': 1.8808158,
            'jupiter': 11.862615,
            'saturn': 29.447498,
            'uranus': 84.016846,
            'neptune': 164.79132,
        }

    def __format_age(self, planet):
        years = self.seconds / (self.seconds_in_year *
                                self.orbits_per_earth_year[planet])
        formatted_year = f'{years:.2f}'
        return float(formatted_year)

    def on_earth(self):
        return self.__format_age('earth')

    def on_mercury(self):
        return self.__format_age('mercury')

    def on_venus(self):
        return self.__format_age('venus')

    def on_mars(self):
        return self.__format_age('mars')

    def on_jupiter(self):
        return self.__format_age('jupiter')

    def on_saturn(self):
        return self.__format_age('saturn')

    def on_uranus(self):
        return self.__format_age('uranus')

    def on_neptune(self):
        return self.__format_age('neptune')
