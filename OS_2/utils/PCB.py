class PCB(object):
    def __init__(self, name, arrive_time, spend):
        self.name = name
        self.arrive_time = arrive_time
        self.spend = spend

        self.real_startTime = 0  # 开始时间
        self.real_endTime = 0  # 结束时间
        self.processWaitTime = 0  # 等待时机
        self.roundTime = 0  # 周转时间
        self.responseRate = 0  # 响应比


def createPCB(name, arrive_time, spend):
    return PCB(name=name, arrive_time=arrive_time, spend=spend)


def get_input():
    PCB_list = []
    while True:
        name = input("name: ")
        if name == "quit" or not name:
            break
        arrive_time = input("arrive_time: ")
        spend = input("spend: ")
        PCB_list.append(PCB(name, arrive_time, spend))
    return PCB_list
