import random, sys

meows = ["meow", "mrrp", "nya", "meowo", "miau", ":3", ":33333"]
if len(sys.argv) > 1:
    amount = int(sys.argv[1])
else:
    amount = 5

print(" ".join(random.choices(meows, k=amount)))
