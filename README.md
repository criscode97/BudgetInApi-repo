# BudgetIn API
 A django CRUD api that allows users to keep track of their expenses and income.
 
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
 
 ## Live Demo
 Upcomming
 
 ## Video Demo
 https://youtu.be/2_4OXnU8s8w
 
 ## Usage
 
 ### User Registration:
url/auth/register/ 
- method: POST
- body: {
          "username": 
              "YOUR_USERNAME"
          ,
          "password": 
              "YOUR_PASSWORD"
          ,
          "password2": 
              "This field is required."
          ,
          "email": 
              "YOUR_EMAIL"
          ,
          "first_name": 
              "YOUR_FIRST_NAME"
          ,
          "last_name": 
              "YOUR_LAST_NAME"
   
      }
- response: {"username":"YOUR_USERNAME","password":"YOUR_PASSWORD","email": "YOUR_EMAIL","first_name":"YOUR_FIRST_NAME","last_name":"YOUR_LAST_NAME"}

### User token:
url/auth/login 
- method: POST
- body: {
            "username": 
                "YOUR_USERNAME"
            ,
            "password": 
                "YOUR_PASSWORD"
            
         }
- response: {"refresh": "YOUR_REFRESH_TOKEN", "access": "YOUR_BEARER_tOKEN"}

### List User Expenses
url/expenses/
- method: GET
- headers: "Authorization: Bearer YOUR_TOKEN"
- response: [
               {
                   "id": 1,
                   "title": "YOUR EXPENSE 1",
                   "date": "2022-02-07T19:14:16.263675Z",
                   "total": 9.99,
                   "user": YOUR_USER_ID
               },
               {
                   "id": 2,
                   "title": "YOUR EXPENSE 2",
                   "date": "2022-02-07T19:15:11.559046Z",
                   "total": 99.99,
                   "user": YOUR_USER_ID
               }
           ]
           
### List User Incomes
url/income/
- method: GET
- headers: "Authorization: Bearer YOUR_TOKEN"
- response: [
               {
                   "id": 1,
                   "title": "YOUR INCOME 1",
                   "date": "2022-02-07T19:14:16.263675Z",
                   "total": 9999.99,
                   "user": YOUR_USER_ID
               },
               {
                   "id": 2,
                   "title": "YOUR INCOME 2",
                   "date": "2022-02-07T19:15:11.559046Z",
                   "total": 999.99,
                   "user": YOUR_USER_ID
               }
           ]
### Posting An Expense
url/expense/  or url/expenses/
- method: POST
- headers: "Authorization: Bearer YOUR_TOKEN"
- body : [
               {
                   "title": "YOUR EXPENSE 1",
                   "total": 9999.99,
               }
             ]
             
- response: [
               {
                   "id": YOUR_ITEM_ID,
                   "title": "YOUR EXPENSE 1",
                   "date": "2022-02-07T19:14:16.263675Z",
                   "total": 9999.99,
                   "user": YOUR_USER_ID
               }
             ]
             
### Posting An Income

url/INCOME/
- method: POST
- headers: "Authorization: Bearer YOUR_TOKEN"
- body : [
               {
                   "title": "YOUR INCOME 1",
                   "total": 9999.99,
               }
             ]
             
- response: [
               {
                   "id": YOUR_ITEM_ID,
                   "title": "YOUR INCOME 1",
                   "date": "2022-02-07T19:14:16.263675Z",
                   "total": 9999.99,
                   "user": YOUR_USER_ID
               }
             ]
             
             
### Access An Expense Item by ID:
url/expense/YOUR_ITEM_ID
- method: GET
- headers: "Authorization: Bearer YOUR_TOKEN"
- response: [
               {
                   "id": YOUR_ITEM_ID,
                   "title": "YOUR INCOME 1",
                   "date": "2022-02-07T19:14:16.263675Z",
                   "total": 9999.99,
                   "user": YOUR_USER_ID
               }
             ]
             
### Access An Income Item by ID:
url/income/YOUR_ITEM_ID
- method: GET
- headers: "Authorization: Bearer YOUR_TOKEN"
- response: [
               {
                   "id": YOUR_ITEM_ID,
                   "title": "YOUR INCOME 1",
                   "date": "2022-02-07T19:14:16.263675Z",
                   "total": 9999.99,
                   "user": YOUR_USER_ID
               }
             ]
             
### Updating An Expense Item by ID:
url/expense/YOUR_ITEM_ID
- method: PUT
- headers: "Authorization: Bearer YOUR_TOKEN"
- body:  [
               {
                   "title": "YOUR NEW EXPENSE 1",
                   "date": "2022-02-07T19:14:16.263675Z",
                   "total": 9.99,
                   "user": YOUR_USER_ID
               }
             ]
             
- response:   [
               {
                   "id" : "YOUR_ITEM_ID"
                   "title": "YOUR NEW EXPENSE 1",
                   "date": "2022-02-07T19:14:16.263675Z",
                   "total": 9.99,
                   "user": YOUR_USER_ID
               }
             ]             

### Updating An Income Item by ID:
url/income/YOUR_ITEM_ID
- method: PUT
- headers: "Authorization: Bearer YOUR_TOKEN"
- body:  [
               {
                   "title": "YOUR NEW INCOME 1",
                   "date": "2022-02-07T19:14:16.263675Z",
                   "total": 9.99,
                   "user": YOUR_USER_ID
               }
             ]
             
- response:   [
               {
                   "id" : "YOUR_ITEM_ID"
                   "title": "YOUR NEW INCOME 1",
                   "date": "2022-02-07T19:14:16.263675Z",
                   "total": 9.99,
                   "user": YOUR_USER_ID
               }
             ]             

### Delete An Expense Item by ID:
url/expense/YOUR_ITEM_ID
- method: DELETE
- headers: "Authorization: Bearer YOUR_TOKEN"
- response: [
               {
                   "id": YOUR_ITEM_ID
                   "title": "YOUR NEW EXPENSE 1",
                   "date": "2022-02-07T19:14:16.263675Z",
                   "total": 9.99,
                   "user": YOUR_USER_ID
               }
             ]         

### Delete An Income Item by ID:
url/income/YOUR_ITEM_ID
- method: DELETE
- headers: "Authorization: Bearer YOUR_TOKEN"
- response: [
               {
                   "id": YOUR_ITEM_ID
                   "title": "YOUR NEW INCOME 1",
                   "date": "2022-02-07T19:14:16.263675Z",
                   "total": 9.99,
                   "user": YOUR_USER_ID
               }
             ]         
        
### User Summary
 url/user-budget/ 
 - method: GET
 - headers: "Authorization: Bearer YOUR_TOKEN"
 - response: {
    "total": YOUR_INCOME_TOTAL - YOUR_TOTAL_EXPENSES,
    "expenses": YOUR_TOTAL_EXPENSES,
    "income": YOUR_INCOME_TOTAL
}
 
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
## UML
![myapp_models](https://user-images.githubusercontent.com/92554847/153736482-7e84b97f-cac8-4ca4-b54b-85bbeb982ecb.png)


