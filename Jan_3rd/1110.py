cycle = 0
input_num = int(input())
start_num = int(input_num)

while True:     
    mid_a = start_num // 10
    mid_b = start_num % 10
    mid_num = mid_a + mid_b
    new_num = mid_b * 10 + mid_num % 10
    cycle += 1

    if new_num == input_num:
        break

    start_num = new_num
    
print(cycle)
