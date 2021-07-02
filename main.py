# import the module
from prsaw import RandomStuffV2

# initiate the object
rs = RandomStuffV2() 

# get a response from an endpoint
while True:
    user_input = input("> ")
    response = rs.get_ai_response(user_input)
    print(response)

# close the object once done (recommended)
rs.close()