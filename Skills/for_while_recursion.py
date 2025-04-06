#####################################
# for vs while vs recursion
#####################################

n = 5
update = 0
for i in range(1,n,1):
	update = update + 1

#####################################

print(f"for = {update}")

update = 0
while update < n-1:
	update = update + 1
print(f"while = {update}")

#####################################

def rec_funct(n):
	while True:
		if n == 0:
			return 0
		else:
			update = update + rec_funct(n-1)
			return update
	return update

update = 0
update = rec_funct(n)
print(update)
