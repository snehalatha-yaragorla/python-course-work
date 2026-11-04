'''str1 = If you trouble the trouble,
trouble will troubles you, I am not the trouble,
I am the truth ---by Jai balayya@9999
lower = str1.lower()
print("lower:",lower)
capitalize = str1.capitalize()
print("capitalize: ",capitalize)
upper = str1.upper()
print("upper: ",upper)
title = str1.title()
print("title: ",title)'''

# checking Methods
'''str1 = If you trouble the trouble,
trouble will troubles you, I am not the trouble,
I am the truth ---by Jai balayya@9999
print(str1.islower())
print(str1.isupper())
print(str1.istitle())
print(str1.isalpha())
print(str1.isalnum())
print(str1.isdigit())
print(str1.isspace()) '''


str1 = '''   If you trouble the trouble,
trouble will troubles you, I am not the trouble,
I am the truth ---by Jai balayya@9999   '''
#print(str1.count("trouble"))
#print(str1.strip())
#print(str1.lstrip())
#print(str1.rstrip())
words = str1.split()
print(words)
print(type(words))

print(len(words))
combined_str = (' ').join(words)
print(combined_str)