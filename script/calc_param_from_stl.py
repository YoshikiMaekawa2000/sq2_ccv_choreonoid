#calcurate inertia
def calc_box_inertia(mass, x, y, z):
    Ix = mass / 12.0 * (y**2 + z**2)
    Iy = mass / 12.0 * (z**2 + x**2)
    Iz = mass / 12.0 * (x**2 + y**2)
    return Ix, Iy, Iz

def calc_cylinder_inertia(mass, radius, length):
    Ix = mass / 12.0 * (3.0 * radius**2 + length**2)
    Iy = mass / 12.0 * (3.0 * radius**2 + length**2)
    Iz = mass / 2.0 * radius**2
    return Ix, Iy, Iz
#main
if __name__ == '__main__':
    
    ##calculate inertia of base_link
    mass = 5.0
    length = 0.105
    width = 0.501
    height = 0.044
    Ix, Iy, Iz = calc_box_inertia(mass, length, width, height)
    print("base_link:")
    print(" Ix: ", Ix)
    print(" Iy: ", Iy)
    print(" Iz: ", Iz)

    ##calculate inertia of base2body_link
    mass = 5.0
    length = 0.319
    width = 0.125
    height = 0.090
    Ix, Iy, Iz = calc_box_inertia(mass, length, width, height)
    print("base2body_link:")
    print(" Ix: ", Ix)
    print(" Iy: ", Iy)
    print(" Iz: ", Iz)

    ##calculate inertia of steer_link
    mass = 1.0
    radius = 0.03
    length = 0.15
    Ix, Iy, Iz = calc_cylinder_inertia(mass, radius, length)
    print("steer_link:")
    print(" Ix: ", Ix)
    print(" Iy: ", Iy)
    print(" Iz: ", Iz)

    ##calculate inertia of wheel_link
    mass = 5.0
    radius = 0.1435
    length = 0.025
    Ix, Iy, Iz = calc_cylinder_inertia(mass, radius, length)
    print("wheel_link:")
    print(" Ix: ", Ix)
    print(" Iy: ", Iy)
    print(" Iz: ", Iz)

    ##calculate inertia of casters_pitch_link
    mass = 1.0
    length = 0.15
    width = 0.15
    height = 0.05
    Ix, Iy, Iz = calc_box_inertia(mass, length, width, height)
    print("casters_pitch_link:")
    print(" Ix: ", Ix)
    print(" Iy: ", Iy)
    print(" Iz: ", Iz)

    ##calculate inertia of pitch2shaft_link
    mass = 1.0
    length = 0.078
    width = 0.120
    height = 0.04
    Ix, Iy, Iz = calc_box_inertia(mass, length, width, height)
    print("pitch2shaft_link:")
    print(" Ix: ", Ix)
    print(" Iy: ", Iy)
    print(" Iz: ", Iz)

    ##calculate inertia of caster link
    mass = 1.0
    radius = 0.0635
    length = 0.024
    Ix, Iy, Iz = calc_cylinder_inertia(mass, radius, length)
    print("caster_link:")
    print(" Ix: ", Ix)
    print(" Iy: ", Iy)
    print(" Iz: ", Iz)

    ##calculate inertia of battery_box_link
    mass = 20.0
    length = 0.208
    width = 0.208
    height = 0.5535
    Ix, Iy, Iz = calc_box_inertia(mass, length, width, height)
    print("upper_body_link:")
    print(" Ix: ", Ix)
    print(" Iy: ", Iy)
    print(" Iz: ", Iz)

    ##calculate inertia of upper_body_link
    mass = 1.0
    length = 0.258
    width = 0.258
    height = 0.508
    Ix, Iy, Iz = calc_box_inertia(mass, length, width, height)
    print("upper_body_link:")
    print(" Ix: ", Ix)
    print(" Iy: ", Iy)
    print(" Iz: ", Iz)






