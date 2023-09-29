# Github (upload and download)

## 1. Github repository 생성
- 깃허브 `Repository` 탭에서 New 버튼으로 저장소를 생성
- 저장소 이름 작성, 컴퓨터에 있는 폴더랑 이름이 달라도 상관없음
- `(중요)` 저장소에 대한 설명 추가 "Add a README file" 체크
## 2.로컬 저장소 생성
- Git bash에서 `$ git init`으로 `.git파일` 생성
## 3. 로컬 저장소와 원격 저장소 연결
-  `$ git remote add origin [원격저장소 주소]`
- 형식: https://github.com/아이디/저장소이름.git

- 폴더에 원격 저장소가 연결되어 있는지 확인 할 때
```
연결된 원격 저장소 확인:
$ git remote -v
```

- 원격 저장소를 잘못 연결해서 다시 정하거나, 기존에 연결했던 것을 삭제 할 때
```
기존 원격 저장소와의 연결 삭제: 
$ git remote rm origin
```

## 4. 파일 업로드 준비

> `branch` : 독립적으로 어떤 작업을 진행하기 위한 개념. 필요에 의해 만들어지는 각각의 브랜치는 다른 브랜치의 영향을 받지 않고 영향을 주지 않기 때문에 여러 작업을 동시에 실행 가능. 

- `branch` 기본 이름은 main이다. 따라서 파일도 main branch에 올려줘야 하는데, 로컬 저장소 기본 이름은 master이기 때문에 master에서 main으로 바꿔줘야 한다.

```
브랜치 이름 바꾸기:
$ git branch -m master main

현재 브랜치 이름 확인:
$ git branch
```
- `merge` (병합)
```
/branch (main)
$ git merge new  -> new를 병합하겠다

/branch (main)
$ git log --oneline ->현재 상태 한줄로 확인
```
- `main` 영구적으로 변경 방법
```
브랜치 기본(default)이름 설정:

$ git config --global init.defaultBranch [브랜치 이름]
```
- `checkout` 
```
main으로 되돌릴 때:
$ git checkout main
```

- `Pull` (원격 저장소 파일 가져오기)
```
README.md가 있을 경우:
$ git pull origin [브랜치 이름]

아래처럼 끌어오는 곳 생략 가능 (현재 작업중인 곳으로):
$ git pull
```

## 5.How to upload 

![add-commit-push](https://res.cloudinary.com/practicaldev/image/fetch/s--Si7ksd-d--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://cdn-images-1.medium.com/max/800/1%2AdiRLm1S5hkVoh5qeArND0Q.png)


> `Working Directory`: 현재 파일을 작업(추가, 수정, 삭제)하고 있는 영역
>
> `Staging Area`: Working Directory에서 add 명령어를 통해 파일이 이동되는 영역, commit전의 상태
>
> `Repository`: commit과 push 명령어를 통해 최종적으로 commit한 사항을 원격 저장소로 업로드함


**업로드 순서**

### (1) `add` 
- 사용 방법
```
모든 변경사항을 올리는 경우:
$ git add .

특정한 파일만 올리는 경우:
$ git add [파일/디렉토리]
```
- add 전에 로컬 저장소에서 변경된 파일 상태 확인 필수
```
현재 버전상태 확인:
$ git status
```
- staging area에서 빼낼때
```
add한 파일 모두 취소:
$ git rm --cached -r .

특정 파일만 add 취소:
$ git rm --cached [파일]
```
### (2) `commit` 
- 사용 방법
```
$ git commit -m "commit message"
```
commit message는 commit이 어떤 변경사항을 담고 있는지 알려주는 글이니 잘 작성해주면 나중에 알아보기 좋음
### (3) `push`

로컬 -> 원격 저장소
```
로컬 저장소에서 원격 저장소로 올리기:
$ git push origin [브랜치 이름]

//또는: 아래처럼 목적지 생략 가능 (현재 작업중인 브랜치로 push됨):
$ git push
```

### [저장소가 이미 있는 경우]

```
$ git pull origin main (해당 경우)
$ git add .
$ git commit -m "commit message"
$ git push origin main
```

### 요약
```
저장소 생성 및 연결:
$ git init
$ git remote add origin [원격저장소 주소]
$ git branch -m master main

파일 업로드:
$ git pull (또는 git pull origin main)
$ git add .
$ git commit -m "commit message"
$ git push (또는 git push origin main)

추가적인 명령어:
$ git remote -v
$ git remote rm origin
$ git branch
$ git config --global init.defaultBranch [브랜치 이름]
$ git status
$ git rm --cached -r .
```
