
def attack(enemy, hero):
    damage = (hero.strength * hero.luck) - enemy.armor
    return int(enemy.health - damage)


def choice(option, hero, enemy=None):
    if not option and not isinstance(option, int):
        raise Exception('You must select an option!')

    if 0 <= option < len(hero.choices):
        if enemy and hero.choices[option] == 'Attack':
            return attack(enemy, hero)

        elif hero.choices[option] != 'Attack':
            return f"Your choice was {hero.choices[option]}."

    raise Exception('Invalid parameters')



