import json

import rest_framework
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView

from .models import Account, Restaurant, Order, Food, Evaluation, Token, OrderandFood, ResandLocation
from rest_framework import viewsets
from rest_framework import permissions
from .serializer import AccountSerializer, RestaurantSerializer, EvaluationSerializer, FoodSerializer, OrderSerializer, \
    ResandLocationSerializer
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from rest_framework import request


# Create your views here.

# class AccountViewSet(viewsets.ModelViewSet):
#     account = Account.objects.all()
#     serializer_class = AccountSerializer(account)
#     queryset = serializer_class.data
#     permission_classes = [permissions.IsAuthenticated]

def getaccounts(request):
    account = Account.objects.all()
    serializer = AccountSerializer(account, many=True)
    return JsonResponse(
        serializer.data,
        json_dumps_params={'ensure_ascii': False}, safe=False
    )


class MyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        data = request.query_params
        token = data.get('token')
        token_obj = Token.objects.filter(token=token).first()
        if not token_obj:
            raise exceptions.AuthenticationFailed('auth fail')
        return token_obj.user, None


@csrf_exempt
def login(request):
    if request.method == "POST":
        print("请求成功")
        print(request.body)
        data = json.loads(request.body.decode('utf-8'))
        # data = request.POST
        print(data)
        username = data['username']
        password = data['password']
        print(data)
        print(username)
        account = Account.objects.filter(username=username, password=password).first()
        if not account:
            print("验证失败")
            error_msg = "登陆验证失败"
            return JsonResponse(
                {
                    "error_msg": error_msg,
                    "username": username,
                    "password": password,
                    "cha": account.charactor,
                    "is_login": False})
        else:
            print("验证成功")
            import hashlib
            m = hashlib.md5(bytes(username, encoding='utf-8'))
            import time
            ctime = str(time.time())
            m.update(bytes(ctime, encoding='utf-8'))
            token = m.hexdigest()
            Token.objects.update_or_create(user=account, defaults={'token': token})
            print(token)
            error_msg = '0'
            return JsonResponse(
                {"token": token,
                 "error_msg": error_msg,
                 "username": username,
                 "password": password,
                 "cha": account.charactor,
                 "is_login": True
                 })


def logout(request, token):
    token_obj = Token.objects.filter(token=token).first()
    if not token_obj:
        return JsonResponse({
            "result": "success"
        })
    else:
        token_obj.delete()
        return JsonResponse({
            "result": "success"
        })


def getallres(request):
    restaurants = Restaurant.objects.all()
    serializer = RestaurantSerializer(restaurants, many=True)
    print(serializer.data)
    return JsonResponse(
        serializer.data,
        json_dumps_params={'ensure_ascii': False}, safe=False
    )


def getfoods(request, pk):
    restaurant = Restaurant.objects.filter(id=pk).first()
    food = Food.objects.filter(belong_to=restaurant)
    serializer = FoodSerializer(food, many=True)
    if not food:
        return JsonResponse({
            "error": "Nodata"
        })
    else:
        return JsonResponse(
            serializer.data,
            json_dumps_params={'ensure_ascii': False}, safe=False
        )


class MyorderView(APIView):
    authentication_classes = [MyAuthentication, ]

    def get(self, request, *args, **kwargs):
        print(request.user.username)
        account = Account.objects.filter(id=request.user.id).first()
        if account.charactor == 2:
            orders = Order.objects.filter(user=request.user.id)
            serializers = OrderSerializer(orders, many=True)
            print(serializers.data)
            return JsonResponse(
                serializers.data,
                json_dumps_params={'ensure_ascii': False}, safe=False
            )
        else:
            res = Restaurant.objects.filter(belong_to=request.user.id).first()
            orders = Order.objects.filter(res=res.id)
            serializers = OrderSerializer(orders, many=True)
            print(serializers.data)
            return JsonResponse(
                serializers.data,
                json_dumps_params={'ensure_ascii': False}, safe=False
            )


class ResView(APIView):
    authentication_classes = [MyAuthentication, ]

    def get(self, request, *args, **kwargs):
        res = Restaurant.objects.filter(belong_to=request.user.id).first()
        locations = ResandLocation.objects.filter(res=res.id)
        serializer = ResandLocationSerializer(locations, many=True)
        return JsonResponse(
            {
                "resname": res.name,
            })


class GetFoodView(APIView):
    authentication_classes = [MyAuthentication, ]

    def get(self, request, *args, **kwargs):
        res = Restaurant.objects.filter(belong_to=request.user.id).first()
        foods = Food.objects.filter(belong_to=res.id)
        serializer = FoodSerializer(foods, many=True)
        return JsonResponse(
            serializer.data,
            json_dumps_params={'ensure_ascii': False}, safe=False
        )


class UpdateFoodView(APIView):
    authentication_classes = [MyAuthentication, ]

    def post(self, request, *args, **kwargs):
        print(request.body)
        data = json.loads(request.body.decode())
        # data = request.POST
        print(data)
        name = data['name']
        price = data['price']
        description = data['description']
        id = data['id']
        res = Restaurant.objects.filter(belong_to=request.user.id).first()
        food = Food.objects.filter(belong_to=res.id, id=id).first()
        food.name = name
        food.price = price
        food.description = description
        print(food.name)
        food.save()
        return JsonResponse({
            "res": "ok"
        })


class AddFoodView(APIView):
    authentication_classes = [MyAuthentication, ]

    def post(self, request, *args, **kwargs):
        print(request.body)
        data = json.loads(request.body.decode())
        # data = request.POST
        print(data)
        name = data['name']
        price = data['price']
        description = data['description']
        res = Restaurant.objects.filter(belong_to=request.user.id).first()
        food = Food.objects.create(
            name=name,
            price=price,
            description=description,
            belong_to=res,
        )
        food.save()
        return JsonResponse(
            {
                "res": "ok"
            }
        )


class SetNicknameView(APIView):
    authentication_classes = [MyAuthentication, ]

    def post(self, request, *args, **kwargs):
        print(request.user.username)
        user = Account.objects.filter(id=request.user.id).first()
        data = json.loads(request.body.decode())
        user.nickname = data['nickname']
        user.save()
        print(user.nickname)
        return JsonResponse(
            {
                "msg": "ok"
            }
        )


class GetUserView(APIView):
    authentication_classes = [MyAuthentication, ]

    def get(self, request, *args, **kwargs):
        user = Account.objects.filter(id=request.user.id).first()
        serializer = AccountSerializer(user, many=False)
        return JsonResponse(
            serializer.data,
            json_dumps_params={'ensure_ascii': False}, safe=False
        )


class TakeOrderView(APIView):
    authentication_classes = [MyAuthentication, ]

    def post(self, request, *args, **kwargs):
        print(request.body)
        data = json.loads(request.body.decode())
        # data = request.POST
        print(data)
        # uid = data['user_id']
        foods = data['data']
        food_dict = json.loads(foods)
        rid = data['res_id']
        total = data['total_price']
        print(foods)

        order = Order.objects.create(
            username=Account.objects.filter(id=request.user.id).first().username,
            resname=Restaurant.objects.filter(id=rid).first().name,
            user=request.user,
            res=Restaurant.objects.filter(id=rid).first(),
            state=1,
            content="没啥要说的",
            total_price=total,
        )
        for item in food_dict.items():
            key = item[0]
            value = item[1]

            print('%s   %s:%s' % (item, key, value))
            orderandfood = OrderandFood.objects.create(
                order=order,
                food=Food.objects.filter(id=key).first()
            )
        return JsonResponse({
            "msg": "ok"
        })


def getMyinfo(request, pk):
    user = Account.objects.filter(id=int(pk)).first()
    serializer = AccountSerializer(user, many=False)
    return JsonResponse(
        serializer.data,
        json_dumps_params={'ensure_ascii': False}, safe=False
    )


def delete(request, pk):
    food = Food.objects.filter(id=pk).first()
    food.delete()
    return JsonResponse({
        "res": "ok"
    })


def accessorder(request, pk):
    order = Order.objects.filter(id=pk).first()
    order.state = 2
    order.save()
    return JsonResponse({
        "res": "ok"
    })


def completeorder(request, pk):
    order = Order.objects.filter(id=pk).first()
    order.state = 3
    order.save()
    return JsonResponse({
        "res": "ok"
    })


def deleteorder(request, pk):
    order = Order.objects.filter(id=pk).first()
    if order.state == 1:
        order.delete()
        return JsonResponse({
            "res": "successfullydelete"
        })
    else:
        return JsonResponse({
            "res": "deletfail"
        })
