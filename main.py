import datetime

import requests

from settings import headers
from user.urls import user_info
from box import Box, BaseBox


box_info = BaseBox()
avalible_boxes = box_info.get_avalible_boxes()
box_info.log_info_boxes(avalible_boxes)


selected_box = str(input('\nНомер коробки: '))
amount_boxes = int(input('\nКоличество коробок (1-20): '))

product_id = avalible_boxes[selected_box]['product_id']
box = Box(product_id=product_id, amount=amount_boxes)


#################################################
# ToDo: Refactoring (Вынести в отдельную функцию)
response = requests.post(user_info, headers=headers)

if response.status_code == 200:
    print('Successfully connected')
else:
    print('Something wrong...')
    print('Check please: COOKIE, CSRFTOKEN, headers')



start_sale = box._get_box_info['startTime']
start_sale = datetime.datetime.fromtimestamp(start_sale/1000)

# ToDo: async
while True:
    current_time = datetime.datetime.today()

    if start_sale <= current_time:
        print('Start buying')
        while True:
            response = box._buy_box
            print(response)


#################################################
# ToDo: Tests
