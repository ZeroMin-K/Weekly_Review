natural_set = set([i for i in range(1, 10001)])
generate_set = set()

for i in range(1, 10001):
    new_num = i
    while True:
        new_num = new_num + new_num // 1000 + new_num // 100 + new_num // 10 + new_num % 10 
        
        if new_num > 10000:
            break

        generate_set.add(new_num)

self_set = natural_set - generate_set

for num in sorted(self_set):
    print(num)
        
