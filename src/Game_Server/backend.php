<?php
    if($_SERVER["REUQUEST_METHOD"]!="POST")
        die("Must Enter in Get");
    $data = $_GET["tag"];


    function filter($text)
    {
        
    }
    function special($text)
    {
        $special_chars = "!@#$%^&*(){}[]|";
        for($i=0;$i<count($text);$i++)
        {
            for($j=0;$j<count($special_chars);$j++)
            {
                
            }
        }
    }
?>