import re
from collections import Counter

def func(s:str):     
    s = s.lower()    
    s = s.replace(banned_str, '') 
    s = re.sub('[^a-z]', ' ', s)
    lst = s.split()  
    counts = Counter(lst)      
    # Counter모듈을 불러와서 리스트의 요소들을 key로, 그 숫자를 value로 하는 딕셔너리를 쉽게 만들 수 있다.
    return counts.most_common()
    # 허나 이 딕녀서리를 추출 하려면 .most_common이 필요하다.
    # most_common(1)을 하면 [(ball: 2)]형태로 출력되어 슬라이싱해 ball을 꺼내온다.

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
banned_str = ''.join(banned)

print(func(paragraph))