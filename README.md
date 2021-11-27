# 한양사이버대학교 졸업과제
## 최성호 H201843063
- [졸업과제URL 13.124.72.116:5000](http://13.124.72.116:5000)
- 현재 github에 모든 소스 올라와있습니다.

## 본문
### 프로젝트 이름
- 이메일 인증 OTP 개발
### 프로젝트 목적
- 홈페이지 로그인 시 이메일 인증 등의 OTP 본인인증 후 로그인하는 웹 페이지 개발

## Skills
- **HTML/CSS, Bootstrap**
- **JavaScript(ES6)**
- **Python, PyOTP**
- **Flask, SQLite3, SQL Alchemy(ORM)**
- **AWS EC2**

## FrontEnd
- **메인 페이지(로그인 전)**
  - ![main_ex1](https://user-images.githubusercontent.com/87958906/143644443-90e328bc-5cf7-4c89-98fe-845ec0b2ab5c.png)

- **메인 페이지(로그인 후)**
  - ![main_ex2](https://user-images.githubusercontent.com/87958906/143645413-90ff66c9-1855-48da-a7f8-b50f0127fd43.png)

- **로그인**
  - ![login](https://user-images.githubusercontent.com/87958906/143660350-145c66a3-d098-4892-9d71-8b0954d17551.png)

- **회원가입**
  - ![register](https://user-images.githubusercontent.com/87958906/143658058-c8249664-360f-428b-bc02-a234e0a57daf.png)

- **OTP체크**
  - ![OTP](https://user-images.githubusercontent.com/87958906/143658111-1305efe1-20a2-42be-a32b-c796e4ae0be8.png)
  - ![실제OTP](https://user-images.githubusercontent.com/87958906/143658167-fc36bcab-8cc1-48c6-baf1-b46450e71a54.png)

## BackEnd
- **DB는 sqlite 사용하여 사용자 정보를 받아옴(아래 예시)**
  - ![example_db](https://user-images.githubusercontent.com/87958906/139253432-3afa4ce7-6f9e-471a-805e-e62b360f77ea.png)

- **서버 호스팅 AWS EC2 무료 버전 이용**
  - ![example_aws](https://user-images.githubusercontent.com/87958906/139256174-2016343d-062c-461c-9921-98999d857072.PNG)

## TodoList
| 업무 | 해당사항 체크(✅,❎ ) |
| ------ | ------ |
| 제안서 작성 | ✅ |
| 계획서 작성 | ✅ |
| 개발 설계 | ✅ |
| 로그인 폼 개발 | ✅ |
| 로그인, 회원가입 로직 개발 | ✅ |
| 중간보고서 작성 | ✅ |
| OTP 로직 개발 | ✅ |
| 패키징 및 외부 접속 확인 | ✅ |
| 작품 제출 | ✅ |

## 과제 진행중 어려웠던 점
- 웹 프로젝트 경험이 없어 처음 시작이 상당히 어려워 공부하는 시간이 많이 들었습니다.
- 네트워크 이해 / html, js, flask의 이해 / DB, sql, sqlite의 이해 등.. 생각보다 공부할게 많았습니다.
- AWS를 처음으로 사용하여 방화벽설정, 백그라운드동작, SSH인증, 패키지업데이트 등 많은 시행착오가 있었습니다.
- github 사용이 생각보다 까다로웠습니다.

## 추가 개발 필요(해결완료)
- OTP 구현하여 이메일 인증된 사용자만 회원가입 (아직 API를 사용할지 직접 구현할지 구체적 구상)
- 사용자 목록 볼 수 있는 페이지 구현 (회원가입 페이지 외 메인페이지 구현하여 페이지 라우팅 추가)
- 로그인 페이지 구현 (패키징 및 외부 접속 확인 절차가 앞당겨지고, 로그인 페이지 구현이 늦어짐)
