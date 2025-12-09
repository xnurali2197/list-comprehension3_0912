import math

def is_prime(n):
	if n < 2:
		return False
	if n == 2:
		return True
	if n % 2 == 0:
		return False
	r = int(n ** 0.5)
	for i in range(3, r + 1, 2):
		if n % i == 0:
			return False
	return True

# 1
uppercase_list = [s.upper() for s in ["hello", "world", "python"]]
# 2
reversed_words = [w[::-1] for w in ["car", "bike", "bus"]]
# 3
doubled = [x * 2 for x in [1, 2, 3, 4]]
# 4
high_scores = [s for s in [65, 85, 45, 95, 70] if s > 70]
# 5
alpha_only = [s for s in ["hello", "123", "world", "456"] if s.isalpha()]
# 6
residue_mod3_eq1 = [i for i in range(1, 21) if i % 3 == 1]
# 7
primes_1_50 = [i for i in range(1, 51) if is_prime(i)]
# 8
even_odd_replace = ["even" if x % 2 == 0 else "odd" for x in [1, 2, 3, 4, 5]]



print(uppercase_list)
print(reversed_words)
print(doubled)
print(high_scores)
print(alpha_only)
print(residue_mod3_eq1)
print(primes_1_50)
print(even_odd_replace)
