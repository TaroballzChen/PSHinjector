# PSHinjector
PSHinjector autoscript is a tool that inject shellcode(x64 payload) by powershell with python3 programing 

PSHinjector是一個由python3編寫的工具，可載入客製Metasploit生成的powershell格式的raw檔(須為x64_rev_https或x64_rev_http)並使用PS1toEXE封裝或是您也可使用本工具生成普通的raw檔再進行封裝。

提取powershell empire專案中shellcode注入模塊將Metasploit生成的shellcode注入

且本工具亦提取Invoke-Obfuscation專案的powershell代碼混淆模塊對powershell代碼混淆

您也可使用python3.HttpServer將生成的payload放置output文件夾中，並讓受害者執行此工具生成的語句獲得會話

![image](https://i.imgur.com/6yEkh58.png)

# Basic Flow
* Example 1
	* msfvenom 產生raw檔
	* sc 引入powershell格式raw檔
	* og 合併powershell文件
  * exe 模塊封裝
	* msf 模塊監聽
* Example 2
	* sc 模塊產生普通raw檔
	* og 合併powershell文件
	* ob 混淆powershell代碼
  * web 開啟HttpServer等待下載語句
  * msf 模塊監聽
* Example 3
	* sc 模塊產生普通raw檔
	* og 合併powershell文件
	* exe 模塊封裝
	* msf 模塊監聽	

還有更多使用方法可以發掘
	
# Requirements 

python3

# Installation 
```
$ git clone https://github.com/curtis992250/PSHinjector.git

```
# Usage
```
$ python3 pshinjector.py
```

# Reference
* 
* 
* 
* 
