class SpaceAge:

    def __init__(self, seconds):
        self.seconds = seconds
        self.seconds_in_year = 31557600

    def __format_years(self, blah):
        years = self.seconds / (self.seconds_in_year * blah)
        formatted_year = f'{years:.2f}'
        return float(formatted_year)

    def on_earth(self):
        return self.__format_years(1)

    def on_mercury(self):
        return self.__format_years(0.2408467)

    def on_venus(self):
        return self.__format_years(0.61519726)

    def on_mars(self):
        return self.__format_years(1.8808158)

    def on_jupiter(self):
        return self.__format_years(11.862615)

    def on_saturn(self):
        return self.__format_years(29.447498)

    def on_uranus(self):
        return self.__format_years(84.016846)

    def on_neptune(self):
        return self.__format_years(164.79132)
