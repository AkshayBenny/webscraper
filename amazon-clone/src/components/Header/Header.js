import React from 'react'
import './Header.css'

function Header() {
    return (
        <div className="nav-bar">
            <div className="logo-cont">
                <img className="logo" src="https://pngimg.com/uploads/amazon/amazon_PNG11.png" alt="amazon-logo"></img>
            </div>

            <div className="search-cont">
                <input type="text"></input>
                <div className="search-icon-cont">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24"><path fill="none" d="M0 0h24v24H0z"/><path d="M18.031 16.617l4.283 4.282-1.415 1.415-4.282-4.283A8.96 8.96 0 0 1 11 20c-4.968 0-9-4.032-9-9s4.032-9 9-9 9 4.032 9 9a8.96 8.96 0 0 1-1.969 5.617zm-2.006-.742A6.977 6.977 0 0 0 18 11c0-3.868-3.133-7-7-7-3.868 0-7 3.132-7 7 0 3.867 3.132 7 7 7a6.977 6.977 0 0 0 4.875-1.975l.15-.15z"/></svg>
                </div>
                
            </div>

            <div className="header-options">
                <div className="signin h-option">
                    <p className="line-one">Hello</p>
                    <p className="line-two">Sign in</p>
                </div>

                <div className="ret-and-ord h-option">
                    <p className="line-one">Returns</p>
                    <p className="line-two">& Orders</p>
                </div>

                <div className="prime h-option">
                    <p className="line-one">Your</p>
                    <p className="line-two">Prime</p>
                </div>

                <div className="cart h-option">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24"><path fill="none" d="M0 0h24v24H0z"/><path d="M4 6.414L.757 3.172l1.415-1.415L5.414 5h15.242a1 1 0 0 1 .958 1.287l-2.4 8a1 1 0 0 1-.958.713H6v2h11v2H5a1 1 0 0 1-1-1V6.414zM6 7v6h11.512l1.8-6H6zm-.5 16a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3zm12 0a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3z" fill="rgba(255,255,255,1)"/></svg>
                    <p className="cart-count">0</p>
                </div>
            </div>
        </div>
    )
}

export default Header
