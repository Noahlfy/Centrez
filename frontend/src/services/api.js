

export async function api (url, method = 'GET') {
    const response = await fetch(`http://localhost:8000/api/${url}/`, {
        method: method,
        headers: {
            'Content-Type': 'application/json',
        },
    });
    const data = await response.json();
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    console.log(data);
    return data;
}

