import requests
import json
from token_keys import keys

class APIException(Exception):
    pass


class CurrencyConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise APIException(f'Невозможно перевести одинаковые валюты {quote}')
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Ну удалось обработать валюту {quote}')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Ну удалось обработать валюту {base}')
        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Ну удалось обработать количество {amount}')
        quote_ticker, base_ticker = keys[quote], keys[base]
        r = requests.get(f'https://api.exchangerate.host/convert?from={quote_ticker}&to={base_ticker}&amount={amount}')
        result = json.loads(r.content)['result']
        return result
