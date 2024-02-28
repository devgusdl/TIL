# 옵셔널 파라미터

파라미터에 '기본값(default value)'을 설정할 수 있는데요. 기본값을 설정해 두면, 함수를 호출할 때 파라미터에 값을 꼭 넘겨주지 않아도 됩니다. 이런 파라미터를 '옵셔널 파라미터(optional parameter)'라고 합니다. 필수로 넘겨줄 필요가 없으니까 '옵셔널'이라고 하는 거죠.

아래 코드를 보세요. myself() 함수를 호출할 때 한 번은 파라미터 nationality에 들어갈 값을 제공했고, 한 번은 제공하지 않았습니다. 각각 어떻게 출력되는지 살펴보세요.

```python
def myself(name, age, nationality="한국"):
    print("내 이름은 {}".format(name))
    print("나이는 {}살".format(age))
    print("국적은 {}".format(nationality))


myself("코드잇", 1, "미국")  # 옵셔널 파라미터를 제공하는 경우
print()
myself("코드잇", 1)  # 옵셔널 파라미터를 제공하지 않는 경우
```
```python
내 이름은 코드잇
나이는 1살
국적은 미국

내 이름은 코드잇
나이는 1살
국적은 한국
```

옵셔널 파라미터는 꼭 마지막에!
참고로 옵셔널 파라미터는 모두 마지막에 있어야 합니다. 아래처럼 옵셔널 파라미터를 중간에 넣으면 오류가 발생합니다.

```python
def myself(name, nationality="한국", age):
    print("내 이름은 {}".format(name))
    print("나이는 {}살".format(age))
    print("국적은 {}".format(nationality))


myself("코드잇", 1)  # 기본값이 설정된 파라미터를 바꾸지 않을 때
print()
myself("코드잇", "미국", 1)  # 기본값이 설정된 파라미터를 바꾸었을 때
```
```python
File "myself.py", line 1
     def myself(name, nationality = "한국", age):
               ^
SyntaxError: non-default argument follows default argument
```
이번 레슨은 어땠나요?