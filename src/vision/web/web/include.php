<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>

<!-- Compiled and minified CSS -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/css/materialize.min.css">

<!-- Compiled and minified JavaScript -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/js/materialize.min.js"></script>

<?php
    function userIndex($username,$users)
    {
        for($i=0;$i<sizeof($users);$i++)
        {
            
            if($users[$i]["Username"] == $username){    
                return $i;
            }
        }
        return -1;
    }
?>