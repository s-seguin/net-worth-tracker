# Net-Worth Tracker

A simple networth tracker

---

## Usage

- starting: `docker-compose up`
- stopping: `docker-compose down`
- executing commands:
  `docker-compose exec web python manage.py showmigrations`

---

## Planned Endpoints

### Assets

- {GET} `/networthtracker/networth/assets`
- {GET} `POST /networthtracker/networth/assets/:type`
- {GET, `PUT, DELETE} /networthtracker/networth/assets/:type/:id`

### Liabilities

- {GET} `/networthtracker/networth/liabilities`
- {GET, `POST} /networthtracker/networth/liabilities/:type`
- {GET, PUT, DELETE} `/networthtracker/networth/liabilities/:type/:id`

### Accounts

- {GET, POST} `/networthtracker/networth/accounts`
- {GET, PUT, DELETE} `/networthtracker/networth/accounts/:id`

### Transactions

- {GET, POST} `/networthtracker/networth/transactions`
- {GET, PUT, DELETE} `/networthtracker/networth/transactions/:id`

### Users / Account Management

- TBD
