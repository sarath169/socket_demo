from .models import User
from asgiref.sync import async_to_sync
import channels.layers
from channels.generic.websocket import JsonWebsocketConsumer
from django.db.models import signals
from .serializers import UserSerializer
from django.dispatch import receiver
import json
from .views import IndexPage


class UpdtaeUserList(JsonWebsocketConsumer):

    # Method to connect web socket
    def connect(self):
        async_to_sync(self.channel_layer.group_add)(
            'update_consumer_group',
            self.channel_name
        )
        self.accept()
        layer = channels.layers.get_channel_layer()
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many = True)

        async_to_sync(layer.group_send)('update_consumer_group', {
            'type': 'events.alarm',
            'data': serializer.data
        })

    # def disconnect(self, close_code):
    #     async_to_sync(self.channel_layer.group_discard)(
    #         'update_consumer_group',
    #         self.channel_name
    #     )
    #     self.close()

    def receive_json(self, content, **kwargs):
        print(f"Received event: {content}")

    def events_alarm(self, event):
        self.send_json(event['data'])


    @staticmethod
    @receiver(signals.post_save, sender=User)
    def UpdateConsumerList(sender, instance, **kwargs):
        try:
            layer = channels.layers.get_channel_layer()
            queryset = User.objects.all()
            serializer = UserSerializer(queryset, many = True)

            async_to_sync(layer.group_send)('update_consumer_group', {
                'type': 'events.alarm',
                'data': serializer.data
            })
        except Exception as e:
            print(e)