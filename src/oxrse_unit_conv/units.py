from si import *
from meta.classes import Unit

# second
minute = Unit(name='minute', abbr='min', si=second, to_si_fun=lambda n: n * 60)
# min shadows the builtin function 'min'

hour = Unit(name='hour', abbr='h', si=second, to_si_fun=lambda n: n * 3600)
h = hour

# meter
kilometer = Unit(name='kilometer', abbr="km", si=meter, to_si_fun=lambda n: n * 1000)
km = kilometer

mile = Unit(name='mile', abbr='mile', si=meter, to_si_fun=lambda n: n * 1_609.344)

lightyear = Unit(name='lightyear', abbr='ly', si=meter, to_si_fun=lambda n: n*9.4607305e15)

# meter_sq
meter_sq = Unit(name='meter_sq', abbr='m2', si=meter, to_si_fun=lambda n: n * n, from_si_fun=lambda n: n ** 0.5)
m2 = meter_sq

# meter_cu

# kilogram

pound = Unit(name='pound', abbr='lb', si=kilogram, to_si_fun=lambda n: n * 0.4535924)
lb = pound

# ampere

# kelvin

# mole

# candela
