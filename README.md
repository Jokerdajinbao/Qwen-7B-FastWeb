# Qwen-7B-Chat-FastWeb
基于ModelScope社区开源Qwen-7B-Chat体验程序修改的web版本，以方便快速体验。  
ModelScope社区提供了开源模型Qwen-7B的快速体验脚本，脚本和运行效果如下所示：  
<div align="center">
  <img src="img/pic1.jpg">
</div>
<div align="center">
  <img src="img/pic2.jpg">
</div>
但是脚本本身只有命令行的输出，这里给脚本加了一个基于gradio简单用法做成的的web界面，运行后会提供一个web界面，体验感应该会好一点。  
运行时先拉取或者下载项目里的文件，然后安装依赖：  
pip install -r requirements.txt  
然后用python运行主程序即可：  
python qwen_web,py  
程序会自动从ModelScope社区拉取与上方脚本一致的模型并运行。
