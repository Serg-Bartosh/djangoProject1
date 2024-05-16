from socialnetwork.models.chat.message import ChatMessage


def change_state_message(chat, user):
    messages = ChatMessage.objects.filter(chat_id=chat.id, state="NEW")
    if messages.exists():
        author_id = messages[0].author.id
        if user.id != author_id:
            messages.update(state="READ")
