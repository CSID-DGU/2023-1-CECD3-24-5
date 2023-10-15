import { useState, useEffect } from 'react';

function useLocalStorage(key, initialValue) {
    // 초기 상태값을 localStorage에서 불러오거나, 기본값을 사용
    const [state, setState] = useState(() => {
        const storedValue = localStorage.getItem(key);
        return storedValue ? JSON.parse(storedValue) : initialValue;
    });

    // 상태가 변경될 때마다 localStorage에 저장
    useEffect(() => {
        localStorage.setItem(key, JSON.stringify(state));
    }, [key, state]);

    return [state, setState];
}

export default useLocalStorage;
