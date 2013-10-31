#!

import sys
import zmapreduce

import mapreduce

print >> sys.stderr, sys.argv, sys.executable, sys.argv0
node_id = int(sys.argv0.split('-')[1])

m = zmapreduce.Mapper(node_id)
m.map_fn = mapreduce.Map
m.reduce_fn = mapreduce.Reduce
m.combine_fn = mapreduce.Combine
m.mritem_size = 28
m.hash_size = 10
m.start()