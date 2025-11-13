"""
- * (single star) expands any iterable (lists, tuples, strings, ranges, generators, sets, or your own iterable type).
- Order matters for ordered iterables; sets are unordered so the order is not guaranteed.

** (double star) expands a mapping (usually a dict) into keyword arguments — keys must match parameter names.
"""


def compute(a, b, c):
    print(a + b + c)


items_list = [11, 22, 33]  # list
print(type(items_list))
compute(items_list[0], items_list[1], items_list[2])
compute(*items_list)

items_tuple = (11, 22, 33)  # tuple
print(type(items_tuple))
compute(*items_tuple)

items_set = {11, 22, 33}  # set
print(type(items_set))
compute(*items_set)

items_generator = (i for i in [11, 22, 33])  # generator
print(type(items_generator))
compute(*items_generator)

items_range = range(11, 34, 11)  # range
print(type(items_range))
compute(*items_range)

items_kwargs = {"a": 11, "b": 22, "c": 33}  # dict
print(type(items_kwargs))
compute(**items_kwargs)
