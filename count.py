count = {}

with open('db/发言用户.txt') as f:
	for line in f.readlines():
		try:
			user_id = int(line.strip()[4:])
		except:
			continue
		count[user_id] = count.get(user_id, 0) + 1

counts = [(count[x], x) for x in count if count[x] > 20]
counts.sort(reverse = True)

with open('db/常发言.txt', 'w') as f:
	for num, user_id in counts:
		f.write('%d %d\n' % (user_id, num))