import random
import time
import schedule
from airtest.core.api import *
from airtest.cli.parser import cli_setup
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

class DouYin:
    def __init__(self):
        if not cli_setup():
            auto_setup(__file__, logdir=True, devices=[
                "Android:///"
            ])
        self.poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
        size = self.poco.get_screen_size()
        self.width = size[0]
        self.height = size[1]

    def VisitHome(self):
        douyin_APP = "com.ss.android.ugc.aweme.lite"
        stop_app(douyin_APP)
        sleep(1)
        start_app(douyin_APP)
#         进入短视频页面后，查找推荐元素是否存在
#         self.poco(name='com.ss.android.ugc.aweme.lite:id/amh').wait(30)

#       找到推荐元素表示已经进入首页，但是视频加载需要一些时间，这里等待5秒
        sleep(5)

#         try:
#             # 初次打开可能会出现青少年模式选项
#             self.poco(text='我知道了').click()
#         except:
#             pass
    def reasure_Chest(self):
        touch(Template(r"tpl1637154426094.png", record_pos=(0.003, 0.85), resolution=(1080, 2280)))
        sleep(2)
        touch(Template(r"tpl1637152803708.png", record_pos=(0.344, 0.779), resolution=(1080, 2280)))
        sleep(1)    
        touch(Template(r"tpl1637154615032.png", record_pos=(-0.011, 0.373), resolution=(1080, 2280)))

        keyevent("BACK") # 返回
        
    def Advertisement(self):
        # 点击来赚钱
        touch(Template(r"tpl1637154426094.png", record_pos=(0.003, 0.85), resolution=(1080, 2280)))
        # 下划
        swipe((300,1200),(300,100),duration=1)
        
        # 点击去领取
        touch(Template(r"tpl1637155648978.png", target_pos=6, record_pos=(-0.023, -0.144), resolution=(1080, 2280)))
    
        sleep(32)

        touch(Template(r"tpl1637153623049.png", threshold=0.6, record_pos=(0.406, -0.931), resolution=(1080, 2280)))

        if exists(Template(r"tpl1637155820637.png", record_pos=(0.005, 0.319), resolution=(1080, 2280))):

            touch(Template(r"tpl1637154149781.png", record_pos=(0.001, 0.32), resolution=(1080, 2280)))
        
        keyevent("BACK") # 返回
            

    def run_Auto(self):
        start_pos = (0.5 * self.width, 0.8 * self.height)
        end_pos = (0.5 * self.width, 0.2 * self.height)
        # 每次刷视频前，判断是否存在随机红包

#         if exists(Template(r"tpl1637198663456.png", record_pos=(-0.002, 0.223), resolution=(1080, 2280))):
#             touch(Template(r"tpl1637198663456.png", record_pos=(-0.002, 0.223), resolution=(1080, 2280)))
#             sleep(1)
#             touch(Template(r"tpl1637198751771.png", record_pos=(-0.001, 0.625), resolution=(1080, 2280)))
#             sleep(0.5)
        # 每次刷视频前，判断是否存在随机红包
        if self.poco("com.ss.android.ugc.aweme.lite:id/sf").exists() :
            self.poco(name="com.ss.android.ugc.aweme.lite:id/c+e").click()
            time.sleep(1)
            self.poco("com.ss.android.ugc.aweme.lite:id/iv_close").click()
            time.sleep(0.5)
        # 从底部滑到上面，切换视频
        swipe(start_pos, end_pos, duration=0.5)
        # 每个视频观看3-5秒
        time.sleep(random.randint(1,4))

        
if __name__ == '__main__':
    
    douyin = DouYin()
    douyin.VisitHome() # 启动抖音app
    
    # 启动定时执行任务
    schedule.every(0.1).minutes.do(douyin.run_Auto) # 刷视频 
    schedule.every(20).minutes.do(douyin.reasure_Chest) # 领取宝箱
    schedule.every(20).minutes.do(douyin.Advertisement) # 看广告
    while True:
        schedule.run_pending()  # run_pending：运行所有可以运行的任务   
        time.sleep(1)

    


