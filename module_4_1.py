from fake_math import divide as F_M_divide
from true_math import divide as T_M_divide

print(F_M_divide(125, 5))
print(F_M_divide(125, 0))
print(T_M_divide(125, 5))
print(T_M_divide(125, 0))

