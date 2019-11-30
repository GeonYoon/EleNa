import React from 'react';
import Slider from "rc-slider";
import Tooltip from 'rc-tooltip';

const Handle = Slider.Handle;

const CustomHandle = (props) => {
    const { value, dragging, index, ...restProps } = props;
    return (
        <Tooltip
            prefixCls="rc-slider-tooltip"
            overlay={`I'm willing to travel ${value}% more distance to minimize elevation.`}
            visible={dragging}
            placement="top"
            key={index}
        >
            <Handle value={`I'm willing to travel ${value}% more distance to minimize elevation.`} {...restProps} />
        </Tooltip>
    );
};

export default CustomHandle;