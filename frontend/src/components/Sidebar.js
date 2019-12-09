import React from 'react';
import Slider from 'rc-slider';
import 'rc-slider/assets/index.css';
import 'rc-tooltip/assets/bootstrap.css';

import Step from './Step';
import CustomHandle from "./Handle";
import '../styles/Sidebar-styles.css'

/**
 * Displays a sidebar containing user input fields, and step-by-step information about the route.
 * @param updateStart
 *      Updates the starting coordinates based on user input to the "start" text field.
 * @param updateEnd
 *      Updates the ending coordinates based on user input to the "end" text field.
 * @param startCoord
 *      Starting coordinates used for computing route.
 * @param endCoord
 *      Ending coordinates used for computing route.
 * @param updateThreshold
 *      Updates the distance threshold based on user input to the slider.
 * @param updateSelectedTextBox
 *      Function that updates the currently selected textBox with the coordinate values on the map.
 * @param nodesArray
 *      Nodes that exist on the elevation adjusted calculated path.
 * @param shortestNodesArray
 *      Nodes that exist on the shortest calculated path.
 * @param calculate
 *      Function that retrieves computed route from the backend.
 * @param selectedTextBox
 *      String value of the currently selected textBox.
 * @param totalElevation
 *      Total elevation traveled over the elevation adjusted route.
 * @param totalDistance
 *      Total distance traveled over the elevation adjusted route.
 * @param shortestTotalElevation
 *      Total elevation traveled over the shortest path route.
 * @param shortestTotalDistance
 *      Total distance traveled over the shortest path route.
 * @param mode
 *      The mode (elevation adjusted route, or shortest path route) that is currently selected.
 * @param setMode
 *      Function for setting the mode.
 * @returns {*}
 *      Returns the Sidebar JSX object.
 */

const Sidebar = ({   updateStart,
                     updateEnd,
                     startCoord,
                     endCoord,
                     updateThreshold,
                     updateSelectedTextBox,
                     nodesArray,
                     shortestNodesArray,
                     calculate,
                     selectedTextBox,
                     totalElevation,
                     totalDistance,
                     shortestTotalElevation,
                     shortestTotalDistance,
                     mode,
                     setMode }) => {

    // State used to determine the visibility of the sideBar component.
    const [display, updateDisplay] = React.useState(true);

    // Default summary value.
    let summary = (<div/>);

    let selectedNodeArray = [];
    let selectedElevation = 0.0;
    let selectedDistance = 0.0;

    if (mode === 'elevation') {
        selectedNodeArray = nodesArray;
        selectedElevation = totalElevation;
        selectedDistance = totalDistance;
    }
    else {
        selectedNodeArray = shortestNodesArray;
        selectedElevation = shortestTotalElevation;
        selectedDistance = shortestTotalDistance;
    }

    // If the nodesArray has values, display them.
    if (selectedNodeArray.length > 0) {
        summary = (
            <>
                <div className={ 'summary' }>
                    <p>Elevation Traveled: { selectedElevation.toFixed(2) } meters</p>
                    <p>Distance Traveled: { selectedDistance.toFixed(2) } meters</p>
                </div>

                <div className={'mode-toggle'}>
                    <span className={ mode === 'elevation' ? 'active' : ''}
                          onClick={ (event) => { setMode('elevation') } }>
                        Elevation Adjusted
                    </span>
                    <span className={ mode === 'distance' ? 'active' : ''}
                          onClick={ (event) => {setMode('distance') } }>
                        Shortest Distance
                    </span>
                </div>
            </>
        );
    }

    return (
        <div className={ 'sidebar-container' }>
            <h1 className={ 'branding' }> EleNa</h1>
            <button className={ 'collapse-button' } onClick={() => updateDisplay(!display)}>{ display ? '▲' : '▼' }</button>
            <div className={ display ? 'collapsible-sidebar visible' : 'collapsible-sidebar'}>
                <div className={ 'form' }>
                    <input onFocus={ (event) => updateSelectedTextBox("updateStart") }
                           // Stops clicking on the map from updating the value of the text box when the text box is not selected.
                           onBlur={(event) => {
                               setTimeout(() => {
                                   if (selectedTextBox !== "updateStart") {
                                       updateSelectedTextBox("")
                                   }
                               }, 200)
                           }}
                           value={ startCoord }
                           onChange={ (event) => updateStart(event.target.value) }
                           placeholder={ 'Starting point' }
                           type={ 'text' }
                    />
                    <input onFocus={ (event) => updateSelectedTextBox("updateEnd") }
                           // Stops clicking on the map from updating the value of the text box when the text box is not selected.
                           onBlur={ (event) => {
                               setTimeout(() => {
                                   if (selectedTextBox !== "updateEnd") {
                                       updateSelectedTextBox("")
                                   }
                               }, 200)
                           } }
                           value={ endCoord }
                           onChange={ (event) => updateEnd(event.target.value) }
                           placeholder={ 'Ending point' }
                           type={ 'text' }
                    />
                    <div className={ 'label-container' }>
                        Distance Threshold
                    </div>
                    <div className={ 'sliderContainer' }>
                        <Slider onChange={ updateThreshold } step={ 10 } defaultValue={ 0 }
                                handle={ CustomHandle }
                                marks={ {
                                    0: { style: {}, label: '0%' },
                                    20: { style: {}, label: '20%' },
                                    40: { style: {}, label: '40%' },
                                    60: { style: {}, label: '60%' },
                                    80: { style: {}, label: '80%' },
                                    100: { style: {}, label: '100%' }
                        } }/>
                    </div>
                    <button onClick={ calculate } type='button'> Calculate</button>
                </div>

                { summary }
                <div className={'result'}>
                    {
                        selectedNodeArray.map((node, key) => {
                            if (node === null) {
                                return <div/>;
                            }

                            return <Step stepNum={ key + 1 }
                                         lat={ node[0] }
                                         lng={ node[1] }
                            />
                        })
                    }
                </div>
            </div>
        </div>
    );
};

export default Sidebar;