<html>
<head>
    <title>xAI | New Classifier</title>

    <?php require("include.php"); ?>

    <link rel="StyleSheet" href="style/master.css" />
    <link rel="StyleSheet" href="style/register.css" />
    
    <script>
        $(document).ready(function() {
            $.ajax({
                url: "/profile",
                success: function(e) {
                    var j = JSON.parse(e);
                    window.J = j;
                    for (var i in j.datasets) {
                        $("#select_dataset").append(
                            $("<option>").attr("value", i).text(j.datasets[i].subject + " (" + i + ")")
                        );
                    }
                    $('select').material_select();
                },
                error: function(a) {
                    if (a.status == 403) {
                        location.href = "/login.php"
                    }
                }
            });

            $("#btn_create").click(function() {
                if ($("#select_dataset").val() == null) {
                    Materialize.toast("Please select a dataset", 3000);
                    return;
                }

                if ($("#txt_classifiername").val().length < 2) {
                    Materialize.toast("Please choose a name", 3000);
                    return;
                }

                $.ajax({
                    url: "/create_classifier",
                    type: "POST",
                    data: JSON.stringify({
                        classifier_id: $("#txt_classifiername").val(),
                        dataset_id: $("#select_dataset").val()
                    }),
                    success: function(e) {
                        var j = JSON.parse(e);
                        if (j.message) {
                            Materialize.toast(j.message, 3000);
                        }
                        else {
                            location.href = "train_classifier.php#" + j.classifier_id
                        }
                    },
                    error: function(a) {
                        try {
                            var j = JSON.parse(a.responseText);
                            Materialize.toast("Error " + a.status + ": " + j.message, 3000);
                        }
                        catch (e) {
                            Materialize.toast("Error connecting: " + a.status, 3000);
                        }
                    }
                })
            });
        });
    </script>

</head>
<body>
    <a href="console.php"><i class="medium material-icons">arrow_back</i></a>
    <div id="title"><strong>New Classifier</strong></div>

    <div class="section"></div>
    <div class="container" style="color: #039be5;">
        <form id="classifier_details" class="col s12">
            <div class="row">
                <div class="col s3"></div>
                <div class="input-field col s6">
                    <input id="txt_classifiername" type="text" />
                    <label for="txt_classifiername">Classifier name</label>
                </div>
            </div>
            <div class="row">
                <div class="col s3"></div>
                <div class="input-field col s6">
                    <select id="select_dataset">
                        <option value="" disabled selected>Choose your option</option>
                    </select>
                    <label>Select your dataset</label>
                </div>
            </div>
            <div class="row">
                <div class="col s4"></div>
                <div class="col s6">
                    <a class="waves-effect waves-light btn" id="btn_create">
                        Create Classifier
                        <i class="material-icons right">add</i>
                    </a>
                </div>
            </div>
        </form>
    </div>
</body>
</html>