<?php
/* by: Semeon Risom (2019-11-10)
 * invitae assessment
 * php version: 5.6.25
*/
/*clear cache*/
header("Cache-Control: no-cache, no-store, must-revalidate"); // HTTP 1.1.
header("Pragma: no-cache"); // HTTP 1.0.
header("Expires: 0"); // Proxies.

/*prevent direct access by url*/
if(!isset($_SERVER['HTTP_REFERER'])){
    // redirect them to your desired location
    header( 'HTTP/1.0 403 Forbidden', TRUE, 403 );
    exit;
};

/* query */
// https://datatables.net/manual/server-side
// https://datatables.net/examples/server_side/object_data.html
$search = $_REQUEST['search']['regex']; # regex search function
$draw = $_REQUEST['draw']; settype($draw, "integer"); # draw counter
$start = $_REQUEST['start']; settype($start, "integer"); # page number
$length = $_REQUEST['length']; settype($length, "integer"); # number of records to display
$filter = empty($_REQUEST['filter']) ? NULL : $_REQUEST['filter']; # filter parameters
# sort parameters
$sortColumn = empty($_REQUEST['sortColumn']) ? NULL : $_REQUEST['sortColumn']; # sorting column
$sortDir = empty($_REQUEST['sortDir']) ? 'DESC' : strtoupper($_REQUEST['sortDir']); # sort direction
if (empty($sortDir) || $sortDir !== 'DESC') {
   $sortDir = 'ASC';
};

/*SQL server connection information*/
// local
$host = '127.0.0.1';
$user = 'risoms';
$pass = 'samboi';
$db = 'invitae';
$table = 'variants';
// my website
$host = 'localhost';
$user = 'semenxgl_risoms';
$pass = 'samboi10';
$db = 'semenxgl_invitae';
$table = 'variants';


/*Connect to mysql database*/
$link = mysqli_connect($host, $user, $pass, $db);

// get row count in db
$query = mysqli_query($link, "SELECT count(1) FROM `$table`");
// set as integer
$recordsTotal = mysqli_fetch_assoc($query);
settype($recordsTotal['count(1)'], "integer");
$recordsTotal = $recordsTotal['count(1)'];

/*if search query*/
if (!is_null($filter)){
	// get keys and values
	$keys = implode(',', array_keys($filter));
	$values = implode(', ', array_map('intval', array_keys($filter)));
	$condition = array(); 
	foreach ($filter as $key => $value){
		if ($value != ''){
			$condition[] = "(`$key` LIKE '%$value%')";
		};
	};
	$condition = join(' AND ', $condition);

	// get user data
	$result = mysqli_query($link, "SELECT * FROM `$table` WHERE $condition ORDER BY `$sortColumn` $sortDir LIMIT 20 OFFSET $start");

	// get total rows in query
	$query = mysqli_query($link, "SELECT count(1) FROM `$table` WHERE $condition ORDER BY `$sortColumn` $sortDir");
	$recordsFiltered = mysqli_fetch_assoc($query);
	settype($recordsFiltered['count(1)'], "integer");
	$recordsFiltered = $recordsFiltered['count(1)'];

	// Create the data output array for JSON
	$outputArray = array();
	while($row = mysqli_fetch_assoc($result)){
		$outputArray[] = $row;
	};

	// format output
	$outputFormat = array(
		"draw"=> $draw, # draw counter
		"recordsTotal"=> $recordsTotal, # total records in db
		"recordsFiltered"=> $recordsFiltered, # total records in query
		"data"=> $outputArray # data pulled from db
	); 
	
// default data
} else {
	// get user data
	$result = mysqli_query($link, "SELECT * FROM `$table` ORDER BY `$sortColumn` $sortDir LIMIT 20 OFFSET $start");

	// get total rows in query
	$query = mysqli_query($link, "SELECT count(1) FROM `$table` ORDER BY `$sortColumn` $sortDir");
	$recordsFiltered = mysqli_fetch_assoc($query);
	settype($recordsFiltered['count(1)'], "integer");
	$recordsFiltered = $recordsFiltered['count(1)'];

	// Create the data output array for JSON
	$outputArray = array();
	while($row = mysqli_fetch_assoc($result)){
		$outputArray[] = $row;
	};

	// format output
	$outputFormat = array(
		"draw"=> $draw, # draw counter
		"recordsTotal"=> $recordsTotal, # total records in db
		"recordsFiltered"=> $recordsFiltered, # total records in query
		"data"=> $outputArray # data pulled from db
	);

};

//send to client
echo json_encode($outputFormat);