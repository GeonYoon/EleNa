import React from 'react';
import '../node_modules/leaflet/dist/leaflet.css';
import queryString from 'query-string';

import './App.css';
import Map from './components/Map'
import Sidebar from './components/Sidebar';

const App = () => {
    const [lat, updateLat] = React.useState(42.373);
    const [lng, updateLng] = React.useState(-72.519);
    const [elevation, updateElevation] = React.useState(0);
    const [distanceTraveled, updateDistanceTraveled] = React.useState(0);
    const [nodesArray, updateNodesArray] = React.useState([]);
    const [zoom, updateZoom] = React.useState(13);

    const [startCoord, updateStart] = React.useState("");
    const [endCoord, updateEnd] = React.useState("");

    const [distanceThreshold, updateThreshold] = React.useState(0);

    const [selectedTextBox, updateSelectedTextBox] = React.useState("");

    // Retrieves path from the backend.
    const calculate = () => {
        // If there is no user input, simply return.
        if (startCoord === "" || endCoord === "") {
            return;
        }

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
                        console.log(fromData[0].lat);
                        console.log(fromData[0].lon);
                        console.log(toData[0].lat);
                        console.log(toData[0].lon);

                        let qString = queryString.stringify({
                            'format': 'json',
                            'start': fromData[0].lat + ',' + fromData[0].lon,
                            'end': toData[0].lat + ',' + toData[0].lon,
                            'threshold': distanceThreshold,
                        });

                        // Sends starting and ending points to the backend.
                        // Retrieves calculated path from the backend.
                        fetch('/path/?' + qString)
                            .then(response => response.json())
                            .then((data) => {
                                console.log('[DEBUG] Set path to:');
                                console.log(data.path);
                                updateNodesArray(data.path);
                                console.log(data);
                            });
                    })
            });
    };

    // Initial position of the map.
    let position = [lat, lng];

    // When no calculated data is present, do not show any steps.
    if (nodesArray.length !== 0) {
        position = nodesArray[0];
    }

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
                     calculate={ calculate }
                     selectedTextBox={ selectedTextBox }
            />
            <div className={'map-container'}>
                <Map center={ position }
                     zoom={ zoom }
                     nodesArray={ nodesArray }
                     updateStart={ updateStart }
                     updateEnd={ updateEnd }
                     updateSelectedTextBox={ updateSelectedTextBoxInMap }
                />
            </div>
        </div>
    );
};

export default App;
