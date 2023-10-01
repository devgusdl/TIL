# HTML structure
## Basic structure
```
<!DOCTYPE html>
<html>
    <head>
        <title>HTML문서의 제목</title>
    </head>
    <body>
        <h1>제목 크기1</h1>
        <h2>제목 크기 2</h2>
        <p>이 부분은 단락</p>
        <p>이 부분은 단락</p>
    </body>
</html>
```

`<!DOCTYPE html>` : 현재 문서가 HTML5 문서임을 명시

`<html>` : HTML 문서의 루트(root) 요소 정의

`<head>` : HTML 문서의 메타데이터(metadata) 정의

- 메타데이터(metadata)란 HTML 문서에 대한 정보(data)로 웹 브라우저에는 직접적으로 표현되지 않는 정보를 의미한다

- 이러한 메타데이터는 `<title>`, `<style>`, `<meta>`, `<link>`, `<script>`, `<base>`태그 등을 이용하여 표현 가능

`<title>` : HTML 문서의 제목(title)을 정의하며, 다음과 같은 용도로 사용됨

- 웹 브라우저의 툴바(toolbar)에 표시

- 웹 브라우저의 즐겨찾기(favorites)의 제목

- 검색 엔진의 결과 페이지에 제목


`<body>` : 웹 브라우저를 통해 보이는 내용(content) 부분

 
`<h1>` ~ `<h6>` : 제목(heading)


`<p>` : 단락(paragraph)

## Element structure

- HTML 요소(element)는 여러 속성을 가질 수 있으며 속성(attribute)은 해당 요소에 대한 추가적인 정보를 제공함
- 시작 태그로 시작, 종료 태그로 종료

![image](https://www.devkuma.com/docs/html/html_element2.png)

> 문법 : <태그이름 속성이름="속성값">


### 주의사항
- 속성이름은 소문자로 작성
- 속성값은 ""로 감싸기

## Semantic element
## Semantic tag란?
- Semantic: 의미의, 의미론적인
- 시멘틱 태그는 "의미 있는 태그"라는 뜻으로, 인터넷 검색엔진에 나의 웹 페이지가 잘 검색되고 해석될 수 있도록 HTML 코드를 작성할 때 사용하는 태그입니다.


|`semantic 요소`|`non-semantic 요소`|
|--|--|
|form, table, img 등이 있으며 이들 태그는 content의 의미를 명확히 설명한다,|div, span 등이 있으며 이들 태그는 content에 대하여 어떤 설명도 하지 않는다.|

## 레이아웃용 시멘틱 태그별 의미

|태그|뜻|
|--|--|
|header|HTML 문서의 상단(제목부분)을 나타냅니다.|
|nav|navigation(탐색)의 줄임말로, 클릭해서 다른 페이지로 넘어갈 수 있는 여러 메뉴들을 배치하는 곳입니다.|
|section|본문 내용을 나타냅니다.|
|article|독립적인  내용을 나타냅니다.|
|aside|사이드바처럼 좌우에 위치하는 공간입니다.|
|footer|문서의 하단부분이며, 내용요약이나 저작권을 나타내는 등의 부분입니다.|
|main|문서의 중요 내용을 나타냅니다.|
|figure|그림, 표 등의 독립적인 내용을 나타냅니다.|

![image](https://blog.kakaocdn.net/dn/1WQJm/btrDERMqdAM/TftCe5NH7NFkUmFikm6U30/img.png)