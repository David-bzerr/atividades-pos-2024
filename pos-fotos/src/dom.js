// src/dom.js
export function displayPhotos(photos) {
    const photosContainer = document.getElementById('photos-container');
    photosContainer.innerHTML = ''; // Limpa o container antes de exibir

    photos.forEach(photo => {
        const col = document.createElement('div');
        col.className = 'col-6 col-md-4 mb-3';
        col.innerHTML = `
            <div class="card">
                <img src="${photo.thumbnailUrl}" class="card-img-top" alt="${photo.title}">
                <div class="card-body">
                    <h5 class="card-title">${photo.title}</h5>
                </div>
            </div>
        `;
        photosContainer.appendChild(col);
    });
}

export function setupSearchHandler(allPhotos) {
    const searchButton = document.getElementById('search-album-btn');
    searchButton.addEventListener('click', () => {
        const albumId = document.getElementById('album-search').value;
        const filteredPhotos = allPhotos.filter(photo => photo.albumId == albumId);
        displayPhotos(filteredPhotos);
    });
}
