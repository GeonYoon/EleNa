/**
 * Takes starting and ending points and outputs an array of nodes along the most elevation efficient route.
 *
 * @param startLat
 *    Starting latitude.
 * @param startLng
 *    Starting longitude.
 * @param endLat
 *    Ending latitude.
 * @param endLng
 *    Ending Longitude.
 * @returns {*[]}
 *    Array of nodes along the route.
 *    lat: latitude of the node.
 *    lng: longitude of the node.
 *    changedElevation: total elevation change of the route at that node (in meters).
 *    totalDistance: total distance traveled over the route at that node (in kilometers).
 */
const Route = ( startLat, startLng, endLat, endLng ) => {
    // @Todo Implement Route.
    return [
        {
            lat: startLat,
            lng: startLng,
            changedElevation: 10,
            totalDistance: 0
        },
        {
            lat: 50,
            lng: 50,
            // This should never decrease. Represents the amount of total change.
            changedElevation: 30,
            totalDistance: 10
        },
        {
            lat: endLat,
            lng: endLng,
            changedElevation: 50,
            totalDistance: 20
        }
    ]
};
export default Route;

/**
 * Takes a coordinate and returns the elevation at that coordinate (in meters).
 * @param lat
 *    Latitude.
 * @param lng
 *    Longitude.
 * @returns {number}
 *    Elevation at the coordinate (in meters).
 */
const getElevationAtCoordinates = (lat, lng) => {
    // @Todo Implement Elevation.
    return 10;
};

/**
 * Takes a query and returns the most likely coordinate corresponding to the location.
 * @param query
 *    Input string from the user.
 * @returns {{lat: number, lng: number}}
 *    lat: latitude for the most likely result of the query.
 *    lng: longitude for the most likely result of the query.
 */
const getCoordinatesAtLocation = (query) => {
  // @Todo Implement Geocoding.
  return {
      lat: 50,
      lng: 50
  }
};