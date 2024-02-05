import React from 'react';
import Plot from 'react-plotly.js';

interface Station {
    latitude: string;
    longitude: string;
    height: string;
    station: string;
    station_code: string;
}

interface MapGraphProps {
    stations: Station[];
}

const MapGraph: React.FC<MapGraphProps> = ({ stations }) => {
    const latitudes = stations.map(station => parseFloat(station.latitude));
    const longitudes = stations.map(station => parseFloat(station.longitude));

    return (
        <Plot
            data={[
                {
                    type: 'scattergeo',
                    mode: 'markers',
                    lat: latitudes,
                    lon: longitudes,
                    marker: {
                        color: 'red',
                        size: 10
                    }
                }
            ]}
            layout={{
                geo: {
                    scope: 'south america', // foco na América do Sul
                    showland: true,
                    landcolor: 'rgb(243, 243, 243)',
                    countrycolor: 'rgb(204, 204, 204)',
                    lakecolor: 'rgb(255, 255, 255)',
                    projection: {
                        type: 'mercator' // tipo de projeção do mapa
                    },
                    center: { // coordenadas do centro do mapa
                        lat: -14.2350, // latitude do Brasil
                        lon: -51.9253 // longitude do Brasil
                    },
                    resolution: 50, // resolução do mapa
                    showcountries: true, // mostrar países no mapa
                    countrywidth: 1, // largura das linhas dos países
                    subunitwidth: 1 // largura das linhas das subunidades
                },
                width: 800,
                height: 600
            }}
        />);
};

export default MapGraph;