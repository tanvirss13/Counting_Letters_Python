letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Write your unique_english_letters function here:

def unique_english_letters(word):
  count = 0
  for letter in letters:
      if letter in word:
        count+=1
  return count


print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4
