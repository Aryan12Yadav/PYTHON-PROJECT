from  P1 import Hero,Enemy
from wP3 import short_bow,iron_sword

hero = Hero(name = "Hero",health = 100 )
hero.equip(iron_sword)
enemy = Enemy(name = "Enemy",health = 100 , weapon 
              = short_bow )

while True:
    hero.attack(enemy) # here hero damage the enemy 

    enemy.attack(hero) # vice versa

    print(f"health of {hero.name} : { hero.health}")
    print(f"health of {enemy.name} : {enemy.health}")
    

    input()


    


