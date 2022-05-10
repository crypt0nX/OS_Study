import utils.PCB as PCB


class FCFS(object):
    def __init__(self):
        self.timeline = 0
        self.processAll = PCB.get_input()
        self.sort_process()

    def sort_process(self):
        self.processAll = sorted(self.processAll, key=lambda process: process.arrive_time)

    def manage(self):
        for i in self.processAll:
            msg_1 = "时刻%s,进程%s正在运行," % (self.timeline, i.name)
            self.timeline += int(i.spend)
            i.real_endTime = self.timeline
            i.roundTime = int(i.real_endTime) - int(i.arrive_time)
            msg_2 = "周转时间为%s" % i.roundTime  # 计算周转时间
            print(msg_1 + msg_2)

    def cal_average_roundTime(self):
        sum_roundTime = 0
        for i in self.processAll:
            sum_roundTime += i.roundTime
        print("平均周转时间为：" + str(sum_roundTime / len(self.processAll)))
        return sum_roundTime / len(self.processAll)

    def cal_average_roundTimeWithWeight(self):
        sum_roundTime = 0
        for i in self.processAll:
            sum_roundTime += float(i.roundTime) / float(i.spend)
        print("平均周转时间为：" + str(sum_roundTime / len(self.processAll)))
        return sum_roundTime / len(self.processAll)



