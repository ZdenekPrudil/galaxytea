import matplotlib.pyplot as plt

def listy(vzdialenost,alfa,M_16,m_1,R_hv):
	d_l,surface_density_l,height_l,density_l = ([] for i in range(4))
	temperature_l,opacity_l,viscosity_l,radial_velocity_l = ([] for i in range(4))
	for R_10 in range(R_hv+1,vzdialenost):
		f=(1-(float(R_hv)/R_10)**(1.0/2))**(1.0/4)
		surface_density = 5.2*alfa**(-4.0/5)*M_16**(7.0/10)*m_1**(1.0/4)*R_10**(-3.0/4)*f**(14.0/5)
		height =  1.7*10**8*alfa**(-1.0/10)*M_16**(3.0/20)*m_1**(-3.0/8)*R_10**(9.0/8)*f**(3.0/5)
		density = 3.1*10**(-8)*alfa**(-7.0/10)*M_16**(11.0/20)*m_1**(5.0/8)*R_10**(-15.0/8)*f**(11.0/5)
		temperature = 1.4*10**4*alfa**(-1.0/5)*M_16**(3.0/10)*m_1**(1.0/4)*R_10**(-3.0/4)*f**(6.0/5)
		opacity = 190*alfa**(-4.0/5)*M_16**(1.0/5)*f**(4.0/5)
		viscosity = 1.8*10**14*alfa**(4.0/5)*M_16**(3.0/10)*m_1**(-1.0/4)*R_10**(3.0/4)*f**(6.0/5)
		radial_velocity = 2.7*10**4*alfa**(4.0/5)*M_16**(3.0/10)*m_1**(-1.0/4)*R_10**(-1.0/4)*f**(-14.0/5)
		d_l.append(R_10)
		surface_density_l.append(surface_density)
		height_l.append(height)
		density_l.append(density)
		temperature_l.append(temperature)
		opacity_l.append(opacity)
		viscosity_l.append(viscosity)
		radial_velocity_l.append(radial_velocity)
	return d_l, surface_density_l, height_l, density_l,temperature_l,opacity_l,viscosity_l,radial_velocity_l

zoznam=listy(10**3,0.5,10,5,1)


plt.plot(zoznam[0], zoznam[1])
plt.title('surface density')
plt.xlabel('radius [R$_{hv}$]')
plt.ylabel('surface density [g.cm$^{-2}$] ')
plt.savefig("surface density")
plt.gcf().clear()

plt.plot(zoznam[0], zoznam[2])
plt.title('height')
plt.xlabel('radius [R$_{hv}$]')
plt.ylabel('height [cm] ')
plt.savefig("height")
plt.gcf().clear()

plt.plot(zoznam[0], zoznam[3])
plt.title('density')
plt.xlabel('radius [R$_{hv}$]')
plt.ylabel('density [g.cm$^{-3}$] ')
plt.savefig("density")
plt.gcf().clear()

plt.plot(zoznam[0], zoznam[4])
plt.title('temperature')
plt.xlabel('radius [R$_{hv}$]')
plt.ylabel('temperature [K] ')
plt.savefig("temperature")
plt.gcf().clear()

plt.plot(zoznam[0], zoznam[5])
plt.title('opacity')
plt.xlabel('radius [R$_{hv}$]')
plt.ylabel('opacity ')
plt.savefig("opacity")
plt.gcf().clear()

plt.plot(zoznam[0], zoznam[6])
plt.title('viscosity')
plt.xlabel('radius [R$_{hv}$]')
plt.ylabel('viscosity [cm$^{2}$.s$^{-1}$] ')
plt.savefig("viscosity")
plt.gcf().clear()

plt.plot(zoznam[0], zoznam[7])
plt.title('radial velocity')
plt.xlabel('radius [R$_{hv}$]')
plt.ylabel('radial velocity [cm.s$^{-1}$] ')
plt.savefig("radial velocity")
plt.gcf().clear()
