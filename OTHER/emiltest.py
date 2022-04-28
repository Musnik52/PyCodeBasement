# given a list of numbers
# show me the highest sum of 2 numbers
# *those two can't be neighbors! one number (at least) must separate them
# **no loop-nesting (best to use one loop)

def EmilsTest(_list):
    max_value = 0
    iter_flag = True
    i = 0
    while i < len(_list):
        a = 2 if iter_flag else a + 1
        try:
            max_value = _list[i] + _list[i +
                                         a] if abs(_list[i] + _list[i + a]) > max_value else max_value
            iter_flag = False
            continue
        except:
            i += 1
            iter_flag = True
            continue
    return max_value


print(EmilsTest([1, 999, 800, 5, 4]))  # => 1004
print(EmilsTest([0, 1, 2, 3, 5]))  # => 7
print(EmilsTest([1000, 90, 200, 99, 100]))  # => 1200
print(EmilsTest([5, 5, 5, 5, 5]))  # => 10
print(EmilsTest([-5, -5, 0, -5, -5]))  # => -5
