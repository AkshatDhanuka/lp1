import xmlrpc.client
proxy = xmlrpc.client.ServerProxy('http://localhost:7500/')
print("Factorial of 3 is ", proxy.factorial_rpc(3))
print("Factorial of 6 is ", proxy.square_rpc(6))
