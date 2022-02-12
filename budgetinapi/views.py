
from .serializer import ExpensesSerializer, IncomeSerializer, UserBudgetSerializer
from rest_framework import generics, mixins, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Expenses, Income
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Expenses, Income
from django.contrib.auth.models import User
from django.db.models import Sum
from django.forms.models import model_to_dict
from django.conf import settings
from django.core import serializers


class UserBudgetAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user_id = request.user.id
        expenses = Expenses.objects.filter(user=user_id)
        income = Income.objects.filter(user=user_id)
        income_total = income.aggregate(Sum('total'))['total__sum']
        expenses_total = expenses.aggregate(Sum('total'))['total__sum']
        return Response({'total': f"{income_total - expenses_total}",
        "expenses":expenses_total,
        "income": income_total})
    
class ExpenseView(generics.GenericAPIView, 
mixins.ListModelMixin, mixins.CreateModelMixin, 
mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = ExpensesSerializer
    queryset = Expenses.objects.all()
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        user_id = request.user.id
        user = User.objects.get(id=user_id)
        if id:
            expense = Expenses.objects.get(id=id)
            if expense.user == user:
                return Response(model_to_dict(expense))
            return Response({"Message": "You do not have permition to access this item"}, status=status.HTTP_401_UNAUTHORIZED)
        expenses = Expenses.objects.filter(user=user)
        serializer = ExpensesSerializer(expenses, many = True)
        return Response(serializer.data)
        
    def post(self, request):
        user_id = request.user.id
        user = User.objects.get(id=user_id)
        title = request.data['title']
        total = request.data['total']
        expense = Expenses.objects.create(user=user, title=title, total=total)
        return Response(model_to_dict(expense), status=status.HTTP_201_CREATED)

    
    def put(self, request, id=None):
        if not id and not request.data['id']:
            return Response({"Message": "Please provide an id for the item you wish to update"}, status=status.HTTP_400_BAD_REQUEST)
        if not id:
            id = request.data['id']
        user_id = request.user.id
        user = User.objects.get(id=user_id)
        expense = Expenses.objects.get(id=id)
        if expense.user != user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        expense.title = request.data['title']
        expense.total = request.data['total']
        expense.save()
        return Response(model_to_dict(expense), status=status.HTTP_202_ACCEPTED)
        
    
    def delete(self, request, id):
        user_id = request.user.id
        user = User.objects.get(id=user_id)
        expense = Expenses.objects.get(id=id)
        if expense.user != user:
            return Response({"Message": "You do not have permition to access this item"}, status=status.HTTP_401_UNAUTHORIZED)
        self.destroy(request, id)
        return Response(status=status.HTTP_200_OK)


class IncomeView(generics.GenericAPIView, 
mixins.ListModelMixin, mixins.CreateModelMixin, 
mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = IncomeSerializer
    queryset = Income.objects.all()
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        user_id = request.user.id
        incomes = Income.objects.filter(user=user_id)
        user = User.objects.get(id=user_id)
        if id:
            income = Income.objects.get(id=id)
            if income.user == user:
                return Response(model_to_dict(income))
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        serializer = IncomeSerializer(incomes, many = True)
        return Response(serializer.data)

    def post(self, request):
        user_id = request.user.id
        user = User.objects.get(id=user_id)
        title = request.data['title']
        total = request.data['total']
        income = Income.objects.create(user=user, title=title, total=total)
        return Response(model_to_dict(income))
    
    def put(self, request, id=None):
        if not id and not request.data['id']:
            return Response({"Message": "Please provide an id for the item you wish to update"}, status=status.HTTP_400_BAD_REQUEST)
        if not id:
            id = request.data['id']
        user_id = request.user.id
        user = User.objects.get(id=user_id)
        income = Income.objects.get(id=id)
        if income.user != user:
            return Response({"Message": "You do not have the required permission to perform this action"},
            status=status.HTTP_401_UNAUTHORIZED)
        income.title = request.data['title']
        income.total = request.data['total']
        income.save()
        return Response(model_to_dict(income), status=status.HTTP_202_ACCEPTED)
    
    def delete(self, request, id):
        user_id = request.user.id
        user = User.objects.get(id=user_id)
        income = Expenses.objects.get(id=id)
        if income.user != user:
            return Response({"Message": "You do not have permition to access this item"}, status=status.HTTP_401_UNAUTHORIZED)
        self.destroy(request, id)
        return Response({"Message": "Income item has ben successfully deleted"}, status=status.HTTP_200_OK)



