def divide(first, second):
    try:
        div = first / second
        return div
    except ZeroDivisionError:
        return "Ошибка"
