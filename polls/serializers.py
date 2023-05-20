from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["id", "task", "completed", "timestamp", "updated", "user"]

    def validate(self, attrs):
        task = attrs.get('task')
        if task == self.instance.id:
            pass
