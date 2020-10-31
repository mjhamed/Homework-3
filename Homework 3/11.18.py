#Mohamed Hamed
#1644926

user_input = input()
entries = user_input.split(' ')
correct_ans = []
for num in (entries):
   num = int(num)
   if num >= 0:
       correct_ans.append(num)
correct_ans.sort()
for n in correct_ans:
    print(n, end=' ')