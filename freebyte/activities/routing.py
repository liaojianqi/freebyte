from channels.routing import route
from freebyte.activities.consumers import ws_connect, ws_disconnect


websocket_routing = [
    route('websocket.connect', ws_connect),
    route('websocket.disconnect', ws_disconnect),
]
