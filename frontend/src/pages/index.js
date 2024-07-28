import React, { useEffect, useState } from 'react';

const Home = () => {
    const [htmlContent, setHtmlContent] = useState('');

    useEffect(() => {
        fetch('http://localhost:8000/') // Replace with your Django server URL
            .then(response => response.text())
            .then(data => setHtmlContent(data))
            .catch(error => console.error('Error fetching HTML:', error));
    }, []);

    return (
        <div>
            <link rel="stylesheet" href="http://localhost:8000/static/css/styles.css" />
            <div dangerouslySetInnerHTML={{ __html: htmlContent }} />
        </div>
    );
}

export default Home;
