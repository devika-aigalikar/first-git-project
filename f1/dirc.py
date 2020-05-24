dic = {'a': 10, 'second': 'element'}
# print(dic['a'])

dic[3] = 80
print(" original dictionary is:", dic)

# dic['a'] = 20
# print("updated a:", dic)
# # print(dic.get['f'])  # to check whether key exists
# print(dic.get('f', '100'))  # 100 is default value ,if exists returns original value
# del (dic['a'])  # to delete element and no return of value
# print("after deleting a:", dic)
# val = dic.pop('a', "does not exist")  # pop is used to return deleted value    dic.pop('a')gives error if deleted earlier
# print("Poped value is:", val)
# print("after again poping a", dic)
# c = dic.popitem()  # removes last element
# print("popitem func:", c)
# dic.setdefault('a', 200)  # if key does not exist it will add new key otherwise print original value
# print("by using set default:",dic)
# new_dic = dic.fromkeys(['l', 'm', 'a'], 300)  # change value of a
# print(new_dic)
# newdemo = dic.fromkeys(dic)
# print(newdemo)
# dic1={'a':100,'y':200}
# dic.update(dic1)
# print("  attaching new dic   :",dic)
d2 = dic.copy()
print("copied & printing new dic:", d2)
# for key in d2:
#     # print(key,":",d2[key])
#     # print("key{} ,value{} ".format(key,d2[key]))  #{}replaced by parameter in format func
#     print("key=%s,value=%s" % (key, d2[key]))

for key in d2.keys(): # only keys
    print(key)
for val in d2.values():
    print(val)
for key,val in d2.items():
    print(key,val)
d2.clear()
print(d2)