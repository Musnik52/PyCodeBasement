import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";

import { createStore } from "redux";
import { Provider } from "react-redux";

import garageReducer from "./reducers/garageReducer";

const garageStore = createStore(garageReducer);

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <Provider store={garageStore}>
    <App />
  </Provider>
);
