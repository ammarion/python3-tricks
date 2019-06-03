def describe_pet(pet_name, animal_type='dog'):
    print(f"I have {pet_name} he is a {animal_type}")


describe_pet('willie')
describe_pet(pet_name='willie')
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')

