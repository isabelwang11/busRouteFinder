########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': 'dcf518637bb646e2b34be90449550228',
}

params = urllib.parse.urlencode({
})

try:
    conn = http.client.HTTPSConnection('hacktj2020api.eastbanctech.com')
    conn.request("GET", "/transitiq/GeoAreas('{lat}|{lon}|{radius}')/Stops?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read() # dictionary
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################