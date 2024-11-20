i = 1
while i <= 10: 
    print(f"Table de {i}: ", end="")
    j = 0
    while j <= 10:  # คูณตั้งแต่ 0 ถึง 10
        print(f"{i * j} ", end="")
        j += 1 
    print()
    i += 1 
