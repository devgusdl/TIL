# CSS position
## position 속성
position 속성은 HTML 요소가 위치를 결정하는 방식을 설정합니다.

CSS에서 요소의 위치를 결정하는 방식에는 다음과 같이 4가지 방식이 있습니다.

 

1. 정적 위치(static position) 지정 방식

HTML 요소의 위치를 결정하는 가장 기본적인 방식은 정적 위치(static position) 지정 방식입니다.

 

position 속성값이 static으로 설정된 요소는 top, right, bottom, left 속성값에 영향을 받지 않습니다.

정적 위치(static position) 지정 방식은 단순히 웹 페이지의 흐름에 따라 차례대로 요소들을 위치시키는 방식입니다.
```
<style>

    div { position: static; }

</style>


```
2. 상대 위치(relative position) 지정 방식
   
상대 위치(relative position) 지정 방식은 해당 HTML 요소의 기본 위치를 기준으로 위치를 설정하는 방식입니다.

 

HTML 요소의 기본 위치란 해당 요소가 정적 위치(static position) 지정 방식일 때 결정되는 위치를 의미합니다.
```
<style>

    div.relative { position: relative; left: 30px; }

</style>
```

3. 고정 위치(fixed position) 지정 방식

고정 위치(fixed position) 지정 방식은 뷰포트(viewport)를 기준으로 위치를 설정하는 방식입니다. 

 

즉, 웹 페이지가 스크롤 되어도 고정 위치로 지정된 요소는 항상 같은 곳에 위치하게 됩니다.

```
<style>

    div.fixed { position: fixed; top: 0; right: 0; }

</style>
```
4. 절대 위치(absolute position) 지정 방식

절대 위치(absolute position) 지정 방식은 고정 위치가 뷰포트를 기준으로 위치를 결정하는 것과 비슷하게 동작합니다.

단지 뷰포트(viewport)를 기준으로 하는 것이 아닌 위치가 설정된 조상(ancestor) 요소를 기준으로 위치를 설정하게 됩니다.

하지만 위치가 설정된 조상(ancestor) 요소를 가지지 않는다면, HTML 문서의 body 요소를 기준으로 위치를 설정하게 됩니다.

```
<style>

    div.absolute { position: absolute; top: 50px; right: 0; }

</style>
```

### 정적 위치(static position) 지정 방식과 다른 방식들과의 차이점
정적 위치(static position) 지정 방식을 제외한 나머지 다른 방식(relative, fixed, absolute)들은 전부 어떤 기준에 대해 해당 요소의 상대적인 위치를 설정하는 방식입니다.

 

- 상대 위치(relative position) : 해당 요소가 정적 위치 지정 방식일 때의 위치에 상대적으로 위치함.
- 절대 위치(absolute position) : 위치가 설정된 바로 상위의 조상(ancestor) 요소에 상대적으로 위치함.

 ```
 <style>

    .static { position: static; }

    .relative { position: relative; }

    .fixed { position: fixed; }

    .absolute { position: absolute; }

</style>


 ```

 ### CSS position 속성
|속성	|설명|
|--|--|
|position|	HTML 요소의 위치를 결정하는 방식을 설정함.|
|top|	위치가 설정된 조상 요소의 위로부터의 여백을 설정함.|
|right|	위치가 설정된 조상 요소의 오른쪽으로부터의 여백을 설정함.|
|bottom	|위치가 설정된 조상 요소의 아래로부터의 여백을 설정함.|
|left|	위치가 설정된 조상 요소의 왼쪽으로부터의 여백을 설정함.|
|z-index|	겹쳐지는 요소들이 쌓이는 스택(stack)의 순서를 설정함.|
|clip|	절대 위치(absolute position) 지정 방식으로 위치한 요소를 자름.|
|cursor|	표시되는 마우스 커서의 모양을 설정함.|
|overflow	|내용(content)의 크기가 해당 요소의 박스(box)를 넘어갈 때 어떻게 처리할지를 설정함.|
|overflow-x	|내용(content)의 크기가 해당 요소의 수평 방향으로 박스(box)를 넘어갈 때 어떻게 처리할지를 설정함.|
<<<<<<< HEAD
|overflow-y|	내용(content)의 크기가 해당 요소의 수직 방향으로 박스(box)를 넘어갈 때 어떻게 처리할지를 설정함.|
=======
|overflow-y|	내용(content)의 크기가 해당 요소의 수직 방향으로 박스(box)를 넘어갈 때 어떻게 처리할지를 설정함.|
>>>>>>> 2860e77d125c3e3b1018df25f7c4b9b81e232cea
