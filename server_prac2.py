from xmlrpc.server import SimpleXMLRPCServer

def factorial(n):
    ans = 1
    for i in range(1, n+1):
        ans = ans*i
    return ans

def square(n):
    pro = n*n
    return pro


port = 7500
server = SimpleXMLRPCServer(("localhost", port), logRequests = False)
server.register_function(factorial, 'factorial_rpc')
server.register_function(square, 'square_rpc')

try:
    print("Server listening on port number ", port)
    server.serve_forever()

except:
    print("Exit")