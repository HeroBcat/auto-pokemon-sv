import logging
import time
import sys
import os

from JoycontrolPlugin import JoycontrolPlugin

sys.path.append(os.getcwd() + '/common')
from Common import Common

logger = logging.getLogger(__name__)

class Release(Common):
    def __init__(self, controller_state, options):
        super().__init__(controller_state, options)

    async def run(self):

        next = 'down'

        for _ in range(0, 6):
            logger.info('new row: ' + next)

            for _ in range (0, 4):
                await self.release()
                await self.button_ctl(next, wait_sec=1.0)

            await self.release()
            await self.button_ctl('right', wait_sec=1.0)

            if next == 'down':
                next = 'up'
            else:
                next = 'down'

    async def release(self):
        await self.button_ctl('a', wait_sec=2.0)
        await self.button_ctl('up', wait_sec=0.5)
        await self.button_ctl('up', wait_sec=0.5)
        await self.button_ctl('a', wait_sec=0.5)
        await self.button_ctl('up', wait_sec=0.5)
        await self.button_ctl('a', wait_sec=0.5)
        await self.button_ctl('a', wait_sec=0.5)
        await self.button_ctl('a', wait_sec=2.0)