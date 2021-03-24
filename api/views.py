from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ContestSerializer

from .models import Contest

@api_view(['GET'])
def overview(request):
    api_urls = {
        'List': 'list/',
        'Detail View': 'contest-detail/<str:pk>/',
        'Create': 'contest-create/',
        'Update': 'contest-update/<str:pk>/',
        'Delete': 'contest-delete/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def ContestList(request):
    items = Contest.objects.all()
    serial = ContestSerializer(items, many=True)
    return Response(serial.data)


@api_view(['GET'])
def ContestDetail(request, pk):
    item = Contest.objects.get(id=pk)
    serial = ContestSerializer(item, many=False)
    return Response(serial.data)


@api_view(['PUT'])
def ContestCreate(request):
    serial = ContestSerializer(data=request.data)
    if serial.is_valid():
        serial.save()

    return Response(serial.data)

@api_view(['POST'])
def ContestUpdate(request, pk):
	item = Contest.objects.get(id=pk)
	serializer = TaskSerializer(instance=item, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['DELETE'])
def ContestDelete(request, pk):
    item = Contest.objects.get(id=pk)
    item.delete()

    return Response('Item successfully delete!')