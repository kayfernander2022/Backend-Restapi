from .models import Todo
from rest_framework import serializers

# Our TodoSerializer
class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # The model it will serialize
        model = Todo
        # choose the fields that should be included in the serialized output we get back,which ones you want
        fields = ['id', 'subject', 'details']


#the seralizers job is to give us pretty objects