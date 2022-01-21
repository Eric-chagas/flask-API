from flask_restful import Resource

HotelList = [
    {'Hotel_id': 0,
     'name': 'Gran Hotel',
     'stars': 3.5,
     'dailyFee': 245,
     'city': 'Los Angeles'
     },
    {'Hotel_id': 1,
     'name': 'Minor Hotel',
     'stars': 5,
     'dailyFee': 1200,
     'city': 'Springfield'
     },
    {'Hotel_id': 2,
     'name': 'My Own Private',
     'stars': 1.3,
     'dailyFee': 12,
     'city': 'Idaho'
     },
    {'Hotel_id': 3,
     'name': 'Roam if you want to',
     'stars': 2.8,
     'dailyFee': 100,
     'city': 'Connecticut'
     }
]


class Hotels(Resource):
    def get(self):
        return {'hotels': HotelList}
