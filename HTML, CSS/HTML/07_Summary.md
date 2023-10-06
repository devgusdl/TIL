# HTML media

## Image 
웹페이지에 이미지 삽입
```
    직접 가지고 있는(local) 파일 위치:
    <img src="./html5.png" alt="html5 로고 이미지" width="300">

    외부 이미지 주소
    <img src="https://blog.kakaocdn.net/dn/GG2Ca/btqBdULBrbA/47T2kcAVIfybTSqkRk3z8K/img.jpg" alt="html5 로고 이미지" width="300">

  ```
  |attribute|Description|
  |--|--|
  |src|이미지 파일 경로|
  |alt|	이미지 파일이 없을 경우 표시되는 문장|
  |width|이미지의 너비 (CSS에서 지정하는 것이 일반적)|
  |height|이미지의 높이 (CSS에서 지정하는 것이 일반적)|

  ## Video 
  웹페이지에 비디오 삽입
  ```
     <video width="640" height="360" controls>
      <source src="assets/video/wildlife.mp4" type="video/mp4">
      <source src="assets/video/wildlife.webm" type="video/webm">
    </video>
  ```

  |attribute|Description|
  |--|--|
  |src|동영상 파일 경로|
  |poster|	동영상 준비 중에 표시될 이미지 파일 경로|
  |preload|재생 전에 동영상 파일을 모두 불러올 것인지 지정|
  |autoplay|동영상 파일을 자동의 재생 개시할 것인지 지정|
  |loop|	동영상을 반복할 것인지 지정|
  |controls|동영상 재생 도구를 표시할 것인지 지정. 재생 도구의 외관은 브라우저마다 차이가 있다.|
  |width|	동영상의 너비를 지정|
  |height|동영상의 높이를 지정|