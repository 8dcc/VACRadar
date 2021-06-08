# VACRadar
A python script to search VAC banned accounts. The script generates random steam id profiles and checks the content of the html to search for the word `ban`.

This readme is about `vacradar.py` (log banned profiles), but there is another script called `steam_finder.py` (log random profiles). All this readme can be aplied to `steam_finder.py`, but the logs will contain normal ids instead of banned ones.

#

⚠️ If you make a lot of requests, you might get banned! I am not responsible at all. ⚠️

Although the download rate will be slower, the `useTorProxy` option is recomended.

#

### Instalation

``` shell
git clone https://github.com/r4v10l1/VACRadar
cd VACRadar
python -m pip install -r requirements.txt
python VACRadar.py
```

### Configuration

* You can edit the `useTorProxy` variable to enable the use of a proxy during the requests. If you enable this, you will need to have tor open and the port it will use will be **9150**.

### Logs

The script writes the following information into a log (`VACFound.log`):
* When the script detects a steam banned profile.
* It will save the id, you can access the logged profile by going to: https://steamcommunity.com/profiles/ + id

The script writes the following information into a log (`VACRadar_debug.log`):
* When the user starts the program.
* When the user stops the program.
