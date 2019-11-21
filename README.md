# [Flask Dashboard Material PRO](https://appseed.us/admin-dashboards/priv-flask-dashboard-material-pro)

**[Open-Source Admin Dashboard](https://appseed.us/admin-dashboards/priv-flask-dashboard-material-pro)** coded in **Flask Framework** on top of **Material Dashboard PRO** design. **Features**:

- SQLite, PostgreSQL
- SQLAlchemy ORM
- Alembic
- Modular design with **Blueprints**
- Session-Based authentication (via **flask_login**)
- Forms validation
- Unitary tests
- Deployment scripts: Docker, Gunicorn
- **License MIT**

<br />

![Flask Dashboard Argon - Open-Source Flask Boilerplate.](https://raw.githubusercontent.com/app-generator/static/master/products/priv-flask-dashboard-material-pro-intro.gif)

<br />

## How to use it

```bash
$ # Get the code
$ git clone https://github.com/app-generator/priv-flask-dashboard-material-pro.git
$ cd priv-flask-dashboard-material-pro
$
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv --no-site-packages env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv --no-site-packages env
$ # .\env\Scripts\activate
$ 
$ # Install modules
$ # SQLIte version (no PostgreSQL)
$ pip3 install -r requirements-sqlite.txt
$ 
$ # OR with PostgreSQL connector
$ pip install -r requirements.txt
$
$ # Set the FLASK_APP environment variable
$ (Unix/Mac) export FLASK_APP=run.py
$ (Windows) set FLASK_APP=run.py
$ (Powershell) $env:FLASK_APP = ".\run.py"
$
$ # Start the application (development mode)
$ # --host=0.0.0.0 - expose the app on all network interfaces (default 127.0.0.1)
$ # --port=5000    - specify the app port (default 5000)  
$ flask run --host=0.0.0.0 --port=5000
$
$ # Access the dashboard in browser: http://127.0.0.1:5000/
```

<br />

## Docker execution

The application can be easily excuted in a docker container. The steps:

> Get the code

```bash
$ git clone https://github.com/app-generator/priv-flask-dashboard-material-pro.git
$ cd priv-flask-dashboard-material-pro
```

> Start the app in Docker

```bash
$ sudo docker-compose pull && sudo docker-compose build && sudo docker-compose up -d
```

Visit `http://localhost:5000` in your browser. The app should be up & running. 

<br />

## Support

24/7 Live [support](appseed.us/support) via [Discord](https://discord.gg/fZC6hup) and eMail **< support@appseed.us >**

<br />

## Credits & Links

- [Material Dashboard PRO](https://www.creative-tim.com/product/material-dashboard-pro) - crafted by Creative-Tim agency
- [Flask Dashboard Material PRO](https://appseed.us/admin-dashboards/flask-dashboard-material-pro) - Product page
- [Flask Framework](https://www.palletsprojects.com/p/flask/) - Offcial website
- [Flask Dashboard - Open-Source Boilerplates](https://dev.to/sm0ke/flask-dashboard-open-source-boilerplates-dkg) - A popular article published on Dev.to platform
- [Flask Dashboard](https://admin-dashboards.com/tags/flask-dashboard) - Index provided by **Admin-Dashboards.com**

<br />

## License

Commercial

<br />

---
[Flask Dashboard Material PRO](https://appseed.us/admin-dashboards/flask-dashboard-material-pro) - provided by **AppSeed**
