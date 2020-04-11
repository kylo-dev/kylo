<?php
//Get the status and decode the JSON
$status = json_decode(file_get_contents('https://api.mcsrvstat.us/2/kylo.xyz'));

//Show the version
echo $status->version;

//Show a list of players
foreach ($status->players->list as $player) {
	echo $player.'<br />';
}
?>