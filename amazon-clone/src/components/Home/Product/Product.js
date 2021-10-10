import React from "react";
import "./Product.css";

function Product({ title, price, rating, img }) {
  return (
    <div className="product">
      <div className="title-cont elem">
        <p className="title">{title}</p>
      </div>

      <div className="price-cont elem">
        <p className="price">$ {price}</p>
      </div>

      <div className="rating-cont elem">
        {Array(rating)
          .fill()
          .map((_, i) => (
            <p className="rating">⭐</p>
          ))}
      </div>

      <div className="pdt-image-cont elem">
        <img className="pdt-img" src={img} alt="img"></img>
      </div>

      <div className="btn-cont elem">
        <button type="submit" className="add-to-cart-btn">
          Add to cart
        </button>
      </div>
    </div>
  );
}

export default Product;
