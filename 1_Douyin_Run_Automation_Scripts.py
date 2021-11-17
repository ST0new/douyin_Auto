import os
import time
import random
import subprocess
import schedule

# 抖音极速版
# https://gitee.com/hamm/douyin_helper
douyin = "com.ss.android.ugc.aweme.lite" # 抖音极速版

def video():
    try:
        subprocess.check_output(['adb', 'shell', 'input', 'swipe' ,'300', str(random.randint(500,1000)) ,'300' ,str(random.randint(100,200))])  ##坐标根据需要自己修改
        time.sleep(random.randint(1,2))

    except subprocess.CalledProcessError as e:
        print(e)

def douyin():
    # 启动抖音极速版
    try:

        print(subprocess.check_output(['adb', 'shell', ' am', ' start', '-n',
                                       'com.ss.android.ugc.aweme.lite/com.ss.android.ugc.aweme.main.MainActivity']))
        # fun = os.system('adb shell am start -n com.ss.android.ugc.aweme.lite/com.ss.android.ugc.aweme.main.MainActivity')
        time.sleep(5)
    except subprocess.CalledProcessError as e:
        print(e)
def douyin_gold_coin(): # 领取发视频随机获得的金币
    try:
        print(subprocess.check_output(['adb', 'shell', 'input', 'tap', '300', '700']))
        time.sleep(1)
        print(subprocess.check_output(['adb', 'shell', 'input', 'tap', '281', '941']))
    except subprocess.CalledProcessError as e:
        print(e)
def douyin_Treasure_Chest(): # 20分钟领一次金币箱
    try:
        print(subprocess.check_output(['adb', 'shell', 'input', 'tap', '560', '2120']))
        time.sleep(1)
        print(subprocess.check_output(['adb', 'shell', 'input', 'tap', '940', '2060']))
        time.sleep(1)
        print(subprocess.check_output(['adb', 'shell', 'input', 'tap', '548', '1569']))
        print(subprocess.check_output(['adb', 'shell', 'input', 'tap', '91', '159']))
    except subprocess.CalledProcessError as e:
        print(e)
def douyin_search(i):
    try:
        subprocess.check_output(['adb', 'shell', 'input', 'tap', '1000', '170'])
        time.sleep(3)
        if i == 0:
            subprocess.check_output(['adb', 'shell', 'input', 'tap', '326', '591'])
        else:
            subprocess.check_output(['adb', 'shell', 'input', 'tap', '535', '300'])
        time.sleep(1)
        for j in range(4):
            video()
        subprocess.check_output(['adb', 'shell', 'input', 'tap', '81', '178'])
        subprocess.check_output(['adb', 'shell', 'input', 'tap', '116', '185'])
    except subprocess.CalledProcessError as e:
        print(e)
def douyin_searchs(): # 搜索金币
    for i in range(3): # 搜索获取金币
        douyin_search(i)
    print("每日搜索任务执行完毕")
def douyin_kill():
    print("任务全部完成")
    fun = os.system('adb kill-server')  ##运行结束杀掉adb进程
    exit()
def run_loop():
    print("已连接设备名称如下:")
    os.system('adb version')
    fun = os.system('adb devices')
    douyin()  # 启动抖音极速版


if __name__ == '__main__':
    # douyin_searchs()
    
    run_loop()
    schedule.every(20).minutes.do(douyin_Treasure_Chest)
    schedule.every(1).to(3).minutes.do(douyin_gold_coin)
    schedule.every(0.1).minutes.do(video)
    schedule.every(3).hours.do(douyin_kill)
    while True:
        schedule.run_pending()
        time.sleep(1)
