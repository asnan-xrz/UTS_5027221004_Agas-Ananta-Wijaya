document.addEventListener('DOMContentLoaded', function() {
    fetchProducts();
});

function fetchProducts() {
    fetch('/products')
        .then(response => response.json())
        .then(data => {
            let productsDiv = document.getElementById('products');
            productsDiv.innerHTML = '';
            data.products.forEach(product => {
                let productDiv = document.createElement('div');
                productDiv.innerHTML = `<h2>${product.name}</h2><p>${product.description}</p><p>$${product.price}</p>`;
                productsDiv.appendChild(productDiv);
            });
        });
}
