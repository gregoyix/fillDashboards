"""

http wrapper

Exporta los metodos get, post y delete

"""

import httplib2
import socks
import simplejson as json

PROXY = "NO"

PROXI_DIR = 'proxytid.hi.inet'
PUERTO = 8080

"""
get
"""
def get(url):
    print url
    if (PROXY == "SI"):
        h = httplib2.Http(proxy_info = httplib2.ProxyInfo(socks.PROXY_TYPE_HTTP, PROXI_DIR, PUERTO))
    else:
        h = httplib2.Http()
    resp, content = h.request(url, "GET")
    print "resp ", resp
    print content
    #print json.dumps(content, indent=4)
    return resp

"""
post
"""
def post(url, data):
    if (PROXY == "SI"):
        h = httplib2.Http(proxy_info = httplib2.ProxyInfo(socks.PROXY_TYPE_HTTP, PROXI_DIR, 8080))
    else:
        h = httplib2.Http()
    resp, content = h.request(url, "POST", data)
    print "resp ", resp
    #print content
    print json.dumps(content, indent=4)
    return content

"""
delete
"""
def delete(url,data=None):
    if (PROXY == "SI"):
        h = httplib2.Http(proxy_info = httplib2.ProxyInfo(socks.PROXY_TYPE_HTTP, PROXI_DIR, 8080))
    else:
        h = httplib2.Http()
    resp, content = h.request(url, "DELETE", data)
    print "resp ", resp
    #print content
    print json.dumps(content, indent=4)
    return content

