# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import sys
import uos, machine
#uos.dupterm(None, 1) # disable REPL on UART(0)
import gc
#import webrepl
#webrepl.start()
sys.path.reverse()
gc.collect()