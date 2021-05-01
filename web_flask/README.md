## Context

### The Application Context

The application context keeps track of the application-level data during a request, CLI command, or other activity.
Rather than passing the application around to each function, the current_app and g proxies are accessed instead This is
similar to the The Request Context, which keeps track of request-level data during a request. A corresponding
application context is pushed when a request context is pushed.

### Lifetime of the App Context

The application context is created and destroyed as necessary. When a Flask application begins handling a request, it
pushes an application context and a [request context](https://flask.palletsprojects.com/en/1.1.x/reqcontext/). When the
request ends it pops the request context then the application context. Typically, an application context will have the
same lifetime as a request.

### The Request Context¶

The request context keeps track of the request-level data during a request. Rather than passing the request object to
each function that runs during a request, the request and session proxies are accessed instead.

This is similar to the The Application Context, which keeps track of the application-level data independent of a
request. A corresponding application context is pushed when a request context is pushed.

### Lifetime of the Context

When a Flask application begins handling a request, it pushes a request context, which also pushes an The Application
Context. When the request ends it pops the request context then the application context.

The context is unique to each thread (or other worker type). request cannot be passed to another thread, the other
thread will have a different context stack and will not know about the request the parent thread was pointing to.

Context locals are implemented in Werkzeug. See Context Locals for more information on how this works internally.

### How the Context Works

The `Flask.wsgi_app()` method is called to handle each request. It manages the contexts during the request. Internally,
the request and application contexts work as stacks, `_request_ctx_stack` and `_app_ctx_stack`. When contexts are pushed
onto the stack, the proxies that depend on them are available and point at information from the top context on the
stack.

When the request starts, a RequestContext is created and pushed, which creates and pushes an AppContext first if a
context for that application is not already the top context. While these contexts are pushed, the `current_app`, `g`,
request, and session proxies are available to the original thread handling the request.

Because the contexts are stacks, other contexts may be pushed to change the proxies during a request. While this is not
a common pattern, it can be used in advanced applications to, for example, do internal redirects or chain different
applications together.

After the request is dispatched and a response is generated and sent, the request context is popped, which then pops the
application context. Immediately before they are popped, the `teardown_request()` and `teardown_appcontext()` functions are
executed. These execute even if an unhandled exception occurred during dispatch.