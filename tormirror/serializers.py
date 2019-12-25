from rest_framework import serializers


class RequestSerializer(serializers.Serializer):

    method = serializers.ChoiceField(choices=('get', 'post', 'delete', 'options', 'put', 'patch'))
    args = serializers.ListField()
    kwargs = serializers.DictField()

    # this serializer is only used for validation
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

