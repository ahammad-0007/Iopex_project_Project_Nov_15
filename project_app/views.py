# from django.shortcuts import render
# from .models import Task
# from rest_framework import viewsets
# from .serializers import TaskSerializers
# from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# from rest_framework_simplejwt.authentication import JWTAuthentication
# # from api.
# # Create your views here.
#
# class UserTasksListCreate(ListCreateAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializers
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]
#
# class UserTasksRetriveUpdateDestroy(RetrieveUpdateDestroyAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializers
#     permission_classes = [IsAuthenticated]
#     authentication_classes = [JWTAuthentication]
#
# # class UserTasksListCreate(viewsets.ModelViewSet):
# #     queryset = Task.objects.all()
# #     serializer_class = TaskSerializers
# #     authentication_classes = [JWTAuthentication]
# #     permission_classes = [IsAuthenticated]
#
# # class UserTasksRetriveUpdateDestroy(viewsets):
# #     queryset = Task.objects.all()
# #     serializer_class = TaskSerializers
# #     permission_classes = [IsAuthenticated]
# #     authentication_classes = [JWTAuthentication]


from django.shortcuts import render
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializers
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly, DjangoObjectPermissions
# from .custompermissions import MyPermission

@api_view(['GET','POST','PUT','PATCH','DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def task_api(request,pk=None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            stu = Task.objects.get(id=id)
            serializer = TaskSerializers(stu)
            return Response(serializer.data)
        stu = Task.objects.all()
        serializer = TaskSerializers(stu, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = TaskSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        id = pk
        stu = Task.objects.get(pk=id)
        serializer = TaskSerializers(stu, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'})
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    if request.method == 'PATCH':
        id = pk
        stu = Task.objects.get(pk=id)
        serializer = TaskSerializers(stu, data= request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated Partially'})
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        id = pk
        stu = Task.objects.get(pk = id)
        stu.delete()
        return Response({'msg':'Data Deleted Successfully!!!'})

