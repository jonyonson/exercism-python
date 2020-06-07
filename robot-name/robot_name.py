import random
import string


class Robot:

    used_names = set()

    def __init__(self):
        self.reset()

    def assign_random_name(self):
        while True:
            random_name = self.generate_random_name()
            if random_name not in self.used_names:
                return random_name

    def generate_random_name(self):
        return random.choice(string.ascii_uppercase) + \
            random.choice(string.ascii_uppercase) + \
            str(random.randrange(0, 10)) + \
            str(random.randrange(0, 10)) + str(random.randrange(0, 10))

    def reset(self):
        self.name = self.assign_random_name()
        self.used_names.add(self.name)
