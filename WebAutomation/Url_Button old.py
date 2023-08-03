import tkinter as tk
import time  # 과도한 트래픽으로 인한 IP 차단 방지를 위해 지연 시간 두기
import pyperclip  # 클립보드에 값을 저장할 수 있게 해주는 라이브러리
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

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
                "login_config": {
                "id_locator": (By.ID, "id"),  # ID field locator (tag_name, identifier)
                "id_value": "본인계정ID",  # 계정 ID
                "pw_locator": (By.ID, "pw"),  # Password field locator (tag_name, identifier)
                "pw_value": "본인계정PW",  # 계정 패스워드
                "login_locator": (By.ID, "log.login")  # 로그인 버튼 locator (tag_name, identifier)
                }
            },
            "Button 2": {"url": "https://accounts.google.com/InteractiveLogin/identifier?continue=https%3A%2F%2Fwww.google.com%2F&ec=GAZAmgQ&hl=ko&passive=true&ifkv=AeDOFXi5UfZUzYEZFRN2icVVSoWuwSe7XCyixC4XHF76Js_aDu5FZA0ixh_72we1VFwnU9ReJNV9&flowName=GlifWebSignIn&flowEntry=ServiceLogin", "id": "입력값", "password": "입력값"},
            "Button 3": {"url": "https://portal.dankook.ac.kr/login.jsp", "id": "본인계정ID", "password": "본인계정PW"},
            "Button 4": {"url": "https://www.twitter.com", "id": "", "password": ""},
            "Button 5": {"url": "https://www.instagram.com", "id": "", "password": ""},
            "Button 6": {"url": "https://www.youtube.com", "id": "", "password": ""},
            "Button 7": {"url": "https://www.github.com", "id": "", "password": ""},
            "Button 8": {"url": "https://www.stackoverflow.com", "id": "", "password": ""},
        }

        self.create_buttons()

    # 버튼 생성 메소드 호출
    def create_buttons(self):
        for i, (button_text, _) in enumerate(self.button_urls.items()):
            row_num = i // 4
            col_num = i % 4

            # 버튼 생성, 버튼이 클릭되면 login 메소드 호출
            if button_text == "Button 1":
                button = tk.Button(self.window, text=button_text, command=lambda b=button_text: self.naver_login(b))
            elif button_text == "Button 2":
                button = tk.Button(self.window, text=button_text, command=lambda b=button_text: self.google_login(b))
            else:
                button = tk.Button(self.window, text=button_text, command=lambda b=button_text: self.default_login(b))

            button.grid(row=row_num, column=col_num, padx=10, pady=5)

    # 네이버 로그인
    def naver_login(self, button_text):
        url = self.button_urls[button_text]["url"]
        id_value = self.button_urls[button_text]["id"]
        password_value = self.button_urls[button_text]["password"]

        self.driver.get(url) # 버튼에 해당되는 url 접속

        # 로그인 필드 찾아서 id 복사-붙여넣기
        id_field = self.driver.find_element(By.ID, "id")
        pyperclip.copy(id_value)
        id_field.send_keys(Keys.CONTROL, 'v')
        time.sleep(1)

        # 로그인 필드 찾아서 pw 복사-붙여넣기
        password_field = self.driver.find_element(By.ID, "pw")
        pyperclip.copy(password_value)
        password_field.send_keys(Keys.CONTROL, 'v')
        time.sleep(1)

        # 로그인 버튼 찾아서 클릭
        self.driver.find_element(By.ID, "log.login").click()

    # 구글 로그인
    def google_login(self, button_text):
        url = self.button_urls[button_text]["url"]
        id_value = self.button_urls[button_text]["id"]
        password_value = self.button_urls[button_text]["password"]

        self.driver.get(url) # 버튼에 해당되는 url 접속

        # 로그인 필드 찾아서 id 복사-붙여넣기
        id_field = self.driver.find_element(By.ID, "identifierId")
        pyperclip.copy(id_value)
        id_field.send_keys(Keys.CONTROL, 'v')
        time.sleep(1)

        # 다음 버튼 찾아서 클릭
        self.driver.find_element(By.CSS_SELECTOR, "#identifierNext > div > button").click()
        time.sleep(3)

        # 로그인 필드 찾아서 pw 복사-붙여넣기
        password_field = self.driver.find_element(By.NAME, "Passwd")
        password_field.click()
        pyperclip.copy(password_value)
        password_field.send_keys(Keys.CONTROL, 'v')
        time.sleep(1)

        # 다음 버튼 찾아서 클릭
        self.driver.find_element(By.CSS_SELECTOR, "#passwordNext > div > button").click()

    # 단국대 포털 로그인
    def default_login(self, button_text):
        url = self.button_urls[button_text]["url"]
        id_value = self.button_urls[button_text]["id"]
        password_value = self.button_urls[button_text]["password"]

        self.driver.get(url) # 버튼에 해당되는 url 접속

        # 로그인 필드 찾아서 id 복사-붙여넣기
        id_field = self.driver.find_element(By.ID, "user_id")
        pyperclip.copy(id_value)
        id_field.send_keys(Keys.CONTROL, 'v')
        time.sleep(1)

        # 로그인 필드 찾아서 pw 복사-붙여넣기
        password_field = self.driver.find_element(By.ID, "user_password")
        pyperclip.copy(password_value)
        password_field.send_keys(Keys.CONTROL, 'v')
        time.sleep(1)

        # 로그인 버튼 찾아서 클릭
        self.driver.find_element(By.CSS_SELECTOR, "#loginFrm > div.login_btn > button").click()


window = tk.Tk()  # 윈도우 창 생성
app = UrlButton(window)  # 위젯을 생성하고 적용
window.mainloop()  # 윈도우 창을 윈도우가 종료될 때 까지 실행시킴