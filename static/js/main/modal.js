function showModalRegistration() {
    document.getElementById('modalFormLogin').style.display = 'none';
    document.getElementById('filterLogin').style.display = 'none';
    document.getElementById('modalFormRegistration').style.display = 'block';
    document.getElementById('filter').style.display = 'block';
}

function showModalLogin() {
    document.getElementById('modalFormRegistration').style.display = 'none';
    document.getElementById('modalFormRegistration').style.display = 'none';
    document.getElementById('modalFormLogin').style.display = 'block';
    document.getElementById('filterLogin').style.display = 'block';
}

function closeModals() {
    document.getElementById('modalFormRegistration').style.display = 'none';
    document.getElementById('modalFormRegistration').style.display = 'none';
    document.getElementById('modalFormLogin').style.display = 'none';
    document.getElementById('filterLogin').style.display = 'none';
}
