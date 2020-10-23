# put your python code here

class_1 = abs(int(input()))
class_2 = abs(int(input()))
class_3 = abs(int(input()))

class_1_desks = int(class_1 / 2) + int(class_1 % 2)
class_2_desks = int(class_2 / 2) + int(class_2 % 2)
class_3_desks = int(class_3 / 2) + int(class_3 % 2)

desks = int(class_1_desks + class_2_desks + class_3_desks)
print(desks)
