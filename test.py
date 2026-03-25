# Импортируем pytest для использования тестов
import pytest
# Импортируем тестируемую функцию из main.py
from main import count_vowels

# Тест 1: строка, содержащая только гласные (в разных регистрах)
def test_only_vowels():
    assert count_vowels("aeiou") == 5          # только строчные
    assert count_vowels("AEIOU") == 5          # только прописные
    assert count_vowels("AaEeIiOoUu") == 10    # смешанный регистр

# Тест 2: строка, не содержащая гласных
def test_no_vowels():
    assert count_vowels("bcdfg") == 0          # только согласные
    assert count_vowels("123!@#") == 0         # цифры и символы
    assert count_vowels("") == 0               # пустая строка

# Тест 3: смешанные строки (гласные и согласные)
def test_mixed():
    assert count_vowels("Hello, World!") == 3  # e, o, o
    assert count_vowels("Python") == 1         # o
    assert count_vowels("PyTest") == 1         # e

# Параметризованный тест: один тест запускается с разными наборами данных
@pytest.mark.parametrize("s, expected", [
    ("apple", 2),          # a, e
    ("BANANA", 3),         # A, A, A
    ("rhythm", 0),         # нет гласных
    ("U", 1),              # одна гласная
    ("   ", 0),            # пробелы
    ("a1b2c3", 1),         # одна гласная среди цифр
])
def test_parametrized(s, expected):
    # Вызываем функцию и сравниваем результат с ожидаемым
    assert count_vowels(s) == expected