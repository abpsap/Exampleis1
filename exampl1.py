import string
from hashlib import sha256

print ("hello")
fav_lang = 'python   '
fav_lang = fav_lang.rstrip()
print (f"The output is {fav_lang}")

msg = b'asjkhdkajsdh'
hash_function = sha256(msg)
print (hash_function.digest())

bro = ["^$%jack;&%$", "jill*&^", "mohan))#$", "guru$^*&"]
brostr = '; '.join(bro)
print (f"the joined brostr is {brostr}")
#brostrstrip = brostr.replace(string.punctuation, '6')
brostrstrip = brostr.strip(string.punctuation)
print (f"{brostrstrip}")

crypto_list = ['Yeti', 'Bigfoot', 'Loch Ness Monster']
crypto_string = ', '.join(crypto_list)

print (f"{crypto_string}")
vowels = ( 'a' \
    "e" '''i''' \
    'o' """u""" \
    )
print (vowels)

# for x in range(12, 1, -1):
#    print(x)
boxc = 'returntheitem'
print (boxc[::-1])

marxes = ['Groucho', 'Chico', 'Harpo']
print (f"{marxes[0:3]}")
marxes.insert(1, 'Zeppo')
print (f"{marxes[0:4]}")

horz = range (2,9)
vert = range (1,11)

mlist = [(row, col) for (row, col) in zip (horz, vert)]
print (mlist)

mlist = [(row, col) for (row, col) in zip (horz, vert) if row %2 != 1]
print (mlist)
