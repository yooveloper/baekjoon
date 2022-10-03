data = input().split(' ')

hour = int(data[0])
minute = int(data[1])

minute -= 45

# 만약에 10시 10분이 들어오면 
# 10 -35
if minute < 0: # 분이 0보다 작으면 ( 음수이면 )
    minute += 60 # 60분을 더해줌
    hour -= 1 # 시간은 1시간을 빼줌 
    # 그럼 최종적으로 10시 10분이 들어왔을때
    # 현재 값은 9시 35분이니까 10시 10분에서 45분 앞당긴 알람시간이 된다.
    if hour < 0: # 만약 시간이 0보다 작으면
        hour = 23

print(str(hour) + ' ' + str(minute))
        
    