# GoIT_WEB_HW_5
#### Individual work at the GoIT school; using of modules `aiohtttp` and `asyncio`
### Decription
The main program `main.py` shows exchange rates for the last days. The information is taken from the official API of PrivatBank in Ukraine.
Requests to the API are sent asynchronously, for this purpose `asyncio` and `aiohttp` modules are used.
You also can work with this program as a client from your Internet browser.<br><br>

### Running the programm
To start the program you need to `clone this repository` with the following command:
```
https://github.com/S-Stepanov-1/GoIT_WEB_HW_5.git
```
<br>

Then navigate to the folder where the `main.py` file is located and run the terminal. In the terminal, type the following command:
```
py main.py n_days
```
where `n_days` is the integer number of days for which you want to get exchange rates.
#### If you enter a number smaller than one or larger than 10, you will only get information for one day.
<br><br>

You can also run the program with the following command:
```
py main.py n_days code_1 code_2 ... code_i
```
where code_1 , code_2 ... _code_i are the codes of the currencies you want to view, e.g. `PLZ`, `CAD`, `XAU`, `CHF` etc.
#### The codes should be entered with a space.
<br>

### Work from Internet browser
For work from browser you need just start the server:
```
py server.py
```
then start the consumer - in this window(s) you will see the results:
```
py consumer.py
```

After that, open the file `index.html` in your browser and type some message into the form. All connected consumers will receive as messages whatever you enter in the form. But if you enter the word `exchange`, you will get the exchange rate for today. You can also type `exchange n_days` through a space to get exchange rates for the last n_days.
