from hashlib import sha256

print ("hello")
fav_lang = 'python   '
fav_lang = fav_lang.rstrip()
print (f"The output is {fav_lang}")

msg = b'asjkhdkajsdh'
hash_function = sha256(msg)
print (hash_function.digest())

bro = ["jack", "jill", "mohan", "guru"]
brostr = ', '.join(bro)
print (f"the joined brostr is {brostr}")
