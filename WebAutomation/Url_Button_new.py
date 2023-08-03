import tkinter as tk
import time  # 과도한 트래픽으로 인한 IP 차단 방지를 위해 지연 시간 두기
import pyperclip  # 클립보드에 값을 저장할 수 있게 해주는 라이브러리
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import tkinter.ttk as ttk # 구분선 모듈
import subprocess  # 프로세스 처리 모듈
import threading
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# UrlButton 위젯 클래스 정의
class UrlButton:
    def __init__(self, root):
        self.window = root
        self.window.title("URL Button")
        # 셀레니움 기본 설정
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True) # 브라우저 꺼짐 방지코드
        self.options.add_experimental_option('excludeSwitches', ['enable-logging']) # 불필요한 에러메세지 없애기
        self.driver = webdriver.Chrome(options=self.options)  # 셀레니움의 Chrome WebDriver 인스턴스 생성

        # 버튼과 연결될 URL, ID, 비밀번호를 포함하는 딕셔너리 생성
        self.button_urls = {
            "Button 1": {
                "url": "https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/",
                "id_locator": (By.ID, "id"),
                "id_value": "본인계정ID입력값",
                "pw_locator": (By.ID, "pw"),
                "pw_value": "본인계정PW입력값",
                "login_locator": (By.ID, "log.login")
            },
            "Button 2": {
                "url": "https://google.co.kr",
                "id_locator": (By.ID, "id"),
                "id_value": "본인계정ID입력값",
                "pw_locator": (By.ID, "pw"),
                "pw_value": "본인계정PW입력값",
                "login_locator": (By.ID, "log.login")
            },
            "Button 3": {
                "url": "https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/",
                "id_locator": (By.ID, "id"),
                "id_value": "본인계정ID입력값",
                "pw_locator": (By.ID, "pw"),
                "pw_value": "본인계정PW입력값",
                "login_locator": (By.ID, "log.login")
            },
            "Button 4": {
                "url": "https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/",
                "id_locator": (By.ID, "id"),
                "id_value": "본인계정ID입력값",
                "pw_locator": (By.ID, "pw"),
                "pw_value": "본인계정PW입력값",
                "login_locator": (By.ID, "log.login")
            },
            "Button 5": {
                "url": "https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/",
                "id_locator": (By.ID, "id"),
                "id_value": "본인계정ID입력값",
                "pw_locator": (By.ID, "pw"),
                "pw_value": "본인계정PW입력값",
                "login_locator": (By.ID, "log.login")
            },
            "Button 6": {
                "url": "https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/",
                "id_locator": (By.ID, "id"),
                "id_value": "본인계정ID입력값",
                "pw_locator": (By.ID, "pw"),
                "pw_value": "본인계정PW입력값",
                "login_locator": (By.ID, "log.login")
            },
            "Button 7": {
                "url": "https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/",
                "id_locator": (By.ID, "id"),
                "id_value": "본인계정ID입력값",
                "pw_locator": (By.ID, "pw"),
                "pw_value": "본인계정PW입력값",
                "login_locator": (By.ID, "log.login")
            },
            "Button 8": {
                "url": "https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/",
                "id_locator": (By.ID, "id"),
                "id_value": "본인계정ID입력값",
                "pw_locator": (By.ID, "pw"),
                "pw_value": "본인계정PW입력값",
                "login_locator": (By.ID, "log.login")
            }
        }

        self.create_buttons()

    # 버튼 생성 메소드 호출
    def create_buttons(self):
        button_frame = tk.Frame(self.window)  # 버튼들을 담을 프레임 생성
        button_frame.grid(row=0, column=0, columnspan=4, padx=10, pady=5)

        for i, (button_text, _) in enumerate(self.button_urls.items()):
            row_num = i // 4
            col_num = i % 4

            url = self.button_urls[button_text]["url"]
            id_value = self.button_urls[button_text]["id_value"]
            pw_value = self.button_urls[button_text]["pw_value"]
            id_locator = self.button_urls[button_text]["id_locator"]
            pw_locator = self.button_urls[button_text]["pw_locator"]
            login_locator = self.button_urls[button_text]["login_locator"]

            # 버튼 생성, 버튼이 클릭되면 login 메소드 호출
            web_button = tk.Button(button_frame, text=button_text, command=lambda url=url, id_locator=id_locator, id_value=id_value, pw_locator=pw_locator, pw_value=pw_value, login_locator=login_locator: self.naver_login(url, id_locator, id_value, pw_locator, pw_value, login_locator))
            web_button.grid(row=row_num, column=col_num, padx=10, pady=5)
        
        # 웹사이트 로그인 자동화 버튼(상) / CS 프로그램 로그인 자동화(하) - 구분선
        separator = ttk.Separator(self.window, orient="horizontal")
        separator.grid(row=1, column=0, columnspan=4, sticky="ew", padx=10, pady=5)

        cs_buttons_frame = tk.Frame(self.window)
        cs_buttons_frame.grid(row=2, column=0, columnspan=4, padx=10, pady=5)

        cs_button_texts = ["CS Button 1", "CS Button 2", "CS Button 3", "CS Button 4"]

        for i, button_text in enumerate(cs_button_texts):
            row_num = i // 4
            col_num = i % 4

            cs_button = tk.Button(cs_buttons_frame, text=button_text, command=lambda button_text=button_text: self.cs_button_clicked(button_text))
            cs_button.grid(row=0, column=i, padx=10, pady=5)


    # 네이버 로그인
    def naver_login(self, url, id_locator, id_value, pw_locator, pw_value, login_locator):
            self.driver.get(url)

            # id/pw field 찾아서 값 붙여넣기
            for locator, value in [(id_locator, id_value), (pw_locator, pw_value)]:
                input_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
                # input_field = self.driver.find_element(*locator) # 튜플 언패킹 방식
                pyperclip.copy(value)
                input_field.send_keys(Keys.CONTROL, 'v')
                time.sleep(1)

            # 로그인 버튼 찾아서 클릭
            login_Btn= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(login_locator))
            login_Btn.click()
            # self.driver.find_element(*login_locator).click() # 튜플 언패킹 방식

    def cs_button_clicked(self, button_text):
        try:
            threading.Thread(target=subprocess.run, args=(["python", r"C:\PROJ_PY\AppAutomation\CS_AutoLogin3.py"],)).start()
            # subprocess.run(["python", r"C:\PROJ_PY\Mission2\CS_AutoLogin3.py"])  # subprocess를 이용하여 CS_AutoLogin3.py를 실행 -> 스레딩 미사용 시, tkinter의 window.mainloop가 멈춤
        except Exception as e:
            print(f"Error: {e}")


window = tk.Tk()  # 윈도우 창 생성
app = UrlButton(window)  # 위젯을 생성하고 적용
window.mainloop()  # 윈도우 창을 윈도우가 종료될 때 까지 실행시킴