import re

def func(s:str):     
    s = s.lower()     # 일단 소문자화
    s = s.replace(banned_str, '')  # replace를 통해 banned의 단어를 지워줌
    s = re.sub('[^a-z]', ' ', s)   # re.sub를 통해 알파벳이 아닌건 공백으로 만들어줌
    lst = s.split()   # 공백을 기준으로 단어들을 리스트로 묶어줌
    lst_count = 0     # 제일 많이 나온 단어의 수를 넣어줌(다른 단어의 수랑 비교하기 위해)
    str_count = ''    # 제일 많이 나온 단어를 넣어줄 문자열을 만든다.
    for i in lst:
        if lst.count(i) > lst_count: # 만약 단어의 수가 lst_count보다 많은 경우에는
            lst_count = lst.count(i) # 그 수를 lst_count에 넣어준다.
            str_count = i            # 그 단어 역시 str_count에 넣어준다.
    return str_count

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
banned_str = ''.join(banned)
print(func(paragraph))