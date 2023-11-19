import xmlrpc.client
proxy = xmlrpc.client.ServerProxy("http://localhost:7500/")
print("Factorial of 4 is ", proxy.factorial_rpc(4))
print("Square of 4 is ", proxy.square_rpc(4))
