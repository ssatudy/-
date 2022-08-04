# 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라.

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

# 입력 값을 모두 소문자로 banned는 리스트 형식이라 for문으로 변환함.
paragraph = paragraph.lower()

for num in range(len(banned)):
    banned[num] = banned[num].lower()

# paragraph에서 문자와 띄어쓰기를 제외하고 없애기
new_paragraph = ""
for alpha in paragraph:
    if alpha.isalpha() or alpha == " ":
        new_paragraph += alpha
    
# new_paragraph를 공백 단위로 쪼개서 리스트 만들기
paragraph_list = new_paragraph.split()

# 리스트에서 banned 단어 제외하고 많이 나온 단서 세기
paragraph_dict = dict()
for word in paragraph_list:
    if (word not in banned) and (word in paragraph_dict):
        paragraph_dict[word] += 1
    # else로만 설정할 경우 banned 단어로만 구성된 문장이 나올 경우 오답이 나올 수 있음.
    else:
        paragraph_dict[word] = 1
print(paragraph_dict)
result = sorted(paragraph_dict.items(), key = lambda x: x[1], reverse = True)

print(result[0][0])