# Anime Atlas

## Run locally with SQLite

From the `myproject` directory:

```powershell
python manage.py migrate
python manage.py test myapp
python manage.py runserver
```

## Use MySQL

Set these variables in the same PowerShell window before running Django. Replace
the password with the password for your MySQL account; do not save credentials
in source files.

```powershell
$env:MYSQL_DATABASE = "PROJECT"
$env:MYSQL_USER = "root"
$env:MYSQL_PASSWORD = "your MySQL password"
$env:MYSQL_HOST = "localhost"
$env:MYSQL_PORT = "3306"
```

Create the `PROJECT` database in MySQL if it does not already exist:

```sql
CREATE DATABASE PROJECT CHARACTER SET utf8mb4;
```

Then run migrations to create/update the tables (including the automatic
`joined_at` timestamp), followed by the app checks:

```powershell
python manage.py migrate
python manage.py test myapp
python manage.py runserver
```
