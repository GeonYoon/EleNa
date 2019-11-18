import React from 'react';

import '../node_modules/leaflet/dist/leaflet.css';
import './App.css';
import Step from './components/Step';
import { Map, Marker, Popup, TileLayer, Polyline } from "react-leaflet";
import query_overpass from "query-overpass";

const App = () => {
  const [lat, updateLat] = React.useState(42.360);
  const [lng, updateLng] = React.useState(-71.058);
  const [elevation, updateElevation] = React.useState(0);
  const [distanceTraveled, updateDistanceTraveled] = React.useState(0);
  const [nodesArray, updateNodesArray] = React.useState([]);
  const [zoom, updateZoom] = React.useState(13);

  // query_overpass('[out:json]; way["highway"](42.26004669282699,-71.06759548187256,42.26253596344967,-71.06314837932587); (._;>;); out;', (error, data)=>{ console.log(data) });

  const calculate = () => {
    fetch('/api/path/?format=json')
      .then(response => response.json())
      .then((data) => {
        console.log('[DEBUG] Set path to:');
        console.log(data.path);
        updateNodesArray(data.path);
      });
  };

  let position = [lat, lng];

  if (nodesArray.length !== 0) {
    position = nodesArray[0];
  }

  let lastNode = null;

  return (
    <div className='App'>
      <div className={ 'sidebar-container' }>
        <h1 className={ 'branding' }> EleNa </h1>
        <div className={ 'form' }>
          <input placeholder={ 'Starting point' } type={ 'text' }/>
          <input placeholder={ 'Ending point'} type={ 'text' }/>
          <button onClick={calculate} type='button'> Calculate </button>
        </div>
        <div className={ 'summary' }>
          <p>Elevation Traveled: 50 meters</p>
          <p>Distance Traveled: 40 kilometers</p>
        </div>
        <div className={ 'result' }>
          {
            nodesArray.map((node, key) => {
              if (node === null) {
                return <div/>;
              }

              return <Step stepNum={key + 1} lat={node[0]} lng={node[1]} />
            })
          }
        </div>
      </div>
      <div>
        <Map center={ position } zoom={ zoom }>
          <TileLayer
            attribution='&amp;copy <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          />
          <Polyline positions={nodesArray} color={'blue'}/>)
        </Map>
      </div>
    </div>
  );
};

export default App;
