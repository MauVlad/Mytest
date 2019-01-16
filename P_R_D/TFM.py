from time import sleep

print ("INFO:tensorflow:Restoring parameters from data/model.ckpt \nINFO:tensorflow:Running local_init_op. \nINFO:tensorflow:Done running local_init_op. \nINFO:tensorflow:Starting Session. \nINFO:tensorflow:Saving checkpoint to path training\model.ckpt \nINFO:tensorflow:Starting Queues.")
print ("INFO:tensorflow:Starting Queues.")

step = 0
loss = 20
sec = 15

while sec >= 1 :

	step = step + 1
	loss = loss - .1142
	sec = sec - .0049

	print ("INFO:tensorflow:global step "+ str(step) +": loss = "+ str(loss) + "(" + str(sec) +"sec/step)")
#	sleep(.5)

	step = step + 1
	loss = loss + .1130
	sec = sec + .0039

	print ("INFO:tensorflow:global step "+ str(step) +": loss = "+ str(loss) + "(" + str(sec) +"sec/step)")
#	sleep(.5)
