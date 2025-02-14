# BidirectionalStreaming 
## Overview
- `boker.proto` defines the data strcuture for the communication

    - The `BrokerRequest` message definition specifies five fields. Each field has a name and a tyoe. The numbers are not values for the fields. They only indicate the order of serializing the fields. 
    - The `BrokerResponse` message definition specifies two fields.
    - To use the message types with an RPC (Remote Procedure Call) system, you can define an RPC service interface in a ``.proto`` file and the protocol buffer compiler will generate service interface code and stubs in your chosen language. 
    - The RPC service defined here takes ``BrokerRequest`` as request and returns ``BrokerResponse``. 

- To generate python classes for the `broker.proto` file, I have created a shell script. It creates a ``generated`` directory and then creates the python classes inside it. It also creates the ``server.py`` and ``client.py`` file for you. Just run the shell script and relax.
````
sh generate_src.sh
````
## Generated class
### ``broker_pb2.py`` - contains message classes
- **broker_pb2.Features** for sending response
- **broker_pb2.Empty** for sending request
### ``broker_pb2_grpc.py`` - contains server and client classes
- **broker_pb2_grpc.BidirectionalStreamingServicer** will be used by server
- **broker_pb2_grpc.BidirectionalStreamingStub** will be used by client

## Server
- The gRPC server will run on port 8061
## Docker
Build the docker image
````
docker build -t databroker:v2 .
````
Run the docker image
````
docker run -p 8061:8061 --rm -ti databroker:v2 /bin/bash
````
On another terminal run the client
````
python3 client.py
````