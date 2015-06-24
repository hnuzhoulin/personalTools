# 办公软件
记录我安装使用过的Linux下的办公软件，记录安装和配置过程。

## 1. xmind
著名的脑图软件，基于java，跨平台，有Linux、Win和MAC，不过，ubuntu下官方安装包无法安装，所以只采用便携版，便携版有一个问题就是需要一些额外配置，简述如下。

#### 1.1 安装

1. 下载便携版xmind-portable-3.5.2.201504270119.zip
2. 解压后将Common(所有平台都需要)和XMind_Linux_64bit(根据你的实际情况修改)文件夹拷贝到你放软件的目录，后文统称xmind家目录记为$XMIND_HOME，我这里是 **/home/zhoulin/soft/xmind/** 后续所有的配置都是以这个目录为例。
3. 添加执行权限  **chmod +x XMind**
4. 验证java是否安装，如果没有可以考虑安装 **sudo apt-get install openjdk-6-jre-headless**

#### 1.2 配置桌面快捷方式

1. 首先修改配置文件： **$XMIND_HOME/XMind_Linux_64bit/XMind.ini**，修改为下面的内容：
```
-product
org.xmind.cathy.product
-configuration
/home/zhoulin/soft/xmind/XMind_Linux_64bit/configuration
-startup
/home/zhoulin/soft/xmind/Commons/plugins/org.eclipse.equinox.launcher_1.3.0.v20120522-1813.jar
--launcher.library
/home/zhoulin/soft/xmind/Commons/plugins/org.eclipse.equinox.launcher.gtk.linux.x86_64_1.1.200.v20120913-144807
-data
/home/zhoulin/soft/xmind/Commons/data/workspace-cathy
--launcher.defaultAction
openFile
-vmargs
-Dfile.encoding=UTF-8
-Dorg.xmind.product.distribution.id=cathy_portable
```
注意，这里的目录都是xmind家目录下的绝对路径，

2. 在桌面新建xmind.desktop文件，内容如下：
```
#!/usr/bin/env xdg-open
[Desktop Entry]
Type=Application
Name=XMind
Comment=XMind Launcher
Categories=Editor;
Exec=/home/zhoulin/soft/xmind/XMind_Linux_64bit/XMind
Icon=/home/zhoulin/soft/xmind/XMind_Linux_64bit/xmind.ico
Terminal=false
StartupNotify=true
```
注意，这里的xmind.ico是从原便携版中的win版目录下拷贝出来的。

#### 1.3 下载地址
[下载地址](http://www.xmind.net/download/portable/)

## 2.wiznote为知笔记
```
sudo add-apt-repository ppa:wiznote-team/ppa
sudo apt-get install wiznote
```