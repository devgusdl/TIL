# HTML link
## Hyperlink (하이퍼링크) 사용법
- `<a>`태그의 href 속성은 링크를 클릭하면 연결할 페이지나 사이트의 URL 주소를 명시
- `<a>`태그는 텍스트나 단락, 이미지 등 다양한 HTML 요소에 사용
```
문법:
<a href="링크주소">HTML 링크</a>

ex)
<a href="/html/intro">

    <h2>이 링크를 클릭해 보세요!</h2>

</a>
```

## Target 속성
|target 속성 값|설명|
|--|--|
|_blank|링크로 연결된 문서를 새 창이나 새 탭에서 오픈|
|_self|링크로 연결된 문서를 현재 프레임(frame)에서 오픈 (기본설정)|
|_parent|링크로 연결된 문서를 부모 프레임(frame)에서 오픈|
|_top|링크로 연결된 문서를 현재 창의 가장 상위 프레임(frame)에서 오픈|
|프레임(frame) 이름|링크로 연결된 문서를 지정된 프레임(frame)에서 오픈|

# HTML style
HTML 스타일(Style)
HTML 요소의 style 속성(attribute)을 이용하면 CSS 스타일을 HTML 요소에 직접 설정 가능

하지만 이러한 style 속성을 이용한 방법은 오직 단 하나의 HTML 요소에만 스타일을 적용 가능
```
<태그이름 style="속성이름:속성값">
```

### 배경색 변경

```
<h1 style="background-color:white">

    style 속성을 이용한 배경색 변경

</h1>
```

### 글자색 변경

```
<h1 style="color:maroon">
    style 속성을 이용한 글자색 변경

</h1>
```

### 글자 크기 변경

```
<h1 style="font-size:250%">
    style 속성을 이용한 글자 크기 변경

</h1>

```

### 문단 정렬 변경

```
<h1 style="text-align:center">

    style 속성을 이용한 문단 정렬 변경

</h1>
```

### 여러 스타일의 설정
style 속성을 이용하여 여러 CSS 스타일을 한 번에 적용 가능
```
<h1 style="background-color:white; color:maroon; font-size:150%; text-align:center">

    style 속성을 이용하여 한 번에 스타일링 하기!

</h1>
```