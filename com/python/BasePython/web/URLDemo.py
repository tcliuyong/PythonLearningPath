# -*- coding:utf-8 -*-
import urlparse
if __name__ == "__main__":
    #url的解析
    r = urlparse.urlparse("http://www.baidu.com:80/test?username=tcliou")
    print r.scheme
    print r.path
    print r.params
    print r.query
    print r.port
    print r.netloc
    #url的拼接
    r = urlparse.urljoin("http://","www.baidu.com")
    print r
    #url的分解 将url的五元组进行组合
    r = urlparse.urlunsplit(("http","www.baidu.com","fla","",""))
    print r
