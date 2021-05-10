from Skymaster import *


obj = Aircraft.fromjsonfile()
front_engine = Engine("IO-360", shaft_power=1570, eta_prop=0.615)
rear_engine = Engine("IO-360", shaft_power=1570, eta_prop=0.615)

obj.add_forward_engine(front_engine)
obj.add_rear_engine(rear_engine)

print(f'CDO estimation = {obj.get_CD0("top speed 1")}')
print(f'CDO estimation = {obj.get_CD0("top speed 2")}')

