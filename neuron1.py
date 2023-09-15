import sys
membrane_potential = float(sys.argv[1])
if membrane_potential >= float(-65):
    print(5)
else:
    print(0)
    