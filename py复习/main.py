def add(li: list, target, left):
	for i in range(1, left // 2+1):
		t = int(f"{i}{target}")
		li.append(t)
		add(li, t, i)

li = [8]
add(li, li[0], li[0])
print(li)

