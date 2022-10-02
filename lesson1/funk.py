int_var = 500
float_var = 50.9
string_var_text = 'Hello World'
string_var_num = '123.2'
boll_var = True

# int()  -  integer
# float()  -  float
# str()  - string
# bool()  -  boolean



print(string_var_text + ' ' + str(int_var))
print(type(int_var))
print(string_var_text + str(float_var))
print(string_var_text + str(boll_var))
# alternativ
print(string_var_text, int_var, True, None, 1000.256)




print(int_var)
print(float(int_var))

print(float_var)
print(int(float_var))

print(float(string_var_num))
print(int(float(string_var_num)))

print(bool(int_var))

