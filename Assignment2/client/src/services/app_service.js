import axiosInstance from "../api/axios";

const getShortestPath = async (start,end,maxTotalDist,maxDistOutdoor) => {

    const params = {
        start: start,
        end: end,
    }


    if (maxTotalDist !== "") {
        params.max_total_dist = maxTotalDist
    }
    if (maxDistOutdoor !== "") {
        params.max_dist_outdoor = maxDistOutdoor
    }
    return await axiosInstance
            .get(`/shortest-path`,
                {
                    params: params
                }
            )
}

const getShortestPathWithStops = async (start,end, maxTotalDist,maxDistOutdoor, stops) => {

        // const url = `http://localhost:8000/api/v1/shortest-path-with-stops?start=${start}&end=${end}&stops=${stops.join(',')}`;
        const params = {
            start: start,
            end: end,
            stops: stops
        }

        // http://localhost:8000/api/v1/shortest-path-with-stops?start=32&end=16&stops=24&stops=4
        // add stops to params if stops is not empty
        // stop is array


        if (maxTotalDist !== "") {
            params.max_total_dist = maxTotalDist
        }
        if (maxDistOutdoor !== "") {
            params.max_dist_outdoor = maxDistOutdoor
        }
        return await axiosInstance
                .get(`/shortest-path-with-stops`,
                    {
                        params: params
                    }
                )

}

const getShortestPathWithClosed = async (start,end,maxTotalDist,maxDistOutdoor, closed) => {
    const params = {
        start: start,
        end: end,
        closed: closed
    }

    if (maxTotalDist !== "") {
        params.max_total_dist = maxTotalDist
    }
    if (maxDistOutdoor !== "") {
        params.max_dist_outdoor = maxDistOutdoor
    }
    return await axiosInstance
            .get(`/shortest-path-with-closed`,
                {
                    params: params
                }
            )

}

const getShortestPathWithStopsAndClosed = async (start,end, maxTotalDist,maxDistOutdoor, stops, closed) => {
    const params = {
        start: start,
        end: end,
        stops: stops,
        closed: closed
    }

    if (maxTotalDist !== "") {
        params.max_total_dist = maxTotalDist
    }
    if (maxDistOutdoor !== "") {
        params.max_dist_outdoor = maxDistOutdoor
    }
    return await axiosInstance
            .get(`/shortest-path-with-stops-and-closed`,
                {
                    params: params
                }
            )


}

const AppService = {
    getShortestPath,
    getShortestPathWithStops,
    getShortestPathWithClosed,
    getShortestPathWithStopsAndClosed
}

export default AppService;