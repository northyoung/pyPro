pyPro/src/Music163/

网易云音乐高品音质音乐下载后音乐本身信息缺失，大多数没有音轨号码，导入ituns，手动整理极为麻烦，/src/Music163/AutoNum.py 从网易云音乐中获取音轨号码，自动检测文件夹下mp3文件，修改文件音轨号码。
文件使用方法：
1.在网易云音乐上下载专辑。比如：radiohead  Kid - A  放入文件夹 F:\CloudMusic
2.在程序中填写专辑信息。比如：kid_a = 'http://music.163.com/album?id=2065424' 
  注：不可使用http://music.163.com/#/album?id=2065424 本地址无法获取音乐专辑列表
3.dirName 是指本地存放下载MP3文件的路径。这里应该是F:\CloudMusic
4.调用getMusicInfo()传入kid_a 
5.done
