#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from process import process
import copy

#change this to True to see the order of execution
verbose=False

def statistic(completed, end):

	tt=0
	tw=0
	tr=0
	for p in completed:
		tt+=p.tt
		tw+=p.tw
		tr+=p.tr

	print("Execution completed in "+str(end)+" clocks")
	print("Average Response Time: "+str(tr/len(completed)))
	print("Average Waiting Time: "+str(tw/len(completed)))
	print("Average Turnaround Time: "+str(tt/len(completed)))
	del completed[:]

def fcfs(memory,completed):
	memory=sorted(memory, key=lambda p: p.enter)

	t=0
	while len(memory)>0:

		p=memory[0]
		if verbose:
			print(str(t)+"\t"+str(p.pid))
		memory.remove(p)
		temp= t-p.enter
		p.tw=temp
		p.tr=temp
		p.tt=temp+p.remaining
		t+=p.remaining
		p.remaining=0
		completed.append(p)
	return t


def srtf(memory, completed):
	maxpid=max(memory, key=lambda p:p.pid)
	memory=sorted(memory, key=lambda p: p.enter)
	clock=0
	ready=list()
	last_exec=[-1 for  x in range(0,maxpid.pid+2)]
	for p in memory:
		p.tt=p.remaining
	while len(memory)>0 or len(ready)>0:
		#reading all process in memory at this time
		while len(memory)>0 and memory[0].enter <= clock:
			p=memory[0]
			memory.remove(p)
			ready.append(p)

		ready=sorted(ready, key=lambda p: p.remaining)
		if len(ready)>0:
			new=ready[0]
			new.remaining-=1
			if verbose:
				print(str(clock)+"\t"+str(new.pid))

			#new process
			if new.tr==-1:
				new.tr=clock - new.enter

			if new.tw==-1:
				new.tw= clock-new.enter
			else:
				new.tw+= (clock-last_exec[new.pid])

			last_exec[new.pid]=clock

			if new.remaining==0:
				ready.remove(new)
				completed.append(new)

		clock+=1

	for p in memory:
			p.tt+=p.tw

	return clock



def sjf(memory, completed):
	memory=sorted(memory, key=lambda p: p.enter)
	clock=0
	ready=list()
	for p in memory:
		p.tt=p.remaining
	while len(memory)>0 or len(ready)>0:
		#reading all process in memory at this time
		while len(memory)>0 and memory[0].enter <= clock:
			p=memory[0]
			memory.remove(p)
			ready.append(p)

		ready=sorted(ready, key=lambda p: p.remaining)
		if len(ready)>0:
			new=ready[0]
			new.remaining=0
			if verbose:
				print(str(clock)+"\t"+str(new.pid))

			new.tr=clock - new.enter
			new.tw= clock-new.enter

			ready.remove(new)
			completed.append(new)

		clock+=new.tt

	for p in memory:
			p.tt+=p.tw

	return clock

def rr(memory, completed, quanto=1):
	maxpid=max(memory, key=lambda p:p.pid)
	memory=sorted(memory, key=lambda p: p.enter)
	clock=0
	ready=list()
	last_exec=[-1 for  x in range(0,maxpid.pid+2)]
	for p in memory:
		p.tt=p.remaining
	while len(memory)>0 or len(ready)>0:
		#reading all process in memory at this time
		while len(memory)>0 and memory[0].enter <= clock:
			p=memory[0]
			memory.remove(p)
			ready.append(p)

		if len(ready)>0:
			new=ready[0]
			temp=new.remaining
			new.remaining=max(0,new.remaining-quanto)
			if verbose:
				print(str(clock)+"\t"+str(new.pid))

			#new process
			if new.tr==-1:
				new.tr=clock - new.enter

			if new.tw==-1:
				new.tw= clock-new.enter
			else:
				new.tw+= (clock-last_exec[new.pid])

			last_exec[new.pid]=clock

			ready.remove(new)

			#if it terminated i remove it
			#if it need more time i append it at the end
			if new.remaining==0:
				completed.append(new)
			else:
				ready.append(new)

		clock+=min(quanto, temp)

	for p in memory:
		p.tt+=p.tw

	return clock


def hrrn(memory,completed):
	memory=sorted(memory, key=lambda p: p.enter)
	clock=0
	ready=list()
	for p in memory:
		p.tt=p.remaining
	while len(memory)>0 or len(ready)>0:
		#reading all process already arrived (in memory)
		while len(memory)>0 and memory[0].enter <= clock:
			p=memory[0]
			memory.remove(p)
			ready.append(p)

		ready=sorted(ready, key=lambda p: 1+(p.tw/p.remaining))
		if len(ready)>0:
			new=ready[0]
			new.remaining=0
			if verbose:
				print(str(clock)+"\t"+str(new.pid))

			new.tr=clock - new.enter
			new.tw= clock-new.enter

			ready.remove(new)
			completed.append(new)

		clock+=new.tt

	for p in memory:
			p.tt+=p.tw

	return clock
