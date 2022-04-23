nums = {
     1 : "one"
    ,2 : "two"
    ,3 : "three"
}
print(1 in nums)
print("three" in nums)
print(4 not in nums)

pairs = {
    1 : "apple",
    "orange" : [2,3,4],
    True : False
    , 12 : "True"
}
print(pairs.get("orange"))
print(pairs.get(7,42))  # means do not found 7 in pairs, so argement two print 42
print(pairs.get(12345,"not found"))
print(pairs)


thisdict = {
  4: "Ford",
 2: "Mustang",
  3: 1964,
  1: 2020
}
print(thisdict)