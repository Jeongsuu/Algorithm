# K번째 수

---



### 문제 설명

---

>배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.
>
>예를 들어 array가 [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5, k = 3이라면
>
>1. array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]입니다.
>2. 1에서 나온 배열을 정렬하면 [2, 3, 5, 6]입니다.
>3. 2에서 나온 배열의 3번째 숫자는 5입니다.
>
>배열 array, [i, j, k]를 원소로 가진 2차원 배열 commands가 매개변수로 주어질 때, commands의 모든 원소에 대해 앞서 설명한 연산을 적용했을 때 나온 결과를 배열에 담아 return 하도록 solution 함수를 작성해주세요.



### 제한사항

---

>- array의 길이는 1 이상 100 이하입니다.
>- array의 각 원소는 1 이상 100 이하입니다.
>- commands의 길이는 1 이상 50 이하입니다.
>- commands의 각 원소는 길이가 3입니다.



### 제출 코드

---

>```python
>def solution(array, commands):
>    answer = []
>    sliced = []
>    for i in range(len(commands)):
>        sliced = array[commands[i][0]-1 : commands[i][1]]
>        sliced.sort()
>        answer.append(sliced[commands[i][2] - 1])
>    return answer
>
>```



### 코드 설명

---

>**line 2** : `return`할 정답 리스트
>
>**line 3** : `list slicing` 결과를 저장할 리스트 선언
>
>**line 4~7** : `list slicing` , `sorting`, `appending`을 통한 `answer` 가공
>
>**line 8** : `answer` list 반환



### 다른 사람의 풀이

---

>```python
>def solution(array, commands):
>    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
>
>```
>
>`lambda`식을 활용하여 한줄로 끝내셨다..ㄷ
>
>`commands`인자를 `lambda x:`로 받아 람다식으로 리스트 슬라이싱 및 인덱싱을 진행했다.
>
>필자는 `map` 내장 함수와 `lambda`를 같이 쓸 생각 조차도 하지 못했다..
>
>매우 깔끔하고 멋있는 코드다..!



### lambda는 왜 쓰는가?

---

>* 익명함수이기 때문에 한번 쓰이고 다음줄로 넘어가면 힙(Heap) 메모리 영역에서 증발.
>
>* 파썬에서는 모든것이 객체로 관리되며 각 객체들은 `reference counter`를 갖게된다.
>
>  이 카운터가 0 (아무도 참조하지 않는 경우)이 된다면 메모리를 환원하게 된다.



### map 함수

---

>* 내장 함수
>
>* 입력받은 자료형의 각 요소가 합수에 의하여 수행된 결과를 묶어서 map iterator 객체로 반환
>
>
>  ```python
>  map(f, iterable)
>  # 함수 f와 반복 가능한(iterable) 자료형을 입력으로 받는다.
>  ```



### map & lambda 예시

---

>```python
># Input : ex = [1,2,3]
># Output : result = [6, 7, 8]
>
>result = list(map(lambda x:x+5, ex))
>```

 

