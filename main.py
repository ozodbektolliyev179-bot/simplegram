import os

from dotenv import load_dotenv

from simplegram import Update


load_dotenv()


result = {
  "ok": True,
  "result": [
    {
      "update_id": 117068966,
      "message": {
        "message_id": 124,
        "from": {
          "id": 6345124148,
          "is_bot": False,
          "first_name": "Laziz",
          "username": "laz_1z",
          "language_code": "uz"
        },
        "chat": {
          "id": 6345124148,
          "first_name": "Laziz",
          "username": "laz_1z",
          "type": "private"
        },
        "date": 1770298386,
        "text": "/start",
        "entities": [
          {
            "offset": 0,
            "length": 6,
            "type": "bot_command"
          }
        ]
      }
    },
    {
      "update_id": 117068967,
      "message": {
        "message_id": 125,
        "from": {
          "id": 6345124148,
          "is_bot": False,
          "first_name": "Laziz",
          "username": "laz_1z",
          "language_code": "uz"
        },
        "chat": {
          "id": 6345124148,
          "first_name": "Laziz",
          "username": "laz_1z",
          "type": "private"
        },
        "date": 1770298403,
        "text": "/start",
        "entities": [
          {
            "offset": 0,
            "length": 6,
            "type": "bot_command"
          }
        ]
      }
    },
    {
      "update_id": 117068968,
      "message": {
        "message_id": 126,
        "from": {
          "id": 6345124148,
          "is_bot": False,
          "first_name": "Laziz",
          "username": "laz_1z",
          "language_code": "uz"
        },
        "chat": {
          "id": 6345124148,
          "first_name": "Laziz",
          "username": "laz_1z",
          "type": "private"
        },
        "date": 1770298408,
        "text": "/start",
        "entities": [
          {
            "offset": 0,
            "length": 6,
            "type": "bot_command"
          }
        ]
      }
    },
    {
      "update_id": 117068969,
      "message": {
        "message_id": 127,
        "from": {
          "id": 6345124148,
          "is_bot": False,
          "first_name": "Laziz",
          "username": "laz_1z",
          "language_code": "uz"
        },
        "chat": {
          "id": 6345124148,
          "first_name": "Laziz",
          "username": "laz_1z",
          "type": "private"
        },
        "date": 1770298410,
        "text": "/start",
        "entities": [
          {
            "offset": 0,
            "length": 6,
            "type": "bot_command"
          }
        ]
      }
    }
  ]
}


updates = []
for data in result['result']:
    updates.append(Update(data))

print(updates)

# print(simplegram.__version__)
