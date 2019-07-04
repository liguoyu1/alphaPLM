# scripts 主要涉及　模型的过滤和瘦身，模型的预测测试

----简介
	model_mlr_lite.py 主要是模型瘦身
	predict_mlr.py　主要是模型的预测测试，模型瘦身后的正确性验证

----使用说明
	path/scripts> python model_mlr_lite.py full_model_file_name lite_model_file_name piece_num
	full_model_file_name: 全量模型的文件名
	lite_model_file_name: 瘦身后模型文件名
	piece_num: 模型切片的个数

	path/scripts> python predict_mlr.py lite_model_file_name result_file_name [piece_num] [thread_num]
	result_file_name: 预测结果存放文件名
	thread_num: 执行线程数，默认１：暂未实现多线程，以后有时间添加
