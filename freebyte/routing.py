from channels import include

channel_routing = [
    # Include subrouting from an app with predefined path matching.
    include("freebyte.activities.routing.websocket_routing",
            path=r"^/notifications/$"),
    include("freebyte.feeds.routing.websocket_routing", path=r"^/feeds/$"),
    include("freebyte.messenger.routing.websocket_routing",
            path=r"^/")
]
