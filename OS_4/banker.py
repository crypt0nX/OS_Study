import numpy as np


class Banker(object):
    def __init__(self, available, Max, allocation, Need):
        self.available = available
        self.max = Max
        self.allocation = allocation
        self.need = Need

    def commitProcess(self, eachProcess, eachProcessRequest):
        # 判断请求向量是否小于需求向量
        length = len(eachProcessRequest)
        i = 0
        for i in range(length):
            if eachProcessRequest[i] > self.need[eachProcess][i]:
                break
        if i != len(eachProcessRequest) - 1:
            print("进程{0}需求资源超出最大值".format(eachProcess))
            return

        # 判断请求向量是否小于可用资源向量
        j = 0
        for j in range(length):
            if eachProcessRequest[i] > self.available[i]:
                break
        if j != length - 1:
            print("现有资源不足以满足{}", eachProcess)
            return

        # 进行尝试分配
        avi_temp = self.available
        all_temp = self.allocation
        need_temp = self.need

        for k in range(length):
            avi_temp[k] = avi_temp[k] - eachProcessRequest[k]
            all_temp[eachProcess][k] = all_temp[eachProcess][k] + eachProcessRequest[k]
            need_temp[eachProcess][k] = need_temp[eachProcess][k] - eachProcessRequest[k]

        if self.checkIfSafe():  # 执行安全性算法
            self.need = need_temp
            self.allocation = all_temp
            self.available = avi_temp
            print("请求成功！系统运行状态：\nNeed={0}\nAllocation={1}\nAvailable{2}\n".format(self.need, self.allocation,
                                                                                   self.available))

        else:
            print("监测到不安全退出！")
            return

    def checkIfSafe(self):  # 安全性算法

        work = self.available
        finish = [False for i in range(self.need.shape[0])]
        pro_number = self.need.shape[0]
        pro_list = [i for i in range(pro_number)]
        length = self.need.shape[1]
        secureSeq = ""

        # 寻找安全序列
        for k in range(pro_number):
            for i in pro_list:
                flag = 1
                for j in range(length):
                    if self.need[i][j] > work[j]:
                        flag = 0
                        break

                if flag and finish[i] is False:
                    work += self.allocation[i]
                    finish[i] = True
                    secureSeq += str(i) + "->"
                    pro_list.remove(i)
                    break

        for i in range(len(finish)):
            if finish[i] is not True:
                return False
        print("存在安全序列为{0}".format(secureSeq.strip("->")))
        return True


if __name__ == "__main__":
    avi = np.array([4, 4, 2])  # 可利用资源向量

    need = np.array([[6, 4, 3],
                     [1, 2, 2],
                     [6, 0, 0],
                     [0, 1, 1],
                     [4, 3, 1]])  # 需求矩阵
    all = np.array([[0, 1, 0],
                    [2, 2, 0],
                    [2, 0, 2],
                    [2, 1, 1],
                    [0, 0, 2]])  # 分配矩阵
    max = np.array([[3, 5, 3],
                    [3, 2, 2],
                    [9, 0, 2],
                    [2, 2, 2],
                    [4, 3, 3]])  # 最大需求矩阵
    Test = Banker(avi, max, all, need)
    Test.commitProcess(1, np.array([1, 0, 2]))
