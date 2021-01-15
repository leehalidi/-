# -
Windows10下如何在断网后自动连接校园网
=

'Requirements:'

	python==3.6
	selenium==2.48.0	
	pywin32==300
	# 还需要下载[chromedriver.exe](http://chromedriver.storage.googleapis.com/index.html)，将其放到所使用的虚拟环境的python.exe所在的文件夹内
	# e.g. 我的程序运行的环境名为“tf", python.exe的路径是：D:\Softwares\Anaconda\envs\tf， 则将下载的chromedriver.exe放到此路径的文件夹内
	# 下载的版本和所使用的谷歌浏览器的版本一致

'Usage:'

	1） 修改以上程序中的一些参数，比如：账号、密码、日志保存位置（必需）； 休眠时间等（可选）
	2） win+R 输入cmd 打开cmd.exe
	3） 命令行输入以下命令：
		{python.exe所在的路径}\python.exe {以上程序文件所在的路径}\SZUAutoLogin.py
		e.g. D:\Softwares\Anaconda\envs\tf\python.exe C:\Users\dell\Desktop\SZUAutoLogin\SZUAutoLogin.py
	4） 程序将在后台运行，可以打开日志文件log.txt 查看网络连接情况
	5） 若想终止程序的运行，ctrl+alt+delete 打开任务管理器，从“后台进程”里面找到“Python”,将其结束即可。
