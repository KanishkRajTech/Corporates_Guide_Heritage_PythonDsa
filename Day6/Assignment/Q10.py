#Write a program that determines the type of triangle given three sides a, b, c. Use conditions to check: (1) if a valid triangle exists (triangle inequality), (2) if Equilateral, Isosceles, or Scalene, (3) if Right-angled (use Pythagorean theorem). Use short-circuit evaluation where applicable.

side_a = int(input("Enter the length of side a: "))
side_b = int(input("Enter the length of side b: "))
side_c = int(input("Enter the length of side c: "))

if side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a:
    print("Valid triangle")
    if side_a == side_b == side_c:
        print("Equilateral triangle")
    elif side_a == side_b or side_a == side_c or side_b == side_c:
        print("Isosceles triangle")
    else:
        print("Scalene triangle")

    if side_a**2 + side_b**2 == side_c**2 or side_a**2 + side_c**2 == side_b**2 or side_b**2 + side_c**2 == side_a**2:
        print("Right-angled triangle")
        
else:
    print("Invalid triangle")