$(document).ready(() => {
    $('#searchForm').on('submit', (e) => {
      let searchText = $('#searchText').val();
      getMovies(searchText);
      e.preventDefault();
    });
  });
  
  function getMovies(searchText){
      
    axios.get('http://www.omdbapi.com?&apikey=31073954&s='+ searchText)
      .then((response) => {
        console.log(response);
        let movies = response.data.Search;
        console.log(movies);
        let output = '';
        $.each(movies, (index, movie) => {
          console.log(movie);
            output += `
            <div class="col-md-3">
              <div class="well text-center">
                <img src="${movie.Poster}">
                <h5>${movie.Title}</h5>
                <ul class="list-group">
                <li class="list-group-item"><strong>Genre:</strong> ${movie.Genre}</li>
                <li class="list-group-item"><strong>Released:</strong> ${movie.Released}</li>
                <li class="list-group-item"><strong>Rated:</strong> ${movie.Rated}</li>
                <li class="list-group-item"><strong>IMDB Rating:</strong> ${movie.imdbRating}</li>
                <li class="list-group-item"><strong>Director:</strong> ${movie.Director}</li>
                <li class="list-group-item"><strong>Writer:</strong> ${movie.Writer}</li>
                <li class="list-group-item"><strong>Actors:</strong> ${movie.Actors}</li>
                <li class="list-group-item"><strong>Actors:</strong> ${movie.Website}</li>
              </ul>
                <a onclick="movieSelected('${movie.imdbID}')" class="btn btn-primary" href="#">Movie Details</a>
              </div>
            </div>
          `;
        });
  
        $('#movies').html(output);
      })
      .catch((err) => {
        console.log(err);
      });
  }
  
  function movieSelected(id){
    sessionStorage.setItem('movieId', id);
    window.location = 'movie.html';
    return false;
  }
  
  