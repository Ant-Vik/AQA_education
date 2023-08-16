from hooch__city_class import City


def apartment_address():
    kyiv = City("Київ", "Хрещатик", "1", "10")
    lviv = City("Львів", "Площадна", "33", "77")
    odessa = City("Одеса", "Деребасівська", "112", "107")

    cities = [kyiv, lviv, odessa]

    for city in cities:
        address = city.get_address()
        print(address)


if __name__ == "__main__":
    apartment_address()