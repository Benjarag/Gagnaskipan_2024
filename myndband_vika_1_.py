
# Time complexity: O(n)
def power(base, exp):
    ret_val = 1
    for _ in range(exp):
        ret_val *= base
    return ret_val

def insert_intro_list(lis, value, index):
    i = lis.size() - 1
    while i > index:
        lis[i] = lis[i-1]
    lis[index] = value


# print(power(2, 2))
# print(power(3, 2))
# print(power(2, 3))
# print(power(2, 8))
# print(power(4, 3))


# O(n), tekur tíma í stakið í öllum stökum
# O(n**2), tekur tíma í stakið í öllum stökum og gerir öll stök síðan aftur í hverju staki
# O(log(n)), helmingar stökin þangað til eitt er eftir, fljót aðferð
# O(2**n), lélegt forrit
