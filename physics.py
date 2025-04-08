class PhysicsLibrary():
    def __init__(self, s, u, v, a, t):
        # pass through suvat equations to do general forces physics with
        # s = displacement
        # u = initial velocity
        # v = final velocity
        # a = acceleration
        # t = time (FPS)

        #init suvat in class
        self.displacement = s
        self.initial_velocity = u
        self.final_velocity = v
        self.acceleration = a
        self.time = t

        #init extra vars that dont need passing through
        self.grav_const = 9.807
        self.temperature = None
        self.mass = None
