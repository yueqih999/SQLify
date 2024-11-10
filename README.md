# SQLify

### 👉 Start the Frontend 

> **Step 1** - Once the project is downloaded, change the directory to `frontend`. 

```bash
$ cd frontend
```

<br >

> **Step 2** - Install dependencies via NPM or yarn

```bash
$ nvm install 16
$ nvm use 16
$ npm i
// OR
$ yarn
```

<br />

> **Step 3** - Start in development mode

```bash
$ npm run start 
// OR
$ yarn start
```

<br />

At this point, the app is available in the browser `localhost:3000` (the default address).


<br /> 

### 👉 Start the Backend Server 

> **Step 1** - Change the directory to `backend`

```bash
$ cd backend
```

<br >

> **Step 2** - Install dependencies using a `virtual environment`

```bash
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
$
$ pip install -r requirements.txt
```

<br />

> **Step 3** - Setup the `Flask` environment 

```bash
$ export FLASK_APP=run.py
$ export FLASK_ENV=development
// OR 
$ (Windows CMD) set FLASK_APP=run.py
$ (Windows CMD) set FLASK_ENV=development
$
$ (Powershell) $env:FLASK_APP = ".\run.py"
$ (Powershell) $env:FLASK_ENV = "development"
```

<br />

> **Step 4** - Start the API server (development mode)

```bash
$ flask run
```

Use the API via `POSTMAN` or `Swagger Dashboard` at `localhost:5000`.

<br /> 

## 👉 Codebase Structure

```bash
< ROOT  >
    |
   api-server-flask/
    ├── api
    │   ├── config.py
    │   ├── __init__.py
    │   ├── models.py
    │   └── routes.py
    ├── requirements.txt
    ├── run.py
    └── tests.py
```

<br />


