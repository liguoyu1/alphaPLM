# -*- coding: utf-8 -*-
# load model and predict mlr
from __future__ import unicode_literals
#!/usr/bin/python
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import numpy as np
import math
print len(sys.argv)
if len(sys.argv)< 3:
	print "please input full model file name and save result file name at least!!!"
	exit(0)

piece_num = 12
if len(sys.argv) == 4:
	piece_num = int(sys.argv[3])
result = open(sys.argv[2], 'w')
line_count = 0
model = {}
for line in open(sys.argv[1], 'r'):
	if not line:
		break
	else:
		line_sp = line.split()
		feature = line_sp[0]
		index = int(line_sp[1])
		u_v = float(line_sp[2])
		w_v = float(line_sp[3])
		if feature in model:
			model[feature][index] = [u_v, w_v]
		else:
			model[feature] = {}
			model[feature][index] = [u_v, w_v]

	line_count+=1
	if line_count % 1000000 == 0:
		print "finished line count:%d"%line_count
		# break

def sigmode(x):
	return 1 / (1 + np.exp(-x))

def get_uw_T_x(features, model):
	u_T_x = np.zeros(piece_num)
	w_T_x = np.zeros(piece_num)
	features.append("bias")
	for feature in features:
		u_zeros = np.zeros(piece_num)
		w_zeros = np.zeros(piece_num)
		if feature in model:
			for v in model[feature]:
				u_zeros[v] = model[feature][v][0]
				w_zeros[v] = model[feature][v][1]
				# print u_zeros
		u_T_x += u_zeros
		w_T_x += w_zeros
	print u_T_x
	print w_T_x
	u_T_x = u_T_x - np.max(u_T_x)
	return np.exp(u_T_x), sigmode(w_T_x)

def predict(features, model):
	features_cal = [feature.split(":")[0] for feature in features]
	uTx, wTx = get_uw_T_x(features_cal, model)
	dim = 0.0
	re = 0.0
	for x, y in zip(uTx, wTx):
		re += x*y
		dim += x
	return re/dim

for line in sys.stdin:
	if not line:
		break
	else:
		# print model
		line_sp = line.split("\t")
		line_news = "\t".join(line_sp[1:-1])
		label = line_sp[0]
		feature_line = line_sp[-1]
		# print feature_line
		features = feature_line.split()
		# print features
		# break
		score = predict(features, model)
		print label+"\t"+str(score)+"\t"+line_news
		result.write(label+"\t"+str(score)+"\t"+line_news)
		break