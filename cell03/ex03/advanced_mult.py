i = 1
while i <= 10: 
    print(f"Table de {i}: ", end="")
    x = 0
    while x <= 10:  # คูณตั้งแต่ 0 ถึง 10
        print(f"{i * x} ", end="")
        x += 1 
    print()
    i += 1 
