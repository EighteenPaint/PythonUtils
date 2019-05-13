# -*- coding:utf-8 -*-
import cookielib
import getopt
import sys
import urllib
import urllib2

username = 'admin'
password = '111111'
loginUrl = 'http://192.168.6.88:8080/BPHCenter/admin/login.action'
targetUrl = 'http://192.168.6.88:8080/BPHCenter/api/mapConfig/getBaseConfig/72/1'
user_agent = ('User-agent',
              'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36')
accept = ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8')
ac_language = ('Accept-Language', 'zh-CN,zh;q=0.9')
accept_encoding = ('Accept-Encoding', 'gzip, deflate, br')
reload(sys)
sys.setdefaultencoding('utf-8')  # 因为ascii无法decode，先将默认的编码设为非ascii，否则所有格式的字节流均会编码为encode
if __name__ == '__main__':
    encoding = sys.stdout.encoding
    try:
        # 这里的 h 就表示该选项无参数，i:表示 i 选项后需要有参数
        opts, args = getopt.getopt(sys.argv[1:], "l:u:p:d:c:")
    except getopt.GetoptError:
        print 'Error'
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-u":
            '''用户名 -u'''
            print u'用户名:', arg
            username = arg
        elif opt == "-p":
            '''密码 -p'''
            print u'密码:', arg
            password = arg
        elif opt == "-d":
            '''目标地址 -d'''
            print u'url:', arg
            targetUrl = arg
        elif opt == '-l':
            '''登录地址 -l'''
            print u'登录地址', arg
            loginUrl = arg
        elif opt == '-e':
            '''编码配置 -e'''
            print u'编码', arg
            encoding = arg
    cj = cookielib.MozillaCookieJar()  # 创建cookie对象
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    opener.addheaders = [user_agent, ac_language]
    urllib2.install_opener(opener)
    req = urllib2.Request(loginUrl, urllib.urlencode({"username": username, "password": password}))
    resp = urllib2.urlopen(req)
    cj.save(filename="bphcenter.cookie", ignore_discard=True, ignore_expires=True)
    if encoding is None: encoding = 'gbk'
    print encoding
    print resp.read().encode(encoding, 'ignore')  # 网页过来的是utf-8编码的字节流，而终端编码是cp936也就是gbk 1.将utf-8 decode 2.encode为gbk
    result = urllib2.urlopen(targetUrl)
    print result.read().encode(encoding, 'ignore')  # 你对编码的理解没有问题，这里需要ignore
