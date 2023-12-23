import hashlib

def KSumm(message):
    return sum(ord(c) for c in message) % 256

def SummKodBukvOtkr(message, a, b, c, t0):
    result = []
    t = t0
    for m in message:
        t = (a * t + b) % c
        result.append(ord(m) ^ t)
    return result

a = 31
b = 7
c = 256
t0 = 126

messages = ['00009999', '99990000', '10000001', '11000000']

for message in messages:
    print(f"Message: {message}")
    print(f"KSumm: {KSumm(message)}")
    print(f"SummKodBukvOtkr: {SummKodBukvOtkr(message, a, b, c, t0)}")
    print("---")
