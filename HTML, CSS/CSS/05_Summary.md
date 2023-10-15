# CSS 수평/ 수직 정렬(Horizontal & Vertical Centering) 
## justify-content (주축 이동)
- flex-start: 요소들을 컨테이너의 왼쪽으로 정렬
- flex-end: 요소들을 컨테이너의 오른쪽으로 정렬
- center: 요소들을 컨테이너의 가운데로 정렬
- space-between: 요소들 사이에 동일한 간격 생성
- space-around: 요소들 주위에 동일한 간격 생성

## align-items(교차축 이동)
- flex-start: 요소들을 컨테이너의 꼭대기로 정렬
- flex-end: 요소들을 컨테이너의 바닥으로 정렬
- center: 요소들을 컨테이너의 세로선 상의 가운데로 정렬
- baseline: 요소들을 컨테이너의 시작 위치에 정렬
- stretch: 요소들을 컨테이너에 맞도록 늘림

## flex-direction (주축을 결정)
- row: 요소들을 텍스트의 방향과 동일하게 정렬
- row-reverse: 요소들을 텍스트의 반대 방향으로 정렬
- column: 요소들을 위에서 아래로 정렬
- column-reverse: 요소들을 아래에서 위로 정렬

* Flex의 방향이 column일 경우 justify-content의 방향이 세로로, 
align-items의 뱡향이 가로로 바뀜

## order (특정 한명만 바꾸고싶을때)
> 특정 한명만 바꾸고 싶을때 order 속성을 각 요소에 적용할 수 있다.
order의 기본 값은 0이며, 양수나 음수로 변경 가능

## flex-wrap
- nowrap: 모든 요소들을 한 줄에 정렬
- wrap: 요소들을 여러 줄에 걸쳐 정렬
- wrap-reverse: 요소들을 여러 줄에 걸쳐 반대로 정렬

## flex-flow
- flex-direction과 flex-wrap이 자주 같이 사용되기 때문에, flex-flow가 이를 대체 가능
- ex) flex-flow: row wrap

## align-content
- flex-start: 여러 줄들을 컨테이너의 꼭대기에 정렬
- flex-end: 여러 줄들을 컨테이너의 바닥에 정렬
- center: 여러 줄들을 세로선 상의 가운데에 정렬
- space-between: 여러 줄들 사이에 동일한 간격 두기
- space-around: 여러 줄들 주위에 동일한 간격을 두기
- stretch: 여러 줄들을 컨테이너에 맞도록 늘림