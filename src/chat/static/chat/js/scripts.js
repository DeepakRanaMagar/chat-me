let url = `ws://${window.location.host}/ws/socket-server/`;

const chatSocket = new WebSocket(url);

let senderName = localStorage.getItem('senderName');
if (!senderName) {
  localStorage.setItem('senderName', senderName);
}

chatSocket.onmessage = function (e) {
  let data = JSON.parse(e.data);
  console.log('Data:', data);

  if (data.type === 'chat') {
    let messages = document.getElementById('messages')
    let cssClass = data.sender === senderName ? 'sender' : 'receiver';
    messages.insertAdjacentHTML('beforeend', `<div class="${cssClass}">
    <p>${data.message}</p>
  </div>`)
  }
}

let form = document.getElementById('form')
form.addEventListener('submit', (e) => {
  e.preventDefault()
  let message = e.target.message.value
  chatSocket.send(JSON.stringify({
    'message': message,
    'sender': senderName
  }))
  form.reset()
})
