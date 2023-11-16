import time
import string_data

from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import InvalidArgumentException

class Webdriver:
    def __init__(self):
        self.chromeDriver()
    def chromeDriver(self):
        self.start_time = time.time()
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")

        options.add_argument(
            f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36")
        #путь до вашего профиля google chrome где вы авторизованы в ютуб
        options.add_argument(f"user-data-dir=C:/Users/usr/AppData/Local/Google/Chrome/User Data/")

        options.add_experimental_option("excludeSwitches", ['enable-automation'])
        self.driver = webdriver.Chrome(options=options)
        stealth(self.driver,
                languages=["en-US", "en"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True,
                )
        self.pars_playlist()
    def pars_video_chanel(self):

        self.driver.get(string_data.url)
        n = 0
        time.sleep(4)
        while n < 3:
            self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
            time.sleep(2)
            n += 1
        time.sleep(2)
        playlist_window = self.driver.find_elements(By.XPATH, '//a[@id="thumbnail"]')
        del playlist_window[0]
        playlist_window = playlist_window[:len(playlist_window) - 19]

        test = print("Текущее количество видео " + str(len(playlist_window)))
        i = 0
        val_comment = 0
        neval_comment = 0
        for listi in playlist_window:
            i += 1
            link_yotube = listi.get_attribute('href')
            print("Видео номер:" + f"{i} " + str(link_yotube))
            self.driver.execute_script(f"window.open('{link_yotube}')")
            self.driver.switch_to.window(self.driver.window_handles[1])
            time.sleep(2)

            try:
                popup = self.driver.find_element(By.XPATH, string_data.path_popup)
                time.sleep(2)
                popup.click()
                # popup_window = self.driver.find_element(By.XPATH, string_data.path_popup_window)
                # time.sleep(2)
                # comment_clik = self.driver.find_element(By.XPATH, string_data.path_comment_click).click()
                #comment = popup_window.find_element(By.XPATH, string_data.path_comment)
                #time.sleep(4)
                #comment.send_keys(string_data.comment_text)
                #time.sleep(3)
                #send_comment = popup_window.find_element(By.XPATH, string_data.path_send_comment).click()
                #time.sleep(3)
                print("Комментарий успешно оставлен!")
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[0])
                val_comment += 1

            except:
                neval = []
                neval.append(link_yotube)
                print("Не удалось оставить комментарий")
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[0])
                neval_comment += 1
        print("Количество прокомментированных видео :" + str(val_comment))
        print("Колличество не прокомментированных видео :" + str(neval_comment))
        self.driver.quit()
        print("--- %s seconds ---" % (time.time() - self.start_time))
    def pars_playlist(self):
        time.sleep(1)
        self.driver.get(string_data.url)
        time.sleep(4)
        play_lists = self.driver.find_elements(By.XPATH, '//a[@id="wc-endpoint"]')
        time.sleep(3)
        print("Колличество видео в плейлисте: " + str(len(play_lists)))
        i = 0
        for play_list in play_lists:
            i += 1
            atribut_link = play_list.get_attribute('href')
            print("Видео номер:" + f"{i} " + str(atribut_link))
            time.sleep(1)
            self.driver.execute_script(f"window.open('{atribut_link}')")
            time.sleep(2)
            self.driver.switch_to.window(self.driver.window_handles[1])
            time.sleep(5)

            self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
            time.sleep(2)
            self.driver.find_element(By.XPATH, '//div[@id="placeholder-area"]').click()
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])

myWebsite = Webdriver()


