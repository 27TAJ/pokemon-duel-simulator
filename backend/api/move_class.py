from .data import get_data 

class Move: 
    def __init__(self, id):
        move_data = get_data("move", id)

        self.id = move_data['id']
        self.name = move_data['name']
        self.type = move_data['type']['name']
        self.accuracy = move_data['accuracy']
        self.pp = move_data['pp']
        self.power = move_data['power']
        self.damage_class = move_data['damage_class']['name'] # "status", "physical", "or special"
        
        #stat_change
        #effect_chance
        
    def __str__(self):
       return f"{self.name}"