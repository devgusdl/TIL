# CSS 기본속성(텍스트 및 글꼴)
## 1. CSS 텍스트
### 1.1 color
color 속성은 텍스트의 색상을 설정합니다.

 

웹 페이지에서 텍스트의 기본 색상은 검정색입니다.

`<body>`태그에 명시된 color 속성값은 웹 페이지 내의 모든 텍스트 요소에 적용됩니다.

하지만 각 요소별로 따로 명시된 color 속성값이 있다면, 해당 속성값이 `<body>`태그에 명시된 속성값보다 우선 적용됩니다.
```
<style>

    body { color: red; }

    p { color: maroon; }

</style>
```
### 1.2 direction

direction 속성은 텍스트가 써지는 방향을 설정합니다.

 

웹 페이지에서 텍스트는 기본적으로 왼쪽에서 오른쪽 방향으로 써집니다.

direction 속성이 left-to-right(ltr)일 때는 기본 설정처럼 텍스트가 왼쪽에서 오른쪽 방향으로 써집니다.

하지만, direction 속성이 right-to-left(rtl)일 때는 텍스트가 반대 방향인 오른쪽에서 왼쪽 방향으로 써집니다.

다음 예제는 "객체 지향 프로그래밍"이라는 문자열을 한글과 아랍어로 각각 나타낸 예제입니다.
```
<style>

    .rightToLeft { direction: rtl; }

</style>
```
### 1.3 letter-spacing
letter-spacing 속성은 텍스트 내에서 글자 사이의 간격을 설정합니다.
```
<style>

    .decLetterSpacing { letter-spacing: -3px; }

    .incLetterSpacing { letter-spacing: 10px; }

</style>
```

### 1.4 word-spacing
word-spacing 속성은 텍스트 내에서 단어 사이의 간격을 설정합니다.

letter-spacing 속성과는 달리 문자 간의 간격이 아닌 단어 간의 간격을 기준으로 설정합니다.
```
<style>

    .decWordSpacing { word-spacing: -3px; }

    .incWordSpacing { word-spacing: 10px; }

</style>
```

### 1.5 text-indent
text-indent 속성은 단락의 첫 줄에 들여쓰기할지 안 할지를 설정합니다.

웹 페이지에서 단락은 기본적으로 들여쓰기가 설정되어 있지 않습니다.
```
<style>

    .paraIndent { text-indent: 30px; }

</style>
```
### 1.6 text-align
text-align 속성은 텍스트의 수평 방향 정렬을 설정합니다.

text-align 속성으로 설정된 정렬 방향은 text-direction 속성과는 상관없이 우선적으로 적용됩니다.
```
<style>

    h2 { text-align: left; }

    h3 { text-align: right; }

    h4 { text-align: center; }

</style>
```
### 1.7 text-decoration
text-decoration 속성은 텍스트에 여러 가지 효과를 설정하거나 제거하는데 사용합니다.
```
<style>

    h2 { text-decoration: overline; }

    h3 { text-decoration: line-through; }

    h4 { text-decoration: underline; }

    a { text-decoration: none; }

</style>
```
### 1.8 text-transform
text-transform 속성은 텍스트에 포함된 영문자에 대한 대소문자를 설정합니다.

이 속성은 텍스트에 포함된 모든 영문자를 대문자나 소문자로 변경시켜 줍니다.

또한, 단어의 첫 문자만을 대문자로 변경시킬 수도 있습니다.
```
<style>

    h2 { text-transform: uppercase; }

    h3 { text-transform: lowercase; }

    h4 { text-transform: capitalize; }

</style>


```
### 1.9 line-height
line-height 속성은 텍스트의 줄 간격을 설정합니다.
```
<style>

    .narrowLineHeight { line-height: 0.8; }

    .wideLineHeight { line-height: 1.8; }

</style>
```
### 1.10 text-shadow
text-shadow 속성은 텍스트에 간단한 그림자 효과를 설정합니다.
```
<style>

    h2 { text-shadow: 2px 1px #3399CC; }

</style>
```
### 요약
|속성	|설명|
|--|--|
|color	|텍스트의 색상을 설정|
|direction	|텍스트가 쓰이는 방향을 설정|
|letter-spacing	|텍스트 내에서 문자 사이의 간격을 설정|
|word-spacing	|텍스트 내에서 단어 사이의 간격을 설정|
|text-indent	|단락의 첫 줄을 들여쓰기할지 안 할지를 설정|
|text-align	|텍스트의 수평 방향 정렬을 설정|
|text-decoration	|텍스트에 여러 가지 효과를 설정하거나 제거|
|text-transform	|텍스트에 포함된 영문자에 대한 대소문자를 설정|
|line-height|	텍스트의 줄 간격을 설정|
|text-shadow	|텍스트에 그림자 효과를 설정|
|unicode-bidi	|direction 속성과 같이 사용하여 텍스트의 기본 출력 방향을 설정|
|vertical-align	HTML |요소 내의 수직 방향 정렬을 설정|
|white-space	HTML| 요소 내의 여백을 설정|

## 2 CSS 글꼴
### 2.1 font-family
font-family 속성은 하나의 글꼴만을 설정할 수도 있고, 여러 개의 글꼴을 같이 설정할 수도 있습니다.

font-family 속성값이 여러 개의 글꼴로 설정되어 있으면, 웹 브라우저는 위에서부터 순서대로 글꼴을 읽어 들입니다.

만약 사용자의 컴퓨터에 첫 번째로 읽어 들인 글꼴이 없으면 다음 글꼴을 확인하게 됩니다.

이런 방식으로 계속해서 읽어 들인 글꼴이 존재하는지를 확인하여, 읽어 들인 글꼴이 사용자의 컴퓨터에 존재하면 해당 글꼴로 표시하게 됩니다.

 

글꼴의 이름이 한 단어 이상으로 이루어지면 반드시 따옴표를 사용하여 둘러 쌓아야 합니다.

또한, 여러 개의 글꼴을 나열할 때에는 쉼표(,)로 구분 짓습니다.
```
<style>

    .serif { font-family: "Times New Roman", Times, serif; }

    .sansserif { font-family: Arial, Helvetica, sans-serif; }

</style>
```
### 2.2 font-style
font-style 속성은 주로 이탤릭체를 사용하기 위해 사용하며, 다음과 같이 3가지의 속성값을 가집니다.

 

- normal : 텍스트에 어떠한 스타일도 적용하지 않습니다.

- italic : 텍스트를 이탤릭체로 나타냅니다.

- oblique : 텍스트를 기울입니다. 이 속성값은 italic과 매우 유사하지만 지원하는 웹 브라우저가 거의 없습니다.
```
<style>

    .normal { font-style: normal; }

    .italic { font-style: italic; }

    .oblique { font-style: oblique; }

</style>
```
### 2.3 font-variant
font-variant 속성은 속성값이 small-caps로 설정되면, 텍스트에 포함된 영문자 중 모든 소문자를 작은 대문자(small-caps) 글꼴로 변경시킵니다.

이때 영문자 중 대문자는 기존 크기 그대로 출력합니다.

작은 대문자(small-caps) 글꼴이란 텍스트의 기존 대문자보다는 약간 작은 크기의 대문자를 의미합니다.

```
<style>

    .normal { font-variant: normal; }

    .smallCaps { font-variant: small-caps; }

</style>
```
### 2.4 font-weight
font-weight 속성은 텍스트를 얼마나 두껍게 표현할지를 설정합니다.

사용할 수 있는 속성값에는 lighter, normal, bold, bolder 등이 있습니다.

또한, 100, 200, 300, ... , 900 등과 같이 숫자로 텍스트의 두께를 설정할 수도 있습니다.
```
<style>

    .normal { font-weight: normal; }

    .bold { font-weight: 600; }

    .bolder { font-weight: bolder; }

</style>


```
### 2.5 font-size
font-size 속성은 텍스트의 크기를 설정합니다.

 

웹 디자인에서 텍스트의 크기는 매우 중요한 표현 요소입니다. 

하지만 제목을 표현하기 위해서 텍스트의 크기만을 크게 해서는 안 됩니다.

이때에는 제목을 위한 HTML 요소인 `<h1>`태그부터 `<h6>`태그를 사용해야 합니다.

### font-size의 크기 단위
font-size 속성값에 자주 사용되는 대표적인 크기 단위는 다음과 같습니다.

 

백분율 단위(%)는 기본 크기를 100%로 놓고, 그에 대한 상대적인 크기를 설정합니다.

배수 단위(em)는 해당 글꼴(font)의 기본 크기를 1em으로 놓고, 그에 대한 상대적인 크기를 설정합니다.

픽셀 단위(px)는 스크린의 픽셀(pixel)을 기준으로 하는 절대적인 크기를 설정합니다.
```
<style>

    body { font-size: 100%; }

    #large { font-size: 2.5em; }

    #small { font-size: 0.7em; }

    #fixed { font-size: 20px; }

</style>
```

CSS font 속성
|속성	|설명|
|--|--|
|font	|모든 font 속성을 이용한 스타일을 한 줄에 설정할 수 있음.
|font-family	|텍스트의 글꼴 집합(font family)을 설정함.|
|font-style|	주로 이탤릭체를 사용하기 위해 사용|
|font-variant|텍스트에 포함된 영문자 중 소문자만을 작은 대문자(small-caps) 글꼴로 변경|
|font-weight|텍스트를 얼마나 두껍게 표현할지를 설정함.
|font-size	|텍스트의 크기를 설정함.|