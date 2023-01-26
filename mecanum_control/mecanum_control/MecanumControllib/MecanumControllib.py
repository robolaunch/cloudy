class MecanumControl:
    """Constructor: wheel attributes are in mm, limits are in mm/sec"""
    def __init__(self,wheel_radius,wheel_track,wheel_base,min_limit,max_limit):
        self.min_limit = min_limit
        self.max_limit = max_limit
        self.wheel_radius = wheel_radius
        self.wheel_track = wheel_track
        self.wheel_base = wheel_base
        self.front_right_motor_speed = 0.0
        self.front_left_motor_speed = 0.0
        self.back_right_motor_speed  = 0.0
        self.back_left_motor_speed = 0.0
        self.linear_x = 0.0
        self.linear_y = 0.0
        self.angular = 0.0
    """ This does what you think it does. """    
    def filterVelocity(self, velocity: float, min_limit: float, max_limit: float):
        return min(max(velocity,min_limit),max_limit)
    #velX,velY: mm/sec | velW:degree/sec | motor_speeds:degree/sec
    def calculateMecanum(self, velX: float, velY: float, velW: float):
        if(self.wheel_radius <= 0):
            raise Exception("WHEELRADIUS argument must be positive")

        filtered_velX = self.filterVelocity(velX,self.min_limit,self.max_limit)
        filtered_velY = self.filterVelocity(velY,self.min_limit,self.max_limit)
        #filtered_velW = self.filterVelocity(velW,VEL_MIN_W,VEL_MA
        linear_sum = filtered_velY+filtered_velX
        linear_subt = filtered_velY-filtered_velX
        chasis_sum = self.wheel_base+self.wheel_track
        inverse_radius = 1.0/self.wheel_radius; 

        self.front_left_motor_speed = (linear_sum - (chasis_sum*velW))*inverse_radius
        self.front_right_motor_speed = (linear_subt + (chasis_sum*velW))*inverse_radius
        self.back_left_motor_speed = (linear_subt - (chasis_sum*velW))*inverse_radius
        self.back_right_motor_speed = (linear_sum + (chasis_sum*velW))*inverse_radius
    #Front left -> 0, Front right -> 1,  Back left -> 2, Back right -> 3. The units are in degrees per second
    def getCalculatedMotorSpeed(self,motorNumber:int):
        if(motorNumber >= 0 and motorNumber <= 3):
            if motorNumber == 0:
                return self.front_left_motor_speed
            elif motorNumber == 1:
                return self.front_right_motor_speed
            elif motorNumber == 2:
                return self.back_left_motor_speed
            elif motorNumber == 3:
                return self.back_right_motor_speed
        else:
            raise Exception("motorNumber argument must be between [0-3]")
    def calculateForwardKinematics(self,front_left_vel,front_right_vel,back_left_vel,back_right_vel):
        self.linear_x = (self.wheel_radius/4.0)*(front_left_vel-front_right_vel-back_left_vel+back_right_vel)
        self.linear_y = (self.wheel_radius/4.0)*(front_left_vel+front_right_vel+back_left_vel+back_right_vel)
        self.angular = (self.wheel_radius/(4*(self.wheel_base+self.wheel_track)))*(-front_left_vel+front_right_vel-back_left_vel+back_right_vel)
    
    def getChasisSpeed(self):
        return self.linear_x, self.linear_y, self.angular