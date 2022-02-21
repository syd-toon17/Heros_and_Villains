from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from  rest_framework import status
from .serializers import SuperSerializer
from super_types.serializers import Super_TypesSerializer
from .models import Super
from super_types.models import Super_Types



@api_view(['GET', 'POST'])
def super_list(request):
    if request.method == 'GET':
        type_param = request.query_params.get('type')
        if type_param == "heroes":
            super = Super.objects.filter(super_type_id=1)
        elif type_param == "villains":
            super = Super.objects.filter(super_type_id=2)
        else:
            super = Super.objects.all()
        serializer = SuperSerializer(super, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def super_detail(request, pk):
    super = get_object_or_404(Super, pk=pk)
    if request.method == 'GET':
        serializer = SuperSerializer(super);
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SuperSerializer(super, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



