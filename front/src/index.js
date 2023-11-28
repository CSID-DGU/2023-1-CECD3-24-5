import React from "react";
import ReactDOM from "react-dom";
import { BrowserRouter } from 'react-router-dom';
import App from "./App";
import './index.css';

import Header from './components/Header';
import Bottom from './components/Bottom';

ReactDOM.render(
  <BrowserRouter>
      <div id="wrapper">
        <Header />
        <App />
        <Bottom />
      </div>
    </BrowserRouter>,
  document.getElementById("root"),
);
