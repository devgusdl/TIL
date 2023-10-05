# HTML Table
테이블(Table)이란 여러 종류의 데이터(data)를 보기 좋게 정리하여 보여주는 표

## Table 태그 구성
1. `<tr>`태그는 테이블에서 열을 구분

2. `<th>`태그는각 열의 제목을 나타내며, 모든 내용은 자동으로 굵은 글씨에 가운데 정렬

3. `<td>`태그는 테이블의 열을 각각의 셀(cell)로 나눔

```
<table style="width:100%">

    <tr style="background-color:lightgrey">

        <th>수달</th>

        <th>범고래</th>      

    </tr>

    <tr>

        <td>북극곰</td>

        <td>펭귄</td>

    </tr>

</table>
```

## Table absorption(테이블 병함)

###  열(column) 병합
`colspan` 속성을 사용하면 테이블의 `열(column)`을 합칠 수 있습니다.
```
<table style="width:100%">

    <tr>

        <td>병아리</td>

        <td colspan="2">거북이</td>        

    </tr>

    <tr>

        <td>물고기</td>

        <td>강아지</td>        

        <td>고양이</td>

    </tr>

</table>
```
### 행(row) 병합
`rowspan` 속성을 사용하면 테이블의 `행(row)`을 합칠 수 있습니다.
```
<table style="width:100%">

    <tr>

        <td rowspan="2">상어</td>

        <td>문어</td>        

        <td>방어</td>

    </tr>

    <tr>

        <td>소라</td>        

        <td>오징어</td>

    </tr>

</table>
```

### 열(column)과 행(row) 병합
```
<table style="width:100%">

    <tr>

        <td colspan="6">1</td>

    </tr>

    <tr>

        <td colspan="6">2</td>

    </tr>

    <tr>

        <td rowspan="3">3</td>

        <td rowspan="3">4</td>

        <td colspan="2">5</td>

        <td>6</td>

        <td>7</td>

    </tr>

</table>
```

## Caption(캡션)
`<caption>`태그를 사용하면 테이블 상단에 제목이나 짧은 설명 추가 가능
```
<table style="width:100%">

    <caption>벌레</caption>

    <tr>

        <td>개미</td>

        <td>나비</td>

        <td>벌</td>    

    </tr>

</table>
```

## Table style 적용 예시
Table을 style을 꾸밀 수 있다.
```
  <style>
    table {
      width: 50%;
      border: 1px solid black;
      border-collapse: collapse;
    }
    th, td {
      border: 1px solid #444444;
      padding: 10px;
      text-align: center;
    }
  </style>
```