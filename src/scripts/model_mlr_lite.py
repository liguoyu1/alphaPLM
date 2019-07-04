# -*- coding: utf-8 -*-
# load model and predict mlr
from __future__ import unicode_literals
#!/usr/bin/python
import sys
piece_num = int(sys.argv[3])
lite_model = open(sys.argv[2], 'w')
line_count = 0
for line in open(sys.argv[1], 'r'):
	if not line:
		break
	else:
		if piece_num == 1:
			if line.split('\t')[2] != '0':
				lite_model.write(line)
		else :
			line_sp = line.split()
			filter = True
			feature = line_sp[0]
			for i in xrange(piece_num):
				if line_sp[1+i] != '0' or line_sp[1+piece_num+i] != '0':
					lite_model.write(feature+"\t"+str(i)+"\t"+line_sp[1+i]+"\t"+line_sp[1+piece_num+i]+"\n")
	line_count+=1
	if line_count % 1000000 == 0:
		print "finishede line count:%d"%line_count
		# break
lite_model.close()