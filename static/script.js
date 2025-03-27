let websocket;

document.addEventListener('DOMContentLoaded', function() {
    connectWebSocket();
    setupEventListeners();
});

function connectWebSocket() {
    websocket = new WebSocket('ws://localhost:8000/ws');
    
    websocket.onmessage = function(event) {
        const data = JSON.parse(event.data);
        addMessage(data.message, data.type === 'bot');
    };

    websocket.onclose = function() {
        console.log('Connection closed');
        setTimeout(connectWebSocket, 1000);
    };
}

function setupEventListeners() {
    const input = document.getElementById('message-input');
    const sendButton = document.getElementById('send-button');

    sendButton.addEventListener('click', sendMessage);
    input.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });
}

function sendMessage() {
    const input = document.getElementById('message-input');
    const message = input.value.trim();

    if (message) {
        websocket.send(message);
        addMessage(message, false);
        input.value = '';
    }
}

function addMessage(text, isBot) {
    const messagesDiv = document.getElementById('chat-messages');
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${isBot ? 'bot-message' : 'user-message'}`;
    messageDiv.textContent = text;
    messagesDiv.appendChild(messageDiv);
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
}
