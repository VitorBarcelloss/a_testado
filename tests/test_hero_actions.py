import pytest
from app.actions import attack, choice


def test_damage_calc_is_correct(hero, enemy):
    response = attack(enemy, hero)
    assert response == -20


def test_attack_is_retuning_integer_type(hero, enemy):
    response = attack(enemy, hero)
    assert type(response) is int


def test_choice_without_option(hero):
    with pytest.raises(Exception) as exception_info:
        choice(None, hero)
    assert str(exception_info.value) == 'You must select an option!'


def test_choice_sending_attack_value(hero, enemy):
    option = 0
    response = choice(option, hero, enemy)
    assert response == -20


def test_choice_with_attack_value_but_without_hero_and_enemy(hero):
    option = 0
    with pytest.raises(Exception) as exception_info:
        choice(option, hero)
    assert str(exception_info.value) == 'Invalid parameters'


def test_choice_different_than_attack(hero):
    option = 1
    response = choice(option, hero)
    assert response == 'Your choice was Defense.'


def test_choice_with_option_out_of_list_of_choices(hero):
    option = 4
    with pytest.raises(Exception) as exception_info:
        choice(option, hero)
    assert str(exception_info.value) == 'Invalid parameters'
