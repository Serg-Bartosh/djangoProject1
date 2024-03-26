var addPostModal = document.getElementById("addPostModal");
var addPostBtn = document.getElementById("addPostBtn");
var closeBtn = document.getElementsByClassName("close")[0];
var addPostForm = document.getElementById("addPostForm");

addPostBtn.onclick = function () {
    addPostModal.style.display = "block";
}

closeBtn.onclick = function () {
    addPostModal.style.display = "none";
}

window.onclick = function (event) {
    if (event.target == addPostModal) {
        addPostModal.style.display = "none";
    }
}

addPostForm.onsubmit = function (event) {
    event.preventDefault();
    var formData = new FormData(addPostForm);
    addPostModal.style.display = "none";
}
