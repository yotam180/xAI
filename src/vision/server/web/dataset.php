<html>
<head>
    <title>xAI | Dataset </title>

    <?php require("include.php"); ?>

    <link rel="StyleSheet" href="style/master.css" />

    <script>
        $(document).ready(function() {
            $.ajax({
                url: "/dataset",
                data: {
                    id: location.hash.substr(1)
                },
                success: function(e) {
                    var j = JSON.parse(e);
                    window.J= j;
                    if (j.message) {
                        Materialize.toast(j.message);
                        return;
                    }

                    $(".dataset_name").text(j.subject);
                    $(".dataset_description").text(j.description);
                    $(".last_updated").text(new Date(j.last_updated * 1000));
                    $(".status").text(j.working ? "Complete and Trainable" : "Downloading...")
                        .css({color: j.working ? "lime" : "red"})
                    $("#positives").html(
                        j.positive_keywords.map(x => "<div class='chip'>" + x + "</div>").join("")
                    )
                    $("#negatives").html(
                        j.negative_keywords.map(x => "<div class='chip'>" + x + "</div>").join("")
                    )
                }
            });

            $('.modal').modal();
        });

        function delete_dataset() {
            $.ajax({
                url: "/delete_dataset",
                data: {
                    id: location.hash.substr(1)
                },
                success: function(e) {
                    var j = JSON.parse(e);
                    Materialize.toast(j.message);
                    if (j.message == "Dataset deleted") {
                        setTimeout(function() {
                            location.href = "/console.php"
                        }, 1000);
                    }
                }
            });
        }
    </script>  
</head>
<body class="white-text">
    <a href="console.php"><i class="medium material-icons">arrow_back</i></a>
    <div class="container">
        <h5 class="header center"><span class="dataset_name">[...]</span></h5>
        <div class="row">
            <b class="dataset_name">[...]</b> — <span class="dataset_description">[...]</span><br/><br/>
            <b>Last Updated</b>: <span class="last_updated">[...]</span><br/><br/>
            <b>Status</b>: <span class="status">[...]</span>
        </div>
        <div class="row">
            <h5 class="header center">Actions</h5>
            <center>
                <a onclick="$('#delete_warning').modal('open');" class="btn-floating btn-large waves-effect waves-light red"><i class="material-icons">delete_forever</i></a>
            </center>

            <div id="delete_warning" class="modal">
                <div class="modal-content black-text">
                    <h4>Warning!</h4>
                    <p>Deleting a dataset is a <b>permanent</b> action, and cannot be undone. Are you really sure 
                    you want to delete this dataset forever?</p>
                </div>
                <div class="modal-footer">
                    <a onclick="delete_dataset();" class="modal-action modal-close waves-effect waves-green btn-flat">Yes, I am</a>
                    <a class="modal-action modal-close waves-effect waves-green btn-flat">No, keep my dataset.</a>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col s6">
                <h5 class="header center">Positives</h5>
                <div id="positives" class="center"></div>
            </div>
            <div class="col s6">
                <h5 class="header center">Negatives</h5>
                <div id="negatives" class="center"></div>
            </div>
        </div>
    </div>
</body>
</html>