

const filterForm = document.getElementById('filter-form');
const productList = document.getElementById('product-list');

filterForm.addEventListener('submit', function(e) {
    console.log('Le script fonctionne.');
    e.preventDefault();
    fetch(this.action + '?' + new URLSearchParams(new FormData(this)))
        .then(response => response.text())
        .then(html => productList.innerHTML = html);
});
