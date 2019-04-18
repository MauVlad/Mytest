from time import sleep

print ("INFO:tensorflow:Restoring parameters from data/model.ckpt \nINFO:tensorflow:Running local_init_op. \nINFO:tensorflow:Done running local_init_op. \nINFO:tensorflow:Starting Session. \nINFO:tensorflow:Saving checkpoint to path training\model.ckpt \nINFO:tensorflow:Starting Queues.")
print ("INFO:tensorflow:global_step/sec: 0")

step = 0
loss = 12
sec = 10


while loss >= 1 :

	if sec >= 1:
		step = step + 1
		loss = loss - .1142
		sec = sec - .0078

		print ("INFO:tensorflow:global step "+ str(step) +": loss = "+ str("{0:.4f}".format(loss)) + " (" + str("{0:.3f}".format(sec)) +" sec/step)")
		sleep(0.5)

		step = step + 1
		loss = loss + .1120
		sec = sec - .0139

		print ("INFO:tensorflow:global step "+ str(step) +": loss = "+ str("{0:.4f}".format(loss)) + " (" + str("{0:.3f}".format(sec)) +" sec/step)")
		sleep(0.5)

	if sec <= 1:
		step = step + 1
		loss = loss - .1142
		sec = sec - .0745


		print ("INFO:tensorflow:global step "+ str(step) +": loss = "+ str("{0:.4f}".format(loss)) + " (" + str("{0:.3f}".format(sec)) +" sec/step)")
#		sleep(0.5)

		step = step + 1
		loss = loss + .1130
		sec = sec + .0745

		print ("INFO:tensorflow:global step "+ str(step) +": loss = "+ str("{0:.4f}".format(loss)) + " (" + str("{0:.3f}".format(sec)) +" sec/step)")
#		sleep(0.5)

###print ("INFO:tensorflow:global step 1: loss = 13.8886 (12.339 sec/step) \nINFO:tensorflow:global step 2: loss = 16.2202 (0.937 sec/step) \nINFO:tensorflow:global step 3: loss = 13.7876 (0.904 sec/step) \nINFO:tensorflow:global step 4: loss = 12.9230 (0.894 sec/step) \nINFO:tensorflow:global step 5: loss = 12.7497 (0.922 sec/step) \nINFO:tensorflow:global step 6: loss = 11.7563 (0.936 sec/step) \nINFO:tensorflow:global step 7: loss = 11.7245 (0.910 sec/step)")
###print ("INFO:tensorflow:global step 8: loss = 10.7993 (0.916 sec/step) \nINFO:tensorflow:global step 9: loss = 9.1277 (0.890 sec/step) \nINFO:tensorflow:global step 10: loss = 9.3972 (0.919 sec/step) \nINFO:tensorflow:global step 11: loss = 9.9487 (0.897 sec/step) \nINFO:tensorflow:global step 12: loss = 8.7954 (0.884 sec/step) \nINFO:tensorflow:global step 13: loss = 7.4329 (0.906 sec/step) \nINFO:tensorflow:global step 14: loss = 7.8270 (0.897 sec/step) \nINFO:tensorflow:global step 15: loss = 6.4877 (0.894 sec/step)")

