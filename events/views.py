from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Event
from .serializers import EventSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from users.models import User
import pprint

class EventListView(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'created_by', 'origin_address'] 

    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response({'event': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class EventListView(APIView):
#     def get(self, request):
#         events = Event.objects.all()
#         serializer = EventSerializer(events, many=True)
#         return Response({'events': serializer.data}, status=status.HTTP_200_OK)


#     def post(self, request):
#         serializer = EventSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(created_by=request.user)
#             return Response({'event': serializer.data}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EventDetailView(APIView):
    def get(self, request, event_id):
        event = get_object_or_404(Event, id=event_id)
        serializer = EventSerializer(event)
        return Response({'event': serializer.data}, status=status.HTTP_200_OK)

    def delete(self, request, event_id):
        event = get_object_or_404(Event, id=event_id)
        event.delete()
        return Response({'message': 'Event deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)

class EventJoinView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, event_id):
        event = get_object_or_404(Event, id=event_id)
        if not event.participants.filter(id=request.user.id).exists():
            event.participants.add(request.user)
            return Response({'message': 'Joined the event successfully.'}, status=status.HTTP_200_OK)
        return Response({'message': 'Already a participant.'}, status=status.HTTP_400_BAD_REQUEST)

class EventLeaveView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, event_id):
        event = get_object_or_404(Event, id=event_id)
        if event.participants.filter(id=request.user.id).exists():
            event.participants.remove(request.user)
            return Response({'message': 'Left the event successfully.'}, status=status.HTTP_200_OK)
        return Response({'message': 'Not a participant.'}, status=status.HTTP_400_BAD_REQUEST)


