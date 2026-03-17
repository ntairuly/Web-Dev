class Character:
    def __init__(self, name, book, age, gender):
        self.name = name
        self.book = book
        self.age = age
        self.gender = gender

    def __str__(self):
        return f" Name: {self.name}\n Age: {self.age}\n Gender: {self.gender}\n Book: {self.book}"


class Protagonist(Character):
    def __init__(self, name, book, age, gender, goal, love_interest=None):
        super().__init__(name, book, age, gender)
        self.love_interest = love_interest
        self.goal = goal
        self.friends = []
        self.enemy = None

    def __str__(self):
        return super().__str__() + f"\n Love Interest: {self.love_interest}\n Goal: {self.goal}"
    
    def add_main_enemy(self, antagonist):
        if isinstance(antagonist, Antagonist):
            self.enemy = antagonist

    def main_enemy(self):
        return f"{self.enemy.name} is the main enemy of {self.name}"
    
    def add_friend(self, friend):
        if isinstance(friend, Character):
            self.friends.append(friend)

    def get_friends(self):
        return self.friends


class Antagonist(Character):
    def __init__(self, name, book, age, gender, motivation):
        super().__init__(name, book, age, gender)
        self.motivation = motivation
        self.loved_phrase = None
        self.enemy = None
    
    def __str__(self):
        return super().__str__() + f"\n Motivation: {self.motivation}.\n Loved Phrase: {self.loved_phrase}"
    
    def add_main_enemy(self, protagonist):
        if isinstance(protagonist, Protagonist):
            self.enemy = protagonist

    def main_enemy(self):
        return f"{self.enemy.name} is the main enemy of {self.name}"
    
    def add_loved_phrase(self, phrase):
        self.loved_phrase = phrase

    def get_loved_phrase(self):
        return self.loved_phrase


class SideCharacter(Character):
    def __init__(self, name, book, age, gender, role):
        super().__init__(name, book, age, gender)
        self.role = role

    def __str__(self):
        return super().__str__() + f"\n Role: {self.role}"
    
    def describe_role(self):
        return f"{self.name} plays the role of {self.role} in the {self.book}"