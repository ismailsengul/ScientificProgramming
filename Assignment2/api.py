from flask import Flask
from flask_cors import CORS
import ps2 

app = Flask(__name__)
CORS(app, origins="*")

LARGE_DIST = 99999
FILE = "mit_map.txt"
ERROR = "Error: graph is None"

from flask import request

@app.route('/api/v1/shortest-path')
def shortest_path():
    start = request.args.get('start')
    end = request.args.get('end')
    max_total_dist = request.args.get('max_total_dist', LARGE_DIST)
    max_dist_outdoor = request.args.get('max_dist_outdoor', LARGE_DIST)  # Get default value if not provided

    # Create a new Digraph
    graph = ps2.load_map(FILE)
    if graph is None:
        # return response object message and response false
        return {"message": ERROR, "response": False}
    # get shortest path
    response = ps2.directed_dfs(graph, start, end, int(max_total_dist), int(max_dist_outdoor))
    if response is None:
        return {"message": ERROR, "response": False}
    else :
        return {"path": response[0], "dist": response[1], "response": True}

@app.route('/api/v1/shortest-path-with-stops')
def shortest_path_with_stops():
    start = request.args.get('start')
    end = request.args.get('end')
    max_total_dist = request.args.get('max_total_dist', LARGE_DIST)
    max_dist_outdoor = request.args.get('max_dist_outdoor', LARGE_DIST)
    stops_param = request.args.get('stops')
    stops = stops_param.split(',')
    # Create a new Digraph
    graph = ps2.load_map(FILE)
    if graph is None:
        return {"message": ERROR, "response": False}
    # get shortest path
    response = ps2.directed_dfs_with_stops(graph, start, end, int(max_total_dist), int(max_dist_outdoor), stops)
    if response is None:
        return {"message": ERROR, "response": False}
    else :
        path_as_strings = [str(node) for node in response[0]]
        return {"path": path_as_strings, "dist": response[1], "response": True}

@app.route('/api/v1/shortest-path-with-closed')
def shortest_path_with_closed():
    start = request.args.get('start')
    end = request.args.get('end')
    max_total_dist = request.args.get('max_total_dist', LARGE_DIST)
    max_dist_outdoor = request.args.get('max_dist_outdoor', LARGE_DIST)
    closed_param = request.args.get('closed')
    closed = closed_param.split(',')
    # Create a new Digraph
    graph = ps2.load_map(FILE)
    if graph is None:
        return {"message": ERROR, "response": False}
    # get shortest path
    response = ps2.directed_dfs_with_closed(graph, start, end, int(max_total_dist), int(max_dist_outdoor), closed)
    if response is None:
        return {"message": ERROR, "response": False}
    else :
        path_as_strings = [str(node) for node in response[0]]
        return {"path": path_as_strings, "dist": response[1], "response": True}

@app.route('/api/v1/shortest-path-with-stops-and-closed')
def shortest_path_with_closed_and_stops():
    start = request.args.get('start')
    end = request.args.get('end')
    max_total_dist = request.args.get('max_total_dist', LARGE_DIST)
    max_dist_outdoor = request.args.get('max_dist_outdoor', LARGE_DIST)
    closed_param = request.args.get('closed')
    closed = closed_param.split(',')
    stops_param = request.args.get('stops')
    stops = stops_param.split(',')
    # Create a new Digraph
    graph = ps2.load_map(FILE)
    if graph is None:
        return {"message": ERROR, "response": False}
    # get shortest path
    response = ps2.directed_dfs_with_stops_and_closed(graph, start, end, int(max_total_dist), int(max_dist_outdoor), stops, closed)
    if response is None:
        return {"message": ERROR, "response": False}
    else :
        path_as_strings = [str(node) for node in response[0]]
        return {"path": path_as_strings, "dist": response[1], "response": True}

if __name__ == '__main__':
    app.run(port=8000, debug=True)
