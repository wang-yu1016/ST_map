import numpy

fname = 'data/ground_truth.txt'
with open(fname, 'r') as f:
    gt = numpy.loadtxt(f)
# gt[0]:Trace  gt[1]:HR  gt[2]:Time

gt_clip = {'trace':[], 'hr':[]}
multiple = 1
last_idx = 0
min_interval = 0xfff
# 取距离2.5的倍数最近的时间作为分段的index
for idx, time in enumerate(gt[2]):
    interval = abs(time - multiple * 2.5)
    if interval <= min_interval:
        min_interval = interval
    else:
        min_interval = 0xfff
        gt_clip['trace'].append(gt[0][last_idx:idx])
        gt_clip['hr'].append(gt[1][last_idx:idx])
        if len(gt[1][last_idx:idx+1]) > 100:
            print('error!')
        last_idx = idx
        multiple += 1
