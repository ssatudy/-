import re                     #re 모듈을 불러온다.

def func(s):   
    s = s.lower()             # 일단 소문자화 시켜준다.
    s = re.sub('[^0-9a-z]', '', s) 
    # re.sub('[]')에서 [^a-z]등으로 설정하면 ^다음에 입력한 값들 이 아닌건 ''으로 없애준다.
    # 앞에 ^를 안해주면 a-z 즉, 알파벳을 ''으로 없애주는 기능이 적용된다.
    return s == s[::-1]   #거꾸로 해서 일치하는지를 리턴

print(func('a@b :b a')) # True
print(func('won'))      # False
print(func('A man, a plan, a canal: Panama')) # True