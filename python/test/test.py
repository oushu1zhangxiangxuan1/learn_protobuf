import test_pb2

req = test_pb2.SearchRequest()
req.query = '100'
req.page_number = 2
req.result_per_page = 5


protoStr = req.SerializeToString()
print(protoStr)

req1 = test_pb2.SearchRequest().ParseFromString(protoStr)
print(req.query)
print(req.page_number)
print(req.result_per_page)