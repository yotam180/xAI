<html>
<head>
    <title>xAI | Dataset Progress </title>

    <?php require("include.php"); ?>

    <link rel="StyleSheet" href="style/master.css" />

    <script>

        $(document).ready(function() {
            var check = function() {
                $.ajax({
                    url: "/classifier_status",
                    data: {
                        classifier_id: location.hash.substr(1)
                    },
                    success: function(e) {
                        var j = JSON.parse(e);
                        if (j.status == "done") {
                            location.href = "/classifier.php" + location.hash;
                            return;
                        }
                        if (j.status == "queued") {
                            $("#queued").show();
                            $("#training").hide();
                            $("#classifier_name").text("queued...");
                            return;
                        }
                        $("#queued").hide();
                        $("#training").show();
                        $("#classifier_name").text(j.data.classifier_id);
                        $("#epochs").text(j.data.epoch + " / 300");
                        $("#epochs_prog").find(".determinate").css({width: (j.data.epoch / 3) + "%"});
                        $("#val_acc").text(j.data.val_acc);
                        $("#val_acc_prog").find(".determinate").css({width: (j.data.val_acc * 100) + "%"});
                        $("#best_val_acc").text(j.data.best_val_acc);
                        $("#best_val_acc_prog").find(".determinate").css({width: (j.data.best_val_acc * 100) + "%"});
                    },
                    error: function(a) {
                        Materialize.toast("Error " + a.status + ": " + a.responseText, 5000);
                    }
                });
            }
            check();
            setInterval(check, 5000);
        });

        function stop() {
            $.ajax({
                url: "/stop_training",
                success: function(e) {
                    var j = JSON.parse(e);
                    Materialize.toast(j.message, 3000);
                    if (j.message == "Training Stopped") {
                        location.href = "/console.php";
                    }
                },
                error: function(a) {
                    try {
                        var j = JSON.parse(a.responseText);
                        Materialize.toast("Error: " + j.message, 3000);
                    }
                    catch (err) {
                        Materialize.toast("Error " + a.status);
                    }
                }
            })
        }

    </script>

</head>
<body>
</body>
    <a href="console.php"><i class="medium material-icons">arrow_back</i></a>
    <div id="title"><strong>Classifier  <span id="classifier_name">[...]</span></strong></div>

    <div class="container">
        <div class="section" id="queued">
            <h5 class="header center">Queued...</h5>
            <div class="progress">
                <div class="indeterminate"></div>
            </div>
        </div>

        <div class="section" id="training">
            <h5 class="header center">Training...</h5>
            <strong>Training epochs completed:</strong> <span id="epochs">[...]</span><br/><br/>
            <div class="progress" id="epochs_prog">
                <div class="determinate" style="width: 70%"></div>
            </div>
            <strong>Accuracy measured:</strong> <span id="val_acc">[...]</span><br/><br/>
            <div class="progress" id="val_acc_prog">
                <div class="determinate" style="background-color: red; width: 70%"></div>
            </div>
            <strong>Best accuract measured so far:</strong> <span id="best_val_acc">[...]</span><br/><br/>
            <div class="progress" id="best_val_acc_prog">
                <div class="determinate" style="background-color: lime; width: 70%"></div>
            </div>
            <br/>
            <center>
                <a onclick="stop();" class="waves-effect waves-light red btn">Stop training<i class="material-icons left">stop</i></a>
            </center>
          </div>
        </div>
    </div>
</body>
</html>