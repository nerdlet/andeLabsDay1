#create a car class

class Car(object):

 def __init__(self, name='General', model='GM', vehicle_type=None, speed = 0):
  self.name = name
  self.model = model
  self.vehicle_type = vehicle_type
  self.speed = 0

#check numb of doors depending on the name of car

  if (name=='Porshe') or (name =='Koenigsegg'):
            self.num_of_doors = 2
  else:
            self.num_of_doors = 4

#check nuumber of wheels depending on vehicletype

  if vehicle_type == 'trailer':
            self.num_of_wheels = 8
  else:
            self.num_of_wheels = 4

#If car is not trailer then it is a saloon
def is_saloon(self):
    if self.vehicle_type !='trailer':
        self.vehicle_type =='saloon'
        return True
    return False


       

