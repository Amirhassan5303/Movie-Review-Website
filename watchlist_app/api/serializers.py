from rest_framework import serializers

from watchlist_app.models import WatchList, StreamPlatform


# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Name is too short")
#     return value
#
#
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])   # third type of validators
#     description = serializers.CharField()
#     is_active = serializers.CharField()
#
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get("name", instance.name)
#         instance.description = validated_data.get("description", instance.description)
#         instance.is_active = validated_data.get("is_active", instance.is_active)
#         instance.save()
#
#         return instance
#
#     def validate_name(self, value):  # field-level validation
#         if len(value) < 2:
#             raise serializers.ValidationError("Name is too short")
#         return value
#
#     def validate(self, data):   # object-level validation
#         if data['name'] == data['description']:
#             raise serializers.ValidationError('title and description should be different')
#         return data

class WatchListSerializer(serializers.ModelSerializer):

    # len_name = serializers.SerializerMethodField()

    class Meta:
        model = WatchList
        fields = "__all__"
        # fields = ["id", "name", "description"]
        # exclude = ["is_active"]

    # def get_len_name(self, obj):
    #     return len(obj.name)
    #
    # def validate_name(self, value):  # field-level validation
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too short")
    #     return value
    #
    # def validate(self, data):   # object-level validation
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError('title and description should be different')
    #     return data


class StreamPlatformSerializer(serializers.ModelSerializer):

    class Meta:
        model = StreamPlatform
        fields = "__all__"
