import React, { Component } from 'react';
import { Routes, Route } from 'react-router-dom';

import Header from './components/Header';
import EnterPage from './pages/EnterPage';
import InputPage from './pages/InputPage';
import QuizPage from './pages/QuizPage';
import ResultPage from './pages/ResultPage';
import './App.css';

function App() {
    return (
      <>
        <Header />
        <Routes>
          <Route path="/" element={<EnterPage />} />
          <Route path="/InputPage" element={<InputPage />} />
          <Route path="/QuizPage/:num" element={<QuizPage />} />
          <Route path="/ResultPage" element={<ResultPage />} />
        </Routes>
      </>
    );
}

export default App;
