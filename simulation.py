# 2150, 2069, 1212, 2296, 2800, 544, 1618, 356, 1523, 4965, 3681
#First Come first Serve scheduling algorithm
import copy
def FCFS_simul(req,head):
	req = copy.copy(req)
	distance_moved = 0  #distance
	cur_head = head
	for track in req:
		distance_moved += abs(track-cur_head)
		cur_head = track
	return distance_moved

# Shortest Seek Time first Algorithm
def SSTF_simul(req,head):
	req = copy.copy(req)
	cur_head = head
	distance_moved = 0
	response = 0
	req = list(set(req))
	max_distance= max(req)
	min_distance = abs(cur_head - max_distance)
	while(len(req) > 0):
		# service requests
		for track in req:
			response = abs(cur_head - track)
			if (response < min_distance):
				min_distance = response
				max_distance = track
		cur_head = max_distance
		req.remove(max_distance)
		distance_moved += min_distance
		if (len(req) > 0):
			min_distance = abs(cur_head - max(req))
			max_distance = max(req)
	return distance_moved
#SCAN algorithm
def SCAN_simul(req,head):
	req = copy.copy(req)
	cur_head = head
	distance_moved = 0
	max_request = max(req)
	req = sorted(req)
	end = 4999
	for check in range(cur_head, max_request+1):
		if (check in req):
			distance_moved+=abs(check-cur_head)
			req.remove(check)
			cur_head = check
	#move to end
	distance_moved += abs(cur_head - end)
	cur_head = end
	while max_request >= 0:
		if (max_request in req):
			distance_moved += abs(cur_head- max_request)
			req.remove(max_request)
			cur_head = max_request
		max_request -= 1
	return distance_moved

def LOOK_simul(req,head):
	req = copy.copy(req)
	cur_head = head
	distance_moved = 0	
	max_request = max(req)
	for i in range(cur_head, max_request+1):
		if (i in req):
			distance_moved += abs(cur_head - i)
			cur_head = i
			req.remove(i)
	while max_request >= 0:
		if (max_request in req):
			distance_moved += abs(cur_head - max_request)
			cur_head = max_request
			req.remove(max_request)
		max_request -= 1
	return distance_moved

def CSCAN_simul(req,head):
	req = copy.copy(req)
	cur_head = head
	distance_moved = 0
	max_request = max(req)
	end = 4999
	for i in range(cur_head,max_request+1):
		if (i in req):
			distance_moved+=abs(cur_head-i)
			cur_head = i
			req.remove(i)
	#move to the start
	distance_moved += abs(cur_head-end)
	distance_moved += end
	cur_head = 0
	for i in range(0, max_request+1):
			if (i in req):
				distance_moved += abs(i-cur_head)
				cur_head = i
				req.remove(i)
	return distance_moved

def CLOOK_simul(req,head):
	req = copy.copy(req)
	cur_head = head
	distance_moved = 0
	max_request = max(req)
	min_request = min(req)
	for i in range(cur_head, min_request-1,-1):
		if (i in req):
			distance_moved += abs(cur_head - i)
			cur_head = i
			req.remove(i) 
	distance_moved += abs(cur_head-max_request)
	cur_head = max_request
	for i in range(max_request,head-1,-1):
		if (i in req):
			distance_moved += abs(cur_head - i)
			cur_head = i
			req.remove(i)
	return distance_moved

# [2069, 1212, 2296, 2800, 544, 1618, 356, 1523, 4965, 3681],2150)

if __name__ == "__main__":
	f = open('data','r')
	head_position = int(f.readline())
	req = list(map(int,f.readline().strip().split(" ")))
	print("Total distance moved for FCFS  is ",FCFS_simul(req,head_position))
	print("Total distance moved for SSTF  is ",SSTF_simul(req,head_position))
	print("Total distance moved for SCAN  is ",SCAN_simul(req,head_position))
	print("Total distance moved for LOOK  is ",LOOK_simul(req,head_position))
	print("Total distance moved for CSCAN is ",CSCAN_simul(req,head_position))
	print("Total distance moved for CLOOK is ",CLOOK_simul(req,head_position))
	
	