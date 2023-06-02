import vpython as vp

#Constants
k=9e9 
d=0.08 #Distance between each charge of the dipole 
R=0.01 #Radius of the charges

#Defining our graph elements

Q1=vp.sphere(pos=vp.vector(0,-d/2,0), 
             radius=R, color=vp.color.red) #Positive charge of the dipole
Q1.q=5e-9

Q2=vp.sphere(pos=vp.vector(0,d/2,0), 
             radius=R, color=vp.color.blue)#Negative charge of the dipole
Q2.q=-5e-9  

particle=vp.sphere(pos=vp.vector(3*d,0,0), 
                   radius=R/2, color=vp.color.cyan, make_trail=True)
particle.q=-1.6e-19 #Charged particle in the dipole (same charge as electron)
particle.m=1e-18 #Mass greater than the electron because the program collapsed with same mass
particle.p = particle.m*vp.vector(0,0,0) #Inicial momentum of the particle

t=0
dt=0.001
while t<2: 
  vp.rate(100)
  r1=particle.pos-Q1.pos
  r2=particle.pos-Q2.pos
  F1=k*Q1.q*particle.q*vp.norm(r1)/vp.mag(r1)**2
  F2=k*Q2.q*particle.q*vp.norm(r2)/vp.mag(r2)**2
  F=F1+F2
  particle.p=particle.p+F*dt
  particle.pos=particle.pos+particle.p*dt/particle.m
  t=t+dt
 
