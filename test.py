class Humano:
    def __init__(self, age):
        self.age = age

    def __repr__(self):
        return f"{self.age}"

humano = Humano(20)

print(humano)

# testing worked
