import React from "react";

/**
 * Takes information about the current step and outputs a JSX representation
 * for the result section.
 * @param stepNum
 *    The ordering of the step in the route.
 * @param lat
 *    Latitude of the step being displayed.
 * @param lng
 *    Longitude of the step being displayed.
 * @param elevation
 *    Elevation traveled at the step being displayed.
 * @param distance
 *    Distance traveled at the step being displayed.
 * @returns {*}
 *    Returns the Step JSX object.
 */
const Step = ({ stepNum, lat, lng, elevation, distance }) => (
    <div className={ 'step' }>
        <span className={ 'step--number' }>1</span>
        <div className={ 'step--info' }>
            <div>42.3601° N, 71.0589° W</div>
            <div className={ 'step--detail' }>
                <span>Elevation: c</span>
                <span>Distance: d</span>
            </div>
        </div>
    </div>
);

export default Step;