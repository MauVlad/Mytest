foo = []
bar = foo
print (foo == bar)
print (foo is bar)

foo.append(bar)
print (foo)

import tensorflow as tf
graph = tf.get_default_graph()
print (graph.get_operations())

input_value = tf.constant(1.0)

operations = graph.get_operations()
print (operations)

print (operations[0].node_def)

input_value
sess = tf.Session()
print (sess.run(input_value))

weight = tf.Variable(0.8)

for op in graph.get_operations(): print (op.name)

output_value = weight * input_value
op = graph.get_operations()[-1]
print (op.name)
for op_input in op.inputs: print(op_input)

init = tf.initialize_all_variables()
sess.run(init)
print (sess.run(output_value))

x = tf.constant(1.0, name='input')
w = tf.Variable(0.8, name='weight')
y = tf.multiply(w,x, name='output')

##summary_writer = tf.train.SummaryWriter('log_simple_graph', sess.graph)
summary_writer = tf.summary.FileWriter('log_simple_graph', sess.graph)
