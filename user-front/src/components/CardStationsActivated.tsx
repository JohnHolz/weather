import React, { useEffect, useState } from 'react';
import { getActivatedStations, getStationsUpdateData } from '../services/api/index';

const CardStationsActivated = () => {
    const [stations, setStations] = useState<any[]>([]);
    const [activatedStations, setActivatedStations] = useState<any[]>([]);

    useEffect(() => {
        const fetchStations = async () => {
            try {
                const data = await getStationsUpdateData();
                console.log('Stations data:', data); // log the data to see what's being returned
                if (Array.isArray(data.stations)) {
                    setStations(data.stations);
                } else {
                    console.error('Data returned from API is not an array');
                }
            } catch (error) {
                console.error('Error fetching stations:', error); // log any errors
            }
        };
        const fetchActivatedStations = async () => {
            try {
                const data = await getActivatedStations();
                console.log('Activated stations data:', data); // log the data to see what's being returned
                if (Array.isArray(data.stations)) {
                    setActivatedStations(data.stations);
                } else {
                    console.error('Data returned from API is not an array');
                }
            } catch (error) {
                console.error('Error fetching activated stations:', error); // log any errors
            }
        };
        fetchStations();
        fetchActivatedStations();
    }, []);
    return (
        <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', backgroundColor: 'white', borderRadius: '10px', border: '1px solid black', width: '400px', height: '700px' }}>
            <h2>Estações Ativadas</h2>
            {activatedStations.map((station, index) => {
                const stationData = stations.find(s => s.station === station);
                return (
                    <div key={index} style={{ display: 'flex', flexDirection: 'row', alignItems: 'center', justifyContent: 'space-between', width: '300px', padding: '8px', border: '1px solid black', margin: '5px', backgroundColor: 'lightgray', borderRadius: '10px' }}>
                        <div style={{ width: '33%' }}>{station}</div>
                        <div style={{ width: '33%', textAlign: 'center', color: stationData ? 'green' : 'red' }}>{stationData ? 'Ativado' : 'Desativado'}</div>
                        <div style={{ width: '33%', textAlign: 'right' }}>{stationData ? stationData.recent_date : '---'}</div>
                    </div>
                );
            })}
        </div>
    );
};
export default CardStationsActivated;