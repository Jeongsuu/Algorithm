# Programmers - H-Index

### 문제 설명
---
H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다. 어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다. 위키백과1에 따르면, H-Index는 다음과 같이 구합니다.

어떤 과학자가 발표한 논문 `n`편 중, `h`번 이상 인용된 논문이 `h`편 이상이고 나머지 논문이 `h`번 이하 인용되었다면 `h`의 최댓값이 이 과학자의 H-Index입니다.

어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.

<br>

### 제한사항
---
- 과학자가 발표한 논문의 수는 1편 이상 1,000편 이하입니다.
- 논문별 인용 횟수는 0회 이상 10,000회 이하입니다.


### 입출력 예
---
**citations return**

[3,0,6,1,5] / 3

<br>

### 제출코드
---

**1차 제출 코드**
```python
def solution(citiations):
    citiations.sort()
    answer = 0

    for i in range(len(citiations)):
        if citiations[i] == len(citiations[i:]):
            answer = len(citiations[i:])
    return answer
```

문제를 제대로 이해하지 못했다.

n편의 논문 중, h번 이상 인용된 논문이 h편 이상이고, 나머지 논문이 h번 이하  인용되었다면 h의 최댓값이 과학자의 `H-Index`라고 하였다.

<br>

**최종 제출 코드**
```python
def solution(citations):
    for idx, value in enumerate(sorted(citations)):
        if value >= len(citations[idx:]):
            return len(citations[idx:])
    return 0
```

<br>

위 문제는 설계하고 구현하는 것 보다 문제를 이해하는데 더 많은 시간이 소요되었다.

문제는 주어진 배열을 통하여 `H-Index`를 구하는 것이며 `H-Index`는 아래와 같의 정의하였다.

```
어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.
```

n편의 논문 중, h번 이상 인용된 논문의 개수가 h편 이상이며 나머지 논문이 h편 이하로 인용되었다면 h의 최댓값이 H-Index라고 하였다.

따라서, 인용된 논문의 개수와 인용된 횟수 모두 고려해야한다.

또한 최댓값을 찾아내라고 하였다.

코드를 살펴본다.

```python
for idx, value in enumerate(sorted(citations)):
```

`enumerate`를 통해 `idx`와 `value` 값을 오름차순 정렬된 배열에서 순차적으로 가져온다.

```python
if value >= len(citations[idx:])
```
문제 풀이의 핵심이 되는 한 줄이다.

value는 인용된 횟수가 들어가있다, 즉 위 코드는 인용 횟수가 인용된 논문의 개수보다 크거나 같다면 논문의 개수를 반환한다.

오름차순 정렬을 진행하였기에 **h번 이상 인용된 논문의 개수가 h편 이상인 경우**를 찾는 것이다.


~~오늘의 교훈 : 문제부터 확실히 이해하자~~