<?php

function getUserIP() {
     $ipaddress = '';
         if (isset($_SERVER['HTTP_CLIENT_IP']))
           $ipaddress = $_SERVER['HTTP_CLIENT_IP'];
      else if(isset($_SERVER['HTTP_X_FORWARDED_FOR']))
               $ipaddress = $_SERVER['HTTP_X_FORWARDED_FOR'];
      else if(isset($_SERVER['HTTP_X_FORWARDED']))
               $ipaddress = $_SERVER['HTTP_X_FORWARDED'];
      else if(isset($_SERVER['HTTP_X_CLUSTER_CLIENT_IP']))
               $ipaddress = $_SERVER['HTTP_X_CLUSTER_CLIENT_IP'];
      else if(isset($_SERVER['HTTP_FORWARDED_FOR']))
               $ipaddress = $_SERVER['HTTP_FORWARDED_FOR'];
      else if(isset($_SERVER['HTTP_FORWARDED']))
               $ipaddress = $_SERVER['HTTP_FORWARDED'];
      else if(isset($_SERVER['REMOTE_ADDR']))
               $ipaddress = $_SERVER['REMOTE_ADDR'];
      else
               $ipaddress = 'UNKNOWN';
         return $ipaddress;
}

if(strlen(file_get_contents("php://input"))>2){
 $postdata = file_get_contents("php://input");
 file_put_contents("sent/contact.txt", $postdata ."userIP=". getUserIP());
 $r = shell_exec("python3.7 /var/www/cgi-bin/parse-comments.py");
 echo $r;
}
else {
 echo "Wrong data";
}
