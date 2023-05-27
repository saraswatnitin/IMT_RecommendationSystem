function recommend() {
    var movie = document.getElementById("movie").value;
    console.log(movie);
    var display= document.getElementById("display");
    var url = "http://127.0.0.1:5000/recommend_movie"; //Use this if you are NOT using nginx which is first 7 tutorials
    // var url = "/api/predict_home_price"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
  
    $.post(url, {
        movie: movie
    },  function(data, status) {
        console.log(data.recomendations);
        var movie_list  = data.recomendations;
        display.innerHTML="";
        for (var i = 0; i < movie_list.length; i++) {
            var movie = movie_list[i];
            var capitalizedMovie = movie.charAt(0).toUpperCase() + movie.slice(1);
            display.innerHTML += "<h3>" + capitalizedMovie + "</h3>";
          }
                
        console.log(status);
    });
  }
