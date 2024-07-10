from django.db import models


# Create your models here.
class Move(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    accuracy = models.IntegerField()
    pp = models.IntegerField()
    power = models.IntegerField()
    damage_class = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Pokemon(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    level = models.IntegerField()
    types = models.JSONField()
    moves = models.ManyToManyField(Move)
    attack = models.IntegerField()
    defense = models.IntegerField()
    special_attack = models.IntegerField()
    special_defense = models.IntegerField()
    speed = models.IntegerField()
    nature = models.CharField(max_length=100)

    def __str__(self):
        move_strings = [str(move) for move in self.moves]
    
        return (f"{self.name}" + " " + f"LVL: {self.level}" + " " + f"ID: {self.id}\n" + f"Moves:{move_strings}" + 
                f" Nature:{self.nature}\nhp:{self.hp}\nattack:{self.attack}\ndefense:{self.defense}\nspecial-attack:{self.special_attack}\n"
                + f"special-defense:{self.special_defense}\nspeed:{self.speed}\n")


