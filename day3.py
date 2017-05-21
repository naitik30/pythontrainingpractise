print("Hello World")
for i in range(3):
	print(i)

test = list()
test.append("rr")
test.append("ss")
for i in test:
	print i

test_dict = {
1:"test",
2:"hello"

}
for i,j in test_dict.iteritems():
	print i,j

a = [i for i in range(3)]
print a

a = a*3
print a

b = set(a)
print list(b)

