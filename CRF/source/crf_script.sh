#crf performance during training and testing
crf_learn template eng.train1 model_crf > training_crf_output
crf_test -n 3 -m model_crf eng.test1 > testing_crf_name_output 
crf_test -n 5 -m model_crf eng.test1 > testing_crf_org_output 


