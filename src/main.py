from datetime import datetime
from utils.functions import list_operations, order_operation, encrypted_account
import os
from config import ROOT_DIR

PATH_TO_OPERATIONS = os.path.join(ROOT_DIR, 'utils', 'operations.json')


def main():
    list_of_operations = list_operations(PATH_TO_OPERATIONS)  # список операций
    filtered_list_of_operations = order_operation(
        list_of_operations)  # отфильтрованный список операций
    for operation in reversed(filtered_list_of_operations[-5:]):
        date = datetime.fromisoformat(operation['date'])
        date = date.strftime('%d.%m.%Y %H:%M')
        description = operation.get('description')
        from_info = operation.get('from')
        to_info = operation.get('to')
        amount = operation['operationAmount']['amount']
        currency = operation['operationAmount']['currency']['name']
        print(f'{date} {description}')
        if from_info:
            print(
                f'{encrypted_account(from_info)} -> '
                f'{encrypted_account(to_info)}')
        else:
            print(f'{encrypted_account(to_info)}')
        print(f'{amount} {currency}\n')


if __name__ == '__main__':
    main()
