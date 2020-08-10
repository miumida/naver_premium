# NAVER CLOUD TTS(PREMIUM) FOR HOME ASSIANT

## ■ Intro
### 이 컴포넌트는 유료 컴퍼넌트 입니다. 1회 호출에 5원 입니다. (네이버에서 부과) <br>
Cache 기능이 있어 한번 이라도 호출 했던 메시지는 금액이 부과가 되지 않습니다.<br> 
NAVER의 Preimium TTS를 HOME ASSIANT에 사용할 수 있습니다.<br>
일반 TTS와 다르게 emotion 항목으로 감정 조절이 가능 합니다.<br>
emotion으로 좀 더 자연스러운 TTS를 구현 해보세요.<br>
※ Voice는 기본 Voice(nara)만 지원 합니다.<br>
<br><br>

## ■ How to Install
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
<img src="https://github.com/chohoo89/HomeAssiant_Componets/blob/master/image/naver_premium/6.jpg?raw=true">
<hr>
(8) HA의 config 파일 경로에 들어 갑니다.<br>
(초보자분들을 위해 설명을 드리면 config 파일 경로는 configuration.yaml 파일이 있는 경로 이고 hass.io를 설치 하신 분들은 /usr/share/hassio 경로 입니다)<hr>
(9) 해당 경로에 custom_components 폴더가 있는지 확인 후 폴더가 있다면 naver_premium 폴더를 만들어 주시고 없으시면 custom_components 폴더를 만드신 후 해당 폴더 안에 naver_premium 폴더를 만들어 주세요.<br>
(리눅스 사용중이고 hass.io를 사용 중이면 "mkdir /usr/share/hassio/custom_components/naver_premium" 를 입력 해주세요) <hr>

(10) `__init__.py, tts.py` 를 naver_premium 폴더안에 넣어 주세요.<br>
최종 경로는 `<config directory>/custom_components/naver_premium/__init__.py` <br> `<config directory>/custom_components/naver_premium/tts.py` 입니다.<hr>

(11) `configuration.yaml` 에서 아래 항목을 입력 합니다. (필수 항목)
```yaml
tts:
  - platform: naver_premium
    client_id: <YOUR_CLIENT_ID> # 7번 항목의 Client ID
    client_secret: <YOUR_CLIENT_SECRET> # 7번 항목의 Client Secret
```
<br>

(11-2) 추가로 옵션을 조정 하시려면 아래와 같은 설정이 조정이 가능 합니다.
```yaml
    speed: # 음성 속도를 설정 할 수 있습니다. (-5~5 사이 값을 입력 하면 되고 -5는 2배 5는 0.5배 입니다.)
    pitch: # 피치를 설정 할 수 있습니다. (-5~5 사이 값을 입력 하면 되고 -5는 1.2배 높은 피치, 5는 0.8배 낮은 피치)
    emotion: # 감정을 조절할 수 있습니다. (0:보통, 1:슬픔, 2:밝음)
```
<br>

(11-3) google_cloud 등 다른 tts 를 사용 하고 있어도 아래와 같이 platform을 붙혀 추가 하시면 google, naver tts 둘다 사용 가능 합니다.
```yaml
tts:
  - platform: google_cloud
    key_file: googlecloud.json
    language: ko-KR
    voice: ko-KR-Wavenet-A
    service_name: google_say
    pitch: -2.8
    speed: 1.07
  - platform: naver_premium
    client_id: <YOUR_CLIENT_ID> # 7번 항목의 Client ID
    client_secret: <YOUR_CLIENT_SECRET> # 7번 항목의 Client Secret
    emotion: 2
```

<hr>

(12) HA를 재부팅 해주시고 제대로 동작하는지 확인 해보세요. <br>
만약 문제가 있으시면 `configuration.yaml` 에서 11번에 추가 한 `naver_premium` 항목을 삭제 후 재부팅 해주세요.

<br><br>

# 제작에 도움을 주신 분
[1] GH-Connecter(아기나무집님)
