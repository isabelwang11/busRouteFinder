########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': 'dcf518637bb646e2b34be90449550228',
}

params = urllib.parse.urlencode({
    # Request parameters
    # '$format': '{String}',
    # '$filter': '{String}',
    # '$select': '{String}',
    # '$top': '{string}',
    # '$skip': '{string}',
    # '$orderby': '{String}',
})

def findChar(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

def write_to_file(data):
    start_index = data.find('[')
    end_index = data.find(']')
    dict_str = data[start_index+1:end_index]
    stop_set = set()
    all_start_indices = findChar(dict_str, '{')
    all_end_indices = findChar(dict_str, '}')
    for num in range(0, len(all_start_indices)):
        stop_str = dict_str[all_start_indices[num]:all_end_indices[num]+1]
        stop_set.add(stop_str)
    with open("routes_stops_data.txt", "w") as f:
        for s in stop_set:
            f.write(s+"\n")

try:
    conn = http.client.HTTPSConnection('hacktj2020api.eastbanctech.com')
    conn.request("GET", "/transitiq/Routes('RiOn432_2565_5589')/Stops?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    decoded_data = data.decode() # includes string version of dictionary
    # print(data)
    write_to_file(decoded_data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################