import React from 'react';
import { Routes, Route} from 'react-router-dom';

import EnterPage from './pages/EnterPage';
import InputPage from './pages/InputPage';
import QuizPage from './pages/QuizPage';
import './App.css';

function App() {
    return (
        <>
          <Routes>
            <Route path="/" element={<EnterPage />} />
            <Route path="/InputPage" element={<InputPage />} />
            <Route path="/QuizPage" element={<QuizPage />} />
          </Routes>
        </>
    );
}

export default App;
