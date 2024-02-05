import React, { useRef, useEffect } from 'react';
import * as d3 from 'd3';

interface ChartProps {
    data: number[];
}

const Chart: React.FC<ChartProps> = () => {
    const ref = useRef<SVGSVGElement | null>(null);
    const data = Array.from({ length: 10 }, () => Math.floor(Math.random() * 100));

    useEffect(() => {
        const svg = d3.select(ref.current);
        svg.selectAll('rect')
            .data(data)
            .enter()
            .append('rect');
        // more D3 chart code here...
    }, [data]);

    return <svg ref={ref} />;
};

export default Chart;