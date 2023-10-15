// console.log('Hello world')

// 67
setTimeout(function () {
    let messages = document.getElementById('messages');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 2000);