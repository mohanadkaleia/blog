Title: How to configure Ratchet with SSL
Date: 2016-02-22 19:33
Author: mohanad
Category: Code
Tags: ratchet, ssl, websocket
Slug: how-to-configure-ratchet-with-ssl
Status: published

If you are using Apache web server (2.4 or above), enable these modules in httpd.conf file :

1.  [mod\_proxy.so](http://httpd.apache.org/docs/2.2/mod/mod_proxy.html)
2.  [mod\_proxy\_wstunnel.so](http://httpd.apache.org/docs/2.4/mod/mod_proxy_wstunnel.html)

Add this setting to your httpd.conf file

``` {.lang-php .prettyprint .prettyprinted dir="ltr"}
ProxyPass /wss2/ ws://ratchet.mydomain.org:8888/
```

Use this URL in your JavaSscript call when you want a WSS connection:

``` {.lang-php .prettyprint .prettyprinted dir="ltr"}
var ws = new WebSocket("wss://ratchet.mydomain.org/wss2/NNN");
```

Restart Apache web server and make sure that your Ratchet worker (web socket connection) is open before applying the settings (telnet hostname port).

 

Source:

http://stackoverflow.com/questions/16979793/php-ratchet-websocket-ssl-connect
