main_array = [[1,1], [3,4], [4,4], [8,2], [8,3], [8,3]]
main_tuple = []

for x in main_array:
    y = tuple(x)
    main_tuple.append(y)

main_tuple = tuple(main_tuple)
main_set = set(main_tuple)
print(main_tuple)
print(main_set)