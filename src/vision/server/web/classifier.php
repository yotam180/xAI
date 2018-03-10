<html>
<head>
    <title>xAI | Classifier </title>

    <?php require("include.php"); ?>

    <link rel="StyleSheet" href="style/master.css" />

    <script>
        window.classifier_name = "";

        $(document).ready(function() {
            $.ajax({
                url: "/classifier",
                type: "GET",
                data: {
                    id: location.hash.substr(1)
                },
                success: function(e) {
                    var j = JSON.parse(e);

                    $(".classifier_name").text(j.classifier_name);
                    $(".dataset_name").text(j.dataset.identifier);
                    $(".trained").text(new Date(j.date_trained).toString());
                    $(".status").text(j.trained ? "Trained!" : "In progress");
                    $(".status").css({color: j.trained ? "lime" : "red"});
                    $("#accuracy").find(".determinate").css({width: j.accuracy + "%"});
                    $(".acc").text(j.accuracy + "%");
                    window.classifier_name = j.classifier_name;
                },
                error: function(e) {
                    Materialize.toast("Error " + e.status, 5000);
                }
            });

            $('.modal').modal();

            $("#fileupload").on("change", function() {
                var ext = $("#fileupload").val().split(".").pop();
                if (!~(["png", "jpg", "jpeg", "bmp"].indexOf(ext.toLowerCase()))) {
                    Materialize.toast("Only png, jpg, and bmp files are allowed", 5000);
                    return;
                }

                var reader = new FileReader();
                reader.readAsDataURL($(this)[0].files[0]);
                reader.onload = function() {
                    //console.log(reader.result); // Never uncomment this.
                    $.ajax({
                        url: "v",
                        type: "POST",
                        data: JSON.stringify({
                            c: window.classifier_name,
                            i: reader.result
                        }),
                        success: function(e) {
                            $("#result_json").text(e);
                        },
                        error: function(e) {
                            $("#result_json").text("Error: " + e.status + ", " + e.responseText);
                        }
                    });
                };
                reader.onerror = function(e) {
                    Materialize.toast("Error: " + e);
                };
            });
        });

        function delete_classifier() {
            $.ajax({
                url: "/delete_classifier",
                type: "GET",
                data: {
                    id: location.hash.substr(1)
                },
                success: function(e) {
                    var j = JSON.parse(e);
                    Materialize.toast(j.message);
                    if (j.message == "Classifier deleted") {
                        setTimeout(function() {
                            location.href = "/console.php"
                        }, 1000);
                    }
                }
            });
        }
    </script>
</head>
<body>
    <a href="console.php"><i class="medium material-icons">arrow_back</i></a>
    <div class="container">
        <h5 class="header center"><span class="classifier_name">[...]</span></h5>
        <div class="row">
            <b class="classifier_name">[...]</b>, trained on dataset <span class="dataset_name">[...]</span><br/><br/>
            <b>Trained</b>: <span class="trained">[...]</span><br/><br/>
            <b>Status</b>: <span class="status">[...]</span>
        </div>
        <div class="row">
            Accuracy: <span class="acc">[...]</span>
            <div class="progress" id="accuracy">
                <div class="determinate" style="background-color: red; width: 70%"></div>
            </div>
        </div>
        <div class="row">
            <h5 class="header center">Actions</h5>
            <center>
                <a onclick="$('#delete_warning').modal('open');" class="btn-floating btn-large waves-effect waves-light red"><i class="material-icons">delete_forever</i></a>
            </center>

            <div id="delete_warning" class="modal">
                <div class="modal-content black-text">
                    <h4>Warning!</h4>
                    <p>Deleting a classifier is a <b>permanent</b> action, and cannot be undone. Are you really sure 
                    you want to delete this classifier forever?</p>
                </div>
                <div class="modal-footer">
                    <a onclick="delete_classifier();" class="modal-action modal-close waves-effect waves-green btn-flat">Yes, I am</a>
                    <a class="modal-action modal-close waves-effect waves-green btn-flat">No, keep my classifier.</a>
                </div>
            </div>
        </div>
        <div class="row">
            <h5 class="header center">Try the classifier</h5>
            <form action="#">
                <div class="file-field input-field">
                <div class="btn red">
                    <span>File</span>
                    <input type="file" id="fileupload">
                </div>
                <div class="file-path-wrapper">
                    <input class="file-path validate" type="text">
                </div>
                </div>
            </form>
            <div id="result_json"></div>
        </div>
    </div>
</body>
</html>