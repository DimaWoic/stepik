need_sleep = int(input())
max_sleep = int(input())
now_sleep = int(input())

if now_sleep < need_sleep:
    print("Недосып")
elif now_sleep > max_sleep:
    print("Пересып")
else:
    print("Это нормально")
