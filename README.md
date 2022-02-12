# BudgetIn API
 A django CRUD api that allows users to keep track of their expenses and income
 
 ## Technologies
- Django v4.0
- Django REST Framework v3.13.1
- Django Rest Framework-SimpleJTW v5.0.0
 
 ## Features
 - User can register using the /auth/register/ route. user must submit an email, a username, a password, and a password confirmation
 - Users can login using the /auth/login/ to obtain an authorization Bearer Token as well as a Refresh token that will allow them to obtain a new token once the current one expires or if the user wishes to retire their old token for security reasons.
 - Users can get a quick access to their current expense total and income total through the /user-budget/ route.
 - Users can POST incomes through the /income/ route or expenses through the /expenses/ route
 - Users can GET a list of their current incomes or expenses through the /icome/ or /expenses/ routes respectively.
 - Users can access, update, post, or delete an item using the item id through the /expense/<int:id>/ route for expenses and /income/<int:id>/ route for incomes
 ## App Structure
 ```bash
 BudgetIn
│   db.sqlite3
│   listing.txt
│   manage.py
│
├───auth
│   │   admin.py
│   │   apps.py
│   │   models.py
│   │   serializers.py
│   │   tests.py
│   │   urls.py
│   │   views.py
│   │   __init__.py
│   │
│   └───migrations
│           __init__.py
│
├───budgetin
│       asgi.py
│       settings.py
│       urls.py
│       wsgi.py
│       __init__.py
│
└───budgetinapi
    │   admin.py
    │   apps.py
    │   models.py
    │   serializer.py
    │   tests.py
    │   urls.py
    │   views.py
    │   __init__.py
    │
    └───migrations
           0001_initial.py
           0002_income.py
           0003_alter_expenses_id_alter_income_id.py
           0004_alter_expenses_total_alter_income_total.py
           __init__.py
```


