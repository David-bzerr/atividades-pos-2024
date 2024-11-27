// src/api.js
export async function fetchPhotos() {
    const url = 'https://jsonplaceholder.typicode.com/photos';
    try {
        const response = await fetch(url);
        return await response.json();
    } catch (error) {
        console.error('Erro ao buscar as fotos:', error);
        throw new Error('Erro ao buscar as fotos.');
    }
}
