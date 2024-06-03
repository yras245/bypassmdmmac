<?php

define('JSON_FILE', 'serial_numbers.json');

if (!file_exists(JSON_FILE)) {
    file_put_contents(JSON_FILE, json_encode([]));
}

$data = json_decode(file_get_contents(JSON_FILE), true);

function add_serial($serial_number) {
    global $data;

    foreach ($data as $item) {
        if ($item['serial_number'] == $serial_number) {
            return ['message' => 'Serial number already exists'];
        }
    }

    $data[] = ['serial_number' => $serial_number];
    file_put_contents(JSON_FILE, json_encode($data));

    return ['message' => 'Serial number added successfully'];
}

function check_serial($serial_number) {
    global $data;

    foreach ($data as $item) {
        if ($item['serial_number'] == $serial_number) {
            return ['exists' => true];
        }
    }

    // Optionally, here you can add code to check the serial number with Dhru Fusion API.

    return ['exists' => false];
}

$input = json_decode(file_get_contents('php://input'), true);
$action = isset($_GET['action']) ? $_GET['action'] : $input['action'];

if ($action == 'add') {
    $serial_number = isset($input['serial_number']) ? $input['serial_number'] : null;
    if ($serial_number) {
        $response = add_serial($serial_number);
    } else {
        $response = ['message' => 'Invalid input'];
    }
} elseif ($action == 'check') {
    $serial_number = isset($_GET['serial_number']) ? $_GET['serial_number'] : null;
    if ($serial_number) {
        $response = check_serial($serial_number);
    } else {
        $response = ['message' => 'Invalid input'];
    }
} else {
    $response = ['message' => 'Invalid action'];
}

header('Content-Type: application/json');
echo json_encode($response);
?>
