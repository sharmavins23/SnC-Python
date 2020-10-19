# Server & Client, Python

A Python socket-programmed web-server and client.

## Overview

This project implements a web server and client in Python, with the express
purpose of sending static HTML files and receiving connections from incoming
users.

The lab utilizes lower level socket libraries for the main purposes of creating
TCP connections, and sending and receiving messages through said TCP
connections. Despite this, the major amount of work is done in the application
layer, through parsing and constructing HTTP request packets and response
packets.

## How To Run

All source code is contained within the `src` file. To run either the server or
client, first open a command line into the main directory, then run either:

```ps
# Server
python src/server.py
# Client
python src/client.py
```

## Server Functionality

The server is created using the socket library, just as the client is. Unlike
the client, however, the server runs constantly, accepting requests of maximum
1024 bytes and responding with two conditions.

If the request is a proper HTTP GET request to the file `index.html`, the server
will respond by loading and sending the `index.html` file to the connection. An
example of this functionality (from the console view) is shown below:

![img](https://cdn.discordapp.com/attachments/385616952963497984/767852768344932352/unknown.png)

As shown, upon a request, the HTTP request is printed to the console, as well as
the specific requested filepath below. The HTML file is also properly sent (in
this case, it is sent to the browser as shown in the following picture.)

![img](https://cdn.discordapp.com/attachments/385616952963497984/767853158738821140/unknown.png)

Upon requesting any other page (for instance, `/` or `/test.html`) an error will
be returned (specifically, the `404` error, denoting a missing or nonexistant
file on the server.) The logging for these events is the same on the console
client; However, the browser shows the proper page load.

![img](https://cdn.discordapp.com/attachments/385616952963497984/767854006114320394/unknown.png)

In this case, the `filenotfound.html` file is sent to the client with an HTML
error code in response.

It is important to note that in order for the server to work across computers
and across the internet, I had to perform several settings and variations on the
provided code. Firstly, I got an error when trying to connect to port 8080 -
this is because 8080 is a reserved port for other applications and development
servers on my computer, and I had to open that in my firewall.

In order to allow access from other computers, I had to forward the port to my
machine while my server was running in my router to get other computers to
connect using my public domain as well.

## Client Functionality

The client application is a simple console application that only runs once and
terminates execution immediately after. It asks the user for a connection host,
port, and filepath to load. After doing so, it creates a connection, requests
information from that connection, and prints out the response (including status
code and body.)

Two examples of the client interacting with my server are shown below:

![img](https://cdn.discordapp.com/attachments/385616952963497984/767851296715571240/unknown.png)

This is the client interacting with the server and requesting the index HTML
file.

![img](https://cdn.discordapp.com/attachments/385616952963497984/767851296715571240/unknown.png)
This is the client interacting with the server and requesting some other HTML
file.

In the above pictures, the client is shown interacting with the server through a
locally hosted application. However, the client is capable of connecting to and
communicating with online resources as well. An example of the client connecting
to and requesting the main index page of `www.google.com` on the HTTP port is
shown below.

![img](https://cdn.discordapp.com/attachments/385616952963497984/767855869018112040/unknown.png)

As shown, the entire HTTP response is printed out (including the `200 OK` status
at the top, notifying our client that we have successfully made a proper
request.) The body is shown at the bottom, separated by some spacing; This is an
HTML response, which when loaded in, contains Google's main metadata for their
site. Since the response from the server is limited to 1024 bytes, this body is
truncated.

# License TL;DR

This project is distributed under the MIT license. This is a paraphrasing of a
[short summary](https://tldrlegal.com/license/mit-license).

This license is a short, permissive software license. Basically, you can do
whatever you want with this software, as long as you include the original
copyright and license notice in any copy of this software/source.

## What you CAN do:

-   You may commercially use this project in any way, and profit off it or the
    code included in any way;
-   You may modify or make changes to this project in any way;
-   You may distribute this project, the compiled code, or its source in any
    way;
-   You may incorporate this work into something that has a more restrictive
    license in any way;
-   And you may use the work for private use.

## What you CANNOT do:

-   You may not hold me (the author) liable for anything that happens to this
    code as well as anything that this code accomplishes. The work is provided
    as-is.

## What you MUST do:

-   You must include the copyright notice in all copies or substantial uses of
    the work;
-   You must include the license notice in all copies or substantial uses of the
    work.

If you're feeling generous, give credit to me somewhere in your projects.
