import json


def list_operations(path_to_file):
    """

    Загружаем список операций из файла operations.json.

    :return: список операций.

    """

    with open(path_to_file, 'rt', encoding='utf-8') as file:
        return json.load(file)


def order_operation(operation):
    """

    :param: operation - список словарей с информацией об банковских операциях.

    :return: список успешных операций, отсортированный по дате и времени.

    """

    date_list = []

    for dictionary in operation:

        if dictionary.get('state') == 'EXECUTED':
            date_list.append(dictionary)

    return sorted(date_list, key=lambda x: x['date'])


def encrypted_account(bank_account):
    """

    Функция для маскировки счета и номера карты.

    :param bank_account: банковский счет или номер карты.

    :return: замаскированный счет или номер карты.

    """

    count = 0

    for check in bank_account:

        if check.isdigit():
            count += 1

    if count == 16:

        number = bank_account[-16:]

        return f'{bank_account[:-16]}{number[:4]} {number[4:6]}** **** {number[-4:]}'

    elif count == 20:

        return f'{bank_account[:-20]}**{bank_account[-4:]}'
