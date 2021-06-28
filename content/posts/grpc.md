Title: gRPC — gentle introduction
Date: 2021-06-28 05:12
Author: mohanad
Category: computing
Tags: grpc, distributed systems
Slug: grpc
Status: published
Cover: https://media.giphy.com/media/HsKTkfCuNdM5y/giphy.gif


# Remote Procedural Call
When I was in school, in the Operating Systems class, we learned about remote procedure calls in short RPC. We learned about [CORBA](https://en.wikipedia.org/wiki/Common_Object_Request_Broker_Architecture) which was used for RPC calls. I did not fully understand it that time, but who cares, never used it and even never used RPC for many years at work. Untill few years ago, started to hear about what is called gRPC. Obviously from its name, it is the same RPC I learned about when I was in school, but with an extra `g` in the beginning. I did not care about it though, I was like yeah that is cool but still did not need to use it at work especially I was working on a monolith architecture. 

But then when I started working at Coinbase where the services are distributed, the communication between services is mainly done using gRPC. So, seems the time has came to learn gRPC 😄. In this post, I’m gonna try to cover everything you need to know with 0 knowledge about it in mind. Hope you enjoy it! 


![](https://media.giphy.com/media/HsKTkfCuNdM5y/giphy.gif)


In this post, I’m gonna cover the following topics: 


1. What is remote procedural calls
2. Why not just REST, SOAP? is RPC better?
3. gRPC hands on tutorial
4. what is next?


# What is Remote Procedure Call

RPC is a mechanism for interprocess communication which enables the communication between processes located on different memory address spaces. It is also described as a client-server transaction oriented model, where a single request is sent from the client to the server with a single reply back from the server. 

RPC is built to hide the network communication from the user making it to seems like the user is making a local call to a procedure. 


## Differences between local calls and RPC procedure calls

There are several differences in between local calling to a function and RPC calls to a function. 

1. **Server/client relationship binding**: for a procedure to be called from a remote client, the client needs to know about the server (the address and port to be used)
2. **No shared memory**: unlike in static local procedure call, where parameters may be passed by reference. In RPC the parameters must only be passed by value. 
3. **Independent failure**: in addition to errors that may occur due to executions errors in the procedure. errors related to the nature of remote execution may appear as well. for example. the remote machine crashes, network errors, binding issues, 

The following figure illustrates the steps taken when a client sends a request to a remote procedure on the network. 


![RPC mechanism [3]](https://paper-attachments.dropbox.com/s_D552F7CCE8020D8F2D83EE1F1DB915062D0E0FD7D2B546CF4713FC976493B3C4_1600109385539_image.png)



# Why not just REST, SOAP? is RPC better?

A question that always comes into my mind, why not just to use REST to communicate between different services? Is there any additional benefits of using RPC (more specifically gRPC)? 
In short “**it depends**”. I think having a full answer that covers this question will require a whole article by itself so for now I recommend reading this article which I found amazing to address this question https://cloud.google.com/blog/products/api-management/understanding-grpc-openapi-and-rest-and-when-to-use-them

# gRPC
![](https://paper-attachments.dropbox.com/s_D552F7CCE8020D8F2D83EE1F1DB915062D0E0FD7D2B546CF4713FC976493B3C4_1622936655565_image.png)


From the above introduction, we got to know little bit about RPC. Now back into the main subject of this article. What is gRPC.

gRPC is defined as “a high performance, open source universal RPC framework” [5]. Yes, gRPC is not protocol, it is a Framework!. 

Also defined as “gRPC is a modern open source high performance Remote Procedure Call (RPC) framework that can run in any environment. It can efficiently connect services in and across data centers with pluggable support for load balancing, tracing, health checking and authentication. It is also applicable in last mile of distributed computing to connect devices, mobile applications and browsers to backend services.” 

RPC part stands for Remote Procedural Calls, the small “g” actually stands for many things! Every version stands for different word, in the recent version 1.38 it stands for **goofy.** Check [here](https://github.com/grpc/grpc/blob/master/doc/g_stands_for.md). 

gRPC uses protocol buffer for defining the service and methods it exposes. In addition, protocol buffer is used as a messages exchanging format. 


## ProtoclBuffer 

Before we get our hands dirty with gRPC, it would be good to get some understanding of protoclbuffer. Here is a nice definition by Google “**Protocol buffers are a language-neutral, platform-neutral extensible mechanism for serializing structured data**.” [7] Soooo protoclbuffer is just data serialization mechanism, where data can be transferred, encoded and decoded by applications regardless of the programming language. 
I highly recommend going through the protoclbuffer tutorial provided by Google [[8](https://developers.google.com/protocol-buffers/docs/pythontutorial)]. 


## gRPC Hands on example

Alright, back on it, lets create a simple app that uses gRPC to expose one of its methods. Hmmm, lets think of a nice app. How about we make a simple coffeeshop app and expose a method `makeCoffee` to be used by other systems 🙂 

I’d love to use Go as a programming language, since I use it at work. In this section we gonna build the following:

1. Define our service using .**proto** file 
2. **Generate** the server and the client code using proto compiler 
3. Use Go API to **implement** the server and client

The example we are implementing is soooo easy, it is actually the hello_world example in gRPC. In our case I named it coffeeshop maybe to expand on for future articles. Our service expose one rpc method named as `MakeCoffee` and basically accepts one parameter in the request and return a string. 

Here is the file structure we gonna implement:

    .
    ├── cmd
    │   ├── client
    │   │   └── main.go
    │   └── server
    │       └── main.go
    ├── go.mod
    ├── go.sum
    └── proto
        ├── cafe.pb.go
        └── cafe.proto


The proto file will look like this:


    syntax = "proto3";
    package coffeeshop;
    message CoffeeRequest {
        string name = 1;
    }
    message CoffeeResponse {
        string message = 1;
    }
    service coffeeshop {
        rpc MakeCoffee(CoffeeRequest) returns (CoffeeResponse) {};
    }

Now next step will be to use protoc to compile the proto file to generate the code that is responsible for serializing the data. oh navigate to your proto directory first.


    protoc --go_out=plugins=grpc:. cafe.proto

Well well, this generated a file called `cafe.pb.go` You can open the file and checkout the generated code, see the `Marshal` and `Unmarshal` methods that have been generated per message. I’m not going to explain the the generated proto go file since it is out of the scope of this article and I also still don’t understand it 😄 

Lets proceed, shall we. Cool so now lets create the grpc server, this server will actually implement the CoffeeshopServer interface that has been defined in the `cafe.pb.go` file. 

The `CoffeeshopServer` interface is defined like this:

    // CoffeeshopServer is the server API for Coffeeshop service.
    type CoffeeshopServer interface {
        MakeCoffee(context.Context, *CoffeeRequest) (*CoffeeResponse, error)
    }

So we need to create a type with a method `MakeCoffee` which handles a request and return a response. Okay, I’m like a chef in cooking shows, and here is the server implementation just out of the oven yaaaaay! 

![](https://media.giphy.com/media/EuesNM8qJVOTu/giphy.gif)



    package main
    import (
        "context"
        "fmt"
        "log"
        "net"
        pb "github.com/cafe/proto"
        "google.golang.org/grpc"
    )
    type server struct {
    }
    func (*server) MakeCoffee(ctx context.Context, request *pb.CoffeeRequest) (*pb.CoffeeResponse, error) {
        name := request.Name
        response := &pb.CoffeeResponse{
            Message: "Hello " + name + ", your coffee is ready for pickup!",
        }
        return response, nil
    }
    func main() {
        address := "0.0.0.0:50051"
        lis, err := net.Listen("tcp", address)
        if err != nil {
            log.Fatalf("Error %v", err)
        }
        fmt.Printf("Server is listening on %v ...", address)
        s := grpc.NewServer()
        pb.RegisterCoffeeshopServer(s, &server{})
        s.Serve(lis)
    }
    

Cool, see how define a type called `server` and this type has a `MakeCoffee` method which has same arguments defined in the interface that we just saw above. The MakeCoffee implementation is actually very simple, it just reads the `name` field from the request and return a response with a message that your coffee is ready! pretty simple hah. 

The main function is just to create a grpc server that listens on port `50051` (you can change it to whatever you want) 

Notice in line 27, we used method `RegisterCoffeeshopServer` to register the `server` type we just defined to be used by the grpc server. 

Now you can run the server by:

    go run cmd/server/main.go

Are we done yet?! 
Nope!! we wrote our grpc server, and now it is ready to accept requests, but we still need to write a client. We will write a Go client to send requests to this gRPC server. Here is the code: 


    package main
    import (
        "context"
        "fmt"
        "log"
        pb "github.com/cafe/proto"
        "google.golang.org/grpc"
    )
    func main() {
        fmt.Println("Client is started...")
        opts := grpc.WithInsecure()
        cc, err := grpc.Dial("localhost:50051", opts)
        if err != nil {
            log.Fatal(err)
        }
        defer cc.Close()
        client := pb.NewCoffeeshopClient(cc)
        request := &pb.CoffeeRequest{Name: "Mohanad"}
        resp, _ := client.MakeCoffee(context.Background(), request)
        fmt.Printf("Receive response => [%v]", resp.Message)
    }



    ~/Workspace/cafe » go run cmd/client/main.go                                    
    
    Client is started...
    Receive response => [Hello Mohanad, your coffee is ready for pickup!]% 
# What next? 

As a homework:

- try to create a client in a different programming language, say Python or Javascript. Also happy to pair with you on it if you need help (and if I have time 😞) 
- Try to read about streaming using gRPC.



![](https://media.giphy.com/media/3osxYpi1698kMO0qHe/giphy.gif)


Resources

1. https://web.cs.wpi.edu/~cs4514/b98/week8-rpc/week8-rpc.html
2. https://web.cs.wpi.edu/~cs4514/b98/ (Computer Networks course)
3. https://book.systemsapproach.org/e2e/rpc.html
4. https://cloud.google.com/blog/products/api-management/understanding-grpc-openapi-and-rest-and-when-to-use-them
5. https://grpc.io/
6. https://github.com/grpc/grpc/blob/master/doc/g_stands_for.md
7. https://developers.google.com/protocol-buffers
8. https://developers.google.com/protocol-buffers/docs/pythontutorial


