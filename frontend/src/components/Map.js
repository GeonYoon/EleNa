import React, { Component } from "react";
import { Map as LeafletMap, TileLayer, Polyline } from 'react-leaflet';

/**
 * Displays the leaflet map and computed routes on that map component.
 * @param center
 *      The coordinate on which the map in default centered to.
 * @param zoom
 *      The default zoom of the map.
 * @param nodesArray
 *       Nodes that exist on the calculated path.
 * @param updateStart
 *      Function that updates the value of the starting coordinates for the route.
 * @param updateEnd
 *      Function that updates the value of the ending coordinates for the route.
 * @param updateSelectedTextBox
 *      Function that updates the value of the currently selected TextBox.
 * @returns {*}
 *      Returns the Map JSX object.
 */

class Map extends Component {
    constructor(props) {
        super(props);
        this.state = {
            currentPos: null
        };
        this.handleClick = this.handleClick.bind(this);
    }

    handleClick(event) {
        this.setState({ currentPos: event.latlng });
        this.props.updateSelectedTextBox(event.latlng.lat + ", " + event.latlng.lng);
        console.log(event.latlng);
    }

    render() {
        return (
            <LeafletMap center={ this.props.center } zoom={ this.props.zoom } onClick={ this.handleClick }>
                <TileLayer
                    attribution='&amp;copy <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
                    url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                />
                <Polyline positions={ this.props.nodesArray } color={ 'blue' }/>)
            </LeafletMap>
        )
    }
}

export default Map;