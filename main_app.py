# import threading
import asyncio
from flask import Flask, jsonify
from flask import request
from app_func import get_gallery_emojis, del_emojis, add_emojis

app = Flask(__name__)

@app.route("/emojies/gallery", methods=["GET"])
def show_gallery():
    user_id = request.args.get('user_id', type = int)
    asyncio.set_event_loop(asyncio.new_event_loop())
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(get_gallery_emojis(user_id))
    return jsonify({"result": result})


@app.route("/emojies/addemoji", methods=['GET', 'POST'])
def add_emoji():
    user_id = request.args.get('user_id', type = int)
    emoji = request.args.get('emoji', type = str)
    print(emoji)
    if not emoji:
        return "need to provide emoji to added"
    asyncio.set_event_loop(asyncio.new_event_loop())
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(add_emojis(emoji, user_id))
    return jsonify({"result": result})


@app.route("/emojies/delemoji", methods=['GET', 'DEL'])
def del_emoji():
    user_id = request.args.get('user_id', type = int)
    emoji = request.args.get('emoji', type = str)
    if not emoji:
        return "need to provide emoji to added"
    asyncio.set_event_loop(asyncio.new_event_loop())
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(del_emojis(emoji, user_id))
    return jsonify({"result": result})


if __name__=='__main__':
    app.run(debug=True)