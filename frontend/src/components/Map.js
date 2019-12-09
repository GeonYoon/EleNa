import React, { Component } from "react";
import { Map as LeafletMap, TileLayer, Polyline, Marker, Popup } from 'react-leaflet';
import "../styles/Map-styles.css";
import queryString from "query-string";

/**
 * Displays the leaflet map and computed routes on that map component.
 * @param center
 *      The coordinate on which the map in default centered to.
 * @param zoom
 *      The default zoom of the map.
 * @param nodesArray
 *       Nodes that exist on the calculated path.
 * @param shortestNodesArray
 *       Nodes that exist on the shortest calculated path.
 * @param mode
 *       Mode the application is currently in.
 * @param updateStart
 *      Function that updates the value of the starting coordinates for the route.
 * @param updateEnd
 *      Function that updates the value of the ending coordinates for the route.
 * @param updateSelectedTextBox
 *      Function that updates the value of the currently selected TextBox.
 * @returns {*}
 *      Returns the Map JSX object.
 */

const Map = ({center, zoom, nodesArray, shortestNodesArray, mode, updateStart, updateEnd, updateSelectedTextBox, friendlyStartName, friendlyEndName }) => {
    const [currentPos, updateCurrentPos] = React.useState(null);

    let selectedNodeArray = [];
    let unselectedNodeArray = [];

    // Checks the mode and sets the displayed steps and highlighted path.
    if (mode === 'elevation') {
        selectedNodeArray = nodesArray;
        unselectedNodeArray = shortestNodesArray;
    }
    else {
        selectedNodeArray = shortestNodesArray;
        unselectedNodeArray = nodesArray;
    }

    const handleClick = (event) => {
        updateCurrentPos(event.latlng);
        updateSelectedTextBox(event.latlng.lat + ", " + event.latlng.lng);
        console.log(event.latlng);
    };

    // Fixes the marker/popup display.
    React.useEffect(() => {
        const L = require("leaflet");

        delete L.Icon.Default.prototype._getIconUrl;

        L.Icon.Default.mergeOptions({
            iconRetinaUrl: require("../../node_modules/leaflet/dist/images/marker-icon-2x.png"),
            iconUrl: require("../../node_modules/leaflet/dist/images/marker-icon.png"),
            shadowUrl: require("../../node_modules/leaflet/dist/images/marker-shadow.png")
        });
    }, []);

    let markers = (<div/>);

    if (selectedNodeArray.length > 0) {
        markers = (
            <>
                <Marker position={ selectedNodeArray[0] }>
                    <Popup>
                        Starting Location
                    </Popup>
                </Marker>
                <Marker className={ 'endMarker' } position={ selectedNodeArray[(selectedNodeArray.length - 1)] }>
                    <Popup>
                        Ending Location
                    </Popup>
                </Marker>
            </>
        )
    }

    return (
        <LeafletMap center={ center } zoom={ zoom } onClick={ handleClick }>
            <TileLayer
                attribution='&amp;copy <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            />
            { markers }
            <Polyline positions={ unselectedNodeArray } color={ 'violet' }/>)
            <Polyline positions={ selectedNodeArray } color={ 'blue' }/>)
        </LeafletMap>
    );
};

export default Map;