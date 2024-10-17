from datetime import datetime

# Get the current time
current_time = datetime.now()

# Set max value
max_value = 10000

# Extract hour, minute, second, and millisecond
hour = current_time.hour
minute = current_time.minute
second = current_time.second
millisecond = current_time.microsecond // 1000  


rand_num = (((hour + 1) * (minute + 1) * (second + 1) * millisecond) % max_value)


print(rand_num)
