from pbor_class import pbor_class

def reassign(param):
    param = 1
    print("param: " + str(param))


def change(param):
    param += 1
    print("param: " + str(param))


# var = [0]

# class_inst = pbor_class(var)


# print("var before: " + str(var))
# class_inst.change()
# print("var after: " + str(var))


var = 0
print("var: " + str(var))
reassign(var)
print("var: " + str(var))
change(var)
print("var: " + str(var))


