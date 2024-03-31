function addUserToGroup() {
    var groupId = document.getElementById('groupSelect').value;
    var userId = document.getElementById('userSelect').value;
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/api/UserGroupManager/addUserToGroup', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                alert(xhr.responseText);
            } else {
                alert('Failed to add user to group');
            }
        }
    };
    xhr.send(JSON.stringify({ groupId: groupId, userId: userId }));
}

document.getElementById('addUserBtn').addEventListener('click', addUserToGroup);
