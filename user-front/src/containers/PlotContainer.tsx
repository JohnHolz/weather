import React, { useState, useEffect } from 'react';
import { getStationData, getStationsMapData } from '../services/api';
import PlotComponent from '../components/PlotComponent';
import dynamic from 'next/dynamic';

const MapGraph = dynamic(() => import('../components/MapGraph'), {
    ssr: false,
});


const TwoLinePlotContainer = () => {
    const [data, setData] = useState([]);
    const [stations, setStations] = useState([]);

    useEffect(() => {
        const fetchData = async () => {
            const result = await getStationData();
            const stations2 = await getStationsMapData();
            setData(result.values);
            setStations(stations2.stations);
            console.log(stations2);
        };
        fetchData();
    }, []);

    return (
        <div>
            {data ? <PlotComponent data={data} /> : <p>Carregando...</p>}
            {stations.length > 0 && <MapGraph stations={stations} />}
        </div>
    );
};

export default TwoLinePlotContainer;