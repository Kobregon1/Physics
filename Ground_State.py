# This code will calculate the ground state for the harmonic oscillator

# import libraries to get the symbol for pi in unicode
import sys
sys.getdefaultencoding()
print("Nuclear Calculation Input:")

# User input of A, Z, then calculates N (NOTE: all will be integers values)
A = int(input('A= '))
Z = int(input('Z= '))

# Determining that Z is an element, so Z > 0
if Z > 0:
    N = A - Z
    print('N=', N)
else:
    print("ERROR: Z must be greater than 0")
print()

'''
-Create a dictionary for l value A.K.A a dictionary data structure
-Analogy: l is a 'door' and it contains 'keys' & each 'key' has a 'value' or 'name' (A.K.A string)
-Helpful for when determining parity
'''
l = {'s': 0,
     'p': 1,
     'd': 2,
     'f': 3,
     'g': 4}

# Create dictionary for orbitals values
# Helpful when determining ground state
orbital = {'s1/2': '1/2',
           'p3/2': '3/2',
           'p1/2': '1/2',
           'd5/2': '5/2',
           'f7/2': '7/2',
           'g9/2': '9/2'}
'''
-Determine parity based of whether l values are odd or even when divisible by 2
-Divisible is represented by %
-If a value is divisible by 2 that means there is no remainder so value % 2 = 0, hence 0 == 0 is true, and it is even
-Otherwise, it is odd
'''

for value in l.values():
    if value % 2 == 0:
        parity_even = '+'  # s, d, g orbitals
    elif value % 2 == 1:
        parity_odd = '-'  # p, f, h orbitals
    else:
        print("ERROR")


'''
Recall the 2 rules for ground state (J^pi):
1) if even Z and even N then J= 0 pi = +
2) if A is odd J^pi gets the LAST ODD j^pi ground state
'''

# Finding J involves having iterations for both Z and N
print("Winner:")
if Z % 2 == 1:
    winner = Z
    loser = N
    print("* PROTON", "\n* Z =", winner)
elif N % 2 == 1:
    winner = N
    loser = Z
    print("* NEUTRON", "\n* N =", winner)
elif Z % 2 == 1 and N % 2 == 1:
    print("ERROR: Z, N Both odd")
else:
    winner = A - Z - N
    loser = A - Z - N
    print("* No Winner")
    print('* J=', 0, '\u03C0=', parity_even) if Z % 2 == 0 and N % 2 == 0 else None
print()
print('Last Odd Ground State:') if Z % 2 == 1 or N % 2 == 1 else None

# s1/2 orbital: 2
if 0 < winner <= 2:
    s = orbital['s1/2']
    print('* J=', s, '\u03C0=', parity_even)
    print('* s1/2 orbital:', winner, 'Protons') if Z % 2 == 1 else None
    print('* s1/2 orbital:', winner, 'Neutrons') if N % 2 == 1 else None
    winner = winner - 2
else:
    print('* s1/2 orbital filled') if winner > 2 else None
    winner = winner - 2

# p3/2 orbital: 4
if 0 < winner <= 4:
    p = orbital['p3/2']
    print('* J=', p, '\u03C0=', parity_odd)
    print('* p3/2 orbital:', winner, 'Protons') if Z % 2 == 1 else None
    print('* p3/2 orbital:', winner, 'Neutrons') if N % 2 == 1 else None
    winner = winner - 4
else:
    print('* p3/2 orbital filled') if winner >= 4 else None
    winner = winner - 4

# p1/2 orbital: 2
if 0 < winner <= 2:
    p = orbital['p1/2']
    print('* J=', p, '\u03C0=', parity_odd)
    print('* p1/2 orbital:', winner, 'Protons') if Z % 2 == 1 else None
    print('* p1/2 orbital:', winner, 'Neutrons') if N % 2 == 1 else None
    winner = winner - 2
else:
    print('* p1/2 orbital filled') if winner >= 2 else None
    winner = winner - 2

# d5/2 orbital: 6
if 0 < winner <= 6:
    d = orbital['d5/2']
    print('* J=', d, '\u03C0=', parity_even)
    print('* d5/2 orbital:', winner, 'Protons') if Z % 2 == 1 else None
    print('* d5/2 orbital:', winner, 'Neutrons') if N % 2 == 1 else None
    winner = winner - 6
else:
    print('* d5/2 orbital filled') if winner >= 6 else None
    winner = winner - 6

# f7/2 orbital: 8
if 0 < winner <= 8:
    f = orbital['f7/2']
    print('* J=', f, '\u03C0=', parity_odd)
    print('* f7/2 orbital:', winner, 'Protons') if Z % 2 == 1 else None
    print('* f7/2 orbital:', winner, 'Neutrons') if N % 2 == 1 else None
    winner = winner - 8
else:
    print('* f7/2 orbital filled') if winner >= 8 else None
    winner = winner - 8

# g9/2 orbital: 10
if 0 < winner <= 10:
    g = orbital['g9/2']
    print('* J=', g, '\u03C0=', parity_even)
    print('* g9/2 orbital:', winner, 'Protons') if Z % 2 == 1 else None
    print('* g9/2 orbital:', winner, 'Neutrons') if N % 2 == 1 else None
    winner = winner - 10
else:
    print('* g9/2 orbital filled') if winner >= 10 else None
    winner = winner - 10

print()

# For losing/even state
# Chooses proton state if neutrons wins, chooses neutron state is proton wins
print('-------Proton State-------') if N % 2 == 1 else None
print('-------Neutron State-------') if Z % 2 == 1 else None

# s1/2 orbital: 2
if 0 < loser < 2:
    print('* s1/2 orbital:', loser, 'Protons') if N % 2 == 1 else None
    print('* s1/2 orbital:', loser, 'Neutrons') if Z % 2 == 1 else None
    loser = loser - 2
else:
    print('* s1/2 orbital filled') if loser >= 2 else None
    loser = loser - 2

# p3/2 orbital: 4
if 0 < loser < 4:
    print('* p3/2 orbital:', loser, 'Protons') if N % 2 == 1 else None
    print('* p3/2 orbital:', loser, 'Neutrons') if Z % 2 == 1 else None
    loser = loser - 4
else:
    print('* p3/2 orbital filled') if loser >= 4 else None
    loser = loser - 4

# p1/2 orbital: 2
if 0 < loser < 2:
    print('* p1/2 orbital:', loser, 'Protons') if N % 2 == 1 else None
    print('* p1/2 orbital:', loser, 'Neutrons') if Z % 2 == 1 else None
    loser = loser - 2
else:
    print('* p1/2 orbital filled') if loser >= 2 else None
    loser = loser - 2

# d5/2 orbital: 6
if 0 < loser < 6:
    print('* d5/2 orbital:', loser, 'Protons') if N % 2 == 1 else None
    print('* d5/2 orbital:', loser, 'Neutrons') if Z % 2 == 1 else None
    loser = loser - 6
else:
    print('* d5/2 orbital filled') if loser >= 6 else None
    loser = loser - 6

# f7/2 orbital: 8
if 0 < loser < 8:
    print('* f7/2 orbital:', loser, 'Protons') if N % 2 == 1 else None
    print('* f7/2 orbital:', loser, 'Neutrons') if Z % 2 == 1 else None
    loser = loser - 8
else:
    print('* f7/2 orbital filled') if loser >= 8 else None
    loser = loser - 8

# g9/2 orbital: 10
if 0 < loser < 10:
    print('* g9/2 orbital:', loser, 'Protons') if N % 2 == 1 else None
    print('* g9/2 orbital:', loser, 'Neutrons') if Z % 2 == 1 else None
    loser = loser - 10
else:
    print('* g9/2 orbital filled') if loser >= 10 else None
    loser = loser - 10
