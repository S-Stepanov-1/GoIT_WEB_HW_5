import platform
from pprint import pprint
from datetime import datetime, timedelta
import aiohttp
import asyncio
import sys
from abc import ABC, abstractmethod


URL = "https://api.privatbank.ua/p24api/exchange_rates?date="


class APIHandler(ABC):
    @abstractmethod
    async def create_session(self):
        raise NotImplemented

    @abstractmethod
    def prepare_data(self, x_days):
        raise NotImplemented


class PBHandler(APIHandler):
    CURRENCIES = ["USD", "EUR"]

    def create_session(self):
        self.session = aiohttp.ClientSession()

    async def prepare_data(self, x_days: int):
        async with self.session as session:

            tasks = []
            for day in range(x_days):
                url = URL + (datetime.today() - timedelta(days=day)).strftime('%d.%m.%Y')
                tasks.append(self.get_data_from_json(session, url))

            result = await asyncio.gather(*tasks)
            return result

    @staticmethod
    async def get_data_from_json(session, url):
        async with session.get(url) as response:
            await asyncio.sleep(0.5)  # delay is needed to avoid status code 429 "Too Many Requests "
            json = await response.json()

            date = json["date"]

            currency_dict = {date: {}}
            rates = json["exchangeRate"]

            for rate in rates:
                if rate["currency"] in PBHandler.CURRENCIES:
                    currency_dict[date][rate["currency"]] = {"purchase": rate["purchaseRateNB"],
                                                             "sale": rate["saleRateNB"]}
            return currency_dict


async def main(x_days):
    pb = PBHandler()
    pb.create_session()

    #       === ADDITIONAL TASKS №1 ===
    pb.CURRENCIES.extend(sys.argv[2:])  # add currency like PLN, CAD etc.

    return await pb.prepare_data(x_days)


if __name__ == "__main__":
    #       === User input handling ===
    if len(sys.argv) < 2 or sys.argv[1].isalpha():
        print(
            "\nPlease, when calling the program, pass the integer number of days for which you want to see the exchange rate.\n")
        exit(1)

    days = int(sys.argv[1]) if 1 < int(sys.argv[1]) <= 10 else 1

    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    answer_data_list = asyncio.run(main(days))
    pprint(answer_data_list)
