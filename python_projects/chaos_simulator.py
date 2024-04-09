import random

class Gym:
    def __init__(self):
        self.dumbbells = [i for i in range(10, 37) if i % 2 == 0]
        self.dumbbell_shelf = {}
        self.reset_day()
        
    def reset_day(self):
        self.dumbbell_shelf = {i: i for i in self.dumbbells}
    
    def list_dumbbells(self):
        return [i for i in self.dumbbell_shelf.values() if i != 0]
    
    def list_spaces(self):
        return [i for i, j in self.dumbbell_shelf.items() if j == 0]
    
    def take_dumbbell(self, weight):
        dumbbell_position = list(self.dumbbell_shelf.values()).index(weight)
        dumbbell_key = list(self.dumbbell_shelf.keys())[dumbbell_position]
        self.dumbbell_shelf[dumbbell_key] = 0
        return weight

    def dumbbell_return(self, pos, weight):
        self.dumbbell_shelf[pos] = weight

    def chaos_calculation(self):
        num_chaos = [i for i, j, in self.dumbbell_shelf.items() if i != j]
        return len(num_chaos) / len(self.dumbbell_shelf)

class User:
    def __init__(self, type, gym):
        self.type = type
        self.gym = gym
        self.weight = 0

    def start_training(self):
        list_weight = self.gym.list_dumbbells()
        self.weight = random.choice(list_weight)
        self.gym.take_dumbbell(self.weight)

    def end_training(self):
        spaces = self.gym.list_spaces()

        if self.type == 1:
            if self.weight in spaces:
                self.gym.dumbbell_return(self.weight, self.weight)
            else:
                pos = random.choice(spaces)
                self.gym.dumbbell_return(pos, self.weight)

        if self.type == 2:
            pos = random.choice(spaces)
            self.gym.dumbbell_return(pos, self.weight)
        self.weight = 0

gym = Gym()

users = [User(1, gym) for i in range(10)]
users += [User(2, gym) for i in range(1)]
random.shuffle(users)

list_chaos = []

for k in range(50):
    gym.reset_day()
    for i in range(10):
        random.shuffle(users)
        for user in users:
            user.start_training()
        for user in users:
            user.end_training()
    list_chaos += [gym.chaos_calculation()]

import seaborn as sns
sns.displot(list_chaos)
list_chaos


gym.dumbbell_shelf
gym.chaos_calculation()