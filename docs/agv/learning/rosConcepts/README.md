# Concepts
Up to know, we've introduced some basic concepts about robotics, ROS, and ROS 2. In this part, we'll dive into ROS 2 essential concepts. 

For more details make sure to check out the links given in each part.

## ROS 2 Filesystem
ROS 2 uses a distributed file system to manage the storage and communication of data between different nodes in a robotic system. The ROS 2 filesystem is based on a set of conventions and rules that govern how data is organized and accessed within a ROS 2 environment.

The ROS 2 filesystem is structured around the concept of packages, which are collections of related ROS 2 nodes, libraries, and other resources. Each package contains a set of directories and files that define its functionality and dependencies.

?> See [**here for official documentation**](http://wiki.ros.org/ROS/Tutorials/NavigatingTheFilesystem) to navigate through ROS 2 filesystem and also [**here**](https://ros2-industrial-workshop.readthedocs.io/en/latest/_source/basics/ROS2-Filesystem.html) for ROS Industrial's document about ROS 2 filesystem.

## ROS 2 Workspace
ROS 2 (Robot Operating System 2) uses a workspace concept for organizing and building packages. A workspace is a directory that contains one or more ROS 2 packages, along with the tools and configuration files needed to build and run them.

?> To create a new ROS 2 workspace, see [**official documentation**](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Creating-A-Workspace/Creating-A-Workspace.html).

## ROS Packages
In ROS 2 (Robot Operating System 2), a package is the basic unit of software organization. A package is a directory that contains one or more ROS 2 nodes, libraries, configuration files, and other resources related to a specific functionality.

Overall, ROS 2 packages provide a flexible and modular way to organize your ROS 2 code, making it easier to develop, share, and collaborate on robotics applications.

?> To create a new ROS 2 package, see [**official documentation**](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Creating-Your-First-ROS2-Package.html).

## ROS Nodes
In ROS 2 (Robot Operating System 2), a node is the basic building block of a ROS 2 system. A node is an executable that performs a specific task and communicates with other nodes via messages.

ROS 2 nodes can be implemented in any programming language as long as they are compatible with the ROS 2 message passing system. Nodes can publish messages on a topic, subscribe to messages on a topic, or provide a service that other nodes can call.

?> To learn about the functions of nodes in ROS 2 and the tools to interact with them, see [**official documentation**](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Nodes/Understanding-ROS2-Nodes.html).
## ROS Topics
In ROS 2 (Robot Operating System 2), a topic is a named bus over which nodes can exchange messages. Topics are the primary communication mechanism used in ROS 2 to enable nodes to communicate with each other.

ROS 2 nodes can publish messages on a topic or subscribe to messages on a topic. When a node publishes a message on a topic, all other nodes that have subscribed to that topic will receive the message. Similarly, when a node subscribes to a topic, it will receive all messages that are published on that topic.

To create a new ROS 2 topic, you can start by creating a new ROS 2 node that publishes or subscribes to the desired topic. 

?> To understand topics more, see [**official documentation**](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Topics/Understanding-ROS2-Topics.html).

## ROS Services
ROS 2 services provide a way for nodes to request specific actions or information from other nodes. Services allow for bi-directional communication between nodes, where one node acts as a client that makes a request, and another node acts as a server that provides the requested service.

ROS 2 services provide a powerful way for nodes to communicate and request actions or information from each other. By defining service types and implementing server and client nodes, you can create complex systems that are capable of responding to a variety of requests and scenarios.

?> To learn more about services in ROS 2, see [**official documentation**](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Services/Understanding-ROS2-Services.html).

## ROS Parameters
ROS 2 parameters provide a way for nodes to store and access configuration data at runtime. Parameters are key-value pairs that can be set and queried by nodes, allowing for dynamic configuration of your ROS 2 system. 

ROS 2 parameters provide a flexible way for nodes to store and access configuration data at runtime. By declaring and setting parameters, you can dynamically configure your ROS 2 system to respond to changing conditions and requirements.

?> To understand parameters, see [**official documentation**](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Parameters/Understanding-ROS2-Parameters.html).

## ROS Actions
ROS 2 Actions are a way to send goals from one node to another and receive feedback and results asynchronously. Actions allow for more fine-grained control over long-running tasks than ROS 2 Services, which are typically used for short-lived, request-response interactions.

In ROS 2, Actions are implemented using a combination of topics and services. The node that sends the goal publishes the goal on an action topic, while the node that receives the goal subscribes to the same topic and provides a service to handle the goal. Once the action server receives the goal, it can provide feedback to the client as the task progresses, and finally provide a result when the task is complete.

One advantage of ROS 2 Actions is that they provide a standard interface for long-running tasks, making it easier to integrate different nodes and systems. Additionally, because Actions are asynchronous, they allow for more complex behaviors and error handling, such as cancelling a task if it takes too long or if the goal becomes irrelevant.

Overall, ROS 2 Actions are a powerful tool for building complex, distributed robotics applications that require fine-grained control over long-running tasks.

?> To learn more about actions, see [**official documentation**](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Actions/Understanding-ROS2-Actions.html).

## ROS Launch Scripts
ROS 2 launch files are similar to ROS 1 launch files, but with some differences in syntax and usage. They are XML files that allow you to start multiple ROS 2 nodes simultaneously with specific configurations and dependencies.

?> To create a launch file to run a complex ROS 2 system, see [**official documentation**](https://docs.ros.org/en/humble/Tutorials/Intermediate/Launch/Creating-Launch-Files.html).