import numpy as np
A = np.array([-3, 1, -2])
B = np.array([3, -2, -2])
dot = np.dot(A, B)
abstime = np.linalg.norm(A) * np.linalg.norm(B)
angle = np.arccos(dot/abstime)
print(f"angle(rad):{angle}")
print(f"angle(degrees):{np.degrees(angle)}")