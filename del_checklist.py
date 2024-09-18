#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests, os
from dotenv import load_dotenv

load_dotenv()

backend = os.environ['BACKEND']
user_uuid = os.environ['USER-UUID']
rooms = ["0XtSpWAOrFXB2sx_%24CikW2",    #1.6 Санузел                /Дом Березина
         "0LCyWq$CD2dxc3fJg$tU$h",      #1 Помещение                /small_test
         "0XtSpWAOrFXB2sx_$CikXn",      #2.8 Офисное помещение 11   /Дом Березина
         "0XtSpWAOrFXB2sx_$CikWC",      #1.3 фисное помещение 3     /Дом Березина
         "0XtSpWAOrFXB2sx_$CikW0",      #1.7 Коридор                /Дом Березина
         "1TkuumuDX8yBoa6oe35u6L"]      #0.15 Коридор               /Дом Березина

def get_room_uuid(room_uuid):
    url_get = f"{backend}room_checklist?roomUuid={room_uuid}"

    response = requests.get(url_get)
    print(response.url, response.status_code)
    content = response.json()['content']
    res = [sub['uuid'] for sub in content]
    uuid = str(*res)
    return uuid

def delete_room_checklist(checklist_uuid):
    if checklist_uuid:
        url = f"{backend}room_checklist/{checklist_uuid}"
        headers = {
            'user-uuid': user_uuid,
        }

        response = requests.delete(url=url, headers=headers)
        return response.status_code
    return

def clean_room_checklists():
    for u in rooms:
        checklist_uuid = get_room_uuid(u)
        delete_room_checklist(checklist_uuid)
    return "Cleaned"




