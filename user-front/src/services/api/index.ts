// import { getToken, setToken } from "../localStorage";
// import { Token, Secret } from "fernet";
// import { stringify } from "querystring";
import LoginType from '../../types/Stations.Type'

const CONTENT_TYPE_APPLICATION_JSON = "application/json";

const doFetch = (path: string, options = {}) =>
  fetch(path, options).then(async response => {
    if (!response.ok) {
      throw new Error("ERRRORORRRORORORRORROROR"
        // await response.json()
      )
    }
    return response
  })

export const getStationData = async () => {
  const path = 'http://localhost:5008/station/A612';
  const options = {
    method: "GET",
    headers: {
      Accept: "application/json",
      "Content-Type": CONTENT_TYPE_APPLICATION_JSON,
    },
  };
  const response = await doFetch(path, options)
  const data = await response.json()
  console.log(data);
  return data as any
};

export const getActivatedStations = async () => {
  const path = 'http://localhost:5008/stations_activated';
  const options = {
    method: "GET",
    headers: {
      Accept: "application/json",
      "Content-Type": CONTENT_TYPE_APPLICATION_JSON,
    },
  };
  const response = await doFetch(path, options)
  const data = await response.json()
  console.log(data);
  return data as { stations: string[] }
};

export const getStationsUpdateData = async () => {
  const path = 'http://localhost:5008/stations_page';
  const options = {
    method: "GET",
    headers: {
      Accept: "application/json",
      "Content-Type": CONTENT_TYPE_APPLICATION_JSON,
    },
  };
  const response = await doFetch(path, options)
  const data = await response.json()
  console.log(data);
  return data as { stations: { last_data: string, station: string }[] }
};

export const getStationsMapData = async () => {
  const path = 'http://localhost:5008/stations_graph_map';
  const options = {
    method: "GET",
    headers: {
      Accept: "application/json",
      "Content-Type": CONTENT_TYPE_APPLICATION_JSON,
    },
  };
  const response = await doFetch(path, options)
  const data = await response.json()
  console.log(data);
  return data as any
};


// const getPublicKey = () => {
//   return "MILLAMANDANOSGATOS";
// };

// const criptographPass = (password: string) => {
//   const secret = new Secret(getPublicKey());
//   const f = new Token({ secret });
//   return f.encode(password.toString());
// };


// export const authUser = async (login: LoginType) => {
//   const path = process.env.NEXT_PUBLIC_AUTH_API_URL + `/login`;
//   let body;

//   body = {
//     email: login.email,
//     password: login.password,
//   };

//   const options = {
//     method: "POST",
//     headers: {
//       Accept: "*/*",
//       "Content-Type": "application/json",
//       "Access-Control-Allow-Origin": "*",
//     },
//     body: JSON.stringify(body),
//   };

//   const response = await doFetch(path, options);
//   const data = await response.json();
//   setToken(data.token);
//   return data;
// };


// export const getUserData = async () => {
//   const path = process.env.NEXT_PUBLIC_AUTH_API_URL + `/get_user_data`;
//   const options = {
//     method: "GET",
//     headers: {
//       Accept: "application/json",
//       "Content-Type": CONTENT_TYPE_APPLICATION_JSON,
//       "x-access-token": getToken(),
//     },
//   };

//   const response = await doFetch(path, options);
//   const data = await response.json();
//   return data.user_data as JSON;
// };
