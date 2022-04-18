class Car:
	def __init__(self, name: str, model: str,  vin: str):
		self.model = model
		self.name = name
		self.vin = vin


class Human:

	def __init__(self, name: str, age: int, current_car: Car, cars: list):
		self.name = name
		self.age = age
		self.current_car = current_car
		self.cars = cars


cars = [
	Car('Beetle', 'Volkswagen', 'A34251B'),
	Car('Belete', 'Volkswagen', '31A1B45'),
	Car('Bteele', 'Volkswagen', '5B214A3'),
	Car('Betele', 'Volkswagen', '12AB534'),
	Car('Beleet', 'Volkswagen', '352AB14'),
	Car('Lteebe', 'Volkswagen', '41B52A3'),
	Car('Btleee', 'Volkswagen', 'A12354B'),
	Car('Tlebee', 'Volkswagen', 'BA24315'),
	Car('Ebleet', 'Volkswagen', '45132BA'),
	Car('Tbelee', 'Volkswagen', 'A2B1345'),
	Car('Eleetb', 'Volkswagen', '2B54A31')
]

vitalik = Human('Vitalik', 49)
