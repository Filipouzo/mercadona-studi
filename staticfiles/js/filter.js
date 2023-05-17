

const filterForm = document.getElementById('filter-form');
const productList = document.getElementById('product-list');

filterForm.addEventListener('submit', function(e) {
    e.preventDefault();

    fetch(this.action + '?' + new URLSearchParams(new FormData(this)), {
        headers: {
            'X-Requested-With': 'XMLHttpRequest'
        }
    })
        .then(response => response.text())
        .then(html => productList.innerHTML = html);
});
