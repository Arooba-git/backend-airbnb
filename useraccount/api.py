
from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from property.serializers import ReservationsListSerializer
from useraccount.models import User
from useraccount.serializers import UserDetailsSerializer


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def landlord_detail(request, pk):
    landlord= User.objects.get(pk=pk)
    print('~~~~landlord', landlord)

    serializer = UserDetailsSerializer(landlord, many=False)
    print('~~~serializer', serializer)

    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def reservations_list(request):
    reservations = request.user.reservations.all()
    print('reservations', reservations)
    serializer = ReservationsListSerializer(reservations, many=True)
    return JsonResponse(serializer.data, safe=False)