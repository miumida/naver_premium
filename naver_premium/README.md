# NAVER CLOUD TTS(PREMIUM) FOR HOME ASSIANT

## Intro
NAVER에서 제공 하는 TTS를 HOME ASSIANT에 사용할 수 있습니다.

## How to Install
(1) 네이버 클라우드에 접속 하셔서 회원 가입을 해주세요.

(2) 네이버 콘솔로 접속 합니다.
https://console.ncloud.com/mc/solution/naverService/application?version=v2


(3) Product & Service를 클릭하고 AI·NAVER API를 클릭 합니다.
<img src="https://github.com/chohoo89/HomeAssiant_Componets/blob/master/image/naver_premium/1.jpg?raw=true">
<br><br><hr><br><br>
(4) Application 등록을 클릭 합니다.
<img src="https://github.com/chohoo89/HomeAssiant_Componets/blob/master/image/naver_premium/2.jpg?raw=true">
<br><br><hr><br><br>
(5) Application 이름은 아무거나 원하는걸로 설정 하고 Clova Premium Voice(CPV)를 체크 합니다.
<img src="https://github.com/chohoo89/HomeAssiant_Componets/blob/master/image/naver_premium/3.jpg?raw=true">
<br><br><hr><br><br>
(6) Web 서비스 URL 등록에 http://127.0.0.1 를 넣습니다. (본인의 HA주소를 넣어도 됩니다만.. 궂이..) 추가 커튼을 누르시고 등록 버튼을 눌러주세요.
<img src="https://github.com/chohoo89/HomeAssiant_Componets/blob/master/image/naver_premium/4.jpg?raw=true">
<br><br><hr><br><br>
(7) 등록 된 API 키에 인증 정보를 클릭 하고 Client ID, Client Secret을 복사 해두세요.
<img src="https://github.com/chohoo89/HomeAssiant_Componets/blob/master/image/naver_premium/5.jpg?raw=true">
<hr>
(8) HA의 config 파일 경로에 들어 갑니다.<br>
(초보자분들을 위해 설명을 드리면 config 파일 경로는 configuration.yaml 파일이 있는 경로 이고 hass.io를 설치 하신 분들은 /usr/share/hassio 경로 입니다)<hr>
(9) 해당 경로에 custom_components 폴더가 있는지 확인 후 폴더가 있다면 naver_premium 폴더를 만들어 주시고 없으시면 custom_components 폴더를 만드신 후 해당 폴더 안에 naver_premium 폴더를 만들어 주세요.<br>
(리눅스 사용중이고 hass.io를 사용 중이면 "mkdir /usr/share/hassio/custom_components/naver_premium" 를 입력 해주세요) <hr>
(10) `__init__.py, tts.py` 를 naver_premium 폴더안에 넣어 주세요.<br>
최종 경로는 `<config directory>/custom_components/naver_premium/__init__.py` , `<config directory>/custom_components/naver_premium/manifest.json` 입니다.<hr>
