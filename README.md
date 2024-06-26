## 2023-1-CECD3-24-5
------

2023년 1학기 동국대학교 컴퓨터공학종합설계 스물넷팀




*****



# 검증된 문제 생성 웹 서비스

### 팀원 구성
|학과|학번|팀원이름|
|:----:|:---:|:---:|
|컴퓨터공학과|2019113328|박근용|
|컴퓨터공학과|2020111655|심여은|
|컴퓨터공학과|2020111765|김소은|
|컴퓨터공학과|2020111802|장동겸|

*****

### 프로젝트 흐름도
<img width="692" alt="스크린샷 2023-08-20 오후 9 01 11" src="https://github.com/CSID-DGU/2023-1-CECD3-24-5/assets/87983309/a0344dff-2b30-45dc-9d10-e9a9ffef8d2d">


### 개발환경 및 오픈소스 활용
- Python
- React
- flask 
- Node.js
- Swagger

### 깃 사용법
1. 자신의 개발 브랜치는 feature/개발 내용으로 브랜치를 생성하여 제작한다
1. 머지는 Squash and Merge 방식을 사용한다.
1. 머지 진행시 conflict가 나지않는 경우 코드 리뷰없이 머지를 진행하고 만약 conflict가 나는 경우 해당 부분의 개발자와 상의하거나 전체 회의 시간에 머지를 진행한다.(단 자신이 결정할 수 있는 conflict 일 경우 독자적으로 결정 후 머지를 진행한다.)

### 깃 브랜치 전략
1. 자신의 개발 브랜치는 feature/개발 내용으로 브랜치를 생성하여 제작한다
1. 테스트 완료 후 feature 브랜치를 develop 브랜치로 머지한다(병합한 feature 브랜치를 삭제한다)
1. develop 브랜치를 master 브랜치로 머지한다
1. develop 브랜치로 배포 진행 후 발생하는 버그들은 develop에서 개선 후 master로 머지한다

### 코딩 컨벤션
1. 서비스 개발을 진행할 때 해당 서비스에 해당하는 컨트롤러, 서비스, 리포지토리를 모아놓는다.
1. 클래스 네이밍은 파스칼 케이스로 작성한다(ex: TestClass)
1. 클래스 변수는 클래스 이름의 카멜 케이스로 작성한다(ex: testClass)
1. 하나의 함수는 20문장이 넘지 않도록 노력한다

