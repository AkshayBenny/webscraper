import React from "react";
import "./CartProduct.css";

function CartProduct({ img, title, rating, price }) {
  return (
    <div className="cart-product">
      <div className="outline">
        <div className="cart-pdt-img-cont cart-d">
          <img className="c-pdt-img" src={img} alt="img"></img>
        </div>

        <div className="cart-details">
          <div className="cart-title-cont cart-d">
            <p className="cart-title">{title}</p>
          </div>

          <div className="cart-price-cont cart-d">
            <p className="cart-price">$ {price}</p>
          </div>

          <div className="cart-rating-cont">
            {Array(rating)
              .fill()
              .map((_, i) => (
                <p className="cart-rating">⭐</p>
              ))}
          </div>
          <button className="cart-rm-btn" type="submit">
            Remove from cart
          </button>
        </div>
      </div>
    </div>
  );
}

export default CartProduct;
