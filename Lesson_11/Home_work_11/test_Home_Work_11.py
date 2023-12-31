import time
import pytest


# =======================================================================================================================

# 2) Напишіть 5 тестів з затримкою в 2 секунди кожен, один з тестів повинен мати унікальне імя.
#  Запустіть їх за домогою pytest-xdist ліби в 5 потоків.
#  Запустіть цей ваш унікальний тест з маркером -k
#  додайте скірншоти виконання(не забудьте додавати -v, що б я бачив що ви проганяли)
#  і біля скріншотів пропишіть команди
#  які ви використовували.


@pytest.mark.sleep
def test_sleep_1():
    time.sleep(2)

    assert True


@pytest.mark.sleep
def test_sleep_2():
    time.sleep(2)
    assert True


@pytest.mark.sleep
def test_sleep_3():
    time.sleep(2)
    assert True


@pytest.mark.sleep
def test_sleep_4():
    time.sleep(2)
    assert True


@pytest.mark.unique
def test_sleep_unique():
    time.sleep(2)
    assert True

# pytest -m "sleep or unique" -v


# =======================================================================================================================

# 3) обновіть requirements.txt
# ВСІ ЗАВДАННЯ ПОВИННІ БУТИ ПЕРЕВІРЕННІ flake8 за кожну помилку яку він знайде
# (окрім E501(там де кількість стрічок в ряд))
# буду знімати по 10 балів.
