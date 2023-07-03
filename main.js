let carts = document.querySelectorAll(".add-cart");
let products = [
  {
    name: "Nicless",
    tag: "AA (10)",
    price: 250000,
    incart: 0,
  },
  {
    name: "Nicless",
    tag: "AA (6)",
    price: 250000,
    incart: 0,
  },
  {
    name: "Micoba",
    tag: "MIKO (13)",
    price: 250000,
    incart: 0,
  },
  {
    name: "Necles",
    tag: "MIKO (6)",
    price: 300250,
    incart: 0,
  },
  {
    name: "Ring",
    tag: "AA7",
    price: 250000,
    incart: 0,
  },
  {
    name: "necless",
    tag: "QQ (3)",
    price: 250329,
    incart: 0,
  },
];
for (let i = 0; i < carts.length; i++) {
  carts[i].addEventListener("click", () => {
    cartNumbers(products[i]);
    totalCost(products[i]);
  });
}
function onLoadCartNumbers() {
  let totalNumberOfProducts = localStorage.getItem("cartNumbers");
  if (totalNumberOfProducts) {
    document.querySelector(".cart span").textContent = totalNumberOfProducts;
  }
}
function setItems(product) {
  let cartItems = localStorage.setItem("productsInCart");
  cartItems = JSON.parse(cartItems);
  if (cartItems != null) {
    if (cartItems[product.tag] == undefined) {
      cartItems = {
        ...cartItems,
        [product.tag]: product,
      };
    }
    cartItems[product.tag].incart += 1;
  } else {
    product.incart = 1;
    cartItems = {
      [product.tag]: product,
    };
  }
  localStorage.setItem("productsInCart", JSON.stringify(cartItems));
}

function cartNumbers(product) {
  let totalNumberOfProducts = localStorage.getItem("cartNumbers");
  totalNumberOfProducts = parseInt(totalNumberOfProducts);
  if (totalNumberOfProducts) {
    localStorage.setItem("cartNumbers", totalNumberOfProducts + 1);
    document.querySelector(".cart span").textContent = totalNumberOfProducts + 1;
  } else {
    localStorage.setItem("cartNumbers", 1);
    document.querySelector(".cart span").textContent = 1;
  }

  setItems(product);
}

function totalCost(product) {
  let cartCost = localStorage.getItem("totalCost");
  console.log("My cartCost is ", cartCost);
  console.log(typeof cartCost);
  if (cartCost != null) {
    cartCost = parseInt(cartCost);
    localStorage.setItem("totalCost", cartCost + product.price);
  } else {
    localStorage.setItem("totalCost", product.price);
  }
}
function displayCart() {
  let cartItems = localStorage.getItem("productsInCart");
  cartItems = JSON.parse(cartItems);
  let productContainer = document.querySelector(".products");
  console.log(cartItems);
  if (cartItems && productContainer) {
    productContainer.innerHTML = "";
    Object.values(cartItems).map((item) => {
      productContainer.innerHTML += `
             <div class="product">
                <ion-icon name="close-circle"><ion-icon>
                img src="./MICKOBA/${item.tag}.jpg"
                img src="./PICTURE/${item.tag}.jpg"
                <span>${item.name}</span>
              </div>
              <div class="price">${item.price}</div>
             `;
    });
  }
}
onLoadCartNumbers();
displayCart();
