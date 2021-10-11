import React from "react";
import "./Checkout.css";
import CartProduct from "./CartProduct/CartProduct";

function Checkout() {
  return (
    <div className="checkout">
      <h1 className="heading">Shopping Cart</h1>
      <CartProduct
        title="ASUS TUF Gaming F15, 15.6-inch (39.62 cms) FHD 144Hz, Intel Core i5-10300H 10th Gen, GTX 1650 Ti GDDR6 4GB Graphics, Gaming Laptop (8GB RAM/512GB SSD/Windows 10/Fortress Gray/2.3 Kg), FX566LI-HN272T"
        rating={5}
        price={600}
        img="https://m.media-amazon.com/images/I/914o5xV1+8L._AC_AA180_.jpg"
      />
    </div>
  );
}

export default Checkout;
