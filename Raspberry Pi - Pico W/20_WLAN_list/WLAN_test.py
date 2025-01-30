'''
WLAN_test.py

Ergebis:

Response content: b'<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="de"><head><meta content="text/html; charset=UTF-8" http-equiv="Content-Type"><meta content="/logos/doodles/2025/lunar-new-year-2025-6753651837110588.3-law.gif" itemprop="image"><meta content="Mond-Neujahr 2025" property="twitter:title"><meta content="Mond-Neujahr 2025 #GoogleDoodle" property="twitter:description"><meta content="Mond-Neujahr 2025 #GoogleDoodle" property="og:description"><meta content="summary_large_image" property="twitter:card"><meta content="@GoogleDoodles" property="twitter:site"><meta content="https://www.google.com/logos/doodles/2025/lunar-new-year-2025-6753651837110588.4-2xa.gif" property="twitter:image"><meta content="https://www.google.com/logos/doodles/2025/lunar-new-year-2025-6753651837110588.4-2xa.gif" property="og:image"><meta content="1000" property="og:image:width"><meta content="400" property="og:image:height"><meta content="https://www.google.com/logos/doodles/2025/lunar-new-year-2025-6753651837110588.4-2xa.gif" property="og:url"><meta content="video.other" property="og:type"><title>Google</title><script nonce="p3gVZ6DaT8waeEw_muynAw">(function(){var _g={kEI:\'LROaZ4XHCIKchbIPofLDoAk\',kEXPI:\'0,4240045,2872,2891,8348,34680,247991,142932,45786,166265,47082,30911,5230292,10463,766,49,8834864,13,22,6,27977849,25228681,42876,74430,5798,15164,8181,5928,15411,49178,580,6756,23879,9139,4599,169,159,6226,6630,26993,687,29855,1341,13707,50,8155,7430,12132,459,1929,3049,242,3491,33,2330,18056,1,6321,10665,5,5038,4721,4,1978,70,9237,3281,1498,14,4,3836,41,3915,9724,1,1720,3210,1811,4106,306,46,4105,6595,1640,2251,663,3626,913,4957,951,628,1521,2830,1784,5774,4309,2372,1263,2,738,4381,335,81,1439,1731,767,461,2030,91,7591,20,1745,3,2,2630,339,1633,1,3017,2666,2803,727,829,129,3261,41,2,415,150,1490,206,684,15,964,780,372,932,394,714,639,2,762,386,93,1,1,1058,76,25,56,559,467,1,827,1,80,11,127,1,37,666,1896,1558,154,4,926,1022,1268,66,569,154,3,2093,116,562,665,599,117,2,292,8,220,10,502,143,2079,654,433,136,46,172,1155,616,407,354,299,5,86,639,15,139,3,676,325,468,1051,239,3,461,810,273,185,6,214,711,6,1552,898,923,2,87,342,12,362,226,406,71,32,303,3,2,2,2,2,2,2,769,4,397,295,13,195,68,664,315,290,79,232,57,158,1143,6,563,11,347,49,136,23,288,1671,89,1,6,98,311,53,782,793,69,165,107,1360,470,95,177,9,269,1,228,1,214,1222,21343575,4,28852,18,2010,48,2482,8,3327,546,12,689,222,842,1198,3\',kBL:\'Gfzc\',kOPI:89978449};(function(){var a;((a=window.google)==null?0:a.stvsc)?google.kEI=_g.kEI:window.google=_g;}).call(this);})();(function(){google.sn=\'webhp\';google.kHL=\'de\';})();(function(){\nvar g=this||self;function k(){return window.google&&window.google.kOPI||null};var l,m=[];function n(a){for(var b;a&&(!a.getAttribute||!(b=a.getAttribute("eid")));)a=a.parentNode;return b||l}function p(a){for(var b=null;a&&(!a.getAttribute||!(b=a.getAttribute("leid")));)a=a.parentNode;return b}function q(a){/^http:/i.test(a)&&window.location.protocol==="https:"&&(google.ml&&google.ml(Error("a"),!1,{src:a,glmm:1}),a="");return a}\nfunction r(a,b,d,c,h){var e="";b.search("&ei=")===-1&&(e="&ei="+n(c),b.search("&lei=")===-1&&(c=p(c))&&(e+="&lei="+c));var f=b.search("&cshid=")===-1&&a!=="slh";c="&zx="+Date.now().toString();g._cshid&&f&&(c+="&cshid="+g._cshid);(d=d())&&(c+="&opi="+d);return"/"+(h||"gen_204")+"?atyp=i&ct="+String(a)+"&cad="+(b+e+c)};l=google.kEI;google.getEI=n;google.getLEI=p;google.ml=function(){return null};google.log=function(a,b,d,c,h,e){e=e===void 0?k:e;d||(d=r(a,b,e,c,h));if(d=q(d)){a=new Image;var f=m.length;m[f]=a;a.onerror=a.onload=a.onabort=function(){delete m[f]};a.src=d}};google.logUrl=function(a,b){b=b===void 0?k:b;return r("",a,b)};}).call(this);(function(){google.y={};google.sy=[];var d;(d=google).x||(d.x=function(a,b){if(a)var c=a.id;else{do c=Math.random();while(google.y[c])}google.y[c]=[a,b];return!1});var e;(e=google).sx||(e.sx=function(a){google.sy.push(a)});google.lm=[];var f;(f=google).plm||(f.plm=function(a){google.lm.push.apply(google.lm,a)});google.lq=[];var g;(g=google).load||(g.l

'''

import network
import requests

# Wi-Fi Zugangsdaten
ssid = 'R2-D2'
password = 'xxx'

# Verbinde mit WiFi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

# Mit WiFI verbunden
wlan.connect(ssid, password)

# GET-Anfrage stellen
response = requests.get("http://www.google.com")
# Abrufen des Antwortcodes
response_code = response.status_code
#   Abrufen von Antwortinhalten
response_content = response.content

# Print Erebnis
print('Response code: ', response_code)
print('Response content:', response_content)
