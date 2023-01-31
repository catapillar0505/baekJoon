n = int(input()) # 입력되는 단어 개수
count = n #그룹단어 개수 체크
for i in range(n): #입력받기
  word = input()
  for k in range(len(word)-1): #마지막 글자는 검사할 필요 없음
    a = word[k] # 단어의 각 글자를 검사 -> 문자열 인덱싱
    if word[k] == word[k+1]: # 연속하는 경우 ex) aaab
      pass
    elif word[k] in word[k+1:]: # 연속하는 경우를 거른 후에 중복되는 글자가 있는지 검사 -> 포함 연산자
      count -= 1 # 그룹 단어가 아닌 경우임 그래서 그룹단어체커에서 하나 빼줌
      break
print(count)