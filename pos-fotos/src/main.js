// src/main.js
import { fetchPhotos } from './api.js';
import { displayPhotos, setupSearchHandler } from './dom.js';

async function main() {
    try {
        const allPhotos = await fetchPhotos(); // Busca fotos da API
        displayPhotos(allPhotos);             // Exibe todas as fotos
        setupSearchHandler(allPhotos);        // Configura busca por álbum
    } catch (error) {
        alert('Não foi possível carregar as fotos.');
    }
}

// Inicializa o script
main();
