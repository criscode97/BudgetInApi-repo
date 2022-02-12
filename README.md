# BudgetIn API
 A django api that allows users to keep track of their expenses and income
 
 ## App Structure
 `
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
        
    `


