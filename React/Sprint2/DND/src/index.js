import React, { StrictMode } from "react";
import ReactDOM from "react-dom";

import App from "./components/app/app";

const rootElement = document.getElementById("root");
ReactDOM.render(
  <StrictMode>
    <App />
  </StrictMode>,
  rootElement
);
