import random
import time

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

        start_app(douyin_APP)
        # 进入短视频页面后，查找推荐元素是否存在
#         self.poco(name='com.ss.android.ugc.aweme.lite:id/amh').wait(30)

        # 找到推荐元素表示已经进入首页，但是视频加载需要一些时间，这里等待5秒
        sleep(5)

        try:
            # 初次打开可能会出现青少年模式选项
            self.poco(text='我知道了').click()
        except:
            pass
    def douyin_Treasure_Chest(self):
        touch(Template(r"tpl1637119126942.png", record_pos=(-0.006, 0.859), resolution=(1080, 2280)))

        touch(Template(r"tpl1637119001840.png", record_pos=(0.337, 0.769), resolution=(1080, 2280)))
        
        if exists()
        touch(wait(,timeout=3))
        time.sleep(30)
        self.poco(name="关闭当前视频").click()
        touch(Template(r"tpl1637135395689.png", record_pos=(0.006, 0.319), resolution=(1080, 2280)))

        keyevent("BACK")
    def douyin_Advertisement(self):
        
        swipe((300,1200),(300,100),duration=1)
        self.poco(text="去领取").click()
        time.sleep(26)
        if poco("再看一个获取180金币").exists():
            poco("再看一个获取180金币").click()
            time.sleep(26)
        else:
            
            ad_close = touch(Template(r"tpl1637134923985.png", record_pos=(0.41, -0.91), resolution=(1080, 2280)))
            

    def LoopMove(self,n=0):
        starttime  = int(time.time())
        start_pos = (0.5 * self.width, 0.8 * self.height)
        end_pos = (0.5 * self.width, 0.2 * self.height)
        
        while n < 1000:
            end_time= int(time.time())
            if 0 < (end_time - starttime % 1200) < 60:
                self.douyin_Treasure_Chest()
                self.douyin_Advertisement()
            # 每次刷视频前，判断是否存在随机红包
            if self.poco("com.ss.android.ugc.aweme.lite:id/sf").exists() :
                self.poco(name="com.ss.android.ugc.aweme.lite:id/c+e").click()
                time.sleep(1)
                self.poco("com.ss.android.ugc.aweme.lite:id/iv_close").click()
                time.sleep(0.5)
            # 从底部滑到上面，切换视频
            swipe(start_pos, end_pos, duration=1)
            # 每个视频观看3-5秒
            time.sleep(random.randint(2,4))
            n = n + 1 

            
if __name__ == '__main__':
    douyin = DouYin()

#     douyin.VisitHome()
#     douyin.LoopMove(0)
    douyin.douyin_Advertisement()
    
    
# from poco.drivers.android.uiautomation import AndroidUiautomationPoco
    
# poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)    
# poco(name="关闭当前视频").click()


