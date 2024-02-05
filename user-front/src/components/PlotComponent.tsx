import React, { useRef, useEffect } from 'react';
import * as d3 from 'd3';

const PlotComponent = ({ data }) => {
    const ref = useRef();

    useEffect(() => {
        const svg = d3.select(ref.current);
        const xScale = d3.scaleLinear().domain([0, data.length]).range([0, 500]);
        const yScale = d3.scaleLinear().domain([0, d3.max(data, d => Math.max(d.temp_max, d.temp_min))]).range([500, 0]);

        const lineTempMax = d3.line()
            .x((d, i) => xScale(i))
            .y(d => yScale(d.temp_max))
            .curve(d3.curveMonotoneX);

        const lineTempMin = d3.line()
            .x((d, i) => xScale(i))
            .y(d => yScale(d.temp_min))
            .curve(d3.curveMonotoneX);

        svg.append("path")
            .datum(data)
            .attr("fill", "none")
            .attr("stroke", "red")
            .attr("stroke-width", 1.5)
            .attr("d", lineTempMax);

        svg.append("path")
            .datum(data)
            .attr("fill", "none")
            .attr("stroke", "blue")
            .attr("stroke-width", 1.5)
            .attr("d", lineTempMin);
    }, [data]);

    return <svg ref={ref} width={500} height={500}></svg>;
};

export default PlotComponent;