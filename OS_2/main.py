from utils import FCFS, HRRF

choice = input("FCFS(1)\nHRRF(2)\n请输入序号选择算法：")

if choice == "1":
    F = FCFS.FCFS()
    F.manage()
    F.cal_average_roundTime()
else:
    H = HRRF.HRRF()
    H.manage()

