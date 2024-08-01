import pytest

from app.classes import Hero, Enemy


@pytest.fixture
def hero():
    yield Hero(
        10,
        5,
        ['Attack', 'Defense', 'Attributes']
    )


@pytest.fixture
def enemy():
    yield Enemy(5, 25)