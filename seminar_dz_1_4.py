# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
for i in range(2):
    for k in range(2):
        for j in range(2):
            A = i
            B = k
            C = j
            if not (A or B or C) == (not (A) and not (B) and not (C)):
                print(A, B, C, "->YES")
            else:
                print(A, B, C, "->NO")
