# Numpy 기본 통계
numpy 라이브러리는 기본적인 통계 기능도 제공합니다.

## 최댓값, 최솟값
max 메소드와 min 메소드를 사용하면 numpy array의 최댓값과 최솟값을 구할 수 있습니다.
```python
import numpy as np

array1 = np.array([14, 6, 13, 21, 23, 31, 9, 5])

print(array1.max()) # 최댓값
print(array1.min()) # 최솟값
31
5
```
## 평균값
mean 메소드를 사용하면 numpy array의 평균값을 구할 수 있습니다.
```python
import numpy as np

array1 = np.array([14, 6, 13, 21, 23, 31, 9, 5])

print(array1.mean()) # 평균값
15.25
```
위 예시에서, 총합(14+6+13+21+23+31+9+5)을 총 개수(8)로 나누면 15.25입니다.

## 중앙값
median 메소드를 사용하면 중간값을 구할 수 있는데요. 특이하게 median은 numpy array의 메소드가 아니라 numpy의 메소드입니다.
```python
import numpy as np

array1 = np.array([8, 12, 9, 15, 16])
array2 = np.array([14, 6, 13, 21, 23, 31, 9, 5])

print(np.median(array1)) # 중앙값
print(np.median(array2)) # 중앙값
12.0
13.5
```
array1을 정렬하면 중앙값이 
12
입니다.

array2에는 짝수개의 요소가 있기 때문에 중앙값이 13과 14
 두 개입니다. 둘의 평균값을 내면 13.5입니다.

## 표준 편차, 분산
표준 편차와 분산은 값들이 평균에서 얼마나 떨어져 있는지 나타내는 지표입니다. 잘 모르신다면 일단 넘어가셔도 좋습니다.
```python
import numpy as np

array1 = np.array([14, 6, 13, 21, 23, 31, 9, 5])

print(array1.std()) # 표준 편차
print(array1.var()) # 분산
8.496322733983215
72.1875
```