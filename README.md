# refinitiv-company
Develop a crawler and an API to represent data to clients

## Requirements
1. Install django:
    `pip install django`
2. Instal django rest framework:
    `pip install djangorestframework`
3. Install numpy:
    `pip install numpy`
4. Install matplotlib:
    `pip install matplotlib`
5. Install selenium:
    `pip install selenium`
6. Download a webdriver

## Phase1
We go randomly because `getLetter()` function returns a string with a length equal to 2 that generates randomly, and then it sends to the search box and we choose the first result, besides crawl data.
The important thing is to get ricCode or company ticker, we must get data from network tab in to inspect for example for the apple company the data is returned `https://www.refinitiv.com/bin/esg/esgsearchresult?ricCode=AAPL.O` but we need `APPL.O`. After all these, we have 5 thread that helps us in timing.

## Phase2
There are 2 apps, one is an account for authentication, and the second is for getting data to show clients.
Two substantial point:
1. after create apps, add to the settings
2. put `AUTH_USER_MODEL = 'account.Account'` in settings to django knows about new user model.

There are two approaches to reading and showing data to clients, the first is converting CSV to SQLite, and Django ORM handles for us, but the other approach is to work with CSV.

## Docker
1. Add `ALLOWED_HOSTS = ['*']` to the settings.
2. build and run container: `sudo docker-compose up --build`
3. Through the container running, go inside the container to convert CSV to SQLite
4. Command for go inside: `sudo docker exec -it CONTAINER_ID bash`
5. Run these commands: `apt update`, `apt install sqlite3`, `sqlite3 db.sqlite3`
6. Now you are inside the database, for convert run these commands: `.mode csv`, `.import dataCompanies.csv refinitiv_refinitiv`
