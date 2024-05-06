class Hero:
    def __init__(self, name, hp, mp):
        self.name = name
        self.max_hp = 100
        self.max_mp = 200
        self.hp = min ( hp, self.max_hp )
        self.mp = min ( mp, self.max_mp )

    def cast_spell(self, spell_name, mp_needed):
        if self.mp >= mp_needed:
            self.mp -= mp_needed
            print ( f"{self.name} has successfully cast {spell_name} and now has {self.mp} MP!" )
        else:
            print ( f"{self.name} does not have enough MP to cast {spell_name}!" )

    def take_damage(self, damage, attacker):
        self.hp -= damage
        if self.hp > 0:
            print ( f"{self.name} was hit for {damage} HP by {attacker} and now has {self.hp} HP left!" )
        else:
            print ( f"{self.name} has been killed by {attacker}!" )

    def recharge(self, amount):
        if (self.mp + amount) > self.max_mp:
            print ( f"{self.name} recharged for {200-self.mp} MP!" )
        else:
            print ( f"{self.name} recharged for {amount} MP!" )
        self.mp = min ( self.max_mp, self.mp + amount )

    def heal(self, amount):
        if (self.hp + amount) > self.max_hp:
            print(f"{self.name} healed for {100-self.hp} HP!")
        else:
            print ( f"{self.name} healed for {amount} HP!" )
        self.hp = min ( self.max_hp, self.hp + amount )



# Read number of heroes
num_heroes = int ( input () )

# Initialize party list
party = []

# Create hero objects and add them to the party
for _ in range ( num_heroes ):
    name, hp, mp = input ().split ()
    hero = Hero ( name, int ( hp ), int ( mp ) )
    party.append ( hero )

# Process commands
while True:
    command = input ()
    if command == "End":
        break

    action, *args = command.split ( " - " )
    if action == "CastSpell":
        hero_name, mp_needed, spell_name = args
        hero = next ( h for h in party if h.name == hero_name )
        hero.cast_spell ( spell_name, int ( mp_needed ) )
    elif action == "TakeDamage":
        hero_name, damage, attacker = args
        hero = next ( h for h in party if h.name == hero_name )
        hero.take_damage ( int ( damage ), attacker )
        if hero.hp <= 0:
            party.remove ( hero )
    elif action == "Recharge":
        hero_name, amount = args
        hero = next ( h for h in party if h.name == hero_name )
        hero.recharge ( int ( amount ) )
    elif action == "Heal":
        hero_name, amount = args
        hero = next ( h for h in party if h.name == hero_name )
        hero.heal ( int ( amount ) )

# Print remaining party members
for hero in party:
    print ( f"{hero.name}\n  HP: {hero.hp}\n  MP: {hero.mp}" )
