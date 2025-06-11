greeting = "Hello"
greeting = (greeting + " World!").lower()
chr = 'o' 
ind = [i for i, c in enumerate(greeting) if c == chr]
print(greeting)
print("index 'o': ", greeting.index('o'))
print("count 'o': ", greeting.count("o"))
print("alle index 'o': ", ind)