t = "acldm1labcdhsnd"
z = "shabcdacasklksjabcdfueuabcdfhsndsabcdmdabcdfa"
substring = "abcd"
def find_max(t, z):
  # A variable is created to store the highest value and initially set to 0.
  max_product = 0

  # The lengths of the strings are calculated.
  t_len = len(t)
  z_len = len(z)

  # Two loops are used to search for all possible subarrays of the t array.
  for i in range(t_len):
      for j in range(i + 1, t_len + 1):
          # Lower hem is formed.
          substring = t[i:j]

          # The number of times the letter z appears in the second sentence.
          substring_count = z.count(substring)

          # The product of the length of the bottom and the number of times z occurs within it is taken.
          product = len(substring) * substring_count

          # If this value is greater than the largest value found so far, the largest value is updated.
          if product > max_product:
              max_product = product

  # The highest value is returned.
  return max_product

if __name__ == '__main__':
  # The function is called with sample inputs and the result is printed to the screen.

  substring_count = z.count(substring)
  result = find_max(t, z)

  print(f"The substring '{substring}' occurs {substring_count} times in 'z'.")
  print("Maximum value:", result)