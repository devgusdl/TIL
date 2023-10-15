# CSS Property(색상 및 배경)
## 1. Color(색상)
CSS에서 색을 표현하는 방법에는 다음과 같이 세 가지 방법이 있습니다. 

## 1.1 색상 이름으로 표현
W3C에서 정의한 16개의 HTML4 표준 색상 이름은 다음과 같습니다.
```
<style>

    .blue { color: blue; }

    .green { color: green; }

    .silver { color: silver; }

</style>
```

## 1.2 RGB 색상값으로 표현
모니터나 스크린은 빨간색(Red), 녹색(Green), 파란색(Blue)을 혼합하여 색을 표현합니다.

따라서 HTML에서도 이 세 가지 색을 가지고 색을 표현하는 RGB 색상을 사용합니다.

RGB 색상의 기본색(Red, Green, Blue)은 각각 0부터 255까지의 범위를 가집니다.
```
<style>

    .blue { color: rgb(0,0,255); }

    .green { color: rgb(0,128,0); }

    .silver { color: rgb(192,192,192); }

</style>
```
## 1.3. 16진수 색상값으로 표현
16진수 색상값은 RGB 색상값을 각각 16진수로 변환한 것입니다.

따라서 RGB 색상의 기본색(Red, Green, Blue)은 각각 00부터 FF까지의 범위를 가집니다.

예를 들면, 녹색을 나타내는 RGB 색상값 rgb(0,255,0)은 16진수 색상값으로는 #00FF00이 됩니다.
```
<style>

    .blue { color: #0000FF; }

    .green { color: #008000; }

    .silver { color: #C0C0C0; }

</style>
```

## 2.Background(배경)

### 2.1 background-color
background-color 속성은 해당 HTML 요소의 배경색(background color)을 설정합니다.
```
<style>

    body { background-color: lightblue; }

    h1 { background-color: rgb(255,128,0); }

    p { background-color: #FFFFCC; }

</style>
```
### 2.2 background-image
background-image 속성은 해당 HTML 요소의 배경으로 나타날 배경 이미지(image)를 설정합니다.

설정된 배경 이미지는 기본 설정으로 HTML 요소 전체에 걸쳐 반복되어 나타납니다.
```
<style>

    body { background-image: url("/examples/images/img_background_good.png"); }

</style>
```
배경 이미지를 사용할 때에는 이미지가 본문의 텍스트를 방해하지 않도록 주의를 기울여야 합니다.
```
<style>

    body { background-image: url("/examples/images/img_background_bad.png"); }

</style>
```
### 2.3 background-repeat
배경 이미지는 기본 설정으로 수평과 수직 방향으로 모두 반복되어 나타납니다.

background-repeat 속성을 이용하면 이러한 배경 이미지를 수평이나 수직 방향으로만 반복되도록 설정할 수 있습니다.

 

다음 예제는 배경 이미지의 수평 반복을 보여줍니다.
```
<style>

    body { background-image: url("/examples/images/img_man.png"); background-repeat: repeat-x; }

</style>
```
다음 예제는 배경 이미지의 수직 반복을 보여줍니다.
```
<style>

    body { background-image: url("/examples/images/img_man.png"); background-repeat: repeat-y; }

</style>
```

배경 이미지가 반복되지 않고 한 번만 나타나게 할 수도 있습니다.
```
<style>

    body { background-image: url("/examples/images/img_man.png"); background-repeat: no-repeat; }

</style>
```
### 2.4 background-position
background-position 속성은 반복되지 않는 배경 이미지의 상대 위치(relative position)를 설정합니다.
```
<style>

    body {

        background-image: url("/examples/images/img_man.png");

        background-repeat: no-repeat;

        background-position: top right;

    }

</style>
```
이 속성에서 사용할 수 있는 키워드의 조합은 다음과 같습니다.

 

1. left top

2. left center

3. left bottom

4. right top

5. right center

6. right bottom

7. center top

8. center center

9. center bottom

 

또한, 퍼센트(%)나 픽셀(px)을 사용하여 상대 위치를 직접 명시할 수도 있습니다.

이때 상대 위치를 결정하는 기준은 해당 요소의 왼쪽 상단(left top)이 됩니다.

 

다음 예제는 배경 이미지의 상대 위치를 픽셀 단위로 직접 명시한 예제입니다.
```
<style>

    body {

        background-image: url("/examples/images/img_man.png");

        background-repeat: no-repeat;

        background-position: 100px 200px;

    }

</style>
```
### 2.5 background-attachment

background-attachment 속성을 사용하여 위치가 설정된 배경 이미지를 해당 위치에 고정시킬 수도 있습니다.

이렇게 고정된 배경 이미지는 스크롤과는 무관하게 화면의 위치에서 이동하지 않습니다.

```
<style>

    body {

        background-image: url("/examples/images/img_man.png");

        background-repeat: no-repeat;

        background-position: left bottom;

        background-attachment: fixed;

    }

</style>
```
### 요약 
|속성|설명|
|--|--|
|background|모든 background 속성을 이용한 스타일을 한 줄에 설정 가능|
|background-color|HTML 요소의 배경색을 설정|
|background-image|HTML 요소의 배경 이미지를 설정|
|background-repeat|설정된 배경 이미지의 반복 유무를 설정|
|background-position|반복되지 않는 배경 이미지의 상대 위치를 설정|
|background-attachment|배경 이미지를 스크롤과는 무관하게 해당 위치에 고정|