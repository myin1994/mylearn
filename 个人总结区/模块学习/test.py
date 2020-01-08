import random
print("".join(random.choices([chr(i) for i in range(122) if chr(i).isalnum()],k=5)))