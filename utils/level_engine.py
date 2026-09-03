TEST_QUESTIONS = {
    'q1': {
        'question': 'Что выводит print(2 + 3 * 4)?',
        'options': ['14', '20', '10', '24'],
        'correct': 14
    },
    'q2': {
        'question': 'Какой тип имеет [1, 2, 3]?',
        'options': ['list', 'tuple', 'dict', 'set'],
        'correct': 'list'
    },
    'q3': {
        'question': 'Что такое переменная в Python?',
        'options': ['Ячейка памяти', 'Функция', 'Класс', 'Модуль'],
        'correct': 'Ячейка памяти'
    },
    'q4': {
        'question': 'Какой оператор используется для сравнения?',
        'options': ['=', '==', '===', ':'],
        'correct': '=='
    },
    'q5': {
        'question': 'Что такое функция def?',
        'options': ['Определение функции', 'Вызов функции', 'Импорт модуля', 'Создание класса'],
        'correct': 'Определение функции'
    }
}


def determine_level(score):
    if score >= 5:
        return 2
    elif score >= 3:
        return 1
    return 0
