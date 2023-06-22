# GoIT_WEB_HW_5
#### Individual work at the GoIT school; using of modules `aiohtttp` and `asyncio`
### Decription
This program shows exchange rates for the last days. The information is taken from the official API of Privatbank in Ukraine.
Requests to the API are sent asynchronously, for this purpose `asyncio` and `aiohttp` modules are used.

### Running the programm
To start the program you need to clone this repository with the following command:
```
https://github.com/S-Stepanov-1/GoIT_WEB_HW_5.git
```
Then navigate to the folder where the `main.py` file is located and run the terminal. In the terminal, type the following command:
```
py main.py n_days
```

where `n_days` is the integer number of days for which you want to get exchange rates.
If you enter a number smaller than one or larger than 10, you will only get information for one day.



