drop table if exists metadata.stations;

create table metadata.stations as
select  r.station,
		max(r.region) as "region",
		max(r.state) as "state",
		max(r.station_code) as "station_code",
		min(r."Data") as "first date", 
		max(r.height) as "height", 
		max(r.longitude) as "longitude", 
		max(r.latitude) as "latitude"
from raw.southeast r
group by r.station
union 
select  r.station,
		max(r.region) as "region",
		max(r.state) as "state",
		max(r.station_code) as "station_code",
		min(r."Data") as "first date", 
		max(r.height) as "height", 
		max(r.longitude) as "longitude", 
		max(r.latitude) as "latitude"
from raw.north r
group by r.station
union 
select  r.station,
		max(r.region) as "region",
		max(r.state) as "state",
		max(r.station_code) as "station_code",
		min(r."Data") as "first date", 
		max(r.height) as "height", 
		max(r.longitude) as "longitude", 
		max(r.latitude) as "latitude"
from raw.northeast r
group by r.station
union 
select  r.station,
		max(r.region) as "region",
		max(r.state) as "state",
		max(r.station_code) as "station_code",
		min(r."Data") as "first date", 
		max(r.height) as "height", 
		max(r.longitude) as "longitude", 
		max(r.latitude) as "latitude"
from raw.south r
group by r.station
union 
select  r.station,
		max(r.region) as "region",
		max(r.state) as "state",
		max(r.station_code) as "station_code",
		min(r."Data") as "first date", 
		max(r.height) as "height", 
		max(r.longitude) as "longitude", 
		max(r.latitude) as "latitude"
from raw.central_west r
group by r.station;