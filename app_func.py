from data import emojis , users, user_emojis
# import asyncio

async def get_gallery_emojis(user_id):
    # await asyncio.sleep(5)
    emojis_to_return = {}
    user_type = -1
    for user in users:
        if user["user_id"] == user_id:
            user_type = user["type_num"]
            break
    if user_type == -1:
        return f"user {user_id} not appear in the system please sign in."
    line_count = 0
    for emoji in emojis:
        if emoji["type_num"] <= user_type:
            line_count += 1
            emojis_to_return[line_count] = emoji["emoji"]
    return emojis_to_return


async def add_emojis(emoji, user_id):
    user_type = -1
    for user in users:
        if user["user_id"] == user_id:
            user_type = user["type"]
            break
    if user_type == -1:
        return f"user {user_id} not appear in the system please sign in."
    count_row = 0
    if user_id in user_emojis.keys():
        count_row = len(user_emojis[user_id])
        if user_type == "Free" and count_row >= 4:
            return "you reach your emoji limit(5) to add more emoji get primiume or remove old emoji"
        if user_type == "Premium" and count_row >= 99:
            return "you reach your emoji limit(100) to add more emoji get Business or remove old emoji"
        if emoji in user_emojis[user_id]:
            return f"emoji {emoji} already exists"
        user_emojis[user_id].append(emoji)
    else:
        user_emojis[user_id] = [emoji]
    return user_emojis[user_id] #f"emoji {emoji} added to user_emojis of {user_id}"



async def del_emojis(emoji, user_id):
    user_type = -1
    for user in users:
        if user["user_id"] == user_id:
            user_type = user["type"]
            break
    if user_type == -1:
        return f"user {user_id} not appear in the system please sign in."
    if user_id not in user_emojis.keys():
        return f"user {user_id} has no emojis to delete"
    if emoji not in user_emojis[user_id]:
        return f"emoji {emoji} not exists to be delete"
    user_emojis[user_id].remove(emoji)
    return user_emojis[user_id] #f"emoji {emoji} added to user_emojis of {user_id}"