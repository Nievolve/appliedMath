class PIDController:
    def __init__(self, Kp, Ki, Kd):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.integral = 0
        self.previous_error = 0

    def update(self, set_value, process_value, dt):
        
        error = set_value - process_value

        
        P = self.Kp * error

        
        self.integral += error * dt
        I = self.Ki * self.integral

        
        derivative = (error - self.previous_error) / dt
        D = self.Kd * derivative

        
        self.previous_error = error

        # Formel PID
        u = P + I + D

        return u
    

    # Skapa utifrån klassen en regulator
pid = PIDController(Kp=1.0, Ki=0.1, Kd=0.05)

#Set value och Process Value.
# dt= tidsstegring
set_value = 10
process_value = 8
dt = 0.1

# Uppdatera PID-regulatorn och få styrsignalen
output = pid.update(set_value, process_value, dt)
print(f"Styrsignal (u): {output}")
