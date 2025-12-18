"""
Educational Purpose Only 📘
This script generates a random numeric OTP.
Used in verification systems (login, signup, payments).
"""

import random

def generate_otp(length=6):
    otp = ""
    for _ in range(length):
        otp += str(random.randint(0, 9))
    return otp

otp = generate_otp()
print("Your OTP is:", otp)
# Note: In production, use secure libraries for OTP generation.
