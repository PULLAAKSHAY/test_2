document.addEventListener('DOMContentLoaded', () => {
    const messageForm = document.getElementById('message-form');
    const messageInput = document.getElementById('message-input');
    const messageList = document.getElementById('message-list');

    async function fetchMessages() {
        const response = await fetch('/messages');
        const messages = await response.json();
        messageList.innerHTML = '';
        messages.forEach(message => {
            const li = document.createElement('li');
            li.textContent = message;
            messageList.appendChild(li);
        });
    }

    messageForm.addEventListener('submit', async (event) => {
        event.preventDefault();
        const message = messageInput.value;
        await fetch('/messages', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message })
        });
        messageInput.value = '';
        fetchMessages();
    });

    fetchMessages();
});
