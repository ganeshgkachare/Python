#################################################
# HW
#################################################
# score_vk = {
#         one_day : 700,
#         test : 740,
#         t_20 : 470,
#         international : 250
# }
# 1. CREATE ABOVE DICTIONARY USING BASIC METHOD 
# {} AND NAME IT AS score_vk_basic
score_vk = {"one_day" : 700,"test" : 740,"t_20" : 470,"international" : 250}
print(score_vk)
print("------------------------------------------------------------------------")

# 2. CREATE ABOVE DICTIONARY USING 
# variable assignments way AND NAME IT AS score_vk_var
score_vk_var= dict(one_day = 700,test = 740,t_20 = 470,international = 250)
print(score_vk_var)
print("------------------------------------------------------------------------")

# 3. CREATE ABOVE DICTIONARY USING 
# tuple pair way  AND NAME IT AS score_vk_basic_tup
score_vk_basic_tup = dict([("one_day", 700),("test" , 740),("t_20" , 470),("international" , 250)])
print(score_vk_basic_tup)
print("------------------------------------------------------------------------")

# 4. CREATE ABOVE DICTIONARY USING 
# zip method CONSIDERING 
# KEYS LIST AS list_keys AND 
# VALUES LIST AS list_values  AND 
# NAME IT AS score_vk_basic_tup
list_keys = ['one_day', 'test', 't_20', 'international']
list_values = [700, 740, 470, 250]
score_vk_basic_tup = dict(zip(list_keys,list_values))
print(score_vk_basic_tup)

