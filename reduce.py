#!

import sys
import zmapreduce

import mapreduce

node_id = int(sys.argv[1].split('-')[1])
print sys.argv
print "reduce %d" % node_id
r = zmapreduce.Reducer(node_id)
r.map_fn = mapreduce.Map
r.reduce_fn = mapreduce.Reduce
r.combine_fn = mapreduce.Combine
r.comparator_fn = mapreduce.ComparatorHash
r.mritem_size = 28
r.hash_size = 10
r.start()