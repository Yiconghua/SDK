# -*- coding: utf-8 -*-

import weakref

from sdk.sdk_logging import ISDKLog




class Foo2(ISDKLog):
    def record_log(self, log):
        print ('im foo 2 {}'.format(log))




class Foo3(ISDKLog):
    def record_log(self, log):
        print ('im foo 3 {}'.format(log))





# p3 = Foo('p3')
# p4 = Foo('p4')





if __name__ == '__main__':
   p1 = Foo2()
   # p2 = Foo3()
   ISDKLog.info("asdafa");
