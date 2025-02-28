import numpy as np
import matplotlib.pyplot as plt
import netCDF4 as nc
from matplotlib.animation import FuncAnimation 

rootgrp = nc.Dataset(" your nc.file ")

# topo would be 'a value' to help you correct the surface  
topo = int(rootgrp.variables['topo'][:])

height = rootgrp.variables['m_zc'][topo:]
pressure = rootgrp.variables['p_zc'][topo:]
rho = rootgrp.variables['rho'][topo:]

#the first dimension is how much the number you catch from initial nc.file
#it may change by how you get the VVM nc.file
#in CA1 I catch , ex. th.shape[0] = 73 

th  = rootgrp.variables['th'][:,topo:]
rv  = rootgrp.variables['qv'][:,topo:]

qv = rv / ( 1+ rv ) 
water_rho = rho * qv

temperature          = np.zeros(( int(th.shape[0])    , int(pressure.shape) ) ) 
water_vapor_pressure = np.zeros(( int(water_rho.shape), int(pressure.shape) ) )

for i in range ( int(th.shape[0]) ):
    temperature[i,:] = ( th[i,:] ) * ( (pressure[:]/1000) )**(0.286) 

water_vapor_pressure = water_rho * 8.314 * temperature

#choose the variable you want to plot (cancel the # in front of gifline )

#gifline_rv , =  plt.plot(rv[0,:]                  ,height)
#gifline_qv , =  plt.plot(qv[0,:]                  ,height)
#gifline_T  , =  plt.plot(temperature[0,:]         ,height)
#gifline_Pv , =  plt.plot(water_vapor_pressure[0,:],height)

def gif (i):
    gifline_ ## .set_data( ## [i,:],height[:])
    plt.title( "ne_20191030  %3d mins"  % (i*20) )

plt.xlabel(' ## ')
plt.ylabel(' ## ')
plt.xlim( ## , ##)

##see 15~17 lines with ##.shape[0]
totalgif = FuncAnimation( plt.gcf() , gif , frames = range(##.shape[0] ) )

#you can use plt.show() to check the gif immediately
#but it may cause some bug when saving the gif to your local
#so, recommand # it when you are saving the file

#plt.show()
totalgif.save(" ## .gif")
rootgrp.close()
