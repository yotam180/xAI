<?php
error_reporting(0);
$INT_MAX_SIZE = 214783648;
$filesCount=$INT_MAX_SIZE;
if($_SERVER["REQUEST_METHOD"]=="GET"){
    $filesCount=(int)$_GET["count"];
}

$arr =(scandir(getcwd()."\images"));
$list = array();
$count = 0;
while($count<$filesCount){
    for($i=0;$i<count($arr);$i++)
    {
        if(in_array($arr[$i],$list))
            continue;
        $val = rand(1,$filesCount);
        if($val!=1)
            continue;
        if(count(explode(".",$arr[$i]))==2)
        {  
            $suffix = strtolower(explode(".",$arr[$i])[1]);
            
            if(($suffix=="png"||$suffix=="jpg")&&$count<$filesCount){
                $list = array_pad($list,count($list)+1,$arr[$i]);
                $count++;
                //echo $count.":".$filesCount."<br/>";
            }
        }
    }
}
echo(json_encode($list));
?>