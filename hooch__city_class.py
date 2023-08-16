class City:
    def __init__(self, city, street, house, apartment):
        self.city = city
        self.street = street
        self.house = house
        self.apartment = apartment

    def get_address(self):
        return f"{self.city}, вулиця {self.street}, будинок {self.house}, квартира {self.apartment}"


# test = City('Kyiv', 'Vasilkivska', 100, 77)
# print(test.get_address())