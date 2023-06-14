from rest_framework import serializers
from .models import Post
from votes.models import Vote

class PostSerializer(serializers.ModelSerializer):
    owner= serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    votes_id = serializers.SerializerMethodField()
    votes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()

    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Image size larger than 2MB!'
            )
        if value.image.width > 4096 :
            raise serializers.ValidationError(
                'Image width larger than 4096px'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_votes_id(self, obj):
        request = self.context['request'].user
        if user.is_authenticated:
            vote = Vote.objects.filter(owner = user, post = obj).first()
            return vote.id if vote else None
        return None
    
    class Meta:
        model = Post 
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'image', 'flower_tag', 'votes_id', 'votes_count',
            'comments_count',
        ]
