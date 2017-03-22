#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from process import process
from algoritmi import statistic, fcfs,sjf,rr,srtf,hrrn
import copy

memory=list()
completed=list()
input=open("process_list")
#PID, entering time, cpu burst lenght
for linea in input:
	p=linea.split(' ')
	memory.append(process(int(p[0]),int(p[1]),int(p[2])))

print(">>>>>>>>>>>>>>>>\tFCFS\t<<<<<<<<<<<<<<<<")
end=fcfs(copy.deepcopy(memory),completed)
statistic(completed,end)


print(">>>>>>>>>>>>>>>>\tSJF\t<<<<<<<<<<<<<<<<")
end=sjf(copy.deepcopy(memory),completed)
statistic(completed,end)


print(">>>>>>>>>>>>>>>>\tSRTF\t<<<<<<<<<<<<<<<<")
end=srtf(copy.deepcopy(memory),completed)
statistic(completed,end)


print(">>>>>>>>>>>>>>>>RR q=1\t<<<<<<<<<<<<<<<<")
end=rr(copy.deepcopy(memory),completed,1)
statistic(completed,end)


print(">>>>>>>>>>>>>>>>RR q=4\t<<<<<<<<<<<<<<<<")
end=rr(copy.deepcopy(memory),completed,4)
statistic(completed,end)

print(">>>>>>>>>>>>>>>>HRRN \t<<<<<<<<<<<<<<<<")
end=hrrn(copy.deepcopy(memory),completed)
statistic(completed,end)
