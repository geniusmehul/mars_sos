msg = input()
len_msg = len(msg)
reps = int(len_msg / 3)
orig_msg = 'SOS' * reps
cnt = 0
for x, y in zip(orig_msg, msg):
    if x != y:
        cnt += 1
print(cnt)