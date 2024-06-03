document.addEventListener("DOMContentLoaded", () => {
    if (!localStorage.getItem('serialNumbers')) {
        localStorage.setItem('serialNumbers', JSON.stringify([]));
    }
});

function addSerialNumber() {
    const serialNumber = document.getElementById('addSerialNumber').value;
    const serialNumbers = JSON.parse(localStorage.getItem('serialNumbers'));

    if (serialNumbers.includes(serialNumber)) {
        document.getElementById('addResult').innerText = 'Serial number already exists';
        return;
    }

    serialNumbers.push(serialNumber);
    localStorage.setItem('serialNumbers', JSON.stringify(serialNumbers));
    document.getElementById('addResult').innerText = 'Serial number added successfully';
}

function checkSerialNumber() {
    const serialNumber = document.getElementById('checkSerialNumber').value;
    const serialNumbers = JSON.parse(localStorage.getItem('serialNumbers'));

    if (serialNumbers.includes(serialNumber)) {
        document.getElementById('checkResult').innerText = 'Serial number exists';
    } else {
        document.getElementById('checkResult').innerText = 'Serial number does not exist';
    }
}
