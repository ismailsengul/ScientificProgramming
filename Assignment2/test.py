import ps2

def shortest() :
  LARGE_DIST = 99999
  graph = ps2.load_map("mit_map.txt")
  start_node = graph.get_node('32')
  end_node = graph.get_node('16')

  
  if graph is None:
      return "Error: graph is None"
    # get shortest path
  response = ps2.directed_dfs_with_stops_and_closed(graph, '32', '34', LARGE_DIST, LARGE_DIST, ['16'], ['36'])

  
if __name__ == '__main__':
          # get shortest path
    path = shortest()
    
    