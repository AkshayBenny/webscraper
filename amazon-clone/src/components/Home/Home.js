import React from "react";
import "./Home.css";
import Product from "./Product/Product";

function Home() {
  return (
    <div className="home">
      <div className="home-top">
        <img
          className="home-top-bkg"
          src="https://www.orissapost.com/wp-content/uploads/2019/09/Top-smartphone-deals-during-Big-Billion-Days-Great-Indian-Festival-sales.jpeg"
          alt="background"
        ></img>
      </div>

      <div className="rows">
        <div className="row-one row">
          <Product
            title="A song of Ice and fire"
            price={20.55}
            rating={4}
            img="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTSjwzQKRhNCGWqxLuMYR_Q34oW7NeqXT7vHA&usqp=CAU"
          />

          <Product />
        </div>
      </div>
    </div>
  );
}

export default Home;
