from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from time import sleep
from subprocess import run, PIPE
import win32api
import win32gui

ct = win32api.GetConsoleTitle()
hd = win32gui.FindWindow(0, ct)
# win32gui.ShowWindow(hd, 6)  # 可见窗口
win32gui.ShowWindow(hd, 0)  # 不可见窗口
# 1111111
print('OK')
print('OK')


class SzuLogin(object):
    def __init__(self, url, account, password):
        self.driver = webdriver.Chrome()
        self.url = url
        self.account = account
        self.password = password

    def browser(self):
        self.driver.get(self.url)
        # self.driver.maximize_window()
        self.driver.implicitly_wait(1)  # 等待1秒

    def login(self):
        while True:
            try:
                input_account = self.driver.find_element_by_xpath('//*[@id="VipDefaultAccount"]')
                input_password = self.driver.find_element_by_xpath('//*[@id="VipDefaultPassword"]')
            except:
                self.driver.refresh()
                continue
            input_account.clear()
            input_password.clear()
            input_account.send_keys(self.account)
            input_password.send_keys(self.password)

            try:
                bt_login = WebDriverWait(self.driver, 60, 1).until(EC.presence_of_element_located((
                    By.XPATH, '//*[@value="登 录 (Login)"]')))
            except:
                self.driver.refresh()
                continue
            bt_login.click()
            # print("点击登录")
            sleep(1)
            self.driver.quit()
            break


def network_state():
    r = run('ping www.baidu.com', stdout=PIPE, stderr=PIPE, stdin=PIPE, shell=True)
    return r.returncode  # return false if the network state is disconnected


def output_log(text, path):
    log_file = open(path, 'a')
    log_file.write(text)
    log_file.close()


if __name__ == '__main__':
    # modify the parameters here --------------------------------------------
    url = "https:/*********"  # 登录校园网的网址
    account = "********"  
    password = "**********"
    log_path = "C:\\Users\\dell\\Desktop\\SZUAutoLogin\\log.txt"  # 日志保存位置
    MaxReconnection = 10  # 最大重连次数
    short_time_sleep = 600  # 10分钟， 用于控制重连失败后的休眠时间
    long_time_sleep = 1800  # 30分钟， 用于控制检测网络情况的时间间隔
    # -----------------------------------------------------------------------
    reconnection = 0
    while True:
        if network_state():
            if reconnection == 0:
                print("{} 断网！开始重连......".format(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
                output_log("{} 断网！开始重连......\n".format(time.strftime('%Y-%m-%d %H:%M:%S',
                                                                     time.localtime(time.time()))), log_path)
            reconnection = reconnection + 1
            print("{} 第 {} 次重连".format(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), reconnection))
            output_log("{} 第 {} 次重连\n".format(time.strftime('%Y-%m-%d %H:%M:%S',
                                                            time.localtime(time.time())), reconnection), log_path)
            if reconnection <= MaxReconnection:
                process = SzuLogin(url, account, password)
                process.browser()
                process.login()
                sleep(1)
            else:
                print("{} 重连失败！稍后重试！".format(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
                output_log("{} 重连失败！稍后重试！\n".format(time.strftime('%Y-%m-%d %H:%M:%S',
                                                                  time.localtime(time.time()))), log_path)
                reconnection = 0
                sleep(short_time_sleep)  # 短时间休眠

        else:
            print("{} 联网成功".format(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
            output_log("{} 联网成功\n".format(time.strftime('%Y-%m-%d %H:%M:%S',
                                                        time.localtime(time.time()))), log_path)
            reconnection = 0
            sleep(long_time_sleep)  # 长时间休眠
