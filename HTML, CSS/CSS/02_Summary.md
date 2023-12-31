# CSS 적용
HTML 문서에 CSS 스타일을 적용할 때에는 다음과 같이 세 가지 방법을 사용할 수 있습니다.

1. 인라인 스타일(Inline style)

2. 내부 스타일 시트(Internal style sheet)

3. 외부 스타일 시트(External style sheet)

### (1) 인라인 스타일(Inline style)
인라인 스타일이란 HTML 요소 내부에 style 속성을 사용하여 CSS 스타일을 적용하는 방법입니다.

이러한 인라인 스타일은 해당 요소에만 스타일을 적용할 수 있습니다.
```
<body>

    <h2 style="color:green; text-decoration:underline">

        인라인 스타일을 이용하여 스타일을 적용하였습니다.

    </h2>

</body>
```

### (2) 내부 스타일 시트(Internal style sheet)
내부 스타일 시트를 이용하는 방법은 HTML 문서 내의 <head>태그에 <style>태그를 사용하여 CSS 스타일을 적용합니다.

이러한 내부 스타일 시트는 해당 HTML 문서에만 스타일을 적용할 수 있습니다.
```
<head>

    <style>

        body { background-color: lightyellow; }

        h2 { color: red; text-decoration: underline; }

    </style>

</head>
```
### (3) 외부 스타일 시트(External style sheet)
외부 스타일 시트를 이용하는 방법은 웹 사이트 전체의 스타일을 하나의 파일에서 변경할 수 있도록 해줍니다.

외부에 작성된 이러한 스타일 시트 파일은 .css 확장자를 사용하여 저장됩니다.

스타일을 적용할 웹 페이지의 <head>태그에 <link>태그를 사용하여 외부 스타일 시트를 포함해야만 스타일이 적용됩니다.
```
<head>

    <link rel="stylesheet" href="/examples/media/expand_style.css">

</head>
```

### 스타일 적용의 우선순위
위에서 설명한 스타일 적용 방법들이 혼합되어 사용될 경우, 최종적으로 적용되는 스타일은 다음 순서에 따라 결정됩니다.

 

1. 인라인 스타일 (HTML 요소 내부에 위치함)

2. 내부 / 외부 스타일 시트 (HTML 문서의 head 요소 내부에 위치함)

3. 웹 브라우저 기본 스타일

 

예를 들어 인라인 스타일이 적용된 태그는 내부나 외부 스타일 시트와는 상관없이 무조건 인라인 스타일이 적용됩니다.

또한, 내부 스타일 시트와 외부 스타일 시트는 가장 마지막에 적용된 스타일 시트가 적용됩니다.

```
<link rel="stylesheet" href="/examples/media/expand_style.css">

...

<h2>이 부분은 외부 스타일 시트만이 적용됩니다.</h2>

<h2 style="color:maroon; text-decoration:line-through"> 이 부분은 인라인 스타일과 외부 스타일 시트가 둘 다 적용됩니다. </h2>
```

따라서 웹 사이트의 스타일 적용은 외부 스타일 시트를 사용하는 것이 유지 보수도 편하며, 가장 안정적입니다.

하지만 우리 수업에서는 CSS 파일을 매번 보여줄 수 없으므로, 대부분의 예제에서 내부 스타일 시트를 사용할 것입니다.