import utils.PCB as PCB


def cal_response_rate(processWaitTime, processSpendTime):
    return (1 + int(processWaitTime)) / int(processSpendTime)  # processWaitTime = timeline - arrive_time


class HRRF(object):
    def __init__(self):
        self.timeline = 0
        self.processAll = PCB.get_input()
        self.sort_process()

    def sort_process(self):
        self.processAll = sorted(self.processAll, key=lambda process: process.arrive_time)

    def sort_processByRate(self):
        self.processAll = sorted(self.processAll, key=lambda process: process.responseRate)[::-1]

    def manage(self):
        sum_roundTime = 0
        sum_roundTimeWithWeight = 0  # 带权
        processNum = len(self.processAll)
        for i in range(processNum):
            currentPCB = self.processAll[0]
            msg_1 = "时刻%s,进程%s正在运行," % (self.timeline, currentPCB.name)
            self.timeline += int(currentPCB.spend)
            currentPCB.real_endTime = self.timeline
            currentPCB.roundTime = int(currentPCB.real_endTime) - int(currentPCB.arrive_time)
            sum_roundTime += currentPCB.roundTime
            sum_roundTimeWithWeight += int(currentPCB.roundTime) / int(currentPCB.spend)
            msg_2 = "周转时间为%s" % currentPCB.roundTime
            print(msg_1 + msg_2)
            del self.processAll[0]
            for j in self.processAll:  # 计算响应比
                j.processWaitTime = int(self.timeline) - int(j.arrive_time)
                j.responseRate = cal_response_rate(j.processWaitTime, j.spend)
            self.sort_processByRate()
        print("平均周转时间为：" + str(float(sum_roundTime) / float(processNum)))
        print("平均带权周转时间为：" + str(float(sum_roundTimeWithWeight) / float(processNum)))
