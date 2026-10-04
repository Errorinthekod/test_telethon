
def format_message(message, ids: bool = False):
    """
    Formats message info to a dictionary.
    Set ::param ids True to see:
    - chat_id
    - sender_id
    - message_id
    """
    data = {
        "date"      : message.date.isoformat(),
        "text"      : message.text,
    }

    id_data = {
        "chat_id"   : message.chat_id,
        "sender_id" : message.sender_id,
        "message_id": message.id,
    }

    if ids:
        return {**id_data, **data}
    else:
        return data
