import logging
import time
import sys
import os

from JoycontrolPlugin import JoycontrolPlugin

sys.path.append(os.getcwd() + '/common')
from Common import Common

logger = logging.getLogger(__name__)

class HatchEggs(Common):
    def __init__(self, controller_state, options):
        super().__init__(controller_state, options)

    async def run(self):

        for idx in range(0, 6):
            logger.info('new row')

            if idx == 0:
                await self.button_ctl('x', wait_sec=2.0)
                await self.button_ctl('a', wait_sec=5.0)
            else:
                await self.button_ctl('right')

            await self.button_ctl('minus', wait_sec=2.0)
            await self.button_ctl('down')
            await self.button_ctl('down')
            await self.button_ctl('down')
            await self.button_ctl('down')
            await self.button_ctl('a', wait_sec=2.0)

            for i in range(0, idx+1):
                await self.button_ctl('left')


            await self.button_ctl('down')
            await self.button_ctl('a', wait_sec=2.0)
            await self.button_ctl('b', wait_sec=2.0)
            await self.button_ctl('b', wait_sec=5.0)

            await self.hatch_egg()
            logger.info('hatch eggs done') 

            await self.button_ctl('x', wait_sec=2.0)
            await self.button_ctl('a', wait_sec=5.0)
            await self.button_ctl('left')
            await self.button_ctl('down')

            await self.button_ctl('minus', wait_sec=2.0)
            await self.button_ctl('down')
            await self.button_ctl('down')
            await self.button_ctl('down')
            await self.button_ctl('down')
            await self.button_ctl('a', wait_sec=2.0)

            for i in range(0, idx+1):
                await self.button_ctl('right')  

            await self.button_ctl('up', wait_sec=2.0)
            await self.button_ctl('a', wait_sec=2.0)
            # await self.button_ctl('b', wait_sec=2.0)
            # await self.button_ctl('b', wait_sec=2.0)          

            idx += 1


    async def hatch_egg(self):
        await self.button_ctl('plus', wait_sec=2.0)

        limit_time = time.time() + 300 #孵化歩数が長いポケモンで4分半だったのでこの数値にした
        notice_time = time.time() + 60

        while time.time() < limit_time:
            await self.left_stick(angle=270)
            await self.wait(3.3)
            await self.left_stick(angle=90)
            await self.wait(2.7)
            await self.button_ctl('a')
            await self.button_ctl('a')
            await self.button_ctl('a')
            
            if notice_time < time.time():
                logger.info('あと{}秒です'.format(round(limit_time-notice_time)))
                notice_time += 60


        await self.left_stick('center')
        await self.wait(1.5)

        await self.button_ctl('plus', wait_sec=2.0)
