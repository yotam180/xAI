<html>
<head>
    <title>xAI | Developer Console</title>

    <?php require("include.php"); ?>

    <link rel="StyleSheet" href="style/master.css" />
    <link rel="StyleSheet" href="style/register.css" />

    <script>
        $(document).ready(function() {
            $.ajax({
                url: "/profile",
                success: function(e) {
                    var j = JSON.parse(e);
                    $("#name_span").text(j.first_name + " " + j.last_name);
                    var h = "";
                    for (var i in j.datasets) if (j.datasets.hasOwnProperty(i)) {
                        h += "<li><div class=\"black-text collapsible-header\"><b>"
                            + j.datasets[i].subject + "</b>&nbsp;(" + i
                            + ")</div><div class=\"collapsible-body\">"
                            + "<b>" + j.datasets[i].subject + "</b> — "
                            + j.datasets[i].description + "<br/><br/>"
                            + "<b>Last updated:</b> " + (new Date(j.datasets[i].last_updated * 1000).toString()) + "<br/>"
                            + "<hr/><b>Trigger keywords:</b> "
                            + j.datasets[i].positive_keywords.map(x => "<a href=\"/keyword.php#" + x + "\"><div class=\"chip\">" + x + "</div></a>").join(" ")
                            + "<br/><hr/><b>Negative keywords:</b> "
                            + j.datasets[i].negative_keywords.map(x => "<a href=\"/keyword.php#" + x + "\"><div class=\"chip\">" + x + "</div></a>").join(" ")
                            + "</div></li>"
                    }
                    $("#datasets_ul").html(h);

                    h = "";
                    for (var i in j.classifiers) if (j.classifiers.hasOwnProperty(i)) {
                        h += "<li><div class=\"black-text collapsible-header\"><b>"
                            + j.classifiers[i].classifier_name + "</b>&nbsp;(" + i
                            + ")</div><div class=\"collapsible-body\">"
                            + "<a href=\"/dataset.php#" + j.classifiers[i].dataset_trained + "\"><b>" + j.datasets[j.classifiers[i].dataset_trained].subject + "</b></a> — "
                            + j.datasets[j.classifiers[i].dataset_trained].description + "<br/><br/>"
                            + "<b>Training Date:</b> " + (new Date(j.classifiers[i].date_trained * 1000).toString()) + "<br/>"
                            + "</div></li>"
                    }
                    $("#classifiers_ul").html(h);
                },
                error: function(a, b, c) {
                    if (a.status == 403) {
                        location.href = "/login.php";
                    }
                }
            });
        });
    </script>
</head>
<body class="white-text">
    <a href="console.php"><img class="top_logo" id="top_logo" src="img/logo_light.png" /></a>
    <div id="title"><strong>Welcome to xAI, <span id="name_span">[...]</span>. <a href="/logout" style="font-size: smaller;">(Log out)</a></strong></div>

    <div class="container">
        <div class="row">
            <div class="col s6">
            <h4 class="header">Datasets &nbsp;&nbsp;&nbsp;<a href="new_dataset.php"><span style="font-size: smaller;">(create new)</span></a></h4>
                <ul id="datasets_ul" class="popout collapsible" data-collapsible="accordion">
                    <div class="progress">
                        <div class="indeterminate"></div>
                    </div>
                </ul>
            </div>
            <div class="col s6">
                <h4 class="header">Classifiers &nbsp;&nbsp;&nbsp;<a href="train_classifier.php"><span style="font-size: smaller;">(train new)</span></a></h4>
                <ul id="classifiers_ul" class="popout collapsible" data-collapsible="accordion">
                    <div class="progress">
                        <div class="indeterminate"></div>
                    </div>
                </ul>
            </div>
        </div>
    </div>
</body>
</html>