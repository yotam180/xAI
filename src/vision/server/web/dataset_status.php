<html>
<head>
    <title>xAI | Dataset Progress </title>

    <?php require("include.php"); ?>

    <link rel="StyleSheet" href="style/master.css" />

    <script>
        $(document).ready(function() {
            $("#indeter,#deter").hide();
            var check = function() {
                $.ajax({
                    url: "/dataset_status",
                    type: "GET",
                    data: {
                        id: window.location.hash.substr(1)
                    },
                    success: function(e) {
                        var j = JSON.parse(e);
                        if (j.message) {
                            Materialize.toast(j.message);
                            if (j.message == "Not Found") {
                                location.href = "/console.php";
                            }
                        }
                        else {
                            $("#dataset_name").text(j.subject);
                            $("#downloaded").html(j.done.map(x => "<div class='chip'>" + x + "</div>").join(""));
                            $("#predownloaded").html(j.ready.map(x => "<div class='chip'>" + x + "</div>").join(""));
                            if (j.working) {
                                Materialize.toast("Finished downloading keywords");
                                location.href = "/dataset.php#" + j.dbid;
                            }
                            else {
                                if (j.current.downloaded) {
                                    $("#indeter").hide();
                                    $("#deter").show();
                                    $(".keyword_name").html("<div class='chip'>" + j.current.keyword + "</div>");
                                    $("#progressbar").find(".determinate").css({width: (j.current.downloaded * 100 / j.current.total) + "%"});
                                    $(".span_progress").text(j.current.downloaded + "/" + j.current.total);
                                }
                                else {
                                    $("#indeter").show();
                                    $("#deter").hide();
                                    $(".keyword_name").html("<div class='chip'>" + j.current.keyword + "</div>");
                                }
                            }
                        }
                    }
                })
            };

            setInterval(check, 5000);
            check();
        });
    </script>

</head>
<body class="white-text">
    <a href="console.php"><i class="medium material-icons">arrow_back</i></a>
    <div id="title"><strong>Your Dataset  <span id="dataset_name">[...]</span></strong></div>
    <div class="container section">
        <strong>Downloaded keywords: <span id="downloaded">[...],</span></strong>
        <br/><br/>
        <strong>Pre-downloaded keywords: <span id="predownloaded">[...],</span></strong>
    </div>
    <div id="title"><strong>Machine Status:</strong></div>
    <div class="container section" id="indeter">
        <strong>Loading images of keyword <span class="keyword_name">[...]</span><br/></strong>
        <div class="progress">
            <div class="indeterminate"></div>
        </div>
    </div>
    <div class="container section" id="deter">
        <strong>Downloading <span class="span_progress">[...]/[...]</span> images of keyword <span class="keyword_name">[...]</span><br/></strong>
        <div class="progress" id="progressbar">
            <div class="determinate" style="width: 70%"></div>
        </div>
    </div>
</body>
</html>