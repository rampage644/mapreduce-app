#!

import sys
import zmapreduce

import mapreduce

print >> sys.stderr, sys.argv, sys.executable, sys.argv0
node_id = int(sys.argv0.split('-')[1])

r = zmapreduce.Reducer(node_id)
r.map_fn = mapreduce.Map
r.reduce_fn = mapreduce.Reduce
r.combine_fn = mapreduce.Combine
r.mritem_size = 28
r.hash_size = 10
r.start()