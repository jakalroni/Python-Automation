import cv2 as cv
import subprocess
import os
import time
import pyautogui
import threading

class KakaoTalkAutomation:
    def __init__(self):
        self.kakao_process = None

    # open_kakao(): 카카오톡을 실행시키는 메소드
    # kill_kakao(): 카카오톡을 강제 종료시키는 메소드
    def open_kakao(self, path):
        try:
            # path = r"C:\Program Files (x86)\Kakao\KakaoTalk\KakaoTalk.exe"
            self.kakao_process = subprocess.Popen(path)
            print('카카오톡 포그라운드 실행 성공!')

            # 카카오톡이 계속 실행되고 있는지 확인하는 루프 (프로세스가 아직 실행 중이면 'None'을 반환)
            while self.kakao_process.poll() is None:
                time.sleep(1)

            print('카카오톡이 종료되었습니다.')
        except Exception as e:
            print(f"카카오톡 실행 실패!: {e}")

    def kill_kakao(self, target_exe_name):
        try:
            os.system(f"TASKKILL /F /IM {target_exe_name}")
        except Exception as e:
            print(f"Failed to kill {target_exe_name}: {e}")

    def login_kakao(self):
        try:
            # 캡처한 이미지로 좌표 정보 얻기 (opencv - 이미지 인식 일치도를 80% 이상)
            kakaotalkLogo_location = pyautogui.locateOnScreen(r'C:\PROJ_PY\AppAutomation\images\kakaotalk_logo.png', confidence=0.8, region=(1500, 380, 440, 660))
            # emailBtn_location = pyautogui.locateOnScreen(r'C:\PROJ_PY\AppAutomation\images\email_inputbox.png', confidence=0.8, region=(1500, 380, 440, 660))
            passwordBtn_location = pyautogui.locateOnScreen(r'C:\PROJ_PY\AppAutomation\images\password_inputbox.png', confidence=0.8, region=(1500, 380, 440, 660))

            if passwordBtn_location is None:
                print("패스워드 입력란 찾기 실패...")
            else:
                button_point = pyautogui.center(kakaotalkLogo_location)  # 이미지의 센터 좌표(클릭할 지점)를 튜플의 형태로 얻음
                pyautogui.click(button_point.x, button_point.y+100)  # 로고 이미지 좌표 기준 y좌표 조절해 이메일 입력란 좌표 계산
                pyautogui.write('본인이메일계정ID 입력')  # 이메일계정 자리
                pyautogui.press('tab')

                button_point = pyautogui.center(passwordBtn_location)
                pyautogui.click(button_point.x, button_point.y)
                pyautogui.write('본인계정PW 입력')  # 비밀번호 자리
                pyautogui.press('tab')
                time.sleep(1)

            loginBtn_location = pyautogui.locateOnScreen(r'C:\PROJ_PY\AppAutomation\images\login_button.png', confidence=0.8, region=(1500, 380, 440, 660))
            button_point = pyautogui.center(loginBtn_location)
            pyautogui.click(button_point.x, button_point.y)

            # 로그인 버튼 클릭 시 로그인에 걸리는 시간이 존재
            time.sleep(5)

            # print([emailBtn_location, passwordBtn_location, loginBtn_location])
        except Exception as e:
            print(f"카카오톡 로그인 중 오류가 발생했습니다: {e}")

    def rest_with_logging(self, duration):  # 프로세스 kill / open 할때 필요한 로딩 시간
        for i in range(duration):
            print("Waiting... %d seconds passed" % (i + 1))
            time.sleep(1)



automation = KakaoTalkAutomation()

# 프로세스 킬할 실행파일명 파라미터로 받기
automation.kill_kakao("KakaoTalk.exe")
print("카카오톡을 종료하였습니다. 잠시 기다려주세요...\n")
automation.rest_with_logging(3)

kakao_path = r"C:\Program Files (x86)\Kakao\KakaoTalk\KakaoTalk.exe"
# 스레딩: open_kakao() 함수를 별도의 스레드에서 실행하고 나머지 코드는 독립적으로 진행
kakao_thread = threading.Thread(target=automation.open_kakao, args=(kakao_path,))
kakao_thread.start()

print("카카오톡을 실행하였습니다. 잠시 기다려주세요...\n")
automation.rest_with_logging(5)

automation.login_kakao()