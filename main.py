#coding=UTF-8
__author__ = 'msemenov'

'''
ID Name isWater Neighbors
'''

class Location:
    def __init__(self, ID, name, isWater, Neighbors):
        self.ID = ID
        self.name = name
        self.isWater = isWater
        self.neighbors = Neighbors
    def __str__(self):
        return self.name

locations = [
    Location(0,  "Северный Тихий Океан", True, [1, 2, 4, 8, 9, 11, 10, 52, 54 ]),
    Location(1,  "Аляска", False, [0, 2]),
    Location(2,  "Канада", False, [0, 1, 3, 4, 5, 7, 18]),
    Location(3,  "Квебек", False, [2, 7, 18]),
    Location(4,  "Сан-Франциско", False, [0, 2, 5, 6, 8]),
    Location(5,  "Чикаго", False, [2, 4, 6, 7]),
    Location(6,  "Хьюстон", False, [4, 5, 7, 8, 9]),  #check
    Location(7,  "Нью-Йорк", False, [2, 3, 5, 6, 18]),
    Location(8,  "Мексика", False, [0, 4, 6, 9, 11]),
    Location(9,  "Карибское море", True, [18, 6, 8, 0, 11, 14, 16, 20, 19]),
    Location(10, "Южный Тихий Океан", True, [54, 58, 0, 12, 13, 20]),
    Location(11, "Колумбия", False, [0, 8, 9, 14, 12]),
    Location(12, "Перу", False, [10, 13, 15, 14, 11]),
    Location(13, "Аргентина", False, [12, 10, 20, 17, 15]),
    Location(14, "Манаус", False, [11, 12, 15, 16, 9]),
    Location(15, "Бразилиа", False, [14, 12, 13, 17, 16]),
    Location(16, "Фортапеза", False, [9, 14, 15, 17]),
    Location(17, "Рио-де-Жанейро", False, [16, 15, 13, 20]),
    Location(18, "Северная Атлантика", True, [2, 3, 7, 9, 19, 27, 26, 25, 23, 21, 22, 33]),
    Location(19, "Гвинейский залив", True, [18, 9, 20, 42, 31, 30, 28, 27]),
    Location(20, "Южная Атлантика", True, [9, 17, 13, 10, 42, 19]),
    Location(21, "Лондон", False, [18]),
    Location(22, "Берлин", False, [18, 23, 24, 32, 33]),
    Location(23, "Париж", False, [18, 25, 24, 22]),
    Location(24, "Рим", False, [22, 23, 25, 38, 32]),
    Location(25, "Средиземное море", True, [24, 23, 18, 26, 42, 41, 38]),
    Location(26, "Северная Африка", False, [25, 18, 27, 28, 29, 42, 41]),
    Location(27, "Гвинея", False, [18, 19, 28, 26]),
    Location(28, "Нигерия", False, [26, 27, 19, 30, 29]),
    Location(29, "Восточная Африка", False, [26, 28, 30, 31, 42]),  #check
    Location(30, "Конго", False, [28, 19, 31, 29]),
    Location(31, "ЮАР", False, [30, 19, 42, 29]),
    Location(32, "Украина", False, [22, 24, 34, 33]),
    Location(33, "Мурманск", False, [18, 22, 32, 34, 35]),
    Location(34, "Москва", False, [33, 32, 38, 40, 37, 35]),
    Location(35, "Новосибирск", False, [33, 34, 37, 61, 36]),
    Location(36, "Владивосток", False, [35, 61, 44, 51, 52]),
    Location(37, "Казахстан", False, [35, 34, 39, 43, 61]),
    Location(38, "Турция", False, [34, 24, 25, 41, 40]),
    Location(39, "Афганистан", False, [37, 40, 48, 47, 43]),
    Location(40, "Иран", False, [34, 38, 41, 42, 48, 39]),
    Location(41, "Ближний Восток", False, [38, 25, 26, 42, 40]),
    Location(42, "Индийский Океан", True, [40, 41, 25, 26, 29, 31, 19, 20, 58, 57, 54, 55, 49, 50, 48]),
    Location(43, "Урумчи", False, [37, 39, 47, 49, 45, 44, 61]),
    Location(44, "Пекин", False, [36, 61, 43, 45, 46, 54, 51]),
    Location(45, "Чунцинь", False, [43, 49, 55, 46, 44]),
    Location(46, "Шанхай", False, [44, 45, 55, 54]),
    Location(47, "Нью-Дели", False, [43, 39, 48, 49]),
    Location(48, "Мумбаи", False, [47, 39, 40, 42, 50, 49]),
    Location(49, "Калькутта", False, [43, 47, 48, 50, 42, 55, 45]), #check
    Location(50, "Ченнай", False, [49, 48, 42]),
    Location(51, "Корея", False, [36, 44, 54, 52]),
    Location(52, "Японское море", True, [0, 36, 51, 53, 54]),
    Location(53, "Япония", False, [52]),
    Location(54, "Китайское море", True, [0, 10, 52, 51, 44, 46, 42, 55, 56, 57, 58]),
    Location(55, "Индокитай", False, [45, 49, 42, 54, 46]),
    Location(56, "Филлипины", False, [54]),
    Location(57, "Индонезия", False, [42, 54, 58]),
    Location(58, "Тасманское море", True, [10, 54, 57, 42, 59, 60]),
    Location(59, "Австралия", False, [58]),
    Location(60, "Новая Зеландия", False, [58]),
    Location(61, "Монголия", False, [35, 37, 43, 44, 36])
]

def checkLocationsForInconsistency():
    for location in locations:
        for neighbor in location.neighbors:
            if  location.ID not in locations[neighbor].neighbors:
                print location.Name + " " + locations[neighbor].Name


class Stock:
    def __init__(self, country, income, cost):
        self.country = country
        self.income = income
        self.cost = cost
    def __str__(self):
        return self.country.name + " " + str(self.income) + " " + str(self.cost)

class Factory:
    def __init__(self, location, type, exists):
        self.location = locations[location]
        self.type = type
        self.exists = exists
    def __str__(self):
        if self.exists:
            if self.type == 0:
                return self.location.name + " " + "Завод"
            else:
                return self.location.name + " " + "Порт"
        return None


class Country:
    def __init__(self, name, mainLocations, factories):
        self.name = name
        self.mainLocations = mainLocations
        self.factories = factories
        self.army = []
        self.fleet = []
        self.money = 0
        self.slaveLocations = []
        self.stocks = [
            Stock(self, 1, 2),
            Stock(self, 2, 4),
            Stock(self, 3, 6),
            Stock(self, 4, 9),
            Stock(self, 5, 12),
            Stock(self, 6, 16),
            Stock(self, 7, 20),
            Stock(self, 8, 25),
            Stock(self, 9, 30)
        ]
    def __str__(self):
        ret = self.name + "\nДеньги: " + str(self.money) + "\nМетрополия: "
        for location in self.mainLocations:
            ret += location.name + " "
        ret += "\nФабрики: "
        for factory in self.factories:
            if factory.exists:
                ret += str(factory) + " "
        ret += "\nАрмия: "
        for tank in self.army:
            ret += locations[tank].name
        ret += "\nФлот: "
        for ship in self.fleet:
            ret += locations[ship].name
        ret += "\nТерритории: "
        for location in self.slaveLocations:
            ret += location.name + " "
        ret += "\nСвободные облигации: "
        for stock in self.stocks:
            ret += str(stock) + " "
        ret += "\n"
        return ret


countries = [
    Country(
        "Россия",
        [locations[33], locations[34], locations[35], locations[36]],
        [
            Factory(33, 1, False),
            Factory(34, 0, True),
            Factory(35, 0, False),
            Factory(36, 1, True),
        ]
    ),
    Country(
        "Китай",
        [locations[43], locations[44], locations[45], locations[46]],
        [
            Factory(43, 0, False),
            Factory(44, 0, True),
            Factory(45, 0, False),
            Factory(46, 1, True),
        ]
    ),
    Country(
        "Индия",
        [locations[47], locations[48], locations[49], locations[50]],
        [
            Factory(47, 0, True),
            Factory(48, 1, True),
            Factory(49, 1, False),
            Factory(50, 0, False),
        ]
    ),
    Country(
        "Бразилия",
        [locations[14], locations[15], locations[16], locations[17]],
        [
            Factory(14, 0, False),
            Factory(15, 0, True),
            Factory(16, 1, False),
            Factory(17, 1, True),
        ]
    ),
    Country(
        "США",
        [locations[4], locations[5], locations[6], locations[7]],
        [
            Factory(4, 1, False),
            Factory(5, 0, True),
            Factory(6, 1, True),
            Factory(7, 1, False),
        ]
    ),
    Country(
        "Европа",
        [locations[21], locations[22], locations[23], locations[24]],
        [
            Factory(21, 1, True),
            Factory(22, 0, False),
            Factory(23, 0, True),
            Factory(24, 1, False),
        ]
    )
]

class Player:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.stocks = []
    def buyStock(self, country, stockIncome):   #TBD: if not?
        for i in range(len(country.stocks)):
            if country.stocks[i].income == stockIncome:
                costToPay = country.stocks[i].cost
                if self.money >= costToPay:
                    self.money -= costToPay
                    self.stocks.append(country.stocks.pop(i))
                return
    def exchangeStock(self, country, stockIncomeOld, stockIncomeNew): #TBD: if not possible
        if stockIncomeOld < stockIncomeNew:
            for i in range(len(self.stocks)):
                if self.stocks[i].income == stockIncomeOld:
                    for j in range(len(country.stocks)):
                        if country.stocks[j].income == stockIncomeNew:
                            costToPay = country.stocks[j].cost - self.stocks[i].cost
                            if self.money >= costToPay:
                                self.money -=costToPay
                                self.stocks[i], country.stocks[j] = country.stocks[j], self.stocks[i]
                                return
    def __str__(self):
        ret = self.name + "\nДеньги: " + str(self.money) + "\nОблигации:\n"
        for stock in self.stocks:
            ret += str(stock) + "\n"
        return ret

a = Player("Player1", 30)
a.buyStock(countries[0], 4)
a.buyStock(countries[2], 1)
a.exchangeStock(countries[0], 4, 5)
a.exchangeStock(countries[0], 5, 8)
print str(a)
print str(countries[0])
print str(countries[2])