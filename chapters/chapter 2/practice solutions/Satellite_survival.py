# aprogram to show if a Satellite survives with it's given situations like mass and hight and speed 
# we take Gravitational constant as GC
import math
#gravitual constant is :
GC = 6.67e-11   #m3/kg*s2

#proof of formula r and v
# F = G m1 m2 /r**2
# m1 a = G m1 m2 /r**2
# m1 v**2/r = G m1 m2 /r**2
# v**2 = G m2 / r

# so that 

# m2 = v**2 r /G
# r =G m2 / v**2


#some information
# 	                MERCURY 	 VENUS 	 EARTH 	 MOON 	 MARS 	 JUPITER 	 SATURN 	 URANUS 	 NEPTUNE 	 PLUTO 
#Mass   (10**24kg)	0.330	     4.87	 5.97	 0.073	 0.642	 1898	     568	     86.8	     102	     0.0130
#Diameter   (km)	4879	     12,104	 12,756	 3475	 6792	 142,984	 120,536	 51,118	     49,528	     2376
#Density (kg/m3)	5429	     5243	 5514	 3340	 3934	 1326	     687	     1270	     1638	     1850
#Gravity  (m/s2)	3.7	         8.9	 9.8	 1.6	 3.7	 23.1	     9.0	     8.7	     11.0	     0.7


# we will take mass as an input 
# and will show the possible v for survival of the satellite

mass = float(input("what is the planet's mass? (kg) \n"))
r = float(input("to what orbid this satellite will be sent? (m) \n"))
v = math.sqrt((GC*mass)/r)

print(f"the velocity of satellite must be {v} (m/s) to survive on the orbit or it will fall")


#15/2/1401
#program is finished 