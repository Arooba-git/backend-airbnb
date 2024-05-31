from django.http import JsonResponse
from rest_framework.decorators import api_view

from chat.models import Conversation
from chat.serializers import ConversationsListSerializer, ConversationsDetailSerializer, ConversationMessageSerializer
from useraccount.models import User


@api_view(['GET'])
def conversations_list(request):
    serializer = ConversationsListSerializer(request.user.conversations.all(), many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def conversations_detail(request, pk):
    conversation = request.user.conversations.get(pk=pk)

    detail_serializer = ConversationsDetailSerializer(conversation, many=False)
    message_serializer = ConversationMessageSerializer(conversation.messages.all(), many=True)

    return JsonResponse({
        'conversation' : detail_serializer.data,
        'messages': message_serializer.data
    }, safe=False)


@api_view(['GET'])
def conversations_start(request, user_id):
    conversations = Conversation.objects.filter(users__in=[user_id]).filter(users__in=[request.user.id])

    if conversations.count() > 0:
        conversation = conversations.first()
        return JsonResponse({
            'success': True,
            'conversation_id': conversation.id
        })
    else:
        user = User.objects.get(pk=user_id)
        conversation = Conversation.objects.create()
        conversation.users.add(user)
        conversation.users(request.user)
        return JsonResponse({
            'success': True,
            'conversation_id': conversation.id
        })
