document.addEventListener('DOMContentLoaded', function () {
    const showsContainer = document.getElementById('shows-container');
    const episodesContainer = document.getElementById('episodes-container');

    // Fetch shows data from the Flask server
    fetch('/get_shows')
        .then(response => response.json())
        .then(data => {
            // Populate shows container with show names and episode count
            data.forEach(show => {
                const showElement = document.createElement('div');
                showElement.classList.add('show');
                showElement.textContent = `${show.name} - ${show.episodeCount} episodes`;

                                // Add click event to show episodes when a show is selected
                showElement.addEventListener('click', () => {
                    fetch(`/get_episodes?show_id=${show.id}`)
                        .then(response => response.json())
                        .then(episodes => {
                            // Populate episodes container with individual episodes
                            episodesContainer.innerHTML = ''; // Clear previous episodes
                            episodes.forEach(episode => {
                                const episodeElement = document.createElement('div');
                                episodeElement.classList.add('episode');
                                episodeElement.textContent = episode.id;    // TODO: Titel anzeigen nicht nur nummer
                                episodesContainer.appendChild(episodeElement);
                            });
                        });
                });

                showsContainer.appendChild(showElement);
            });
        });
});
