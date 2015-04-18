# ceph
跟ceph相关的小脚本，小工具收集。

### ceph_s3.py
这个主要是为了方便当前使用linux系统有需要频繁查看ceph对象存储数据而写的简单脚本，目前的简单功能如下：

需要先修改当前脚本，修改其中的accesskey 和secretkey，执行时结构如下：

python ceph_s3.py HOST_IP/HOSTNAME [command] [option]

支持的command列表以及对应option如下：

1. listbucket：列出当前账户下所有bucket
2. listobject BUCKET_NAME: 列出bucket下的所有object
3. delbucket BUCKET_NAME :删除bucket及其下所有object
4. delobject BUCKET_NAME  OBJECT_NAME :删除bucket下的指定object
5. createbucket BUCKET_NAME ：新建bucket