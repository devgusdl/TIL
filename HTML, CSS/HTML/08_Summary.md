# HTML Form
## Form 요소
웹 페이지에서는 form 요소를 사용하여 사용자로부터 입력 받기 가능

또한, 사용자가 입력한 데이터를 서버로 보낼 때에도 form 요소를 사용

```
문법:
<form action="처리할페이지주소" method="get|post"></form>
```
action 속성은 입력받은 데이터를 처리할 서버 상의 스크립트 파일의 주소를 명시

이렇게 전달받은 데이터를 처리하는 스크립트 파일을 폼 핸들러(form-handler)라고 합니다.

method 속성은 입력받은 데이터를 서버에 전달할 방식을 명시합니다.


따라서 사용자가 form 요소를 통해 입력한 데이터는 action 속성에 명시된 위치로 method 속성의 방식을 통해 전달됩니다.

## Method 속성
method 속성을 통해 명시할 수 있는 form 요소의 전달 방식은 GET 방식과 POST 방식으로 나눠집니다.

- GET 방식
  - 주소에 데이터(data)를 추가하여 전달하는 방식

  - 데이터가 주소 입력창에 그대로 나타나며, 전송할 수 있는 데이터의 크기 또한 제한적

  - 따라서 검색 엔진의 쿼리(query)와 같이 크기가 작고 중요도가 낮은 정보를 보낼 때 주로 사용

 

- POST 방식
  - 데이터(data)를 별도로 첨부하여 전달하는 방식

  - 데이터가 외부에 드러나지 않으며, 전송할 수 있는 데이터의 크기 또한 제한이 없음

  - 따라서 보안성 및 활용성이 GET 방식보다 좋음



## Input
- 사용자로부터 데이터를 입력받기 위해 사용
- form 태그 내에 존재하여야 입력 데이터를 전송할 수 있으나 ajax를 사용할 시에는 form 태그 내에 존재하지 않아도 된다.
- 서버에 전송되는 데이터는 name 어트리뷰트를 키로, value 어트리뷰트를 값으로하여 key=value의 형태로 전송


|Attribute|Description|
|--|--|
|button	|버튼 생성|
|checkbox	|checkbox 생성|
|color	|컬러 선택 생성|
|date|	date control (년월일) 생성|
|datetime|	date & time control (년월일시분초) 생성. HTML spec에서 drop되었다.|
|datetime-local	|지역 date & time control (년월일시분초) 생성|
|email|	이메일 입력 form 생성. subumit 시 자동 검증한다.|
|file|	파일 선택 form 생성|
hidden	|감추어진 입력 form 생성|
|image	|이미지로 된 submit button 생성|
|month	|월 선택 form 생성|
|number|	숫자 입력 form 생성|
|password	|password 입력 form 생성|
|radio|	radio button 생성|
|range	|범위 선택 form 생성|
|reset	|초기화 button 생성|
|search	|검색어 입력 form 생성|
|tel	|전화번호 입력 form 생성|
|text	|텍스트 입력 form 생성|
|time	|시간 선택 form 생성|
|url	|url 입력 form 생성|
|week	|주 선택 입력 form 생성|

```python
<!DOCTYPE html>
<html>
  <body>
    <h3>button</h3>
    <input type="button" value="Click me" onclick="alert('Hello world!')">
    <hr>

    <h3>checkbox</h3>
    <input type="checkbox" name="fruit1" value="apple" checked> 사과<br>
    <input type="checkbox" name="fruit2" value="grape"> 포도<br>
    <input type="checkbox" name="fruit3" value="peach"> 복숭아<br>
    <hr>

    <h3>color</h3>
    <input type="color" name="mycolor">
    <hr>

    <h3>date</h3>
    <input type="date" name="birthday">
    <hr>

    <h3>datetime</h3>
    <input type="datetime" name="birthdaytime">
    <hr>

    <h3>datetime-local</h3>
    <input type="datetime-local" name="birthdaytime">
    <hr>

    <h3>email</h3>
    <input type="email" name="useremail">
    <hr>

    <h3>file</h3>
    <input type="file" name="myfile">
    <hr>

    <h3>hidden</h3>
    <input type="hidden" name="country" value="Norway">
    hidden filed는 사용자에 표시되지 않는다.
    <hr>

    <h3>image</h3>
    <input type="image" src="img/img_submit.gif" alt="Submit" width="48" height="48">
    <hr>

    <h3>month</h3>
    <input type="month" name="birthdaymonth">
    <hr>

    <h3>number</h3>
    <input type="number" name="quantity" min="2" max="10" step="2" value="2">
    <hr>

    <h3>password</h3>
    <input type="password" name="pwd">
    <hr>

    <h3>radio</h3>
    <input type="radio" name="gender" value="male" checked> 남자<br>
    <input type="radio" name="gender" value="female"> 여자<br>
    <hr>

    <h3>range</h3>
    <input type="range" name="points" min="0" max="10" step="1" value="5">
    <hr>

    <h3>reset</h3>
    <input type="reset">
    <hr>

    <h3>search</h3>
    <input type="search" name="googlesearch">
    <hr>

    <h3>submit</h3>
    <input type="submit" value="Submit">
    <hr>

    <h3>tel</h3>
    <input type="tel" name="mytel">
    <hr>

    <h3>text</h3>
    <input type="text" name="myname">
    <hr>

    <h3>time</h3>
    <input type="time" name="mytime">
    <hr>

    <h3>url</h3>
    <input type="url" name="myurl">
    <hr>

    <h3>week</h3>
    <input type="week" name="week_year">
  </body>
</html>

```

## Select, Option
`<select>` 및 `<option>`은 드롭다운 리스트(복수 리스트)를 만드는 태그입니다.
```
<select>
	<option value="ktx">KTX</option>
	<option value="itx">ITX 새마을</option>
	<option value="mugung">무궁화호</option>
</select>
```

##  Textarea
textarea 태그는 여러 줄의 글자를 입력할 때 사용
```
 <body>
    <textarea name="message" rows="10" cols="30">Write something here</textarea>
  </body>
```
## Button
- 사용자가 누를 수 있는 버튼 생성
- `<input type="button">`과 유사하지만 input 태그는 빈 태그인 반면 button 태그는 그렇지 않다. 따라서 button 요소에는 텍스트나 이미지 같은 콘텐츠를 사용 가능
```
<body>
    <button type="button" onclick="alert('Hello World!')">Click Me!</button>

    <input type="button" value="Click Me!" onclick="alert('Hello world!')">
  </body>
```

## Fieldset / Legend
- fieldset 태그는 관련된 입력 양식들을 그룹화할 때 사용
- legend 태그는 fieldset 태그 내에서 사용되야 하며 그룹화된 fieldset의 제목을 정의
```
 <fieldset>
        <legend>Login</legend>
        Username <input type="text" name="username">
        Password <input type="text" name="password">
</fieldset>
```