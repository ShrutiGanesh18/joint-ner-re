#use this model to generate best-n ner tags for final_data
crf_test -n 3 -m model_crf final_data1 > final_data_best3tags 
crf_test -n 5 -m model_crf final_data1 > final_data_best5tags 
crf_test -n 1 -m model_crf final_data1 > final_data_best1nametags 
crf_test -n 1 -m model_crf final_data1 > final_data_best1orgtags 

