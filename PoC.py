first_name = "avinash"
last_name = "baroth"
skill_level = 8
target_skill_level = 10
rank = 1.0
print (first_name)
diff_skill_level = target_skill_level - skill_level
print (diff_skill_level)
type (diff_skill_level)
type (first_name)
print (first_name + " " + last_name)
print (first_name + " " + last_name + " - " + str(skill_level))
print (target_skill_level + rank)
float_num = 10.7
int_num = int(float_num)
print(f"Float to int: {int_num}, type: {type(int_num)}")
truthy_val = bool(1)
falsy_val = bool(0)
empty_string_bool = bool("")
non_empty_string_bool = bool("hello")
print(f"1 to bool: {truthy_val}")
print(f"0 to bool: {falsy_val}")
print(f"Empty string to bool: {empty_string_bool}")
print(f"Non-empty string to bool: {non_empty_string_bool}")
int_val = 20
float_val = float(int_val)
print(f"Int to float: {float_val}, type: {type(float_val)}")