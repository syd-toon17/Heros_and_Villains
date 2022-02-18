from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from  rest_framework import status
from .serializers import SuperSerializer
from .models import Super
from super_types.models import Super_Types


@api_view(['GET', 'POST'])
def super_list(request):
    if request.method == 'GET':
        super = Super.objects.all()
        super_type = Super_Types.objects.all()
        serializer = SuperSerializer(super, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)