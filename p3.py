a = "sami"
b = "abdul"

sorted_string1 = ''.join(sorted(a))
print(sorted_string1)

sorted_string2 = ''.join(sorted(b))
print(sorted_string2)

if sorted_string1 == sorted_string2:
    print("Words are anagrams")
else:
    print("Words are not anagrams")
