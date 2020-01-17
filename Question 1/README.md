# To Run:
    Navigate to /src and Execute:
        docker build -t message_server:latest .

        docker run --rm -p 8080:8080 message_server:latest

# Solution Notes:
    The solution utilizes http.server's SimpleHTTPServer to receive and process
    GET and POST requests. A dictionary is used to store the hashes as keys and 
    messages as its values. This is currently not a optimal implementation
    for the data layer, it would be more secure, safer, and more efficient to use a 
    more durable storage system such as Microsoft's Azure Blob or also distributed 
    storage using Redis to store the same key -> value pairs as mentioned above. 
    Caching could also be utilized to respond with increased speed to more probable 
    requests. 

    A potential bottleneck is the computational intensity levied by the sha256 hashing.
    With increasing users this could slow response times by utilizing increasing CPU power. 
    The microserver could then be scaled vertically (adding more CPU, RAM to the server) 
    or horizontally (by adding more machines to our resource pool) in tandem with a load 
    balancer to distribute the load of the microservice. 

    Deployment and updating of this system could be run by utilizing one of the many 
    version control systems available such as GitHub that would allow for pushing updates
    as well as maintaining a historical record of changes to the microservice. 


# Test Output:
    curl -X POST -H "Content-Type: application/json" -d '{"message": "foo"}' http://localhost:8080/messages

    {

     "digest": "2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae" 

    }   

    curl http://localhost:8080/messages/2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae

    {

     "message": "foo" 

    }

    curl http://localhost:8080/messages/aaaaaaaaaaaaaaaaaaaaaaaaaaa

    {

     "err_msg": "Message not found" 

    }

    HTTP/1.0 404 Not Found
    Server: BaseHTTP/0.6 Python/3.8.1
    Date: Fri, 17 Jan 2020 20:07:47 GMT