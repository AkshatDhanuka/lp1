import xmlrpc.client
proxy = xmlrpc.client.ServerProxy('http://localhost:7500/')
print("factorial of 3 is: ", proxy.factorial_rpc(3))
print("Square of 5 is: ", proxy.square_rpc(5))
