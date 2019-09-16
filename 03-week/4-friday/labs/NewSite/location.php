<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="" href="navigation.html">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
    <script src="https://unpkg.com/leaflet@1.5.1/dist/leaflet.js"
    integrity="sha512-GffPMF3RvMeYyc1LWMHtK8EbPv0iNZ8/oTtHPx9/cc2ILxQ+u905qIwdpULaqDkyBKgOaB57QTMg7ztg8Jm2Og=="
    crossorigin=""></script> 
    <script src="http://maps.google.com/maps/api/js?key=YOUR_API_KEY"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gmaps.js/0.4.25/gmaps.js"></script>
    
    <link rel="" href="navigation.html">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <link rel="stylesheet" href="navigationcss.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Courgette&display=swap">
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.5.1/dist/leaflet.css"
    integrity="sha512-xwE/Az9zrjBIphAcBb3F6JVqxf46+CDLwfLMHloNu6KEQCAWi6HcDUbeOfBIptF7tcCzusKFjFw2yuvEpDL9wQ=="
    crossorigin=""/>
    <link rel="stylesheet" href="navigationcss.css">
    <link rel="" href="location.js">

    <!-- Make sure you put this AFTER Leaflet's CSS -->
   

    <title>Huynh's Restaurant</title>
</head>
<body>
    <?php include("navigation.html"); ?>
    <div class="map-example">
    <div class="row">
        <div class="col-lg-6">
        <div id="mapid"></div>

        </div>
        <div class="col-lg-6">
            <div class="heading">
                <h3>Lorem Ipsum Dolor</h3>
                <div class="rating">
                    <i class="fa fa-star icon"></i>
                    <i class="fa fa-star icon"></i>
                    <i class="fa fa-star icon"></i>
                    <i class="fa fa-star icon"></i>
                    <i class="fa fa-star-o icon"></i>
                </div>
            </div>
            <div class="info">
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam ornare leo porta cursus porttitor. Proin quis tempor lectus. Cras sodales nisi ut felis tincidunt suscipit. Nullam consectetur odio et lacus tempor vestibulum.</p>
                <p>Aenean convallis, tortor eget vehicula vestibulum, sem nibh rutrum sem, vel sodales nisl velit eu ex. Sed hendrerit efficitur sollicitudin. Maecenas tempus augue lacus.</p>
            </div>
            <div class="gallery">
                <h4>Photos</h4>
                <div class="row">
                    <div class="col-md-4">
                        <a href="assets/img/image2.jpg"><img class="img-fluid image" src="viet1.jpg"></a>
                    </div>
                    <div class="col-md-4">
                        <a href="assets/img/image3.jpg"><img class="img-fluid image" src="viet2.jpg"></a>
                    </div>
                    <div class="col-md-4">
                        <a href="assets/img/image4.jpg"><img class="img-fluid image" src="vietfood1.jpg"></a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
</body>

<script src="./location.js"> </script>

</html>