<?php
//error_reporting(0);
$INT_MAX_SIZE = 214783648;
$filesCount=$INT_MAX_SIZE;
if($_SERVER["REQUEST_METHOD"]=="GET")
    $filesCount=(int)$_GET["count"];

$arr =(scandir(getcwd()."\images"));
$list = array();
$count = 0;
for($i=0;$i<count($arr);$i++)
{
    if(count(explode(".",$arr[$i]))==2)
    {  
        $suffix = strtolower(explode(".",$arr[$i])[1]);
        if($suffix=="png"||$suffix=="jpg"&&count<=$filesCount){
            $list = array_pad($list,count($list)+1,$arr[$i]);
        }
    }
}
echo(json_encode($list));
?>