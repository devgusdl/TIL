# HTML list
1. Unordered list(순서가 없는 리스트)

2. Ordered list(순서가 있는 리스트)

3. Definition list(정의 리스트)

## Unordered list(순서가 없는 리스트)
- `<ul>`태그를 사용하며, 여기에 포함되는 리스트요소는 `<li>`태그를 사용

```
<ul>

    <li>뻥튀기</li>

    <li>약과</li>

    <li>호두과자</li>

</ul>
```
CSS의 list-style-type 속성을 사용하면 리스트 요소 앞에 위치하는 마커(marker)를 다른 모양으로 변경 가능
- disc : 검정색 작은 원 모양 (기본설정)
- circle : 흰색 작은 원 모양
- square : 사각형 모양
```
<ul style="list-style-type: circle">
    <li></li>
</ul>
```
## Ordered list(순서가 있는 리스트)
- ` <ol>`태그를 사용하며, 여기에 포함되는 각각의 리스트 요소는 `<li>`태그를 사용
```
<ol>

    <li>마카롱</li>

    <li>스콘</li>

    <li>까눌레</li>

</ol>
```
CSS의 list-style-type 속성을 사용하면 리스트 요소 앞에 위치하는 마커(marker)를 다른 모양으로 변경할 수 있습니다.

- decimal : 숫자 (기본설정)
- upper-alpha : 영문 대문자
- lower-alpha : 영문 소문자
- upper-roman : 로마 숫자 대문자
- lower-roman : 로마 숫자 소문자
```
<ol style="list-style-type: upper-alpha">       
    <li></li>
</ol>
```
## Definition list(정의 리스트)
`<dl>`태그를 사용하며, `<dt>`태그에는 용어의 이름이 들어가고, `<dd>`태그에는 해당 용어에 대한 정의가 들어간다.
```
<dl>

    <dt>앙버터</dt>

    <dd>- 팥앙금과 버터가 들어간 빵</dd>

    <dt>소금빵</dt>

    <dd>- 버터 베이스로 만든 빵에 소금 올린 빵</dd>

</dl>
```