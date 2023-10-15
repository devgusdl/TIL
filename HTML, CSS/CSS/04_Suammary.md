# CSS Dimension
## CSS 크기 단위
css에서 사용하는 크기의 단위에는 %, em, px, cm, mm, inch 등이 있습니다.


그 중에서도 가장 많이 쓰이는 크기 단위는 다음과 같습니다.

 

1. 백분율 단위(%)

2. 배수 단위(em)

3. 픽셀 단위(px)

 

백분율 단위(%)는 기본 크기를 100%로 놓고, 그에 대한 상대적인 크기를 설정합니다.

배수 단위(em)는 해당 글꼴(font)의 기본 크기를 1em으로 놓고, 그에 대한 상대적인 크기를 설정합니다.

픽셀 단위(px)는 스크린의 픽셀(pixel)을 기준으로 하는 절대적인 크기를 설정합니다.

 ```
 <style>

    #large { font-size: 200%; }

    #small { font-size: 0.7em; }

    #fixed { font-size: 20px; }

</style>
 ```

## 크기(Dimension)
CSS를 이용하면 HTML 요소의 크기를 마음대로 설정할 수 있습니다.

CSS에서 크기 조절을 위해 사용할 수 있는 속성은 다음과 같습니다.

 
1. height

2. width

3. max-width

4. min-width

5. max-height

6. min-height

## height와 width 속성
- CSS에서 height와 width 속성을 설정할 때 그 크기가 가르키는 부분은 내용(content) 부분만을 대상으로 합니다.

- height와 width 속성은 HTML 요소의 높이와 너비를 각각 설정합니다.

- 기본 설정값은 auto이며, 웹 브라우저가 각 HTML 요소에 맞게 자동으로 높이와 너비를 설정해 줍니다.

- HTML 요소의 height와 width 속성으로 설정된 높이와 너비에 패딩(padding), 테두리(border), 마진(margin)의 크기는 포함되지 않습니다.

> 만일 width와 height로 지정한 콘텐츠 영역보다 실제 콘텐츠가 크면 콘텐츠 영역을 넘치게 된다는 것에 유의하여야 한다.
```
<style>

    div {

        width: 320px;

        padding: 10px;

        border: 5px solid maroon;

        margin: 0;

    }
</style>

```
기본적으로 width와 height 프로퍼티는 콘텐츠 영역을 대상으로 요소의 너비와 높이를 지정하므로 박스 전체 크기는 다음과 같이 계산할 수 있다.

![HEIGHT,WIDTH](box-model-calc.png)
>전체 너비:
>
> width + left padding + right padding + left border + right border + left margin + right margin
>
>전체 높이:
>
> height + top padding + bottom padding + top border + bottom border + top margin + bottom margin

- width와 height 프로퍼티를 비롯한 모든 박스모델 관련 프로퍼티(margin, padding, border, box-sizing 등)는 상속되지 않는다.

## 크기 속성 표
|속성|	설명|
|--|--|
|height	|해당 HTML 요소의 높이 설정|
|width|	해당 HTML 요소의 너비 설정|
|max-width	|해당 HTML 요소가 가질 수 있는 최대 너비(width) 설정|
|min-width	|해당 HTML 요소가 가질 수 있는 최소 너비(width) 설정|
|max-height|	해당 HTML 요소가 가질 수 있는 최대 높이(height) 설정|
|min-height|	해당 HTML 요소가 가질 수 있는 최소 높이(height) 설정|