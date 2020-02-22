import requests
import lxml.etree as etree

text = """
<body><div id="_dict_status" style="position: absolute; background-color: rgb(231, 247, 247); padding: 1px; margin: 0px; font-size: 14px; left: 3px; top: 3px; width: 138px; height: 22px; text-align: center; z-index: 99; border: 1px solid rgb(126, 152, 214); display: none;"></div><div id="_dict_layer" style="position: absolute; display: none; padding: 0px; margin: 0px; width: 240px; z-index: 98; background-color: rgb(255, 255, 255);"><table width="240" border="0" cellspacing="0" cellpadding="0" style="border-top:1px solid #7E98D6;border-left:1px solid #7E98D6;border-right:1px solid #7E98D6;border-bottom:1px solid #7E98D6;"><tbody><tr><td width="100%" style="border:none;padding:0px;margin:0px;"><div style="width:240px;height:20px;cursor:move;background-color:#C8DAF3;display:inline;border:none;padding:0px;margin:0px;" onmouseover="_dict_onmove=1;" onmouseout="_dict_onmove=0;"><table width="100%" border="0" cellspacing="0" cellpadding="0"><tbody><tr><td align="left" width="60%" height="20" style="background-color:#C8DAF3;color:#1A9100;font-size:14px;line-height:20px;border:none;padding:0 3px;margin:0px;font-weight:normal;font-family:Verdana, Geneva, Arial, Helvetica, sans-serif;" id="_dict_title" name="_dict_title">划词翻译 - Dict.CN</td><td align="right" height="20" style="background-color:#C8DAF3;line-height:20px;border:none;padding:0 3px;margin:0px;font-weight:normal;font-family:Verdana, Geneva, Arial, Helvetica, sans-serif;" valign="middle"><a href="http://dict.cn/scb/" target="_blank" title="生词本" style="border:none;padding:0px;margin:0px;font-weight:normal;font-family:Verdana, Geneva, Arial, Helvetica, sans-serif;" id="_dict_add" name="_dict_add"><img src="http://dict.cn/img/add.gif" border="0" style="border:none;display:inline;border:none;padding:0px;margin:0px;" align="absmiddle" data-bd-imgshare-binded="1"></a> <a href="http://dict.cn/" target="_blank" title="详细解释" style="border:none;padding:0px;margin:0px;font-weight:normal;font-family:Verdana, Geneva, Arial, Helvetica, sans-serif;" id="_dict_detail" name="_dict_detail"><img src="http://dict.cn/img/detail.gif" border="0" style="border:none;display:inline;border:none;padding:0px;margin:0px;" align="absmiddle" data-bd-imgshare-binded="1"></a> <a href="http://dict.cn/foot/help.htm" target="_blank" title="帮助" style="border:none;padding:0px;margin:0px;font-weight:normal;font-family:Verdana, Geneva, Arial, Helvetica, sans-serif;"><img src="http://dict.cn/img/help.gif" border="0" style="border:none;display:inline;border:none;padding:0px;margin:0px;" align="absmiddle" data-bd-imgshare-binded="1"></a> <a href="javascript:_dictClose()" title="关闭" target="_self" style="border:none;padding:0px;margin:0px;font-weight:normal;font-family:Verdana, Geneva, Arial, Helvetica, sans-serif;"><img src="http://dict.cn/img/close.gif" border="0" style="border:none;display:inline;border:none;padding:0px;margin:0px;" align="absmiddle" data-bd-imgshare-binded="1"></a></td></tr></tbody></table></div><table border="0" cellspacing="4" cellpadding="3" width="100%" align="center" onmouseover="_dict_onlayer=1;" onmouseout="_dict_onlayer=0;" style="border:none;padding:0px;margin:0px;"><tbody><tr><td style="border:none;padding:0px;margin:0px;"><fieldset color="#00c0ff" style="padding:0 2px;margin:0px;font-weight:normal;font-family:Verdana, Geneva, Arial, Helvetica, sans-serif;"><legend align="center" style="padding:0px;margin:0px;"><a href="http://dict.cn/" target="_blank" style="border:none;padding:0px;margin:0px;"><img src="http://dict.cn/img/qdict.gif" width="126" height="53" border="0" data-bd-imgshare-binded="1"></a></legend><table border="0" cellspacing="0" cellpadding="0" align="center" style="border:none;padding:0px;margin:0px;"><tbody><tr><td width="100%" height="120" style="border:none;padding:0px;margin:0px;" id="_dictContent" name="_dictContent"><iframe id="_dictFrame" name="_dictFrame" height="120" src="about:blank" frameborder="0" width="100%"></iframe></td></tr><tr align="center"><td width="100%" height="18" style="color:#999999;font-size:10px;line-height:18px;border:none;padding:0px;margin:0px;font-weight:normal;font-family:Verdana, Geneva, Arial, Helvetica, sans-serif;" valign="bottom"><a href="http://www.oralpractice.com/" target="_blank" title="鍏嶈垂瀛﹀彛璇紝涓€瀵逛竴缁冧範"><font color="#0000ff">鍏嶈垂瀛﹀彛璇紝涓€瀵逛竴缁冧範</font></a></td></tr><tr align="center"><td width="100%" height="18" style="color:#999999;font-size:10px;line-height:18px;border:none;padding:0px;margin:0px;font-weight:normal;font-family:Verdana, Geneva, Arial, Helvetica, sans-serif;" valign="bottom">©2003-2008 <a href="http://dict.cn/" target="_blank" style="color:#2EA8ED;font-size:10px;line-height:18px;text-decoration:none;border:none;padding:0px;margin:0px;font-weight:normal;font-family:Verdana, Geneva, Arial, Helvetica, sans-serif;">Dict.CN</a> <a href="http://dict.cn/" target="_blank" style="color:#999999;font-size:10px;line-height:18px;text-decoration:none;border:none;padding:0px;margin:0px;font-weight:normal;font-family:Verdana, Geneva, Arial, Helvetica, sans-serif;">海词</a></td></tr></tbody></table></fieldset></td></tr></tbody></table></td></tr></tbody></table></div>
<div id="container">
<div id="navigation">
<div id="logo">
   <a href="http://www.etymon.cn/" title="The Online Etymology Dictionary">
    <img src="http://www.etymon.cn/images/logo.jpg" title="英语词根词源在线字典" data-bd-imgshare-binded="1">
   </a>
  </div>
 <!-- LOGO -->
  <form action="/plus/search.php" method="get">
  <input type="hidden" name="kwtype" value="0">
  <div id="search">
   Search:
   <input type="text" name="q" value="在这里搜索..." onfocus="if(this.value=='在这里搜索...'){this.value='';}" onblur="if(this.value==''){this.value='在这里搜索...';}" size="40" maxlength="255" class="initial_focus">
	<select name="typeid" style="width:200">
<option value="0" selected="">--智能--</option>
<option value="1">词根</option>
<option value="2">词缀</option>
<option value="2">词源</option>
   </select>
   <input type="submit" value="OK">
  </div> <!-- SEARCH -->
  </form>
  <div id="browse">
  <ul><li><a href="http://www.etymon.cn/">主页</a></li>

<li><a href="/yingyucigen/">英语词根</a></li>

<li><a href="/yingyucizhui/">英语词缀</a></li>

<li><a href="/danciyinbian/">单词音变</a></li>

<li><a href="/ciyuanrumen/">词源入门</a></li>

<li><a href="/origins/">词源字典</a></li>

<li><a href="/vocabulary/">英语词汇</a></li>

<li><a href="/exam/">测试练习</a></li>

<li><a href="/yinbiao/">英语音标</a></li>
</ul>
  </div>
 </div>

<!-- NAVIGATION -->
  <div id="dictionary">
<dl>
<dt class="highlight"><h1>词根seism，seismo = seism 地震</h1></dt>
<dd class="highlight">&nbsp; 来源于希腊语 seismos/seiein 地震，晃动，seismo 为 seism 的变体。<br>
<br>
<strong>同源词：</strong><br>
<br>
1.seismic&nbsp; [seism 地震 +<a href="http://www.etymon.cn/yingyucizhui/yingyuhouzhui/201.html"> -ic</a> (a.) 表示“…的”→]<br>
&nbsp; adj. 地震的，地震引起的<br>
<br>
2.seismology&nbsp; [seism 地震 + -ology 名词后缀 ...学→]<br>
&nbsp; n. 地震学<br>
<br>
3.anti-seismic&nbsp; [<a href="http://www.etymon.cn/yingyucizhui/yingyuqianzhui/187.html">anti- </a>反对，反抗 + seism 地震 + -ic (a.) 表示“…的”→]<br>
&nbsp; adj. 抗地震的<br>
<br>
4.isoseismic&nbsp; [iso 相等、-ic (a.) 表示“…的”→]<br>
&nbsp; adj.&amp; n. 等震的，等震线<br>
<br>
5.microseism&nbsp; [<a href="http://www.etymon.cn/yingyucizhui/yingyuqianzhui/160.html">micro- </a>微，小 + seism 地震→]<br>
&nbsp; n. 微震<br>
<br>
6.seismogram&nbsp; [seism 地震 + gram 写，画 →画写与地震波有关的图形→]<br>
&nbsp; n.震波图，地震波曲线</dd>
 </dl>
<div style="width:400px;margin-left:auto; margin-right:auto; ">
<div class="bdsharebuttonbox bdshare-button-style0-16" data-bd-bind="1579004197707"><a href="#" class="bds_more" data-cmd="more">分享到：</a><a title="分享到QQ空间" href="#" class="bds_qzone" data-cmd="qzone">QQ空间</a><a title="分享到新浪微博" href="#" class="bds_tsina" data-cmd="tsina">新浪微博</a><a title="分享到腾讯微博" href="#" class="bds_tqq" data-cmd="tqq">腾讯微博</a><a title="分享到人人网" href="#" class="bds_renren" data-cmd="renren">人人网</a><a title="分享到微信" href="#" class="bds_weixin" data-cmd="weixin">微信</a></div>
<script>window._bd_share_config={"common":{"bdSnsKey":{},"bdText":"","bdMini":"2","bdMiniList":false,"bdPic":"","bdStyle":"0","bdSize":"16"},"share":{"bdSize":16},"image":{"viewList":["qzone","tsina","tqq","renren","weixin"],"viewText":"分享到：","viewSize":"32"},"selectShare":{"bdContainerClass":null,"bdSelectMiniList":["qzone","tsina","tqq","renren","weixin"]}};with(document)0[(getElementsByTagName('head')[0]||body).appendChild(createElement('script')).src='http://bdimg.share.baidu.com/static/api/js/share.js?v=89860593.js?cdnversion='+~(-new Date()/36e5)];</script>
</div>
<div class="paging">
<ul>

</ul>
</div> <!-- PAGING -->

 </div> <!-- DICTIONARY -->
 <div id="google-adsense"><!--广告位--><script src="/plus/ad_js.php?aid=24" language="javascript"></script></div>
 <div class="blank">&nbsp;</div><script language="javascript" type="text/javascript"> 
document.body.oncopy = function () { setTimeout( function ()
 { var text = clipboardData.getData("text"); if (text) 
{ text = text + "\r\n 本篇文章来源于http://www.etymon.cn  [英语词根词缀词源网] 原文链接地址："+location.href; clipboardData.setData("text", text); } }, 100 ) }
</script>
<div id="footer">
  <ul id="links">
   <li><a href="http://www.etymon.cn/yingyucigen/3093.html">词根seism，seismo = seism 地震</a></li>
<li><a href="http://www.etymon.cn/yingyucigen/1082.html">词根radi-,-ray-,-rad-,-radio-</a></li>
<li><a href="http://www.etymon.cn/yingyucigen/1121.html">词根ac,acr,acid = sour（酸的</a></li>
<li><a href="http://www.etymon.cn/yingyucigen/2489.html">词根paleo,pale,palae = old 老</a></li>

  </ul>
  <ul id="credits">
  <center><li><a href="http://www.etymon.cn/">英语词源字典</a><a href="http://www.etymon.cn/data/sitemap.html">地图</a></li></center>
   <li>英语词源词根词缀记忆法，是最科学背单词方法！</li>
   <li>专业<a href="http://www.etymon.cn/">英语词根</a>、词缀、词源以及词汇相关知识学习网站！</li>
   <li>© 2012-2022 Powered by http://www.etymon.cn/</li>
  </ul>
  <div class="blank">&nbsp;</div>
 </div><script src="/img/hc/hc.js" type="text/javascript"></script>
<script language="javascript" type="text/javascript" src="http://js.users.51.la/16789340.js"></script>
<!-- FOOTER -->
</div>


<iframe frameborder="0" id="bdSharePopup_selectshare1579004197711bg" class="bdselect_share_bg" style="display:none;"></iframe><div id="bdSharePopup_selectshare1579004197711box" style="display: none;" share-type="selectshare" class="bdselect_share_box" data-bd-bind="1579004197711"><div class="selectshare-mod-triangle"><div class="triangle-border"></div><div class="triangle-inset"></div></div><div class="bdselect_share_head"><span>分享到</span><a href="http://www.baidu.com/s?wd=&amp;tn=SE_hldp08010_vurs2xrp" class="bdselect_share_dialog_search" target="_blank"><i class="bdselect_share_dialog_search_i"></i><span class="bdselect_share_dialog_search_span">百度一下</span></a><a class="bdselect_share_dialog_close"></a></div><div class="bdselect_share_content"><ul class="bdselect_share_list bdshare-button-style0-16"><div class="bdselect_share_partners"><a href="#" class="bds_qzone" data-cmd="qzone"></a><a href="#" class="bds_tsina" data-cmd="tsina"></a><a href="#" class="bds_tqq" data-cmd="tqq"></a><a href="#" class="bds_renren" data-cmd="renren"></a><a href="#" class="bds_weixin" data-cmd="weixin"></a></div><a href="#" class="bds_more" data-cmd="more"></a></ul></div></div><div id="bdimgshare_1579004197721" class="sr-bdimgshare sr-bdimgshare-list sr-bdimgshare-32 sr-bdimgshare-black" style="height:48px;line-height:38px;font-size:14px;width:autopx;display:none;" data-bd-bind="1579004197721"><div class="bdimgshare-bg"></div><div class="bdimgshare-content bdsharebuttonbox bdshare-button-style0-32"><label class="bdimgshare-lbl">分享到：</label><a href="#" onclick="return false;" class="bds_qzone" data-cmd="qzone" hidefocus=""></a><a href="#" onclick="return false;" class="bds_tsina" data-cmd="tsina" hidefocus=""></a><a href="#" onclick="return false;" class="bds_tqq" data-cmd="tqq" hidefocus=""></a><a href="#" onclick="return false;" class="bds_renren" data-cmd="renren" hidefocus=""></a><a href="#" onclick="return false;" class="bds_weixin" data-cmd="weixin" hidefocus=""></a><a href="#" onclick="return false;" class="bds_more" data-cmd="more" hidefocus=""></a></div></div></body>
"""

"""
解析
"""

# 解析html字符串：使用"lxml.etree.HTML"解析
htmlElement = etree.HTML(text)
print(etree.tostring(htmlElement, encoding="utf-8").decode('utf-8'))

# 解析html文件：使用"lxml.etree.parse"解析
htmlElement = etree.HTML("tencent.html")
print(etree.tostring(htmlElement, encoding="utf-8").decode('utf-8'))

# 解析不确定编码格式的html文件，需要自己创建HTML解析器
parser = etree.HTMLParser(encoding='utf-8')
htmlElement = etree.parse("lagou.html", parser=parser)
print(etree.tostring(htmlElement, encoding='utf-8').decode('utf-8'))