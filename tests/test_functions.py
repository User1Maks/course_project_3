import os
from utils.functions import list_operations, order_operation, encrypted_account
from config import ROOT_DIR
import pytest


@pytest.fixture()
def operations():
    dictionary = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        }
    ]
    return dictionary


def test_order_operation(operations):
    assert order_operation(operations)[1] == {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }


def test_list_operations(operations):
    assert list_operations(os.path.join(
        ROOT_DIR,
        'utils',
        'operations.json'))[0] == operations[0]


def test_encrypted_account(operations):
    assert encrypted_account(
        operations[0]['from']) == 'Maestro 1596 83** **** 5199'
    assert encrypted_account(
        operations[0]['to']) == 'Счет **9589'
