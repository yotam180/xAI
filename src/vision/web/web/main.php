<html>
<head>
    <title>xAI</title>
    <?php require_once("include.php"); ?>

    <script>
        window.Navigator = {
            PopInitiatedByUser: false,
            LoadPage: function(url, nopush) {
                if (!nopush) {
                    history.pushState(null, null, (url || "index.php"));
                }
                Navigator.PopInitiatedByUser = true;
                $("#error_panel").hide();
                $.ajax({
                    type: "GET",
                    url: "/back/" + (url || "index.php"),
                    success: function(e) {
                        $("#main").hide();
                        $("#main").html(e);
                        $("#main").animate({height: "show"});
                        console.log(e);
                    },
                    error: function(e) {
                        $("#loader").fadeOut(complete=() => {
                            $("#error_panel").show();
                            $("#main").html("<h1>An error occured while showing the page!</h1>");
                        });
                    }
                });
            }
        };

        $(document).ready(function() {
            var load_current = function() {
                var path = window.location.pathname.split("/");
                var page = path[path.length - 1];
                Navigator.LoadPage(page, true);
            };
            load_current();

            window.onpopstate = function(e) {
                if (Navigator.PopInitiatedByUser) {
                    Navigator.PopInitiatedByUser = false;
                    return;
                }
                console.log(e);
                load_current();
            };
        });
    </script>

</head>
<body>
    <?php require("header.php"); ?>
    <div id="error_panel" style="text-align: center; display: none;">
          <div class="card blue-grey darken-1">
            <div class="card-content white-text">
              <span class="card-title">That's an error!</span>
              <p>This seems like an error! The page may have taken too much time to load, or was not found on the server.</p>
            </div>
            <div class="card-action">
              <a href="#">Go Back</a>
              <a href="#" onclick="Navigator.LoadPage();">Main Page</a>
            </div>
          </div>
    </div>
    <div id="main">
        &nbsp;
    </div>
</body>
</html>