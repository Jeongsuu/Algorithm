# 문자열 내 p와 y의 개수

---



### 문제 설명

---

>대문자와 소문자가 섞여있는 문자열 s가 주어집니다. s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요. 'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.
>
>예를 들어 s가 pPoooyY면 true를 return하고 Pyy라면 false를 return합니다.



### 제한사항

---

>- 문자열 s의 길이 : 50 이하의 자연수
>- 문자열 s는 알파벳으로만 이루어져 있습니다.



### 제출코드

---

>```python
>def solution(s):
>    cnt = [0, 0]
>    for i in list(s.upper()):
>        if i == 'P':
>            cnt[0] += 1
>        elif i == 'Y':
>            cnt[1] += 1
>    return True if cnt[0] == cnt[1] else False
>```



### 코드설명

---

>Line 2 : P와 Y의 개수를 각각 카운팅하기 위한 변수 생성
>
>Line 3 : 전달받은 문자열 s를 대문자로 변환한 뒤, `list`로 타입을 변환하여 순회
>
>Line 4~7 : 만일 대문자 P이면 cnt[0]을 , Y이면 cnt[1]을 각각 1씩 증가시킨다.
>
>Line 8 : cnt[0]과 cnt[1]이 같을 경우 `True`를, 그 외 경우 모두 `False` 반환



### 다른 사람의 풀이

---

>```python
>def solution(s);
>	return s.lower().count('p') == s.lower().count('y')
>```
>
>.... 매우 간결하고 깔끔하다.
>
>`count()` 함수를 처음 보았다.
>
>확실히 난 아직 너무나도 멀었다...