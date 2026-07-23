import time
mins = int(input("Enter time in minutes: "))

total_secs = mins*60 


while total_secs >= 0:
    
    mins = total_secs // 60
    secs = total_secs % 60
    
    time.sleep(1)
    
    print(f"\rTime remaning: {mins:02d}:{secs:02d}",end = " ")
    
    total_secs -= 1

print("\nTime fenish, take a brear")