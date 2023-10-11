import React, { Component } from 'react';
import { Routes, Route } from 'react-router-dom';

import Header from './components/Header';
import EnterPage from './pages/EnterPage';
import InputPage from './pages/InputPage';
import QuizPage from './pages/QuizPage';
import './App.css';

function App() {
    return (
      <>
        <Header />
        <Routes>
          <Route path="/" element={<EnterPage />} />
          <Route path="/InputPage" element={<InputPage />} />
          <Route path="/QuizPage" element={<QuizPage />} />
        </Routes>
      </>
    );
}

export default App;
