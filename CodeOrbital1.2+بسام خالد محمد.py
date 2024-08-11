import math 
rnode_x =float(input('Enter the component of R node in X-direction:'))
rnode_y =float( input('Enter the component of R node in Y-direction:'))
vnode_x =float( input('Enter the component of V node in X-direction:'))
vnode_y =float( input('Enter the component of V node in Y-direction:'))
rnode_z=vnode_z=0
delta_theta= float(input('Enter the change in true anamoly:'))
miou = (3.986013502)*(10**24)
cos_theta = math.degrees(math.cos(delta_theta))
sin_theta = math.degrees(math.sin(delta_theta))
print( 'we just assumed that our body move in x-y plane with no z axis ')

h=(rnode_x*vnode_y)-(rnode_y * vnode_x)   
print('h=',h)

r_x_v = rnode_x**2 
r_y_v = rnode_y**2
sqr=r_x_v + r_y_v
r_node_magnitude = math.sqrt(sqr)
print( 'r node =', r_node_magnitude)

v_x_v = vnode_x**2 
v_y_v = vnode_y**2
sqv=v_x_v + v_y_v
v_node_magnitude = math.sqrt(sqv)
print('V node = ', v_node_magnitude)

v_r_node_x = rnode_x * vnode_x
v_r_node_y = rnode_y * vnode_y   
v_r_nodeX = v_r_node_x / r_node_magnitude
v_r_nodeY = v_r_node_y / r_node_magnitude
print ("Vr0 =",v_r_nodeX,"X", "+",v_r_nodeY,"y")
Vr0_magnitude = math.sqrt(v_r_nodeX**2 + v_r_nodeY**2)


r=(h*h/miou)*(1/((1+(((h*h)/miou*r_node_magnitude)-1)*cos_theta)-(((h*Vr0_magnitude)/miou)*sin_theta)))
print ('r=',r)


f = 1-((miou*r)/h**2)*(1-cos_theta)
g = ((r*r_node_magnitude)/h)*sin_theta
f_dot=(miou/h)*((1-cos_theta)/sin_theta)*((miou/h*h)*(1-cos_theta) -1/r_node_magnitude -1/r)
g_dot = 1-((miou*r_node_magnitude)/h*h)*(1-cos_theta)


print ('f=',f,'g=',g,'f dot=',f_dot,'g dot=',g_dot)

r_vector_r_direction = f*r_node_magnitude
r_vector_v_direction = g*v_node_magnitude
print ( "r =  ",r_vector_r_direction ,"r0  + " ,r_vector_v_direction, " v0")

v_vector_r_direction = f_dot*r_node_magnitude
v_vector_v_direction = g_dot*v_node_magnitude
print ( "v =  ",v_vector_r_direction ,"r0  + " ,v_vector_v_direction, " v0")

#____Bassam Khaled Mohamed Eldawy_____NSST_____3rd LVL
