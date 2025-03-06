from weaponClass import Weapon

fist = Weapon(
    name = 'Fist',
    type = '',
    rank = 0,
    range = 1,
    dice = (1,4),
    stat = "Stykr",
    attacks = 3,
    hands = 1
)

shield = Weapon(
    name = 'Shield',
    type = '',
    rank = 0,
    range = 1,
    dice = (1,6),
    stat = "Styrkr",
    attacks = 1,
    hands = 1
)

bronzeAxe = Weapon(
    name = '',
    type = 'axe',
    rank = 0,
    range = 1,
    dice = (2,4),
    stat = "Styrkr",
    attacks = 2
)

bronzeSword = Weapon(
    name = '',
    type = 'sword',
    rank = 0,
    range = 1,
    dice = (1,8),
    stat = "Styrkr",
    attacks = 2,
    hands = 1
)

bronzeSpear = Weapon(
    name = '',
    type = 'spear',
    rank = 0,
    range = 2,
    dice = (1,6),
    stat = "Fimr",
    attacks = 2,
    hands = 2
)

bronzeGreatAxe = Weapon(
    name = '',
    type = 'greataxe',
    rank = 0,
    range = 2,
    dice = (2,10),
    stat = "Styrkr",
    attacks = 2,
    hands = 2
)
