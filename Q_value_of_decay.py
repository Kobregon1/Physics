A = float(input('Parent A value= '))
Z = float(input('Parent Z protons= '))

N = float(A - Z)

A1 = float(input('Product A value= '))

Z1 = float(input('Product Z protons= '))

N1 = float(A1 - Z1)

# Multiply by A to get keV then divide by 1000.0 to get MeV
BE_data = float(input('BE of parent from data (keV)=')) * (A / 1000.0)
BE_data = BE_data / 931.5  # Divide by 931.5 MeV to get a.m.u
print(BE_data)

# Multiply by A to get keV then divide by 1000.0 to get MeV
BE_data1 = float(input('BE of product from data (keV)=')) * (A1 / 1000.0)
BE_data1 = BE_data1 / 931.5  # Divide by 931.5 MeV to get a.m.u
print (BE_data1)
mp = 1.007300054
me = 5.485775631E-4
mn = 1.008665

def MassX(Z,N):
    MassX = (Z * (mp + me)) + (N * (mn)) - BE_data
    return MassX
print('Parent Mass= ', MassX(Z,N), 'u')

def MassY(Z1, N1):
    MassY = (Z1 * (mp + me)) + (N1 * (mn)) - BE_data1
    return MassY
print('Product Mass= ', MassY(Z1,N1), 'u')

Q = MassX(Z,N) - MassY(Z1,N1) - 4.008267248782268
print('Reaction Q value(u)= ', Q, 'u')
print('Reaction Q value(MeV)= ', Q * 931.5, 'MeV')

if Q > 0.0:
    print('- Exothermic reaction \n- Decay can occur')
else:
    print('- Endothermic reaction \n- Decay cannot occur')