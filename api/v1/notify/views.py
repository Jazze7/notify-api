from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from api.v1.notify.serializers import NotificationSerializer
from web.models import Notification

@api_view(["GET"])
def notify(request):
    instances = Notification.objects.all()

    if instances.exists():
        serializer = NotificationSerializer(instances, many=True)
        response_data = {
            "status_code": 200,
            "data": serializer.data,
        }
        return Response(response_data, status=status.HTTP_200_OK)
    else:
        response_data = {
            "status_code": 404,
            "message": "No notifications found."
        }
        return Response(response_data, status=status.HTTP_404_NOT_FOUND)
