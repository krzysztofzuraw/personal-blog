Http and websockets logging handlers
####################################

:date: 2016-01-16 10:20
:tags: python, logging
:category: blog
:slug: http-websockets-logging-handlers
:summary: Quick introduction to HTTP and Websockets logging handlers.
:header_cover: /images/covers/log.jpg

**Hello, this posts will be about 3 specific logging handlers:
HTTPHandler, SocketHandler and DatagramHandler.**


HTTPHandler
===========

Let's start with HTTPHandler: reading python docs about
`HTTPHandler <https://docs.python.org/3.4/library/logging.handlers.html#httphandler>`__
we can see that:

    The HTTPHandler class, located in the logging.handlers module,
    supports sending logging messages to a Web server, using either GET
    or POST semantics.

So this will be useful to have such handler in case of many different
modules in different machines that sends logs to one central server.

As an example, I will build simple flask application which prints out
the logging message from the client.

To install Flask:

.. code-block:: terminal

    $ pip install Flask


Then make server.py:

.. code-block:: python

    from flask import Flask, request

    app = Flask(__name__)

    @app.route("/", methods=['POST', 'GET'])
    def hello():
    for key, value in request.args.items():
        print(key,value)
    return 'response' # it has to return something


    if __name__ == "__main__":
    app.run(debug=True)

To send some data, create script called send_log.py:

.. code-block:: python

    import logging
    import logging.handlers

    logger = logging.getLogger(__name__)

    server = '127.0.0.1:5000'
    path = '/'
    method = 'GET'

    sh = logging.handlers.HTTPHandler(server, path, method=method)

    logger.addHandler(sh)
    logger.setLevel(logging.DEBUG)

    logger.debug("Test message.")

Running server.py and send_log.py will result in this output:

.. raw:: html

    <video src="/videos/http_logger.mp4" autoplay width="720" loop>
    Your browser does not support the video tag.
    </video>

SocketHandler
=============

Now let's move to the
`SocketHandler <https://docs.python.org/3.4/library/logging.handlers.html#sockethandler>`__:
this is what python docs say about it

    The SocketHandler class, located in the logging.handlers module,
    sends logging output to a network socket. The base class uses a TCP
    socket.

Based on this we can now guess that web socket will receive logging
message.Then we can process it further. It will be useful when there is
a lot of logs to be sent to the server. So opening HTTP connection every
time is not a good solution.

So first we need some TCP server:

.. code-block:: python

    class LogRecordSocketReceiver(socketserver.ThreadingTCPServer):
        allow_reuse_address = True

        def __init__(self, host='localhost',
                     port=logging.handlers.DEFAULT_TCP_LOGGING_PORT,
                     handler=LogRecordStreamHandler):
            socketserver.ThreadingTCPServer.__init__(self, (host, port), handler)
            self.abort = 0
            self.timeout = 1
            self.logname = None

        def serve_until_stopped(self):
            import select
            abort = 0
            while not abort:
                rd, wr, ex = select.select([self.socket.fileno()],
                                           [], [],
                                           self.timeout)
                if rd:
                    self.handle_request()
                abort = self.abort

    def main():
        tcpserver = LogRecordSocketReceiver()
        print('About to start TCP server...')
        tcpserver.serve_until_stopped()

    if __name__ == '__main__':
        main()

What is going on here? In the ``main`` function we instantiate threading TCP server and
we serve it until we don't hit Ctrl+C. In the ``serve_until_stopped`` method of ``LogRecordSocketReceiver``
we are waiting for the key combination to the stop server and if this not happening the we retrieve information about the
socket by ``self.socket.fileno()`` which is a descriptor of a socket. Then we pass it to another function
call: this time ``select()``. Select is system call for examining the status of file descriptors of open input/output channels
which in this case is information from the socket. If there is anything ready to be read we handle the request and
process it.

To process it we need handler:

.. code-block:: python

    class LogRecordStreamHandler(socketserver.StreamRequestHandler):

        def handle(self):
            while True:
                chunk = self.connection.recv(4)
                if len(chunk) < 4:
                    break
                slen = struct.unpack('>L', chunk)[0]
                chunk = self.connection.recv(slen)
                while len(chunk) < slen:
                    chunk = chunk + self.connection.recv(slen - len(chunk))
                obj = pickle.loads(chunk)
                print(obj)

In method ``handle`` we read chunks of information from sent logging message. The chunk is byte type so
then we need to translate it to python object by calling ``pickle.loads()``.

So running our TCP server and sending log looks like this:

.. raw:: html

    <video src="/videos/socket_logger.mp4" autoplay width="720" loop>
    Your browser does not support the video tag.
    </video>


Full gist with socket logger looks like this:

.. raw:: html

   <script src="https://gist.github.com/krzysztofzuraw/dea92aad16cd157e5ea6.js"></script>

And with socket sender:

.. raw:: html

  <script src="https://gist.github.com/krzysztofzuraw/8d7684664ba16fc43b6c.js"></script>

DatagramHandler
===============

Lastly, there is
`DatagramHandler <https://docs.python.org/3.4/library/logging.handlers.html#datagramhandler>`__
which supports sending logging messages over UDP.

The actual code is very similar to SocketHandler:

.. code-block:: python

    class MyUDPHandler(socketserver.BaseRequestHandler):
        def __init__(self, request, client_address, server):
            socketserver.BaseRequestHandler.__init__(self, request,
                                                     client_address,
                                                     server)

        def handle(self):
            msg, socket = self.request
            print("{} wrote:".format(self.client_address[0]))
            print(pickle.loads(msg[4:]))
            socket.sendto(msg.upper(), self.client_address)

Thanks to `RooTer <http://stackoverflow.com/users/5807830/rooter>`__
answer on
`stackoverflow <http://stackoverflow.com/questions/34761688/unpickling-data-in-udp-server-send-from-logger-results-in-eoferror>`__
I got this working by omitting first 4 bytes of data because they
contain length of dumped object.

So the full upd_server looks as follows:

.. raw:: html

   <script src="https://gist.github.com/krzysztofzuraw/24e21feeadaff88ae6f5.js"></script>

Which works like this:

.. raw:: html

    <video src="/videos/udp_logger.mp4" autoplay width="720" loop>
    Your browser does not support the video tag.
    </video>


Resources
---------

-  Socket server and log sender based on python logging
   `cookbook <https://docs.python.org/3/howto/logging-cookbook.html#sending-and-receiving-logging-events-across-a-network>`__

Updates
-------

-  23.01.16 Thanks to RooTer answer I added UDP log handler

Cover image by `Quinn Dombrowski <https://www.flickr.com/photos/quinnanya/>`_ under `CC BY 2.0 <https://creativecommons.org/licenses/by/2.0/>`_.
