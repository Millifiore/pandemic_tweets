document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('button').forEach(button => {
        button.onclick = () => {
            const request = new XMLHttpRequest();
            request.open('POST', `/${button.id}`);
            request.onload = () => {
                const response = request.responseText;
                document.getElementById('count').innerHTML = response;
            }; 
            request.send();
        };
    });
});
