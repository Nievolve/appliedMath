import math

def sin_double_angle(alpha):
    return 2 * math.sin(alpha) * math.cos(alpha)

def cos_double_angle(alpha):
    return math.cos(alpha)**2 - math.sin(alpha)**2

# Test the functions with an example angle (in radians)
alpha = math.radians(30)  # Example: 30 degrees in radians

sin_2alpha = sin_double_angle(alpha)
cos_2alpha = cos_double_angle(alpha)

print(f"sin(2α) for α = 30°: {sin_2alpha}")
print(f"cos(2α) for α = 30°: {cos_2alpha}")