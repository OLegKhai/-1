class Cat:
    def __init__(self, name, breed, color, age, weight, category):
        self.name = name
        self.breed = breed
        self.color = color
        self.age = age
        self.weight = weight
        self.category = category
    
    def get_info(self):
        return f"Cat({self.name}, {self.breed}) - {self.color}, {self.age} years old, {self.weight} kg"
    
    def get_message(self):
        if self.age < 0.5:
            age_category = "Кошеня"
        elif self.age < 2:
            age_category = "Підліток"
        elif self.age < 10:
            age_category = "Доросла"
        elif self.age < 14:
            age_category = "Літка"
        else:
            age_category = "Дуже літня"
        
        if self.category == "короткошерстий":
            category_desc = "короткошерстий"
        else:
            category_desc = "довгошерстий"
        
        return f'"{age_category} {self.name} породи {self.breed}, що відноситься до {self.category} пород", ' \
               f'"{self.age} years old and weighs {self.weight} kg, has {self.color} color"'
cat1 = Cat("Барсик", "Персидська", "білий", 0.3, 1.5, "довгошерстий")
cat2 = Cat("Мурзик", "Сіамська", "сіра", 3, 4, "короткошерстий")
cat3 = Cat("Вася", "Мейн-кун", "плямистий", 10, 7, "довгошерстий")

print(cat1.get_info())
print(cat1.get_message())

print(cat2.get_info())
print(cat2.get_message())

print(cat3.get_info())
print(cat3.get_message())
