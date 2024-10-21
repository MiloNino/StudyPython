import random

friends = ["Alice","Bob","Charlie","David","Emanuel"]
invita= random.randint(0,(len(friends)-1))
print(f"quien paga la cuenta es: {friends[invita]}")
print(random.choice(friends))

