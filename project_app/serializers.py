from rest_framework import serializers

class TaskSerializers(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    due_date = serializers.DateTimeField()
    # status = models.Choices(status_choice)
    status = serializers.CharField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()