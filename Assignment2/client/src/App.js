import "./App.css";
import { useState } from "react";
import AppService from "./services/app_service";
import { FaArrowRight } from "react-icons/fa";

const App = () => {
  const nodeArray = [
    32, 36, 57, 76, 68, 66, 56, 26, 24, 16, 34, 12, 8, 39, 37, 31, 35, 33, 46,
    48, 54, 62, 64, 50, 18, 14, 10, 4, 6, 2, 1, 3, 5, 7, 9, 38,
  ];

  // create state for the start, end, maxTotalDist, and maxDistOutdoor
  const [start, setStart] = useState("");
  const [end, setEnd] = useState("");
  const [maxTotalDist, setMaxTotalDist] = useState("");
  const [maxDistOutdoor, setMaxDistOutdoor] = useState("");
  const [stops, setStops] = useState("");
  const [closed, setClosed] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [path, setPath] = useState(null);
  const [distance, setDistance] = useState(null);

  const clearForm = () => {
    setStart("");
    setEnd("");
    setMaxTotalDist("");
    setMaxDistOutdoor("");
    setStops("");
    setClosed("");
    setPath(null);
    setDistance(null);
    setError(null);
  };

  const getShortestPath = async (start, end, maxTotalDist, maxDistOutdoor) => {
    return AppService.getShortestPath(start, end, maxTotalDist, maxDistOutdoor);
  };

  const getShortestPathWithStops = async (
    start,
    end,
    maxTotalDist,
    maxDistOutdoor,
    stops
  ) => {
    // convert stops to array
    const stopArray = stops.split(",");
    return AppService.getShortestPathWithStops(
      start,
      end,
      maxTotalDist,
      maxDistOutdoor,
      stopArray.join(",")
    );
  };

  const getShortestPathWithClosed = async (
    start,
    end,
    maxTotalDist,
    maxDistOutdoor,
    closed
  ) => {
    // convert closed to array
    const closedArray = closed.split(",");
    return AppService.getShortestPathWithClosed(
      start,
      end,
      maxTotalDist,
      maxDistOutdoor,
      closedArray.join(",")
    );
  };

  const getShortestPathWithStopsAndClosed = async (
    start,
    end,
    maxTotalDist,
    maxDistOutdoor,
    stops,
    closed
  ) => {
    // convert stops to array
    const stopArray = stops.split(",");
    // convert closed to array
    const closedArray = closed.split(",");
    return AppService.getShortestPathWithStopsAndClosed(
      start,
      end,
      maxTotalDist,
      maxDistOutdoor,
      stopArray.join(","),
      closedArray.join(",")
    );
  };

  const formValidation = () => {
    if (start === "" || end === "") {
      alert("Please fill start and end node");
      return false;
    }

    if (start === end) {
      alert("Start and end node cannot be same");
      return false;
    }

    if (!nodeArray.includes(parseInt(start))) {
      alert("Start node is not valid");
      return false;
    }

    if (!nodeArray.includes(parseInt(end))) {
      alert("End node is not valid");
      return false;
    }

    // stops includes number and comma
    if (stops.trim() !== "") {
      const stopArray = stops.split(",");
      for (let i = 0; i < stopArray.length; i++) {
        if (!nodeArray.includes(parseInt(stopArray[i]))) {
          alert("Stop node is not valid");
          return false;
        }
      }
    }

    // closed includes number and comma
    if (closed.trim() !== "") {
      const closedArray = closed.split(",");
      for (let i = 0; i < closedArray.length; i++) {
        if (!nodeArray.includes(parseInt(closedArray[i]))) {
          alert("Closed node is not valid");
          return false;
        }
      }
    }

    if (stops.trim() !== "" && closed.trim() !== "") {
      const stopArray = stops.split(",");
      const closedArray = closed.split(",");
      for (let i = 0; i < stopArray.length; i++) {
        if (closedArray.includes(stopArray[i])) {
          alert("Closed and Stop nodes cannot be same");
          return false;
        }
      }
    }

    return true;
  };

  const formSubmit = async (e) => {
    e.preventDefault();
    if (!formValidation()) {
      return;
    }
    setLoading(true);
    const isClosed = closed.trim() !== "";
    const isStops = stops.trim() !== "";
    if (isClosed && isStops) {
      const response = await getShortestPathWithStopsAndClosed(
        start,
        end,
        maxTotalDist,
        maxDistOutdoor,
        stops,
        closed
      );
      if (!response.data.response) {
        setError(response.data.message);
      } else {
        setError(null);
      }
      setLoading(false);
      setPath(response.data.path);
      setDistance(response.data.dist);
    } else if (isClosed) {
      const response = await getShortestPathWithClosed(
        start,
        end,
        maxTotalDist,
        maxDistOutdoor,
        closed
      );
      if (!response.data.response) {
        setError(response.data.message);
      } else {
        setError(null);
      }
      setLoading(false);
      setPath(response.data.path);
      setDistance(response.data.dist);
    } else if (isStops) {
      const response = await getShortestPathWithStops(
        start,
        end,
        maxTotalDist,
        maxDistOutdoor,
        stops
      );
      if (!response.data.response) {
        setError(response.data.message);
      } else {
        setError(null);
      }
      setPath(response.data.path);
      setLoading(false);
      setDistance(response.data.dist);
    } else {
      const response = await getShortestPath(
        start,
        end,
        maxTotalDist,
        maxDistOutdoor
      );
      if (!response.data.response) {
        setError(response.data.message);
      } else {
        setError(null);
      }
      setPath(response.data.path);
      setLoading(false);
      setDistance(response.data.dist);
    }
  };

  const NumberNode = ({ number }) => {
    return (
      <div
        style={{
          width: "50px", // Dairelerin genişliği
          height: "50px", // Dairelerin yüksekliği
          borderRadius: "50%", // Daire şeklinde
          backgroundColor: "white", // Örnek renk, istediğiniz renge değiştirebilirsiniz
          display: "inline-flex", // Yan yana göstermek için
          justifyContent: "center",
          alignItems: "center",
          margin: "10px", // Aralık
        }}
      >
        {number}
      </div>
    );
  };

  const shortestPathForm = () => {
    // Add title to the form
    return (
      <div className="card">
        <div className="card-body" style={{marginTop: path ? "" : "60px"}}>
          <div className="card-header">
            Shortest Path MIT Campus by Greedies
            <a style={{marginLeft:"10px"}} href="https://news.mit.edu/sites/default/files/images/inline/directions-to-mit-news-office.jpg">
             Map</a>
            </div>            
          <form onSubmit={formSubmit}>
            <div style={{ display: "flex", marginTop: "80px" }}>
              <div className="form-group col-md-6">
                <label htmlFor="start">Start</label>
                <input
                  placeholder="exp:1"
                  type="number"
                  value={start}
                  onChange={(e) => setStart(e.target.value)}
                  className="form-control"
                  id="start"
                  name="start"
                  required
                />
              </div>
              <div
                className="form-group col-md-6 ml-1"
                style={{ marginLeft: "10px" }}
              >
                <label htmlFor="end">End</label>
                <input
                  placeholder="exp:2"
                  type="number"
                  value={end}
                  onChange={(e) => setEnd(e.target.value)}
                  className="form-control"
                  id="end"
                  name="end"
                  required
                />
              </div>
            </div>
            <div className="mt-3" style={{ display: "flex" }}>
              <div className="form-group col-md-6">
                <label htmlFor="maxTotalDist">Max Total Distance</label>
                <input
                  placeholder="exp:100"
                  type="number"
                  value={maxTotalDist}
                  onChange={(e) => setMaxTotalDist(e.target.value)}
                  className="form-control"
                  id="maxTotalDist"
                  name="maxTotalDist"
                />
              </div>
              <div
                className="form-group col-md-6 ml-1"
                style={{ marginLeft: "10px" }}
              >
                <label htmlFor="maxDistOutdoor">Max Distance Outdoor</label>
                <input
                  placeholder="exp:50"
                  type="number"
                  value={maxDistOutdoor}
                  onChange={(e) => setMaxDistOutdoor(e.target.value)}
                  className="form-control"
                  id="maxDistOutdoor"
                  name="maxDistOutdoor"
                />
              </div>
            </div>
            <div className="mt-3" style={{ display: "flex" }}>
              <div className="form-group col-md-6">
                <label htmlFor="stops">Stops</label>
                <input
                  placeholder="exp:7,9"
                  type="text"
                  value={stops}
                  onChange={(e) => setStops(e.target.value)}
                  className="form-control"
                  id="stops"
                  name="stops"
                />
              </div>
              <div
                className="form-group col-md-6 ml-1"
                style={{ marginLeft: "10px" }}
              >
                <label htmlFor="closed">Closed</label>
                <input
                  placeholder="exp:3,4"
                  type="text"
                  value={closed}
                  onChange={(e) => setClosed(e.target.value)}
                  className="form-control"
                  id="closed"
                  name="closed"
                />
              </div>
            </div>
            <br />
            <div
              style={{
                display: "flex",
                justifyContent: "space-between",
                padding: "0 30px",
                marginBottom: path || error ? "0px" : "80px",
              }}
            >
              <button
                type="button"
                className="btn btn-secondary"
                onClick={() => {
                  setStart("3");
                  setEnd("5");
                }}
              >
                Example
              </button>
              <button
                type="button"
                className="btn btn-warning"
                onClick={clearForm}
              >
                Clear
              </button>
              {loading ? (
                <button className="btn btn-primary" disabled>
                  <span
                    className="spinner-border spinner-border-sm"
                    role="status"
                    aria-hidden="true"
                  />
                  Loading...
                </button>
              ) : (
                <button type="submit" className="btn btn-primary">
                  Submit
                </button>
              )}
            </div>

            {path ? (
              <div className="alert alert-success mt-3" role="alert">
                {
                  // response is 3 7 5 array
                  path.map((node, index) => {
                    return (
                      <span key={index}>
                        {<NumberNode number={node} />}{" "}
                        {index === path.length - 1 ? "" : <FaArrowRight />}
                      </span>
                    );
                  })
                }
                <br />
                Distance: {distance}
              </div>
            ) : (
              ""
            )}
            {error ? (
              <div className="alert alert-danger mt-3" role="alert">
                {error}
              </div>
            ) : (
              ""
            )}
          </form>
        </div>
      </div>
    );
  };

  return ( 
  <div className="App">
    {shortestPathForm()}
    <footer style={{justifyContent : "center", alignItems : "center", display : "flex", textAlign:"center", marginTop: path ? "12px" : "25px"}}>
        Created by Ali Colak, Ismail Sengul, Burcu Acan - Akdeniz University - Computer Science and Engineering - CSE 408 Scientific Programming - Fall 2024
      <a style={{marginLeft:"10px"}} href="https://github.com/ismailsengul/ScientificProgramming/tree/main/Assignment2" target="_blank">Github</a>
    </footer>
    </div>
  )
};

export default App;
