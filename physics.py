class PhysicsLibrary:
    def __init__(self):
        # okay so after realising that suvat really wasnt going to cut it (see design docs)
        # i changed to just have it a very loose library that i dont have to pass info to
        # i just call what i want and (hopefully) get a straight answer

        self.gravity = 9.81  # m/s sq
        self.air_density = 1.225  # kg/m cb
        self.drag_coefficient = 0.75 # drag

    def calculate_forces(self, rocket): # okay same as rocket.py's update func but for physics engine instead
        weight = rocket.mass * self.gravity
        thrust = self.get_thrust(rocket.fuel_type, rocket.fuel_oxi_ratio)
        drag = 0.5 * self.air_density * (rocket.velocity ** 2) * self.drag_coefficient
        net_force = thrust - weight - drag

        return {
            'thrust': thrust,
            'gravity': weight,
            'drag': drag,
            'net': net_force
        } # returns a dictionary for getting variables about the physics stuff, pretty cool

    def get_thrust(self, fuel_type, ratio):
        base_thrusts = {
            "kerosene": 250000,
            "hydrogen": 300000,
            "methane": 200000
        } # another dictionary with getter for the fuel types
        # meant to be somewhat accurate with the fuel cap or smth i read
        base = base_thrusts.get(fuel_type, 100000) # oxidiser and stuff too
        return base * ratio # returns the fuel thing with fuel ratio
        # too much fuel over oxidiser = bad rocket
        # too much oxidiser over fuel = bad rocket
        # somewhere in the middle = cool rocket
