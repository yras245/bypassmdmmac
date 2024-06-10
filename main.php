<?php

// Включення виводу помилок для налагодження
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Підключення до бази даних MySQL
$servername = "su545660.mysql.tools";
$username = "su545660_db"; // Замініть на своє ім'я користувача MySQL
$password = "3CEYTzCx"; // Замініть на свій пароль MySQL
$dbname = "serial_numbers";

$conn = new mysqli($servername, $username, $password, $dbname);

// Перевірка з'єднання
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Функція для додавання серійного номера в базу даних
function add_serial_number($conn, $serial_number) {
    // Перевірка наявності серійного номера
    if (check_serial_number($conn, $serial_number)) {
        return ['message' => 'Serial number already exists'];
    }
    
    $sql = "INSERT INTO serials (serial_number) VALUES ('$serial_number')";

    if ($conn->query($sql) === TRUE) {
        return ['message' => 'Serial number added successfully'];
    } else {
        return ['message' => 'Error adding serial number: ' . $conn->error];
    }
}

// Функція для перевірки серійного номера в базі даних
function check_serial_number($conn, $serial_number) {
    $sql = "SELECT * FROM serials WHERE serial_number='$serial_number'";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        return true;
    } else {
        return false;
    }
}

// Отримуємо дію з параметрів запиту
$action = isset($_GET['action']) ? $_GET['action'] : '';

// Якщо додавання серійного номера
if ($action == 'add') {
    $serial_number = isset($_POST['serial_number']) ? $_POST['serial_number'] : '';

    // Якщо серійний номер не порожній
    if ($serial_number !== '') {
        // Додаємо серійний номер в базу даних
        $response = add_serial_number($conn, $serial_number);

        // Виводимо відповідь у форматі JSON
        header('Content-Type: application/json');
        echo json_encode($response);
        exit;
    } else {
        // Повідомлення про помилку вводу
        $response = ['message' => 'Invalid input'];
        header('Content-Type: application/json');
        echo json_encode($response);
        exit;
    }
}

// Якщо перевірка серійного номера
elseif ($action == 'check') {
    $serial_number = isset($_GET['serial_number']) ? $_GET['serial_number'] : '';

    // Якщо серійний номер не порожній
    if ($serial_number !== '') {
        // Перевіряємо серійний номер в базі даних
        $exists = check_serial_number($conn, $serial_number);

        // Виводимо відповідь у форматі JSON
        header('Content-Type: application/json');
        echo json_encode(['exists' => $exists]);
        exit;
    } else {
        // Повідомлення про помилку вводу
        $response = ['message' => 'Invalid input'];
        header('Content-Type: application/json');
        echo json_encode($response);
        exit;
    }
}
?>
