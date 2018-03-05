<html>
<head>
    <title>xAI | Keyword </title>

    <?php require("include.php"); ?>

    <link rel="StyleSheet" href="style/master.css" />

    <script>
        $(document).ready(function() {
            $("#img1").attr("src", "/keyword?k=" + location.hash.substr(1));
            $(".kw").text(location.hash.substr(1));
        });
    </script>

</head>
<body>
    <a href="console.php"><i class="medium material-icons">arrow_back</i></a>
    <h5 class="header center">Keyword: <span class="kw">[...]</span></h5>
    <center>
        <img id="img1" onerror="Materialize.toast('Keyword not found');" />
    </center>
</body>
</html>