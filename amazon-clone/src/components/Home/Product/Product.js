import React from 'react'
import './Product.css'

function Product() {
    return (
        <div className="product">
            <div className="title-cont elem">
                <p className="title">From Goethe to Gundolf by Roger Paulin</p>
            </div>

            <div className="price-cont elem">
                <p className="price">$ 119.9</p>
            </div>

            <div className="rating-cont elem">
              <p className="rating">⭐⭐⭐⭐⭐</p>  
            </div>

            <div className="pdt-image-cont elem">
                <img className="pdt-img" src="https://www.openbookpublishers.com/shopimages/products/thumbnails/1425.jpg"></img>
            </div> 

            <div className="btn-cont elem">
                <button type="submit" className="add-to-cart-btn">Add to cart</button>
            </div>
            
        </div>
    )
}

export default Product
