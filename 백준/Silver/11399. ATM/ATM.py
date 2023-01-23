n = int(input()) 
waiting = list(map(int, input().split()))  

waiting.sort() #오름차순

total = 0  
for x in range(1, n+1):
    total += sum(waiting[0:x])
print(total)  