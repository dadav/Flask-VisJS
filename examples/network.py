from flask import Flask, render_template_string
from flask_visjs import VisJS4, Network
from flask_socketio import SocketIO, emit
from pathlib import Path
from scapy.sendrecv import sniff
from scapy.layers.inet import IP, TCP
from collections import defaultdict

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
VisJS4().init_app(app)


def start_sniffing():
    packet_counter = defaultdict(int)

    def on_packet(myapp, pkt):
        src_ip = pkt[IP].src
        dest_ip = pkt[IP].dst
        packet_counter[src_ip] += 1
        packet_counter[dest_ip] += 1
        from_node = {
            'id': src_ip,
            'label': src_ip,
            'value': packet_counter[src_ip]
        }
        to_node = {
            'id': dest_ip,
            'label': dest_ip,
            'value': packet_counter[dest_ip]
        }
        edge = {'id': f'{src_ip}_{dest_ip}', 'from': src_ip, 'to': dest_ip}

        with myapp.app_context():
            emit('update', {
                'fromNode': from_node,
                'toNode': to_node,
                'edge': edge},
                 broadcast=True,
                 namespace='/')

    sniff(prn=lambda x: on_packet(app, x), store=False, filter="ip")


@app.route('/')
def index():
    """
    Use scapy to visualize the network traffic
    """
    net = Network("1024px", "1024px")
    socketio.start_background_task(start_sniffing)
    return render_template_string("""

<html>
    <head>
      {{ net.inject_css() }}
      {{ net.inject_js() }}
    </head>
    <body>
      <div id = "mynetwork"></div>
      <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.0.1/socket.io.js" integrity="sha512-q/dWJ3kcmjBLU4Qc47E4A9kTB4m3wuTY7vkFJDTZKjTs8jhyGQnaUrxa0Ytd0ssMZhbNua9hE+E7Qv1j+DyZwA==" crossorigin="anonymous"></script>
      <script type="text/javascript" charset="utf-8">
        var container = document.getElementById('mynetwork');
        var options = {edges: {arrows: {to: {enabled: true}}}};
        var network, edges, nodes, data;
        nodes = new vis.DataSet([{'id': 0, 'label': 'test'}]);
        edges = new vis.DataSet([]);
        data = {nodes: nodes, edges: edges};
        network = new vis.Network(container, data, options);
        network.redraw();
        var socket = io();
        socket.on('update', function(data) {
            nodes.update(data.fromNode);
            nodes.update(data.toNode);
            edges.update(data.edge);
            network.redraw();
        });
      </script>

    </body>
</html>
""", net=net)
