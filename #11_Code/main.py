import re, getpass

password = input("Enter your password: ")

checks = [
    (len(password) >= 8, "8+ Characters"),
    (bool(re.search(r"[A-Z]", password)), "Uppercase Letter"),
    (bool(re.search(r"[a-z]", password)), "Lowercase Letter"),
    (bool(re.search(r"\d", password)), "Number"),
    (bool(re.search(r"[!@#$%^&*]", password)), "Special Character"),
    (len(password) >= 12, "12+ Characters"),
    (not bool(re.search(r"(.)\1{2,}", password)), "No Repeated Characters")
]

score = sum(1 for check, _ in checks if check)

strength_levels = [
    "❌ Very Weak",
    "⚠️ Weak",
    "⚠️ Average",
    "✅ Good",
    "✅ Very Good",
    "🔒 Strong",
    "🔐 Very Strong"
]

strength = strength_levels[score]

print("\n" + "─" * 30)
for check, message in checks:
    print("✅" if check else "❌", message)

print(f"\nPassword Strength: {strength}")
print("─" * 30)
