# 2150, 2069, 1212, 2296, 2800, 544, 1618, 356, 1523, 4965, 3681
#First Come first Serve scheduling algorithm
def FCFS_simul(req,head):
	distance_moved = 0  #distance
	cur_head = head
	for track in req:
		distance_moved += abs(track-cur_head)
		cur_head = track
	return distance_moved

# Shortest Seek Time first Algorithm
def SSTF_simul(req,head):
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

# SCAN algorithm
def SCAN_simul(req,head):
	cur_head = head
	req = sorted(list(set(req)))
	req_size = len(req)
	distance_moved = 0
	cur_track = min(req,key=lambda x: abs(cur_head - x))
	#if initial direction is towards right
	start_index = req.index(cur_track)
	distance_moved += abs(cur_head - cur_track)
	if cur_track >= cur_head and req_size!=0:
		#serve towards right
		for ix in range(start_index,req_size):
			 cur_head = req[ix-1]
			 cur_track = req[ix]
		#serve towards left
		cur_head = req[-1]
		cur_tack = req[0]
		distance_moved+=abs(cur_track-cur_head)
		for ix in range(1,start_index):
			cur_head = req[ix-1]
			cur_track = req[ix]
			distance_moved+= abs(cur_track-cur_head)
	else:
		pass
	return distance_moved

SSTF_simul([2069, 1212, 2296, 2800, 544, 1618, 356, 1523, 4965, 3681],2150)
FCFS_simul([2069, 1212, 2296, 2800, 544, 1618, 356, 1523, 4965, 3681],2150)