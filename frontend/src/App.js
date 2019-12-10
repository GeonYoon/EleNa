import React from 'react';
import '../node_modules/leaflet/dist/leaflet.css';
import queryString from 'query-string';

import './App.css';
import Map from './components/Map'
import Sidebar from './components/Sidebar';

const App = () => {
    const [lat, updateLat] = React.useState(42.39);
    const [lng, updateLng] = React.useState(-72.524);

    // State hooks for the elevation adjusted path.
    const [nodesArray, updateNodesArray] = React.useState([]);
    const [elevation, updateElevation] = React.useState(0);
    const [distanceTraveled, updateDistanceTraveled] = React.useState(0);

    // State hooks for the shortest path.
    const [shortestNodesArray, updateShortestNodesArray] = React.useState([]);
    const [shortestPathElevation, updateShortestPathElevation] = React.useState(0);
    const [shortestDistanceTraveled, updateShortestDistanceTraveled] = React.useState(0);

    const [zoom, updateZoom] = React.useState(16);
    const [startCoord, updateStart] = React.useState("");
    const [endCoord, updateEnd] = React.useState("");
    const [distanceThreshold, updateThreshold] = React.useState(0);
    const [selectedTextBox, updateSelectedTextBox] = React.useState("");

    // State hooks for the reverse-geocoded names to display coordinate locations to the user.
    const [friendlyStartName, setFriendlyStartName] = React.useState('Starting Point');
    const [friendlyEndName, setFriendlyEndName] = React.useState('Starting Point');

    // Represents the mode (shortest path or elevation adjusted path) shown to the user.
    const [mode, setMode] = React.useState('elevation');

    // Represents the state of loading in progress or not.
    const [loading, updateLoading] = React.useState(false);

    // Retrieves path from the backend.
    const calculate = () => {
        // If there is no user input, simply return.
        if (startCoord === "" || endCoord === "") {
            return;
        }

        // Sets loading value to true when we start calculation.
        updateLoading(true);

        // Construct query for geo-coding.
        let gString = queryString.stringify({
            format: 'json',
        });

        // Construct fetch request from Nominatim API for the starting coords.
        fetch('https://nominatim.openstreetmap.org/search/' + startCoord + '?' + gString)
            .then(response => response.json())
            .then(fromData => {
                // Construct fetch request from Nominatim API for the ending coords.
                fetch('https://nominatim.openstreetmap.org/search/' + endCoord + '?' + gString)
                    .then(response => response.json())
                    .then(toData => {
                        // Returns an alert if locations for start and end cannot be converted to coords.
                        if (fromData.length === 0 || toData.length === 0) {
                            alert("Please enter a valid location.");
                            updateLoading(false);
                            return;
                        }
                        let qString = queryString.stringify({
                            'format': 'json',
                            'start': fromData[0].lat + ',' + fromData[0].lon,
                            'end': toData[0].lat + ',' + toData[0].lon,
                            'threshold': (1 + (distanceThreshold * 0.01)),
                        });

                        // Sends starting and ending points to the backend.
                        // Retrieves calculated path from the backend.
                        fetch('api/path/?' + qString)
                            .then(response => response.json())
                            .then((data) => {
                                // setFriendlyStartName(fromData[0].display_name);
                                // setFriendlyEndName(toData[0].display_name);
                                // updateStart(fromData[0].display_name);
                                // updateEnd(toData[0].display_name);

                                updateNodesArray(data.elevation_path.path);
                                updateElevation(parseFloat(data.elevation_path.total_elevation));
                                updateDistanceTraveled(parseFloat(data.elevation_path.total_distance));

                                updateShortestNodesArray(data.shortest_path.path);
                                updateShortestPathElevation(parseFloat(data.shortest_path.total_elevation));
                                updateShortestDistanceTraveled(parseFloat(data.shortest_path.total_distance));

                                // Sets loading value to false when we finish calculation.
                                updateLoading(false);
                            });
                    })
            });
    };

    // Initial position of the map.
    let position = [lat, lng];

    // Reference to the selected textBox's updateSelected function.
    let updateSelectedTextBoxInMap = () => {};
    if (selectedTextBox === "updateStart") {
        updateSelectedTextBoxInMap = updateStart;
    }
    if (selectedTextBox === "updateEnd") {
        updateSelectedTextBoxInMap = updateEnd;
    }

    return (
        <div className='App'>
            <Sidebar updateStart={ updateStart }
                     updateEnd={ updateEnd }
                     startCoord={ startCoord }
                     endCoord={ endCoord }
                     updateThreshold={ updateThreshold }
                     updateSelectedTextBox={ updateSelectedTextBox }
                     nodesArray={ nodesArray }
                     shortestNodesArray={ shortestNodesArray }
                     calculate={ calculate }
                     selectedTextBox={ selectedTextBox }
                     totalElevation={ elevation }
                     totalDistance={ distanceTraveled }
                     shortestTotalDistance={ shortestDistanceTraveled }
                     shortestTotalElevation={ shortestPathElevation }
                     mode={ mode }
                     setMode={ setMode }
                     loading={ loading }
            />
            <div className={'map-container'}>
                <Map center={ position }
                     zoom={ zoom }
                     nodesArray={ nodesArray }
                     shortestNodesArray={ shortestNodesArray }
                     mode={ mode }
                     updateStart={ updateStart }
                     updateEnd={ updateEnd }
                     updateSelectedTextBox={ updateSelectedTextBoxInMap }
                     friendlyStartName={ friendlyStartName }
                     friendlyEndName={ friendlyEndName }
                />
            </div>
        </div>
    );
};

export default App;
