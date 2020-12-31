'''
Author: Wings
Date: 2020-08-28 21:17:26
LastEditTime: 2020-08-31 11:22:25
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \RoomHunter.py
'''
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

DRIVER_PATH = 'chromedriver.exe'
ROME_URL = 'http://ehall.xidian.edu.cn/xsfw/sys/ssxfapp/*default/index.do#/indexPage'

# TODO: 这里修改您的Chrome用户目录, 用于直接登录
# TODO: 默认安装的话路径一般是 C:/Users/[你的用户名]/AppData/Local/Google/Chrome/User Data
USER_DATA_PATH = 'C:/Users/abc/AppData/Local/Google/Chrome/User Data'


def main():

    # 设置用户路径, 方便直接登录
    chrome_options = ChromeOptions()
    chrome_options.add_argument(r'user-data-dir=' + USER_DATA_PATH)

    driver = webdriver.Chrome(executable_path=DRIVER_PATH, options=chrome_options)

    # 一个奇怪的方法加速Chrome加载
    try:
        driver.set_page_load_timeout(0.1)
        driver.get("chrome://version/")
    except:
        pass
    driver.set_page_load_timeout(20)

    # 跳转网页
    driver.get(ROME_URL)

    # 通过获取元素判断是否加载完成
    WebDriverWait(driver, 10, 0.1).until(EC.presence_of_element_located((By.LINK_TEXT, "点击进入")))

    # 判断是否有两个按钮, 这样计时一结束出现按钮就可以马上点击
    button_elements_into = driver.find_elements_by_link_text("点击进入")
    while len(button_elements_into) != 2:
        button_elements_into = driver.find_elements_by_link_text("点击进入")
    # 第二个是选房的
    button_elements_into[1].click()

    # 通过获取宿舍意愿个数的标签来判断是否加载完成
    element_label = WebDriverWait(driver, 10, 0.1).until(EC.presence_of_element_located((By.ID, 'xfyhgsLabel')))
    element_button_choose = driver.find_element_by_id('oneKeyChooseBtn')
    # 如果有数字, 则加载完成
    while element_label.text == 'N/A':
        pass
    # 怕翻车, 等一下
    sleep(0.01)
    # 点击 "一键选房"
    element_button_choose.click()

    # 等1h
    sleep(3600)

    driver.quit()


if __name__ == "__main__":
    main()
