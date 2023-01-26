checkList = [0 for k in range(1, 10040)]
for i in range(1, 10001):  #index 오류 -> 마지막 수로 테스트 ex i=9999->10035
  sum = i  # ex) 24
  s = str(i)  #"24"
  for j in range(len(s)):  # 24 -> 2 , 4
    sum += int(s[j])
  checkList[sum] += 1
result = ""
for c in range(1, 10001):
  if not checkList[c]:
    result += str(c)
    result += "\n"
print(result)