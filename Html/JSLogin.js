const usernameInput = document.getElementById('username');
const passwordInput = document.getElementById('password');
const loginBtn = document.getElementById('loginBtn');

loginBtn.addEventListener('click', function() {
    const username = usernameInput.value.trim();
    const password = passwordInput.value.trim();

    if (!username || !password) {
        alert('请填写完整信息');
        return;
    }

    // 发送到 FastAPI 后端
    fetch('http://127.0.0.1:8000/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password })
    })
        .then(response => response.json())
        .then(data => {
            alert('服务器响应：' + JSON.stringify(data.message));
        })
        .catch(err => {
            alert('请求失败，请确保 FastAPI 服务已启动');
            console.error(err);
        });
});