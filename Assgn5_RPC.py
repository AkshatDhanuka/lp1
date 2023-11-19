from xmlrpc.server import SimpleXMLRPCServer

# factorial Function
def factorial(n):
    ans = 1
    for i in range(1, n+1):
        ans = ans*i
    return ans

# square function
def square(n):
    sq = n*n
    return sq


port = 7500
server = SimpleXMLRPCServer(("localhost", port), logRequests=False)
server.register_function(factorial, 'factorial_rpc')
server.register_function(square, 'square_rpc')

try:
    print("Starting and listening on port ", port)
    server.serve_forever()

except:
    print("Exit")