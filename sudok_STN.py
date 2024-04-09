import math
import cmath
import itertools

# Sudok
U_f = 110e3/math.sqrt(3)  # modul fazoveho napatia vo V
h_1 = 9.83  # ekvivalentna vyska fazoveho vodica nad zemou v m
h_2 = 17.43
h_3 = 13.63
r_ed = 0.0144 # polomer fazoveho vodica v m
a_1 = 2.7  # vodorovna vzájomná vzdialenosť fázového vodiča a telekom. vodiča v m,  stredny fazovy vodic
a_2 = 2.7  # vodic blizsie ku telekom. vodicu
a_3 = 3.5   # vzdialenejsi od telekom vodica
d_12 = math.sqrt((abs(h_2-h_1))**2 + (abs(a_2-a_1))**2) # vzdialenost medzi fazovymi vodicmi v m
d_23 = math.sqrt((abs(h_2-h_3))**2 + (abs(a_3-a_2))**2)
d_13 = math.sqrt((abs(h_3-h_1))**2 + (abs(a_3-a_1))**2)
b = 21.93  # výška telekom. vodiča nad zemnou v m
l_i = 1   # dĺžka telekom. vodica vo vypoctovom useku v km
l_v = 1  # celková dĺžka telekom. vodica  v km
q = 1 # vysledny cinitel tienenia
n = 0 # počet uzemnených vodičov telekom. vedenia

k_1 = math.log((2*h_1)/r_ed)
k_2 = math.log((2*h_2)/r_ed)
k_3 = math.log((2*h_3)/r_ed)
k = (k_1+k_2+k_3)/3
k_c1 = math.log( (math.sqrt((2*h_1)**2 + d_12**2)) / d_12)
k_c2 = math.log( (math.sqrt((2*h_2)**2 + d_23**2)) / d_23)
k_c3 = math.log( (math.sqrt((2*h_3)**2 + d_13**2)) / d_13)
k_c = (k_c1+k_c2+k_c3)/3
k_a1 = math.log( (math.sqrt(a_1**2 + (h_1+b)**2)) / (math.sqrt(a_1**2 + (h_1-b)**2)))
k_a2 = math.log( (math.sqrt(a_2**2 + (h_2+b)**2)) / (math.sqrt(a_2**2 + (h_2-b)**2)))
k_a3 = math.log( (math.sqrt(a_3**2 + (h_3+b)**2)) / (math.sqrt(a_3**2 + (h_3-b)**2)))

# Upravena STN
U_A_real = (U_f/(k-k_c))* (-k_a1 + 1/2*(k_a2+k_a3))
U_A_imag = (U_f/(k-k_c))* ((math.sqrt(3)/2*(k_a2-k_a3)))
U_v = complex(U_A_real, U_A_imag)
amplituda = abs(U_v)
uhol_v_rad = cmath.phase(U_v)
uhol_v_stupnoch = math.degrees(uhol_v_rad)
#U_A_i = (U_f/(k-k_c))* (-k_a1 + 1/2*(k_a2+k_a3) + (math.sqrt(3)/2*(k_a2-k_a3)))
#U_A = abs(U_A_i*l_i)*(q/l_v)
print('Napätie pre upravenu STN je: {} ∠ {} '.format(amplituda, uhol_v_stupnoch))
I= 5.7E-3 * ((abs(U_v)*l_v)/(n+2))
print('Prúd pre upravenu STN je {}'.format(I))


# STN povodna
U_A_real = (U_f/(k+k_c))* (-k_a1 + 1/2*(k_a2+k_a3))
U_A_imag = (U_f/(k+k_c))* ((math.sqrt(3)/2*(k_a2-k_a3)))
U_v = complex(U_A_real, U_A_imag)
amplituda = abs(U_v)
uhol_v_rad = cmath.phase(U_v)
uhol_v_stupnoch = math.degrees(uhol_v_rad)
#U_A_i = (U_f/(k-k_c))* (-k_a1 + 1/2*(k_a2+k_a3) + (math.sqrt(3)/2*(k_a2-k_a3)))
#U_A = abs(U_A_i*l_i)*(q/l_v)
print('Napätie pre povodnu STN je: {} ∠ {} '.format(amplituda, uhol_v_stupnoch))
I= 5.7E-3 * ((abs(U_v)*l_v)/(n+2))
print('Prúd pre povodnu STN je {}'.format(I))

# Nezmyselna varianta
# U_A_real = (U_f/(k+k_c))* (-k_a1 + 1/2*(k_a2-k_a3))
# U_A_imag = (U_f/(k+k_c))* ((math.sqrt(3)/2*(k_a2-k_a3)))
# U_v = complex(U_A_real, U_A_imag)
# amplituda = abs(U_v)
# uhol_v_rad = cmath.phase(U_v)
# uhol_v_stupnoch = math.degrees(uhol_v_rad)
# #U_A_i = (U_f/(k-k_c))* (-k_a1 + 1/2*(k_a2+k_a3) + (math.sqrt(3)/2*(k_a2-k_a3)))
# #U_A = abs(U_A_i*l_i)*(q/l_v)
# print('Napätie pre nezmyselnu variantu je: {} ∠ {} '.format(amplituda, uhol_v_stupnoch))


# Povodna kniha
U_A_real = (U_f/(k-k_c))* (-k_a1 + 1/2*(k_a2+k_a3))
U_A_imag = (U_f/(k-k_c))* ((math.sqrt(3)/2*(k_a2+k_a3)))
U_v = complex(U_A_real, U_A_imag)
amplituda = abs(U_v)
uhol_v_rad = cmath.phase(U_v)
uhol_v_stupnoch = math.degrees(uhol_v_rad)
#U_A_i = (U_f/(k-k_c))* (-k_a1 + 1/2*(k_a2+k_a3) + (math.sqrt(3)/2*(k_a2-k_a3)))
print('Napätie pre variant  z knihy je: {} ∠ {} '.format(amplituda, uhol_v_stupnoch))

# ITU metoda priemeru D a d
hx = (h_1*h_2*h_3) ** (1/3)
rx = (r_ed*d_12*d_23*d_13) ** (1/9)
D_1T = math.sqrt(a_1**2+(h_1+b)**2)
D_2T = math.sqrt(a_2**2+(h_2+b)**2)
D_3T = math.sqrt(a_3**2+(h_3+b)**2)
Dx = (D_1T*D_2T*D_3T) ** (1/3)
d_1T = math.sqrt(a_1**2+(h_1-b)**2)
d_2T = math.sqrt(a_2**2+(h_2-b)**2)
d_3T = math.sqrt(a_3**2+(h_3-b)**2)
dx = (d_1T*d_2T*d_3T) ** (1/3)
n_a= math.log(math.sqrt(Dx/dx))
g= 1 / math.log((2*hx)/rx)
U_j = n_a * g * U_f
print('ITU  metodou priemeru  D, d a nasledneho vypoctu n_aje {}'.format(U_j))

#ITU metoda priemeru a, h
hx = (h_1*h_2*h_3) ** (1/3)
rx = (r_ed*d_12*d_23*d_13) ** (1/3)
ax = (a_1*a_2*a_3) ** (1/3)
n_a = math.log(math.sqrt(ax**2+(hx+b)**2)/math.sqrt(ax**2+(hx-b)**2))
g = 1 / math.log((2*hx)/rx)
U_jx = n_a * g * U_f
U_dlh= (n_a/ math.log((2*hx)/rx)) * U_f #odvodeny dlhsi vzorec
print('ITU metodou priemeru a, h a nasledneho vypoctu n_a  je {}'.format(U_jx))

#Nezatazene potrubie 1. Vzorec CIGRE sudok
d_1p = math.sqrt(2.7**2+12.1**2)
d_2p = math.sqrt(3.5**2+8.3**2)
d_3p = math.sqrt(2.7**2+4.5**2)
A_1p = 9.83 / d_1p**2
A_2p = 13.63 / d_2p**2
A_3p = 17.43 / d_3p**2
V_op_real= 0.25 * 110 *21.93 * (A_1p - 0.5*(A_2p+A_3p))
V_op_imag= 0.25 * 110 *21.93 * (math.sqrt(3)/2*(A_2p-A_3p))
V_op = complex(V_op_real, V_op_imag)
amplituda = abs(V_op)
uhol_v_rad = cmath.phase(V_op)
uhol_v_stupnoch = math.degrees(uhol_v_rad)
print('Napätie pre CIGRE 1. sudok variant je: {} ∠ {} '.format(amplituda, uhol_v_stupnoch))

#variatnt 1.1
D_1T = math.sqrt(a_1**2+(h_1+b)**2)
D_2T = math.sqrt(a_2**2+(h_2+b)**2)
D_3T = math.sqrt(a_3**2+(h_3+b)**2)

d_1T = math.sqrt(a_1**2+(h_1-b)**2)
d_2T = math.sqrt(a_2**2+(h_2-b)**2)
d_3T = math.sqrt(a_3**2+(h_3-b)**2)

FAZ_1 = (math.log(D_1T/d_1T))/(math.log((2*h_1)/r_ed))
FAZ_2 = (math.log(D_2T/d_2T))/(math.log((2*h_2)/r_ed))
FAZ_3 = (math.log(D_3T/d_3T))/(math.log((2*h_3)/r_ed))
U_j= FAZ_1+FAZ_2+FAZ_3  * U_f

print('CiGRE  variant 1.1 sudok je {}'.format(U_j))

#variatnt 1.2
D_1T = math.sqrt(a_1**2+(h_1+b)**2)
D_2T = math.sqrt(a_2**2+(h_2+b)**2)
D_3T = math.sqrt(a_3**2+(h_3+b)**2)

d_1T = math.sqrt(a_1**2+(h_1-b)**2)
d_2T = math.sqrt(a_2**2+(h_2-b)**2)
d_3T = math.sqrt(a_3**2+(h_3-b)**2)

FAZ_1 = (math.log(D_1T/d_1T))/(math.log((2*h_1)/r_ed))
FAZ_2 = (math.log(D_2T/d_2T))/(math.log((2*h_2)/r_ed))
FAZ_3 = (math.log(D_3T/d_3T))/(math.log((2*h_3)/r_ed))
U_j= FAZ_1+FAZ_2+FAZ_3  * U_f

print('CiGRE  variant 1.2 sudok je {}'.format(U_j))
