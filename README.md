# Hydroponics-Desktop-App

## Overview
- [ScreenShot](#ScreenShot)
- [Introduce](#Introduce)
- [Requirement](#Requirement)
- [Reference](#Reference) 
- [License](#License)
## ScreenShot


<img src="screenshots/before_login.png" alt="로그인 전"></img>
<img src="screenshots/after_login.png" alt="로그인 후"></img> 
<img src="screenshots/info.png" alt="개요 창"></img>
<img src="screenshots/graph.png" alt="그래프 창"></img>
<img src="screenshots/kakao_login.png" alt="셀레니움 로그인 창"></img>
<img src="screenshots/gallery.png" alt="이미지 창"></img>
<img src="screenshots/setting.png" alt="설정 창"></img>

## Introduce
- 서버 설명
  - c++ 기반의 소켓 서버가 존재합니다.
  - 이 서버는 작물의 수경재배를 관리하고 온도와 습도, 물의 성분, 작물의 이미지 등을 각종 센서들을 통해 전달받아 작물이 정상적으로 성장할 수 있도록 환경을 조절하는 기능을 가집니다.
  - 또한 그러한 센서들의 정보와 회원 정보를 관리하기 위해 내부에 DB를 가지고 있습니다.
  - 서버는 http 프로토콜을 사용하도록 코딩되어있으며 GET, POST와 같은 request에 응답합니다.
  - 서버와 앱은 Json 타입으로 데이터를 송수신합니다.
- 앱 설명
  - 파이썬에서 화면을 출력하는 GUI 라이브러리로 tkinter를 사용합니다.
  - 설정 변경의 권한을 제한하기 위해 카카오 로그인 API를 사용하며 토큰 기반의 사용자 인증 기능을 구현하였습니다.
  - 로그인을 위해서는 외부 웹 브라우저를 사용하여야 했기에 celenium을 사용하여 해당 기능을 구현하였습니다.
  - 작물의 상태를 나타내는 그래프를 그리기 위해 matplotlib 라이브러리를 사용하였습니다. 


## Requirement

- celenium을 사용하므로 크롬과 크롬 드라이버가 반드시 설치되어있어야합니다.
  - 크롬 드라이버 다운로드 링크 https://chromedriver.chromium.org/downloads
- http 서버와 통신을 위해 requests 모듈이 필요합니다.
- gui 구성을 위해 tkinter 모듈이 필요합니다.
- 이미지 사이즈 조정을 위해 PIL 모듈이 필요합니다.
- 그래프를 그리기 위해 matplotlib 모듈이 필요합니다.

## Reference

- 참고링크 폴더 참조

## License
- MIT License
